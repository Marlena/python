from selenium import selenium
from vars import ConnectionParameters
import unittest2 as unittest
from addons_site import AddonsHomePage
from addons_site import AddonsSearchHomePage

class APITestsWithSelenium(unittest.TestCase):
    
    def setUp(self):
        self.selenium = selenium(ConnectionParameters.server, 
                                ConnectionParameters.port,
                                ConnectionParameters.browser, 
                                ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()
        
    def test_type_method_and_AddonHomePage(self):
        addon_search_page = AddonsHomePage(self.selenium)
        self.selenium.type("name=q", "Pixlr Grabber")
        #results in:
        #14:58:54.255 INFO - Command request: type[name=q, Pixlr Grabber] on session fb1288ec091a46d9a4f8c6b8ba6528b5
        #14:58:54.294 INFO - Got result: OK on session fb1288ec091a46d9a4f8c6b8ba6528b5
        

    def test_type_method_and_AddonSearchHomePage(self):
        addon_search_page = AddonsSearchHomePage(self.selenium)
        #self.selenium.wait_for_page_to_load("3000") 
        self.selenium.type("name=q", "Pixlr Grabber")
        #results in:
        #14:58:59.181 INFO - Command request: type[name=q, Pixlr Grabber] on session f34e3ac290214af08d0f778949c09cb7
        #14:58:59.197 INFO - Got result: ERROR: Element name=q not found on session f34e3ac290214af08d0f778949c09cb7
if __name__ == "__main__":
    unittest.main()