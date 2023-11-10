from flask import Flask, Blueprint, jsonify, g, request
import importlib
import traceback
import time
from app.logging import set_log_context
import random
import string
from app.logging.log_utils import get_perf_logger, get_logger
from app.logging.splunk_utils import request_msg
import logging

# root logger
app_logger = logging.getLogger()
# named logger
logger = get_logger(__name__)
# performance logger
perf_logger = get_perf_logger()

def create_app(config=None):
    if config is None:
        app = Flask(__name__)
    else:
        app = Flask(__name__)
        app.config.from_object(config)

    with app.app_context():
        # Register blueprints:
        if app.config.get('AUTO_REGISTER_BP', True):
            app.logger.info("Registering blueprints ...")
            register_blueprints(app)

        # pre/post request processing hooks
        if app.config.get('AUTO_REQ_FILTERS', True):
            app.logger.info("Adding flask request hooks ...")
            initialize_request_filters(app)

        # Initialize flask extension objects
        if app.config.get('AUTO_INIT_FLASK_EXT', True):
            app.logger.info("Initializing flask extensions ...")
            register_extensions(app)

        # Register error handlers
        if app.config.get('AUTO_REG_ERR_HANDLERS', True):
            app.logger.info("Initializing app request error handlers ...")
            register_error_handlers(app)

    return app

def random_uuid_8():
    chars = string.ascii_letters + string.digits
    token = ''.join(random.choice(chars) for i in range(8))
    return token

def register_blueprints(app):
    # get environment specific blueprints
    BLUEPRINTS = app.config.get('BLUEPRINTS', [])
    app.logger.debug(f"processing blueprints {BLUEPRINTS} ...")

    # locate each blueprint and register with app instance
    for service in BLUEPRINTS:
        service_path = service.get('path')
        try:
            app.logger.info(f"loading module from path {service_path} ...")
            module = importlib.import_module(service_path)
        except ModuleNotFoundError as e:
            app.logger.error(f"{service_path} module couldn't be imported: {e}")
        except Exception as e:
            traceback.print_exc()
            app.logger.error(f"Unable to load blueprint module: {e}")
        else:   # run this block when there is no exception
            for name, obj in module.__dict__.items():
                if isinstance(obj, Blueprint):
                    bp_url_prefix = service.get('url_prefix')
                    app.logger.info(f"Registering Blueprint - {name} with prefix {bp_url_prefix} ...")
                    try:
                        app.register_blueprint(obj, url_prefix=bp_url_prefix)
                    except Exception as e:
                        app.logger.error(f"{name} Registration Error: {e}")

def initialize_request_filters(app):
    @app.before_request
    def init_context():
        g.start = time.time()
        tx_id = request.headers.get('X-transactionId', request.headers.get('transactionId')) if request.headers else None
        g.end_point=request.path
        set_log_context(transaction_id=tx_id, in_transaction_id=random_uuid_8())
        logger.debug('*** START REQUEST ***')
        logger.info(request_msg(request))
    
    @app.after_request
    def end_context(response):
        diff = int((time.time() - g.start) * 1000)
        perf_logger.info(f'end_point={g.end_point} | status={response.status} | total_execution_time={diff} ms')
        logger.debug('*** END REQUEST ***')
        return response
    
def register_extensions(app):
    pass

def register_error_handlers(app):
    @app.errorhandler(400)
    def error400(error):
        msg = app.config['HTTP_ERR_CODE'][400]
        app.logger.error(f"HTTP 400: {msg}")
        return jsonify({
            "status": {
                "code": 400,
                "message": msg,
                "details": error.description
            }
        }), 400

    @app.errorhandler(403)
    def error403(error):
        msg = app.config['HTTP_ERR_CODE'][403]
        app.logger.error(f"HTTP 403: {msg}")
        return jsonify({
            "status": {
                "code": 403,
                "message": msg,
                "details": error.description
            }
        }), 403

    @app.errorhandler(404)
    def error404(error):
        msg = app.config['HTTP_ERR_CODE'][404]
        app.logger.error(f"HTTP 404: {msg}")
        return jsonify({
            "status": {
                "code": 404,
                "message": msg,
                "details": error.description
            }
        }), 404

    @app.errorhandler(405)
    def error405(error):
        msg = app.config['HTTP_ERR_CODE'][405]
        app.logger.error(f"HTTP 405: {msg}")
        return jsonify({
            "status": {
                "code": 405,
                "message": msg,
                "details": error.description
            }
        }), 405

    @app.errorhandler(500)
    def error500(error):
        msg = app.config['HTTP_ERR_CODE'][500]
        app.logger.error(f"HTTP 500: {msg}")
        return jsonify({
            "status": {
                "code": 500,
                "message": msg,
                "details": error.description
            }
        }), 500

    @app.errorhandler(502)
    def error502(error):
        msg = app.config['HTTP_ERR_CODE'][502]
        app.logger.error(f"HTTP 502: {msg}")
        return jsonify({
            "status": {
                "code": 502,
                "message": msg,
                "details": error.description
            }
        }), 502

    @app.errorhandler(504)
    def error504(error):
        msg = app.config['HTTP_ERR_CODE'][504]
        app.logger.error(f"HTTP 504: {msg}")
        return jsonify({
            "status": {
                "code": 504,
                "message": msg,
                "details": error.description
            }
        }), 504
   

