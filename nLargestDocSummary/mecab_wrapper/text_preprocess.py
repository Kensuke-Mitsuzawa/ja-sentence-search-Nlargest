#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from builtins import str
import unicodedata
import re
import sys
import six
__author__ = 'kensuke-mi'

python_version = sys.version_info

if python_version >= (3,0,0):
    kanji = r'[一-龠]+'
    hiragana = r'[ぁ-ん]+'
    zenkaku_katakana = r'[ァ-ヴ]+'
    hankaku_symbol_prefix = r'[^A-Za-z]'
    hankaku_symbol_seq = r'[A-Za-z]'
else:
    kanji = ur'[一-龠]+'
    hiragana = ur'[ぁ-ん]+'
    zenkaku_katakana = ur'[ァ-ヴ]+'
    hankaku_symbol_prefix = ur'[^A-Za-z]'
    hankaku_symbol_seq = ur'[A-Za-z]'


def normalize_text(text):
    """
    Text should be codee in UTF-8
    :param text:
    :return:
    """

    try:
        text = unicodedata.normalize('NFKC', text)
    except TypeError:
        sys.exit("argument should be coded in UTF-8")

    if python_version >= (3, 0, 0):
        text = re.sub(r'˗|֊|‐|‑|‒|–|⁃|⁻|₋|−', '-', text)
        text = re.sub(r'﹣|－|ｰ|—|―|─|━', 'ー', text)
        text = re.sub(r'~|∼|∾|〜|〰|～', '', text)

        text = re.sub(r' +', ' ', text)
        text = re.sub(r'^\s+(.+)$', r'\1', text)
        text = re.sub(r'(.+)\s+$', r'\1', text)
    else:
        text = re.sub(ur'˗|֊|‐|‑|‒|–|⁃|⁻|₋|−', u'-', text)
        text = re.sub(ur'﹣|－|ｰ|—|―|─|━', u'ー', text)
        text = re.sub(ur'~|∼|∾|〜|〰|～', u'', text)

        text = re.sub(ur' +', u' ', text)
        text = re.sub(ur'^\s+(.+)$', ur'\1', text)
        text = re.sub(ur'(.+)\s+$', ur'\1', text)

    # 半角カタカナはすでに全角カタカナに正規化されている
    # 全角英数はすでに半角英数に正規化されている前提
    pattern = u'{}|{}|{}|{}'.format(hiragana, zenkaku_katakana, hankaku_symbol_prefix, kanji)
    if python_version >= (3, 0, 0):
        while re.findall(r'({})\s+({})'.format(pattern, pattern), text) != []:
            text = re.sub(r'({})\s+({})'.format(pattern, pattern), r'\1\2', text)


        pattern = u'{}|{}|{}'.format(hiragana, zenkaku_katakana, kanji)
        while re.findall(r'({})\s+({})'.format(pattern, hankaku_symbol_seq), text) != []:
            text = re.sub(r'({})\s+({})'.format(pattern, hankaku_symbol_seq), r'\1\2', text)
    else:
        while re.findall(ur'({})\s+({})'.format(pattern, pattern), text) != []:
            text = re.sub(ur'({})\s+({})'.format(pattern, pattern), r'\1\2', text)


        pattern = u'{}|{}|{}'.format(hiragana, zenkaku_katakana, kanji)
        while re.findall(ur'({})\s+({})'.format(pattern, hankaku_symbol_seq), text) != []:
            text = re.sub(ur'({})\s+({})'.format(pattern, hankaku_symbol_seq), ur'\1\2', text)


    return text


def test():
    text = u'あるBさんとCさんがーで〜で-ーだった。   やばい   。＆＊（）＆％。　　プログラミング　Cは難しい。でもLanguage C＋＋はそんなに難しくない。'
    res = normalize_text(text)



if __name__ == '__main__':
    import sys
    import codecs
    test()
    sys.exit()

    #path_to_text = '../fuman_pipeline/resources/input/fuman_hotel.tsv'
    with codecs.open(path_to_text, 'r', 'utf-8') as f_obj:
        for line in f_obj.readlines():
            print(normalize_text(line).encode('utf-8'))