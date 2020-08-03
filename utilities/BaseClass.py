import inspect
import time

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self) :
        loggerName = inspect.stack ()[1][3]
        logger = logging.getLogger (loggerName)
        fileHandler = logging.FileHandler ('logfile.log')
        formatter = logging.Formatter ("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter (formatter)
        logger.addHandler (fileHandler)  # filehandler object
        logger.setLevel (logging.DEBUG)
        return logger


    def VerifyLinkPresence(self, text):
        element= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,text)))


    def Screenshots(self):
         ts = time.strftime ("%Y_%m_%d_%H%M%S")
         activityname = self.driver.current_activity
         filename = activityname + ts
         self.driver.save_screenshot (
             "C:\\Users\\raa918070\\PycharmProjects\\Eguru_Sandbox\\Screenshot\\" + filename + ".png")


    def verifyLinkPresence(self, text) :
        element = WebDriverWait (self.driver, 20).until (
            EC.presence_of_element_located ((By.ID, text)))
