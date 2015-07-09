__author__ = 'kensuke-mi'

import unittest
from test_parser import TestParser
from test_summarizer import TestSummarizer

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestParser))
    suite.addTest(unittest.makeSuite(TestSummarizer))


    return suite