import logging as log

# configures the root logger
log.basicConfig(level=log.INFO)

log.debug("test debug msg")
log.info("test info msg")
log.warning("test warn msg")
log.critical("test critical msg")