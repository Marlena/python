#! /usr/bin/env python

class Bunch(dict):
    #gets you dict funciton and can pass in keywords
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self