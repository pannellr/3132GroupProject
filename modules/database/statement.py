#!/usr/bin/env python

class Statement:
    string = None

    def __init__(self):
        string = ''

    def setString(self, s):
        self.string = s

    def getString(self):
        return self.string
