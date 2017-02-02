#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'

from setuptools import setup, find_packages
import sys
import traceback

sys.path.append('./nLargestDocSummary')
sys.path.append('./test')
python_version = sys.version_info

if python_version >= (3, 0, 0):
    install_requires = ['mecab-python3', 'nltk==3.0.1', 'six', 'JapaneseTokenizer']
else:
    install_requires = ['mecab-python', 'nltk==3.0.1', 'six', 'JapaneseTokenizer']

try:
    import MeCab
    mecabObj = MeCab.Tagger('-Ochasen')
    if python_version >= (3, 0, 0):
        text = '本日は晴天なり'
    else:
        text = u'本日は晴天なり'.encode('utf-8')
    node = mecabObj.parseToNode(text)
    node = node.next
    while node.next is not None:
        if python_version >= (3, 0, 0):
            word_surface = node.surface
        else:
            word_surface = node.surface.decode('utf-8')

        node = node.next
except Exception:
    print(traceback.format_exc())
    sys.exit("Mecab and Mecab-python is not ready to use. Please setup first")


setup(
    author='Kensuke Mitsuzawa',
    name = 'nLargestDocSummary',
    test_suite = 'test_all.suite',
    install_requires = install_requires,
    version = 0.2,
    packages = [
        "nLargestDocSummary",
        "nLargestDocSummary.mecab_wrapper",
        "nLargestDocSummary.models",
        "nLargestDocSummary.parsers",
        "test"
    ],
    include_package_data=True,
    zip_safe=False
)
