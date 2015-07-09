#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'

from .sentence_model import Sentence
from .paragraph_model import Paragraph
import itertools

class DocumentModel(object):

    def __init__(self, paragraphs):
        self._paragraphs = paragraphs


    def paragraphs(self):
        return self._paragraphs


    def words(self):
        words = (p.words for p in self._paragraphs)
        return tuple(itertools.chain(*words))


    def sentences(self):
        sentences = (p.sentences for p in self._paragraphs)
        return tuple(itertools.chain(*sentences))


    def __repr__(self):
        return str("DocumentModel")

    """
    datamodel が持つべき要素
    * 段落ごとに分解したdocument
    * sentenceごとに分解したdocument
    * sentenceはtokenizeされた状態も保持
    * 段落区切り記号

    戻り値はリストの中にParagphクラスのオブジェクトが入っている感じ
    あと、段落区切り記号
    """