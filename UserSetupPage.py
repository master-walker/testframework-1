from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class UserSetupPage(BasePage):
	user_profile = {
		"uname": "userSetup_add_user_username_",
		"passwd": "userSetup_add_user_password_",
		"confirmpw": "userSetup_add_user_password_conf_",
		"firstname": "userSetup_add_user_fname_",
		"lastname": "userSetup_add_user_lname_",
		"profile": "userSetup_add_user_type_",
		"confirm": "userSetup_west_ui_jqgrid_adduser_conf_",
		"cancel": "userSetup_west_ui_jqgrid_adduser_cancel"
	}

	def get_page_id(self):
		pcnts = self.driver.find_elements_by_xpath("//div[starts-with(@id, 'pCnt_')]")
		ID = ''
		for pcnt in pcnts:
			if pcnt.is_displayed():
				pcnt_id = pcnt.get_attribute('id')
				ID = pcnt_id.split('_')[-1]
		if ID is not '':
				#print 'PageID: ' + ID
				return str(ID)
		else:
			#print 'getPageID failed'
			raise Exception("get Page ID failed")

	def get_page_title(self):
		titleID = "hdrTitle_" + self.get_page_id()
		return self.driver.find_element(By.ID, titleID).get_attribute("textContent")

	def add_user(self, username, password, firstname="", lastname="", profile="admin"):
		ID = self.get_page_id()
		newBtnID = "userSetup_west_ui_jqgrid_btn_add_" + ID
		newBtn = self.driver.find_element(By.ID, newBtnID)
		newBtn.click()

		userName = self.driver.find_element(By.ID, UserSetupPage.user_profile['uname'] + ID)
		passwd = self.driver.find_element(By.ID, UserSetupPage.user_profile['passwd'] + ID)
		confirmPasswd = self.driver.find_element(By.ID, UserSetupPage.user_profile['confirmpw'] + ID)
		firstName = self.driver.find_element(By.ID, UserSetupPage.user_profile['firstname'] + ID)
		lastName = self.driver.find_element(By.ID, UserSetupPage.user_profile['lastname'] + ID)
		profileSel = Select(self.driver.find_element(By.ID, UserSetupPage.user_profile['profile'] + ID))
		confirmBtn = self.driver.find_element(By.ID, UserSetupPage.user_profile['confirm'] + ID)
		cancelBtn = self.driver.find_element(By.ID, UserSetupPage.user_profile['cancel'])

		userName.send_keys(username)
		passwd.send_keys(password)
		confirmPasswd.send_keys(password)
		firstName.send_keys(firstname)
		lastName.send_keys(lastname)
		profileSel.select_by_visible_text(profile)
		confirmBtn.click()





