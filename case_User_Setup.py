import unittest, time
import Common, LogUtility
from LoginPage import LoginPage
from UserSetupPage import UserSetupPage
from selenium import webdriver
from Common import TestCaseInfo
from TestReport import TestReport
from OverViewPage import StatusBar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_TC_User_Setup(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(Common.driverPath())
		self.base_url = Common.baseUrl()
		self.testCaseInfo = TestCaseInfo(id=1,name="UserSetup",owner='eli')
		self.testResult = TestReport()
		LogUtility.CreateLoggerFile("Test_TC_User_Setup")

	def test_UserSetup(self):
		try:
			self.testCaseInfo.starttime = Common.getCurrentTime()
			#Step1: Login as Admin
			LogUtility.Log("Open Base site"+self.base_url)
			self.driver.get(self.base_url)
			self.driver.maximize_window()
			login_page = LoginPage(self.driver)
			login_page.set_username("Admin")
			login_page.set_password("Admin")
			time.sleep(5)
			login_page.click_login()
			time.sleep(5)

			#Step2: Click button "Menu"
			status_bar = StatusBar(self.driver)
			LogUtility.Log('Menu ID: ' + status_bar.get_menu_id())
			status_bar.click_menu()

			#Step3: Click section "System" - "User Setup"
			status_bar.click_menu_task("System", "UserSetup")
			time.sleep(10)

			#Step4: Check if "User Setup" really opened
			user_setup = UserSetupPage(self.driver)
			LogUtility.Log("User Setup page has been opened or not")
			self.assertEqual(user_setup.get_page_title(),'User Setup')
			user_setup.add_user('hall', 'hall', 'ha', 'll', 'user')
			time.sleep(10)
			self.testCaseInfo.result = "Pass"

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