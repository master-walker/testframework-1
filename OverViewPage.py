import time
from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StatusBar(BasePage):
	logout = (By.ID, "logout")
	menu = (By.XPATH, "//button[span/text()='Menu']")
	desktop = (By.XPATH, "//button[span/text()='Desktop']")

	def click_logout(self):
		logoutButton = self.driver.find_element(*StatusBar.logout)
		logoutButton.click()

	def click_desktop(self):
		desktopButton = self.driver.find_element(*StatusBar.desktop)
		desktopButton.click()

	def click_menu(self):
		menuButton = self.driver.find_element(*StatusBar.menu)
		menuButton.click()

	def get_menu_id(self):
		button = self.driver.find_element(*StatusBar.menu)
		button_id = button.get_attribute('id')
		ID = button_id.split('_')[-1]
		#print 'Menu ID: ' + ID
		return str(ID)

	def click_menu_task(self, section="", task=""):
		ID = self.get_menu_id()
		if section == "System" or section == "":
			sectionID = "ui-accordion-XMenu_" + ID + "-header-0"
		elif section == "Tools":
			sectionID = "ui-accordion-XMenu_" + ID + "-header-1"
		elif section == 'Acq':
			sectionID = "ui-accordion-XMenu_" + ID + "-header-2"

		if task == "UserSetup" or task == "":
			taskName = "tskUSERSETUP-MN"
		#elif task == "DeviceSetup":
		#	pass

		menuPanel = self.driver.find_element(By.ID, 'XMenuPH_' + ID)
		sectionTab = menuPanel.find_element(By.ID, sectionID)
		sectionTab.click()
		time.sleep(5)
		taskPanel = menuPanel.find_element(By.NAME, taskName)
		taskPanel.click()
		time.sleep(5)

	def click_shortcuts(self, icon='Overview'):
		ID = self.get_menu_id()
		if icon == 'Parameters':
			iconID = 'parprog_' + ID
		elif icon == 'Overview':
			iconID = 'home_' + ID
		elif icon == 'DeviceView':
			iconID = 'deviceview_' + ID
		elif icon == 'Chart':
			iconID = 'chart_' + ID
		elif icon == 'Layout':
			iconID = 'layout_' + ID
		shortcut = self.driver.find_element(By.ID, iconID)
		shortcut.click()

class Widget_ActiveAlarms(BasePage):
	pass

class Widget_GlobalCommands(BasePage):
	pass

class Widget_HaccpPrint(BasePage):
	pass
