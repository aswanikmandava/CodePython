import logging
from logging.handlers import RotatingFileHandler
import os
import sys
import errno
from app.settings import log_config, log_file_name, log_level
from app.logging import get_log_context

root_log_fmtr = logging.Formatter('%(asctime)s | %(levelname)s | %(process)d | %(thread)d | %(pathname)s:%(lineno)d | %(message)s')
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(process)d | %(thread)d | %(pathname)s:%(lineno)d | TID=%(in_transaction_id)s | EXT_TID=%(transaction_id)s | %(key_fields)s %(message)s')

class AppLogFilter(logging.Filter): 
    def filter(self, record):
        record.transaction_id = get_log_context()['transaction_id']
        record.in_transaction_id = get_log_context()['in_transaction_id']
        record.key_fields = get_log_context()['key_fields']
        return True 
   
class AppLogAdapter(logging.LoggerAdapter): 
    def process(self, msg, kwargs):
        kwargs.setdefault('extra', get_log_context())
        return msg, kwargs

def mkdir_p(path):
    try:
        os.makedirs(path, exist_ok=True)
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

def get_file_handler(file_name, log_level=logging.INFO): 
    mkdir_p(os.path.dirname(file_name))
          
    file_handler = RotatingFileHandler(file_name, mode='a', 
                                        maxBytes=int(log_config['maxBytes']), 
                                        backupCount=int(log_config['backupCount'])) 
    file_handler.setLevel(log_level) 
    file_handler.setFormatter(log_formatter) 
    return file_handler 
  

def get_stream_handler():
    # get standard errors
    stream_handler = logging.StreamHandler(sys.stderr) 
    stream_handler.setLevel(logging.ERROR) 
    stream_handler.setFormatter(root_log_fmtr) 
    return stream_handler 
  
# Module logger
def get_logger(logger_name): 
    logger = logging.getLogger(logger_name) 
    logger.setLevel(log_level) 
    flhandler = get_file_handler(log_config['file_path'].format(log_file_name), log_level) 
    flhandler.addFilter(AppLogFilter())
    logger.addHandler(flhandler) 
    logger.addHandler(get_stream_handler()) 
    logger.addFilter(AppLogFilter())
    logger.propagate = False
    return logger 
 
# Performance logger
def get_perf_logger(): 
    logger = logging.getLogger('perf') 
    logger.setLevel(log_level) 
    flhandler = get_file_handler(log_config['file_path'].format(f'{log_file_name}_perf'), logging.INFO) 
    logger.addHandler(flhandler) 
    logger.addFilter(AppLogFilter()) 
    logger.propagate = False 
    return logger 

# root logger
logger = logging.getLogger() 
logger.setLevel(log_level) 
flhandler = get_file_handler(log_config['file_path'].format(log_file_name), log_level) 
flhandler.setFormatter(root_log_fmtr)
logger.addHandler(flhandler) 
logger.addHandler(get_stream_handler()) 
logger.propagate = False
