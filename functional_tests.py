import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        #Ryan heard about a coo new online to-do app.
        #He goes to check out its home page
        self.browser.get('http://localhost:8000')

        #He notices the page title mention "To-do"
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #He is invited to enter a to-do item straight away!
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #He types "Buy peacock feathers" into a text box    
        inputbox.send_keys('Buy peacock feathers')
        #When he hits enter, the page updates and the page lists:
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
    
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
                        "New To-Do Item did not appear in table")
        #There is still a test box inviting him to add another item.
        #He enters "Use peacock feathers to make a fly"

        self.fail('Finish the test!')
        #The page updates again and now shows both item on his 			list.             Then he sees that the site has generated a 			unique url for him             -- there is some explanatory 		text to that effect

        #He visits that URL- his to-do list is still there

        #Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main()


