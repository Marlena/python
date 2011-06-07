from selenium import selenium
from addons_site import AddonsHomePage
from addons_site import AddonsDetailsPage
from addons_search_home_page import AddonsSearchHomePage
import pytest
from unittestzero import Assert

class TestAPITestsWithSelenium:
    #Design doc for new details def page(self, 
    #http://chowse.github.com/amo-redux/detail.html
    
    #Design doc for new home page
    #http://chowse.github.com/amo-redux/
    
    #link for new impala version _addon_detail_base_url
    #/z/i/addon/"
    
            
    def test_version_number_locator(self, testsetup):   #ok in impala 
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.true(tab_mix_plus_page.is_element_present("css=span.version"))       

    def test_addon_id_locator(self, testsetup): #ok in impala
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.true(tab_mix_plus_page.is_element_present("//div[@data-id='1122']"))

    def test_author_group_locator(self, testsetup): #ok in impala
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.true(tab_mix_plus_page.is_element_present("//h4[@class='author']/a"))

    def test_first_author_name(self, testsetup): #ok in impala
        #Firebug test
        #Assert.equal("Joe Hewitt",self.selenium.get_text("//h4[@class='author']/a[1]"))
        #Tab Mix Plus test
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.equal("onemen",tab_mix_plus_page.get_text("//h4[@class='author']/a[1]"))

    def test_get_author_children_locators(self, testsetup): #ok in impala      
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        i = 1
        author_list = [ tab_mix_plus_page.get_text("//h4[@class='author']/a[%i]" % (i+1)) 
            for i in range(tab_mix_plus_page.selenium.get_xpath_count("//h4[@class='author']/a")) ]

        #These tests are for Firebug data
        #Assert.equal(5, len(author_locator))
        #Assert.equal("Joe Hewitt",self.selenium.get_text("//h4[@class='author']/a[1]"))
        #Assert.equal("johnjbarton",self.selenium.get_text("//h4[@class='author']/a[2]"))
        #Assert.equal("robcee",self.selenium.get_text("//h4[@class='author']/a[3]"))
        #Assert.equal("FirebugWorkingGroup",self.selenium.get_text("//h4[@class='author']/a[4]"))
        #Assert.equal("Jan Odvarko",self.selenium.get_text("//h4[@class='author']/a[5]"))
        
        #These tests are for 
        Assert.equal(2, len(author_list))
        Assert.equal("onemen",author_list[0])
        Assert.equal("Gary Reyes",author_list[1])

    def test_icon_locator(self, testsetup): #broken in impala
        #Firebug icon
        #image_url = "https://static-cdn.addons.mozilla.net/en-US/firefox/images/addon_icon/1843-32.png?modified=1300780225"   
        #Tab Mix Plus icon        
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        image_url = "https://gs1.adn.edgecastcdn.net/801237/addons-cdn.allizom.org/en-US/firefox/images/addon_icon/1122-32.png?modified=1305054615" #?modified=1305054615"     
        Assert.true(tab_mix_plus_page.is_element_present("css=input[type=img], [src=" +  image_url + "]"))
              
    def test_summary_locator(self, testsetup): 
        #This was written as the details page was being upgraded, thus 2 locators.
        new_impala_summary_locator = "css=p[id=addon-summary]"
        old_zamboni_summary_locator = "css=div[id=addon-summary]>p"
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.true(tab_mix_plus_page.is_element_present(old_zamboni_summary_locator))
    
    def test_ratings_locator(self, testsetup): 
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.true(tab_mix_plus_page.is_element_present("css=span[itemprop='rating']"))
        
    def test_install_locator(self, testsetup):    
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus") 
        Assert.true(tab_mix_plus_page.is_element_present("css=p[class='install-button'] > a"))
        
    def test_contribute_locator(self, testsetup): 
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus") 
        Assert.true(tab_mix_plus_page.is_element_present("css=a[id='contribute-button']"))

    def test_that_details_object_has_selenium(self, testsetup):
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.equal("<class 'selenium.selenium.selenium'>", str(type(tab_mix_plus_page.selenium)) )

    def test_that_details_page_object_opens_the_right_page(self, testsetup):
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.true( len( str(tab_mix_plus_page.page_title) ) > 0)

    def test_navigate_to_detail_page_from_addon_search_page(self, testsetup):
        home_page = AddonsHomePage(testsetup)
        search_page = home_page.search_for("Firebug")
        detail_page = search_page.click_addon("Firebug")
        Assert.equal("Firebug :: Add-ons for Firefox", detail_page.page_title)

    def test_details_page_object_version_number(self, testsetup):
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.true(len (str(tab_mix_plus_page.version_number)) > 0)

    def test_details_page_object_authors(self, testsetup):
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        authors = tab_mix_plus_page.authors
        Assert.equal("onemen", authors[0])
        Assert.equal("Gary Reyes", authors[1])

    def test_details_page_object_summary(self, testsetup):
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        summary = "Tab Mix Plus enhances Firefox's tab browsing capabilities. It includes such features as duplicating tabs, controlling tab focus, tab clicking options, undo closed tabs and windows, plus much more. It also includes a full-featured session manager."
        Assert.equal(summary, tab_mix_plus_page.summary)

    def test_addon_rating(self, testsetup):
        tab_mix_plus_page = AddonsDetailsPage(testsetup, "Tab Mix Plus")
        Assert.equal("4", tab_mix_plus_page.rating)
    
        
if __name__ == "__main__":
    unittest.main()