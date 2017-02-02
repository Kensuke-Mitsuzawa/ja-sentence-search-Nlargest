#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'

from nLargestDocSummary.models.sentence_model import Sentence
import itertools

class Paragraph(object):
    __slots__ = (
        "_sentences"
    )

    def __init__(self, sentences):
        # sentencesはobject
        sentences = tuple(sentences)
        for s in sentences:
            if isinstance(s, Sentence)==False: raise TypeError("you must give sentence object from 'Sentence' model")

        self._sentences = sentences

    def sentences(self):
        return tuple(s for s in self._sentences)


    def words(self):
        # return tokenized surface word when this method is called
        return tuple(itertools.chain(* [s.words for s in self._sentences]))


    def __repr__(self):
        return str(u'Paragraph model')