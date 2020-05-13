# -*- coding: utf-8 -*-
import logging
import collections
from ngramlanguagemodel.preprocess import preprocess


def create_language_model(samples):
    """
    Creates character ngram language model from provided samples and minimum ngram frequency.
    :param samples: iterable of sentence strings.
    :return: iterator yielding ngrams.
    """
    logging.info('Creating language model ...')

    counter = collections.Counter()
    for sample in samples:
        ngrams = preprocess(sample.rstrip())
        counter.update(ngrams)

    logging.info("Done.")

    return counter
