# -*- coding: utf-8 -*-
class Event:
    def __init__(self, name, count=1):
        if not name.isidentifier():
            raise ValueError("names must be valid identifier")
        self.name = name
        self.count = count
