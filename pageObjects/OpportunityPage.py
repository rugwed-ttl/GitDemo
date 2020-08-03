from selenium.webdriver.common.by import By


class OpportunityPage:

    def __init__(self,driver):
        self.driver = driver

    optyRadioButton = (By.ID, "com.tatamotors.eguruhybrid:id/radio_opty")
    optyCreateNew = (By.ID, "com.tatamotors.eguruhybrid:id/tvCreateNew")
    optyVcSearchField = (By.ID, "com.tatamotors.eguruhybrid:id/edit_text_search")
    optyVcSearchButton = (By.ID, "com.tatamotors.eguruhybrid:id/image_view_search")
    optyVcList = (By.ID, "com.tatamotors.eguruhybrid:id/container")
    optyVehicleAppField = (By.XPATH, "//android.widget.Spinner[@bounds='[28,737][525,803]']")
    optyVehicleApp = (By.XPATH, "//android.widget.TextView[@text='Fruits & Vegetables']")
    optyBodyType = (By.XPATH,"//android.widget.TextView[@text='High Deck']" )
    optyCustomerTypeField = (By.XPATH,"//android.widget.Spinner[@bounds='[555,737][1052,803]']" )
    optyCustomerType = (By.XPATH,"//android.widget.TextView[@text='Government Existing']" )
    optySOCfield = (By.XPATH,"//android.widget.Spinner[@bounds='[28,934][525,1000]']")
    optySOC = (By.XPATH,"//android.widget.TextView[@text='Customer Meet']")
    optyQuantity = (By.ID,"com.tatamotors.eguruhybrid:id/editText")
    optyLPMfield = (By.XPATH,"//android.widget.Spinner[@bounds='[28,1131][525,1197]']")
    optyLPM = (By.XPATH,"//android.widget.TextView[@text='August']")
    optyUsageCatField = (By.XPATH,"//android.widget.Spinner[@bounds='[28,1328][525,1394]']")
    optyUsageCat = (By.XPATH,"//android.widget.TextView[@text='Captive']")
    optyMMGfield = (By.XPATH,"//android.widget.EditText[@bounds='[555,1131][1052,1197]']")
    optyMMG = (By.XPATH,"//android.widget.EditText[@bounds='[555,1131][1052,1197]']")
    optySearchContact = (By.ID,"com.tatamotors.eguruhybrid:id/edit_text_search_contact")
    optySearchConButton = (By.ID,"com.tatamotors.eguruhybrid:id/button_search_contact")
    optySearchSubmit = (By.ID,"com.tatamotors.eguruhybrid:id/submitButton")
    optyMessage = (By.ID, "android:id/message")


    def getOptyRadioButton(self):
        return self.driver.find_element(*OpportunityPage.optyRadioButton)

    def getOptyCreateNew(self):
        return self.driver.find_element(*OpportunityPage.optyCreateNew)

    def getOptyVcSearchField(self):
        return self.driver.find_element(*OpportunityPage.optyVcSearchField)

    def getOptyVcSearchButton (self):
        return self.driver.find_element(*OpportunityPage.optyVcSearchButton)

    def getOptyVcList(self):
        return self.driver.find_element(*OpportunityPage.optyVcList)

    def getOptyVehicleAppField(self):
        return self.driver.find_element(*OpportunityPage.optyVehicleAppField)

    def getOptyVehicleApp(self):
        return self.driver.find_element(*OpportunityPage.optyVehicleApp)

    def getOptyBodyType(self):
        return self.driver.find_element(*OpportunityPage.optyBodyType)

    def getOptyCustomerTypeField(self):
        return self.driver.find_element(*OpportunityPage.optyCustomerTypeField)

    def getOptyCustomerType(self):
        return self.driver.find_element(*OpportunityPage.optyCustomerType)

    def getOptySOCfield(self):
        return self.driver.find_element(*OpportunityPage.optySOCfield)

    def getOptySOC(self):
        return self.driver.find_element(*OpportunityPage.optySOC)

    def getOptyQuantity(self):
        return self.driver.find_element(*OpportunityPage.optyQuantity)

    def getOptyLPMfield(self):
        return self.driver.find_element(*OpportunityPage.optyLPMfield)

    def getOptyLPM(self):
        return self.driver.find_element(*OpportunityPage.optyLPM)


    def getOptyUsageCatField(self):
        return self.driver.find_element(*OpportunityPage.optyUsageCatField)


    def getOptyUsageCat(self):
        return self.driver.find_element(*OpportunityPage.optyUsageCat)

    def getOptyMMGfield(self):
        return self.driver.find_element(*OpportunityPage.optyMMGfield)

    def getOptyMMG(self):
        return self.driver.find_element(*OpportunityPage.optyMMG)

    def getOptySearchContact(self):
        return self.driver.find_element(*OpportunityPage.optySearchContact)

    def getOptySearchConButton(self):
        return self.driver.find_element(*OpportunityPage.optySearchConButton)

    def getOptySearchSubmit(self):
        return self.driver.find_element(*OpportunityPage.optySearchSubmit)

    def getOptyMessage (self):
        return self.driver.find_element(*OpportunityPage.optyMessage)





