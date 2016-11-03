import time
from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Widget_ParProg(BasePage):
	deviceSelection = (By.XPATH, '//select[@class="dvs"]')
	actionSelection = (By.XPATH, '//select[@class="pt"]')
	groupSelection = (By.ID, 'gs_g')
	unitSelection = (By.ID, 'gs_u')
	executeButton = (By.XPATH, '//button[contains(@class,"execute")]')

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

	def select_device(self, device):
		devSel = Select(self.driver.find_element(*Widget_ParProg.deviceSelection))
		devSel.select_by_visible_text(device)

	def select_action(self, action):
		actSel = Select(self.driver.find_element(*Widget_ParProg.actionSelection))
		executeBtn = self.driver.find_element(*Widget_ParProg.executeButton)
		time.sleep(5)
		actSel.select_by_visible_text(action)
		executeBtn.click()

	def select_group(self, group):
		groupSel = Select(self.driver.find_element(*Widget_ParProg.groupSelection))
		groupSel.select_by_visible_text(group)

	def select_unit(self, unit):
		unitSel = Select(self.driver.find_element(*Widget_ParProg.unitSelection))
		unitSel.select_by_visible_text(unit)

	def edit_par(self, par, newValue, newVis=''):
		parTable = self.driver.find_element(By.ID, 'tabpar_' + self.get_page_id())
		parCell = parTable.find_element(By.XPATH, '//td[@title="'+ par + '"]')
		parRow = parCell.find_element_by_xpath('..')   # find the parent element of "parCell", use xpath ".."
		rowID = parRow.get_attribute('id')
		parCell.click()
		parEdit = parRow.find_element(By.ID, rowID+'_vc')
		if parEdit.tag_name == "input":
			parEdit.clear()
			parEdit.send_keys(newValue)
		else:
			parSel = Select(parEdit)
			parSel.select_by_visible_text(newValue)

		if newVis != '':
			parVis = Select(parRow.find_element(By.ID, rowID+'_v'))
			parVis.select_by_visible_text(newVis)

		parRow.send_keys(Keys.RETURN)
		time.sleep(1)

	def select_all(self):
		selectAll = self.driver.find_element(By.ID, 'cb_tabpar_' + self.get_page_id())
		selectAll.click()