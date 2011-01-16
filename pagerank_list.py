#!/usr/bin/env python

#pagerank is from Corey Goldberg's post:
#http://coreygoldberg.blogspot.com/2010/01/python-lookup-google-pagerank-score.html
#The code on google code:
#http://code.google.com/p/corey-projects/source/browse/trunk/python2/pagerank.py

import pagerank
import sys
import json

file = sys.argv[1]
file_data = open(file, "r").read()
json_data = json.loads(file_data)
pages_dict = json_data

pages = pages_dict.keys()

def printSortedPageRankList( pages ):
        for page in sorted(pages ):
                url = pages_dict[page]
                rank = pagerank.get_pagerank(url)
                print page + "'s pagerank is: " + rank

printSortedPageRankList( pages )
