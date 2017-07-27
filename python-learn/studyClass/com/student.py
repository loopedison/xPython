#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_self(self):
        print('name:%s;\tscore:%s' %(self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score


