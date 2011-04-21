#! /usr/bin/env python
#!/usr/bin/env python


from xml.dom.minidom import parse
import xml.dom.minidom
import urllib

def printResults(results):
	addon = myResults.getElementsByTagName("addon")
	for addon in addons:
		print ("***Addon***")
		print ("Name: %s" % addon.getElementsByTagName("name")[0].childNodes[0].data)
		for author in addon.getElementsByTagName("author"):
			print ("Author Name: %s" % author.getElementsByTagName("name")[0].childNodes[0].data)
			
			
#open an xml file and parse it into a dom
myDoc = parse (urllib.urlopen('https://addons.allizom.org/en-us/firefox/api/1.5/search/fire'))
myResults = myDoc.getElementsByTagName("searchresults")[0]
#Get all the addon elements in the library
addons = myResults.getElementsByTagName("addon")
#Print each addon's title and name(s)
printResults(myResults)

"""
#insert a new addon in the library
newaddon = myDoc.createElement("addon")
newaddonTitle = myDoc.createElement("title")
titleText = myDoc.createTextNode("Beginning Python")
newaddonTitle.appendChild(titleText)
newaddon.appendChild(newaddonTitle)
newaddonname = myDoc.createElement("name")
nameName = myDoc.createTextNode("PeterNorton, et al")
newaddonname.appendChild(nameName)
newaddon.appendChild(newaddonname)
myResults.appendChild(newaddon)
print("Added a new addon!")
printLibrary(myResults)

#Find ellison addon
for addon in myResults.getElementsByTagName("addon"):
	for name in addon.getElementsByTagName("name"):
		if name.childNodes[0].data.find("Ellison") != -1:
			removedaddon = myResults.removeChild(addon)
			removedaddon.unlink()
print ("Removed a addon.")
"""