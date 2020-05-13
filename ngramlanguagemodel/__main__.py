# -*- coding: utf-8 -*-
import sys
import logging
import math
import json
from ngramlanguagemodel import ngramlanguagemodel

if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)

    if len(sys.argv) < 3:
        logging.error("Please provide at least two arguments: 1) Input file with lines in the id TAB sentence format "
                      "2) the language the file is in and optionally 3) the minimum frequency of ngrams to be "
                      "considered for the resulting model (defaults to 5).")
        sys.exit(2)

    input_file = sys.argv[1]
    language = sys.argv[2]
    if len(sys.argv) == 4:
        min_freq = sys.argv[3]
    else:
        min_freq = 5

    logging.info('Creating language model in %s from file %s with minimum ngram frequency %s',
                 language,
                 input_file,
                 min_freq)

    with open(input_file, 'r') as f:
        sentences = []
        for line in f:
            line_data = line.split('\t')
            if len(line_data) != 2:
                logging.error("Invalid line format. Format should be id TAB sentence.")
                sys.exit(2)
            sentence = line_data[1].rstrip()
            sentences.append(sentence)
        ngrams_with_counts = ngramlanguagemodel.create_language_model(sentences)

        logging.info('Calculating n-gram scores and grouping them by score ...')

        score_to_ngram = dict()
        total = sum(ngrams_with_counts.values())
        for ngram in filter(lambda x: x[1] >= min_freq, ngrams_with_counts.items()):
            ngram_text = ''.join(c for c in ngram[0])
            ngram_frequency = ngram[1]
            relative_frequency = ngram_frequency / total
            score = math.log(relative_frequency)
            if score in score_to_ngram:
                score_to_ngram.get(score).append(ngram_text)
            else:
                score_to_ngram[score] = [ngram_text]
        result = dict()
        result["language"] = language
        result["ngrams"] = score_to_ngram
        result["samples"] = total
        out_file = language + ".json"
        logging.info('Saving model to file %s ...', out_file)

        with open(out_file, 'w') as out:
            json.dump(result, out)

        logging.info('Done.')
