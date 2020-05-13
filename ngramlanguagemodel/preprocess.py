# -*- coding: utf-8 -*-
from itertools import chain
import regex


def preprocess(sentence):
    """ Preprocess sentence using normalisation, '_' padding and n-gram (n=5) extraction. """
    normalised_sentence = normalise(sentence)
    n = 5
    for token in normalised_sentence.split():
        for ngram_size in range(1, n + 1):
            for ngram in ngrams(token, ngram_size):
                yield ngram


def normalise(sentence):
    """ Normalises a string in that it removes all numbers and punctuation except for the apostrophe,
    merging consecutive whitespace characters into one. """
    return regex.sub(r"[^\p{L}'\s]+", "", sentence)


# pad_sequence as well as ngrams methods copied from NLTK util.py in slightly simplified form
def pad_sequence(
        sequence,
        n,
):
    """
    Returns a '_' padded sequence of items.

        >>> list(pad_sequence([1,2,3,4,5], 2))
        ['_', 1, 2, 3, 4, 5, '_']

    :param sequence: the source data to be padded
    :type sequence: sequence or iter
    :param n: the degree of the ngrams
    :type n: int
    :rtype: sequence or iter
    """
    pad_symbol = "_"
    sequence = iter(sequence)
    sequence = chain((pad_symbol,) * (n - 1), sequence)
    sequence = chain(sequence, (pad_symbol,) * (n - 1))
    return sequence


def ngrams(
        sequence,
        n
):
    """
    Return the ngrams generated from a sequence of items, as an iterator.
    For example:

        >>> list(ngrams([1,2,3,4,5], 2))
        [('_', 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, '_')]


    :param sequence: the source data to be converted into ngrams
    :type sequence: sequence or iter
    :param n: the degree of the ngrams
    :type n: int
    :rtype: sequence or iter
    """
    sequence = pad_sequence(
        sequence, n
    )

    history = []
    while n > 1:
        # PEP 479, prevent RuntimeError from being raised when StopIteration bubbles out of generator
        try:
            next_item = next(sequence)
        except StopIteration:
            # no more data, terminate the generator
            return
        history.append(next_item)
        n -= 1
    for item in sequence:
        history.append(item)
        yield tuple(history)
        del history[0]
