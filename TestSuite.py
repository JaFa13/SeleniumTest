__author__ = 'Joseph'


import unittest


class TestSuite():

     def __init__(self, testClass):
          self.TestClass = testClass


     def createPreLoginSuite(self):

        tests = ['test_01checkMainPage','test_02signUP']

        return unittest.TestSuite(map(self.TestClass, tests))


     def createPostLoginSuite(self):

        tests = ['test_03Login','test_05SearchRepository']

        return unittest.TestSuite(map(self.TestClass, tests))