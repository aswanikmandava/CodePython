import logging

log_file_name = 'modular_app'
log_level = logging.getLevelName(logging.INFO)
log_config = {
'file_path': 'E:\\Learning\\Python\\MyProjects\\CodePython\\flask apps\\modular\\{}.log',
'maxBytes': 10000000,
'backupCount': 1,
}