#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'

from setuptools import setup, find_packages
import sys

sys.path.append('./nLargestDocSummary')
sys.path.append('./test')

install_require = ['nltk==3.0.1']

try:
    import MeCab
    mecabObj = MeCab.Tagger('-Ochasen')
    text = u'本日は晴天なり'.encode('utf-8')
    node = mecabObj.parseToNode(text)
    node = node.next
    while node.next is not None:
        word_surface = node.surface.decode('utf-8')
        node = node.next
except Exception as e:
    print e
    sys.exit("Mecab and Mecab-python is not ready to use. Please setup first")


setup(
    author='Kensuke Mitsuzawa',
    name = 'nLargestDocSummary',
    test_suite = 'test_all.suite',
    install_requires = install_require,
    version = 0.2,
    packages = [
        "nLargestDocSummary",
        "nLargestDocSummary.mecab_wrapper",
        "nLargestDocSummary.models",
        "nLargestDocSummary.parsers",
        "test"
    ],
)
