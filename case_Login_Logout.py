import unittest, time 
import Common, LogUtility
from LoginPage import LoginPage
from selenium import webdriver
from Common import TestCaseInfo
from TestReport import TestReport
from OverViewPage import StatusBar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_TC_Login_Logout(unittest.TestCase):  
	def setUp(self):
		self.driver = webdriver.Chrome(Common.driverPath())
		self.base_url = Common.baseUrl()
		self.testCaseInfo = TestCaseInfo(id=1,name="Login",owner='eli')
		self.testResult = TestReport()
		LogUtility.CreateLoggerFile("Test_TC_Login_Logout")

	def test_Login_Logout(self):
		try:
			self.testCaseInfo.starttime = Common.getCurrentTime()
			#Step1: open base site  
			LogUtility.Log("Open Base site"+self.base_url)
			self.driver.get(self.base_url)
			self.driver.maximize_window()

			#Step2: Open Login page  
			login_page = LoginPage(self.driver)
  
			#Step3: Enter username & password  
			LogUtility.Log("Login web using username")
			login_page.set_username("Admin")
			login_page.set_password("Admin")
  
			time.sleep(15)
			#Checkpoint1: Check the login page upper text
			LogUtility.Log("Check whether sign in dialog exists or not")  
			self.assertEqual(login_page.get_dialog_title(),"Welcome to XWEB EVO")

			#Step4: Click Login
			time.sleep(5)
			login_page.click_login()

			time.sleep(10)

			#Step5: transfer driver to StatusBar
			status_bar = StatusBar(self.driver)
			LogUtility.Log('Menu ID: ' + status_bar.get_menu_id())

			#Step6: Click Logout
			status_bar.click_logout()
			self.testCaseInfo.result = "Pass"
			time.sleep(5)
  
		except Exception as err:
			self.testCaseInfo.errorinfo = str(err)
			LogUtility.Log(("Got error: "+str(err)))
		finally:
			self.testCaseInfo.endtime = Common.getCurrentTime()
			self.testCaseInfo.secondsDuration = Common.timeDiff(self.testCaseInfo.starttime,self.testCaseInfo.endtime)
	def tearDown(self):  
		self.driver.close()
		self.testResult.WriteHTML(self.testCaseInfo)
  
if __name__ == '__main__':
	unittest.main()