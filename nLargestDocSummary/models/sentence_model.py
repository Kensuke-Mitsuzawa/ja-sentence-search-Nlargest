#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'


class Sentence(object):
    __slots__ = ("_text", "_MecabTokenizer", "_tokens")

    def __init__(self, text, MecabTokenizer, sentenceEOS=u'。'):
        self._text = text.strip(sentenceEOS).strip()
        self._MecabTokenizer = MecabTokenizer
        self._tokens = self.words()

    def words(self):
        return self._MecabTokenizer.tokenize(self._text).convert_list_object()

    def __repr__(self):
        return str(u'Sentence model')