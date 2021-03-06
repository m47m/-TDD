from typing_extensions import Self
from urllib import response
#from matplotlib.pyplot import table
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	
	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')


		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		self.check_for_row_in_list_table('1: Buy peacock feathers')


		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.fail('finish the test')
	

if __name__ == '__main__':
	unittest.main(warnings='ignore')
