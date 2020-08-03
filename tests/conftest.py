import time

import pytest
from appium import webdriver

@pytest.fixture(scope="class")
def setup(request): #Request instance is used when you have send valus from pytest fixture
    desired_cap = {
        "deviceName" : "DRGID18083101432",
        # "deviceName" : "emulator-5554",
        "app" : "C:\\Users\\raa918070\\Downloads\\EGuru_V1.1.2_B45-sandbox-financier.apk",
        "platformName" : "Android"
        # "appPackage" : "com.google.android.contacts",
        # "appActivity" : "com.android.contacts.activities.PeopleActivity"
    }
    driver = webdriver.Remote ("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait (50)
    request.cls.driver = driver