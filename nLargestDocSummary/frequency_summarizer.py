#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'

from collections import defaultdict
from string import punctuation
from heapq import nlargest
from nLargestDocSummary.models.document_object_model import DocumentModel
import logging
logging.basicConfig(level=logging.INFO)

class FrequencySummarizer:

    def __init__(self, language, documentObj, min_cut=0.1, max_cut=0.9):
        """
         Initilize the text summarizer.
         Words that have a frequency term lower than min_cut
         or higer than max_cut will be ignored.
        """
        self._min_cut = min_cut
        self._max_cut = max_cut
        self._language = language
        self._document = documentObj

        if isinstance(documentObj, DocumentModel)==False:
            raise TypeError('documentObj argument must be object of DocumentModel')
        self._document = documentObj

        if language=='en':
            raise NotImplemented
            self._stopwords = set(stopwords.words('english') + list(punctuation))
        elif language=='ja':
            # TODO stopword機能の実装
            self._stopwords = set([u'、', u'。', u'（', u'）'])


    def _compute_frequencies(self, word_sent):
        """
          Compute the frequency of each of word.
          Input:
           word_sent, a list of sentences already tokenized.
          Output:
           freq, a dictionary where freq[w] is the frequency of w.
        """
        freq = defaultdict(int)
        for s in word_sent:
          for word in s:
            if word not in self._stopwords:
              freq[word] += 1
        # frequencies normalization and fitering
        m = float(max(freq.values()))
        freq_count_dict = {}
        for w in freq.keys():
            freq_count_dict[w] = freq[w]/m
            #freq[w] = freq[w]/m
            if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                pass
                #del freq[w]
        return freq


    def summarize(self, n):
        """
          Return a list of n sentences
          which represent the summary of text.
        """
        best_sentences_garagraph = []

        paragraphs = self._document._paragraphs
        for parapgraph in paragraphs:
            sents = parapgraph._sentences
            #assert n <= len(sents)
            if n > len(sents):
                best_sentences = [s._text for s in sents]
                logging.warning(msg = "n parameter is bigger than sentences. All sentences are put in")
            else:
                word_sent = [s._tokens for s in sents]
                self._freq = self._compute_frequencies(word_sent)
                ranking = defaultdict(int)
                for i,sent in enumerate(word_sent):
                  for w in sent:
                    if w in self._freq:
                      ranking[i] += self._freq[w]
                sents_idx = self._rank(ranking, n)
                best_sentences = [sents[j]._text for j in sents_idx]
            
            best_sentences_garagraph.append(best_sentences)

        return best_sentences_garagraph


    def _rank(self, ranking, n):
        """ return the first n sentences with highest ranking """
        return nlargest(n, ranking, key=ranking.get)
