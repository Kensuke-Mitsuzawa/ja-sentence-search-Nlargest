#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'

# 機能 document集合が入力されたら、段落に分割してデータモデルを生成する
# 段落区切り記号
# mecabParser

from nLargestDocSummary.models.document_object_model import DocumentModel
from nLargestDocSummary.models.sentence_model import Sentence
from nLargestDocSummary.models.paragraph_model import Paragraph

class Parser(object):

    def __init__(self, document, mecabTokenizer, paragraphSeprator=u'\n\n', sentenceEOS=u'。'):
        self._text = document.rstrip(paragraphSeprator)
        self._tokenizer = mecabTokenizer
        self._paraSep = paragraphSeprator
        self._sentenceEOS = sentenceEOS

    def make_document(self):
        paragraphs = []

        text_paragraph = [text.strip() for text in self._text.split(self._paraSep)]
        for paraLine in text_paragraph:
            current_paragraph = []
            for sentence in paraLine.split(self._sentenceEOS):
                s = Sentence(sentence, self._tokenizer, sentenceEOS=self._sentenceEOS)
                current_paragraph.append(s)

            paragraphs.append(Paragraph(current_paragraph))

        return DocumentModel(paragraphs)

