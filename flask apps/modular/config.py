class Config:
    """
    Base configuration class
    """
    # Default settings
    FLASK_ENV = 'development'
    FLASK_DEBUG = False
    TESTING = False
    APP_SERVER_PORT = 7100
    # register blueprint automatically
    AUTO_REGISTER_BP = True
    # initialize flask extensions
    AUTO_INIT_FLASK_EXT = True
    # add pre/post request processing hooks
    AUTO_REQ_FILTERS = True
    # apply error handlers to flask app
    AUTO_REG_ERR_HANDLERS = True

    # Settings applicable to all environments to follow
    BLUEPRINTS = [
        {'name': 'main', 'path': 'app.main', 'url_prefix': '/main'},
        {'name': 'status', 'path': 'app.api.status', 'url_prefix': '/status'},
    ]

    # HTTP ERROR CODE MAP
    HTTP_ERR_CODE = {
        400: 'Bad Request',
        403: 'Access denied',
        404: 'URL not found',
        405: 'Method Not Allowed',
        500: 'Internal Server Error',
        502: 'Bad Gateway',
        504: 'Gateway Timeout',
    }

class DevConfig(Config):
    """
    Settings for Development environment
    """
    FLASK_DEBUG = False

class QAConfig(Config):
    """
    Settings for QA/Test environment
    """
    TESTING = True

class ProdConfig(Config):
    """
    Settings for Prod environment
    """
    FLASK_ENV = 'production'


