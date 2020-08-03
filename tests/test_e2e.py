import time
#from selenium import webdriver
from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#import pytest
from pageObjects.ContactPage import ContactPage
from pageObjects.HomePage import HomePage
from pageObjects.OpportunityPage import OpportunityPage
from utilities.BaseClass import BaseClass

#from appium import webdriver


class TestOne(BaseClass):

    def test_e2e(self):
        try:
            log = self.getLogger()
            time.sleep(5)
            homePage = HomePage(self.driver)
            homePage.getPermission1().click()
            homePage.getPermission2().click()
            homePage.getPermission1().click()
            homePage.getUsername().send_keys("DUSER146")
            log.info("Entered UserName 'DUSER146' Successfully")
            homePage.getPassword().send_keys("Tata@0909")
            log.info("Entered Password Successfully")
            homePage.getLoginSubmitButton().click()
            time.sleep(3)
            Epin = 0
            while Epin < 8:
                homePage.getEnterPin().click()
                Epin += 1
                time.sleep(0.5)
            time.sleep(2)
            homePage.getVersionUpdate ().click ()
            log.info("Login Successfully by using DSM credentials")
        except Exception as e :
            log.error(e)
            self.Screenshots()

    def test_contact(self):
        log = self.getLogger()
        time.sleep (2)

        try :
            contactPage = ContactPage(self.driver)
            contactPage.getContactButton().click()
            time.sleep (2)
            log.info ("Create Contact Page")
            contactPage.getContactName ().send_keys ("Test")
            log.info ("Entered Name as 'Test' ")
            contactPage.getContactLName ().send_keys ("User")
            log.info ("Entered lastname as 'User' ")
            contactPage.getContactNumber ().send_keys ("9898989898")
            log.info ("Entered mobile number as '9898989898' ")
            time.sleep (6)
            # driver.find_element_by_id("android:id/button2").click()
            State = contactPage.getContactState ()
            State.send_keys ('Maharashtra')
            log.info ("Selected State as 'Maharashtra' ")
            Taluka = contactPage.getContactTaluka ()
            Taluka.send_keys ('Arv')
            log.info ("Selected Taluka as 'Arvi' ")
            time.sleep (10)
            User_Action = TouchAction (self.driver)
            User_Action.tap (x=957, y=1110).perform ()
            time.sleep (3)
            # User_Action.tap (x=842, y=1066).perform ()
            time.sleep (3)
            User_Action.press (x=874, y=1350).move_to (x=889, y=900).release ().perform ()
            time.sleep (3)
            add = contactPage.getContactAdd1 ()
            add.send_keys ("add1")
            log.info ("Entered address line1 as 'Add1' ")
            add2 = contactPage.getContactAdd2 ()
            add2.send_keys ("add2")
            log.info ("Entered address line2 as 'Add2' ")
            time.sleep (5)
            contactPage.getContactSubmitButton ().click ()
            time.sleep (35)
        except Exception as e :
            log.exception (e)
            assert False
        try :
            Contact_Id = contactPage.getContact_ID ().text
            ContactSuccess = contactPage.getContactSuccessMessage ().text
            # log.info (f'Final message:{Contact_Id}, {ContactSuccess}')
            log.info ("Success Message- " + ContactSuccess)
            log.info ("Contact Id- " + Contact_Id)
            self.Screenshots ()
            contactPage.getContactHomeButton ().click ()
        except Exception as e :
            Contact_msg = contactPage.getContactFailureMessage ().text
            log.exception (Contact_msg)
            contactPage.getContactErrorOkButton ().click ()
            contactPage.getContact2Home ().click ()
            self.Screenshots ()
            assert False

    def test_opportuinity(self):
        try :
            log = self.getLogger ()
            opportunityPage = OpportunityPage (self.driver)
            opportunityPage.getOptyRadioButton ().click ()
            log.info ("Clicked on Opportunity radio button")
            opportunityPage.getOptyCreateNew ().click ()
            log.info ("Moved on Create Opportunity page")
            opportunityPage.getOptyVcSearchField ().send_keys ("28182024ABFR")
            opportunityPage.getOptyVcSearchButton ().click ()
            log.info ("Entered VC number '28182024ABFR' ")
            opportunityPage.getOptyVcList ().click ()
            opportunityPage.getOptyVehicleAppField ().click ()
            opportunityPage.getOptyVehicleApp ().click ()
            log.info ("Selected Vehicle application as 'Fruits & Vegetables' ")  # Market Load
            opportunityPage.getOptyBodyType ().click ()
            log.info ("Selected Body type as 'High Deck' ")  # Cowl
            opportunityPage.getOptyCustomerTypeField ().click ()
            opportunityPage.getOptyCustomerType ().click ()
            log.info ("Selected Customer type as 'Government Existing' ")  # First Time
            opportunityPage.getOptySOCfield ().click ()
            opportunityPage.getOptySOC ().click ()
            log.info ("Selected Source of contact as 'Customer Meet' ")  # Cold Call
            opportunityPage.getOptyQuantity ().send_keys (2)
            log.info ("Selected quantity as '2' ")
            opportunityPage.getOptyLPMfield ().click ()
            opportunityPage.getOptyLPM ().click ()
            log.info ("Selected Likely Purchase month as 'August' ")
            opportunityPage.getOptyUsageCatField ().click ()
            opportunityPage.getOptyUsageCat ().click ()
            log.info ("Selected Usage Category as 'Captive' ")
            opportunityPage.getOptyMMGfield ().click ()
            opportunityPage.getOptyMMG ().send_keys ("Akol")
            time.sleep (3)
            log.info ("Entered MMGeo location as 'Akola' ")
            User_Action = TouchAction (self.driver)
            User_Action.tap (x=686, y=1228).perform ()
            opportunityPage.getOptySearchContact ().send_keys ("8999413547")
            opportunityPage.getOptySearchConButton ().click ()
            log.info ("Entered '8999413547' mobile number to create opportunity for this contact")
            time.sleep (10)
            User_Action.tap (x=83, y=1196).perform ()
            opportunityPage.getOptySearchSubmit ().click ()
            time.sleep (40)
            log.info ("Entered all opty details and clicked on Submit button ")
            Fmsg = opportunityPage.getOptyMessage ().text
            log.error ("Opportunity is not created successfully due to error : " + Fmsg)
            assert False
        except Exception as e :
            log.info ("This message is because of error" + e)
            assert False
        finally :
            self.Screenshots ()
