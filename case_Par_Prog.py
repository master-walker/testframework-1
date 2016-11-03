#!-*- coding: utf-8 -*-
import unittest, time 
import Common, LogUtility
from LoginPage import LoginPage
from selenium import webdriver
from Common import TestCaseInfo
from TestReport import TestReport
from OverViewPage import StatusBar
from ParProgPage import Widget_ParProg
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_TC_Par_Prog(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(Common.driverPath())
		self.base_url = Common.baseUrl()
		self.testCaseInfo = TestCaseInfo(id=1,name="ParProg",owner='eli')
		self.testResult = TestReport()
		LogUtility.CreateLoggerFile("Test_TC_Par_Prog")

	def test_Par_Prog(self):
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

			#Step2: Click shortcut 'Parameters'
			status_bar = StatusBar(self.driver)
			LogUtility.Log('Menu ID: ' + status_bar.get_menu_id())
			status_bar.click_shortcuts('Parameters')

			#Step3: Select device, and then execute "Read"
			parProg_widget = Widget_ParProg(self.driver)
			parProg_widget.select_device('RS1-010 New_XR60CX')
			parProg_widget.select_action('Read')
			time.sleep(10)

			#Step4: Select group "Regulation", and select unit "C"
			parProg_widget.select_group('Regulation')
			parProg_widget.select_unit(u'°C')
			parProg_widget.edit_par('CCS', '12.0')

			#Step5: Select group "All", and select unit "All"
			parProg_widget.select_group("All")
			parProg_widget.select_unit("All")
			parProg_widget.edit_par("SEt", '55.5')
			parProg_widget.edit_par("HES", '22')
			parProg_widget.edit_par("dPC", 'dEF', 'Pr2')
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