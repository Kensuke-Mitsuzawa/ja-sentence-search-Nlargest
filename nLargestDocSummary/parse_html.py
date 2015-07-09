#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'

import urllib2
from bs4 import BeautifulSoup

def get_only_text(url):
    """
    return the title and the text of the article
    at the specified url
    """
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page)
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text