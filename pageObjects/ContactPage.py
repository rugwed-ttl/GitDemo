from selenium.webdriver.common.by import By


class ContactPage :

    def __init__(self,driver):
        self.driver = driver

    contactButton = (By.ID, "com.tatamotors.eguruhybrid:id/tvCreateNew")
    contactName = (By.XPATH, "//android.widget.EditText[@bounds='[18,616][527,711]']")
    contactLName = (By.XPATH,"//android.widget.EditText[@bounds='[553,616][1062,711]']")
    contactNumber = (By.XPATH, "//android.widget.EditText[@bounds='[18,828][527,923]']")
    contactState = (By.XPATH, "//android.widget.EditText[@bounds='[18,1513][520,1608]']")
    contactTaluka = (By.XPATH, "//android.widget.EditText[@bounds='[559,1513][1062,1608]']")
    contactAdd1 = (By.XPATH, "//android.widget.EditText[@text='Address Line 1']")
    contactAdd2 = (By.XPATH, "//android.widget.EditText[@text='Address Line 2']")
    contactSubmitButton = (By.ID, "com.tatamotors.eguruhybrid:id/next_button")
    contact_ID = (By.ID, "com.tatamotors.eguruhybrid:id/dialog_title_text")
    contactSuccessMessage = (By.ID, "com.tatamotors.eguruhybrid:id/dialog_message_text")
    contactFailureMessage = (By.ID, "android:id/message")
    contactHomeButton = (By.ID, "com.tatamotors.eguruhybrid:id/dialog_no_btn")
    contactErrorOkButton = (By.ID,"android:id/button2")
    contact2Home = (By.ID, "com.tatamotors.eguruhybrid:id/menu_home")

    #self.driver.find_element_by_id ("").click ()
    def getContactButton(self):
        return self.driver.find_element(*ContactPage.contactButton)

    def getContactName(self):
        return self.driver.find_element(*ContactPage.contactName)

    def getContactLName(self):
        return self.driver.find_element(*ContactPage.contactLName)

    def getContactNumber(self):
        return self.driver.find_element(*ContactPage.contactNumber)

    def getContactState(self):
        return self.driver.find_element(*ContactPage.contactState)

    def getContactTaluka(self):
        return self.driver.find_element(*ContactPage.contactTaluka)

    def getContactAdd1(self):
        return self.driver.find_element(*ContactPage.contactAdd1)

    def getContactAdd2(self):
        return self.driver.find_element(*ContactPage.contactAdd2)

    def getContactSubmitButton(self):
        return self.driver.find_element(*ContactPage.contactSubmitButton)

    def getContact_ID(self):
        return self.driver.find_element(*ContactPage.contact_ID)

    def getContactSuccessMessage(self):
        return self.driver.find_element(*ContactPage.contactSuccessMessage)

    def getContactFailureMessage(self):
        return self.driver.find_element(*ContactPage.contactFailureMessage)

    def getContactHomeButton (self):
        return self.driver.find_element(*ContactPage.contactHomeButton)

    def getContactErrorOkButton (self):
        return self.driver.find_element(*ContactPage.contactErrorOkButton)

    def getContact2Home (self):
        return self.driver.find_element(*ContactPage.contact2Home)