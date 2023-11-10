import logging 

# Create a custom logger
logger = logging.getLogger(__name__) 

# Create Stream handler
"""
    StreamHandler() sends logging output to streams such as sys.stdout, sys.stderr or 
        any file-like object (or, more precisely, any object which supports write() and flush() methods).
    FileHandler() outputs logs to disk file
    SMTPHandler() outputs log messages to an email address via SMTP
    HTTPHandler() outputs log messages to a web server using GET or POST verbs
"""
stream_handle = logging.StreamHandler 

# Create HTTP handler
http_handle = logging.HTTPHandler('example.com','/path',method='POST',secure=True, credentials=('username','password'), context=None) 

# Set Severity level
"""
    Filters attached to handlers are consulted before an event is emitted by the handler, 
    whereas filters attached to loggers are consulted whenever an event is logged before sending an event to handlers.
"""
stream_handle.setLevel(logging.INFO)
http_handle.setLevel(logging.WARNING) 

# Create formatters 
"""
    %(asctime)s attribute represents the time the log message was generated
    %(name)s attribute represents the name of the logger object
    %(levelname)s attribute represents the severity level of the log message
    %(message)s attribute represents the log message.
"""
stream_handle_format = logging.Formatter('%(process)s - %(message)s')
http_handle_format = logging.Formatter('%(levelname)s - %(message)s - %(asctime)s') 

# Assign formatters to handlers
stream_handle.setFormatter(stream_handle_format)
http_handle.setFormatter(http_handle_format) 

# Add handlers to the logger
logger.addHandler(stream_handle)
logger.addHandler(http_handle) 

# Log messages
logger.warning('This is a warning')
logger.error('This is an error')