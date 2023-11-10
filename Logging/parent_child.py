import logging

# create child logger
logger = logging.getLogger("parent.child")

# Emit a log message of level INFO, by default this is not print to the screen
# since root logger has a level of WARNING set
logger.info("first info level")

# create parent logger
parent_logger = logging.getLogger("parent")
s_handler = logging.StreamHandler()
s_formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
# set formatter to handler
s_handler.setFormatter(s_formatter)
parent_logger.setLevel(logging.INFO)

# add handler to logger
parent_logger.addHandler(s_handler)
logger.info(f"emitting log from child")