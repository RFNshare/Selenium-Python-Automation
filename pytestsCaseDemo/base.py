import inspect
import logging

import pytest


@pytest.mark.usefixtures("cross")
class Base():
    def test_Log(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file.setFormatter(formatter)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        logger.info("AD")
        return logger
