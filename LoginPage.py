from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):

	username = (By.ID, 'username')
	password = (By.ID, 'password')
	loginBtn = (By.ID, 'loginButton')
	upperText = (By.ID, 'login-welcome1')

	def set_username(self, username):
		name = self.driver.find_element(*LoginPage.username)
		name.send_keys(username)

	def set_password(self, password):
		pwd = self.driver.find_element(*LoginPage.password)
		pwd.send_keys(password)

	def get_dialog_title(self):
		'''login-welcome1'''
		upper = self.driver.find_element(*LoginPage.upperText)
		return upper.get_attribute('textContent')

	def click_login(self):
		loginButton = self.driver.find_element(*LoginPage.loginBtn)
		loginButton.click()



