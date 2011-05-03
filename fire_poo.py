#! /usr/bin/env python
#!/usr/bin/env python


from xml.dom.minidom import parse
import xml.dom.minidom
from BeautifulSoup import BeautifulStoneSoup, SoupStrainer
import urllib2
import re

def printResults(results):
	addons = myResults.getElementsByTagName("addon")
	for addon in addons:
		print ("***Addon***")
		print ("Name: %s" % addon.getElementsByTagName("name")[0].childNodes[0].data)
		for author in addon.getElementsByTagName("author"):
			print ("Author Name: %s" % author.getElementsByTagName("name")[0].childNodes[0].data)
			
			

myDoc = parse (urllib2.urlopen('https://addons.allizom.org/en-us/firefox/api/1.5/search/firebug'))
myResults = myDoc.getElementsByTagName("searchresults")[0]

#print "****Get type***"
#print myResults.getElementsByTagName("addon")



#Get all the addon elements in the library
#addons = myResults.getElementsByTagName("addon")

#Print each addon's title and name(s)
#printResults(myResults)

#############################BEAUTIFUL SOUP####################################
xml_soup = BeautifulStoneSoup(urllib2.urlopen('https://addons.allizom.org/en-us/firefox/api/1.5/search/fire'))

#print xml_soup.addon
addon_id = xml_soup.addon["id"]
addon_name = xml_soup.addon.nameTag.string
addon_type = xml_soup.addon.type.string
addon_type_num = xml_soup.addon.type["id"]
addon_version = xml_soup.addon.version.string
print 'Name is: ' + addon_name + '\tID is: ' + addon_id + '\tType is: ' + addon_type + "\tType Number is: " + addon_type_num
print 'Version is:' + addon_version

all_addons = xml_soup.searchresults
#print "Number in all_addons:\t" + str(len(xml_soup.findAll('addon')))

#print xml_soup.findAll(lambda tag: tag.nameTag.string == "Firebug")
#print xml_soup.find(text="FireGestures")
#print xml_soup.find(text='FireGestures').parent.parent #gets complete xml for addon "FireGestures"
#print xml_soup.find(text='FireGestures').findNext() #gets extenstion tag for FireGestures

#string below gets the id into a string based on the addon name.  
numeric_id_tuple =  xml_soup.find(text='FireGestures').findParent().findParent().attrs[0] #"get id for addon name"
numeric_id = str( numeric_id_tuple[1] ) #numeric_id is now a string

#print xml_soup.findAll(id=numeric_id)  #prints just the Firegestures xml
#firegestures_xml = xml_soup.findAll(id=numeric_id)
firegestures_xml = xml_soup.find(text='Firefox 3 theme for Firefox 4').findParent().findParent()
print firegestures_xml.version.string 


#Here is the code for getting an addon's id field.
#def get_addon_id(self, addon_name):
    #numeric_id =  self.parsed_xml.find(text=addon_name).findParent().findParent().attrs[0] #"get id for addon name"
    #return numeric_id[1]
