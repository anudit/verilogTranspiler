import logzero as l0

DEF_STYLE = "SUCCESS"

def log(*msgs, STYLE = DEF_STYLE):

    log_format = '%(color)s%(message)s%(end_color)s'
    formatter = l0.LogFormatter(fmt=log_format)
    l0.setup_default_logger(formatter=formatter)

    msg =""
    for m in msgs:
        msg+=m

    if (STYLE == "GREEN" or STYLE == "SUCCESS"):
        l0.logger.info(str(msg))
    elif (STYLE == "BLUE" or STYLE == "INFO"):
        l0.logger.debug(str(msg))
    elif (STYLE == "YELLOW" or STYLE == "WARNING"):
        l0.logger.warning(str(msg))
    elif (STYLE == "RED" or STYLE == "ERROR"):
        l0.logger.error(str(msg))
    else:
        l0.logger.error(str("INVALID TYPE"))
    print

def setDefaultStyle(STYLE = "SUCCESS"):
    if (STYLE == "GREEN" or STYLE == "SUCCESS"):
        DEF_STYLE = "SUCCESS"
    elif (STYLE == "BLUE" or STYLE == "INFO"):
        DEF_STYLE = "INFO"
    elif (STYLE == "YELLOW" or STYLE == "WARNING"):
        DEF_STYLE = "WARNING"
    elif (STYLE == "RED" or STYLE == "ERROR"):
        DEF_STYLE = "ERROR"
    else:
        pass

def test():
    log("THIS IS A TEST MSG!", STYLE = "YELLOW")
