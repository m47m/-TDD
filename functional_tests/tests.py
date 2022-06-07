# from typing_extensions import Self
# from urllib import response
#from matplotlib.pyplot import table
from tracemalloc import start
from selenium import webdriver
# import unittest
import time
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class NewVisitorTest(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	
	# def check_for_row_in_list_table(self,row_text):
	# 	table = self.browser.find_element_by_id('id_list_table')
	# 	rows = table.find_elements_by_tag_name('tr')
	# 	self.assertIn(row_text,[row.text for row in rows])
	
	def wait_for_row_in_list_table(self,row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text,[row.text for row in rows])
				return
			except (AssertionError ,WebDriverException) as e:
				if time.time() - start_time >MAX_WAIT:
					raise e
				time.sleep(0.5)
		

	def test_can_start_a_list_for_one_user(self):
		# self.browser.get('http://localhost:8000')

		self.browser.get(self.live_server_url)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		#time.sleep(1)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')


		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		#time.sleep(1)

		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
		#self.fail('finish the test')
	
	def test_multiple_users_can_start_lists_at_different_urls(self):
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url,'/lists/.+')


		self.browser.quit()

		self.browser = webdriver.Firefox()

		self.browser.get(self.live_server_url)

		page_text = self.browser.find_element_by_tag_name('body').text

		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly' ,page_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')

		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')

		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url,'/lists/.+')
		self.assertNotEqual(francis_list_url,edith_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers' ,page_text)
		self.assertIn('Buy milk',page_text)

	def test_layout_and_styling(self):
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)


		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta=10
		)

		
		inputbox.send_keys('testing')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: testing')

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta=10
		)
	

# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')
