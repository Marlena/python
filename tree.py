#! /usr/bin/env python

class Tree:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next