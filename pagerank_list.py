#!/usr/bin/env python

import pagerank
import sys
import json

file = sys.argv[1]
file_data = open(file, "r").read()
json_data = json.loads(file_data)
pages_dict = json_data
#pages_dict = {'Marlena' : 'http://marlenacompton.com', 'Chris McMahon' : 'http://chrismcmahonsblog.blogspot.com/', 'Google':'http://google.com', "Lisa Crispin" : 'http://lisacrispin.com/wordpress/', 'James Bach' : 'http://www.satisfice.com/blog/', 'Sauce Labs Blog': 'http://saucelabs.com/blog/', 'Corey Goldberg': 'http://coreygoldberg.blogspot.com', "David Burns":"http://www.theautomatedtester.co.uk/"}

pages = pages_dict.keys()

def printSortedPageRankList( pages ):
	for page in sorted(pages ):
		url = pages_dict[page]
		rank = pagerank.get_pagerank(url)
		print page + "'s pagerank is: " + rank

printSortedPageRankList( pages )
