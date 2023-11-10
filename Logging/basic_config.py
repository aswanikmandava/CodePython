import logging

"""
The call to logging.basicConfig() is to alter the root logger. 
In our example, we set the handler to output to a file instead of the screen, 
adjust the logging level such that all log messages of level DEBUG or above are handled, 
and also change the format of the log message output to include the time.
"""
logging.basicConfig(filename = 'file.log',
                    level = logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
 
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')