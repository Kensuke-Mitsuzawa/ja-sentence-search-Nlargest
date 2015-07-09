__author__ = 'kensuke-mi'

from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./test')


setup(
    test_suite = 'test_all.suite'
)