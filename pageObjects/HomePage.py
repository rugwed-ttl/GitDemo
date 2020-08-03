
from selenium.webdriver.common.by import By


class HomePage :

    def __init__(self,driver):
        self.driver = driver

    permission1 = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    permission2 = (By.ID, "com.android.permissioncontroller:id/permission_allow_always_button")
    userName = (By.ID, "com.tatamotors.eguruhybrid:id/user_id")
    password = (By.ID, "com.tatamotors.eguruhybrid:id/password")
    loginSubmitButton = (By.ID, "com.tatamotors.eguruhybrid:id/email_sign_in_button")
    pin = (By.ID, "com.tatamotors.eguruhybrid:id/btn1")
    versionUpdate= (By.ID, "android:id/button1")

    def getPermission1(self):
        return self.driver.find_element(*HomePage.permission1)

    def getPermission2(self) :
        return self.driver.find_element (*HomePage.permission2)

    def getUsername(self) :
        return self.driver.find_element (*HomePage.userName)

    def getPassword(self) :
        return self.driver.find_element (*HomePage.password)

    def getLoginSubmitButton(self) :
        return self.driver.find_element (*HomePage.loginSubmitButton)

    def getEnterPin(self) :
        return self.driver.find_element (*HomePage.pin)

    def getVersionUpdate(self) :
        return self.driver.find_element (*HomePage.versionUpdate)