import logging

class Logger:
    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        # Add handlers and formatters
        return logger

# @brief : Common Logging Config function
# @param cur_app: flask app
# @param debug_log : logging.XXX level
def cfg_dbg_logger(cur_app, debug_log):
    log_level = logging.INFO
    log_format = '%(message)s'
    if debug_log:
        log_level = logging.DEBUG
        log_format = '%(asctime)s %(module)-15s %(levelname)-8s %(message)s'
    logging.basicConfig(format=log_format, level=log_level)

    log_handler = logging.StreamHandler()
    log_handler.setLevel(log_level)
    log_handler.setFormatter(log_format)

    cur_app.logger.addHandler(log_handler)
    cur_app.logger.addHandler(debug_log)


# @brief : Common Logging Config function
def config_logging(log_level:int=logging.INFO):
    log_format = '%(message)s'
    # DEBUG is less than INFO
    if log_level < logging.INFO :
        log_level = logging.DEBUG
        log_format = '%(asctime)s %(module)-15s %(levelname)-8s %(message)s'

    log_format = '%(asctime)s %(module)-15s %(levelname)-8s %(message)s'
    logging.basicConfig(format=log_format, level=log_level)

    # TODO
    log_handler = logging.StreamHandler()
    log_handler.setLevel(log_level)
    log_handler.setFormatter(log_format)

    return log_handler
