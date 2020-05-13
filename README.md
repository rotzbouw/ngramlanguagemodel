# Create models for language detection based on character n-grams.

## Specifications
Currently, the size of the n-grams is not configurable and hard-coded to 5.

N-Grams are scored by the logarithmic probability of their relative frequency, i.e. if an n-gram appears 9 times in a corpus of 300 n-grams, its relative frequency would be 9/300 and its score log(3/100) => -1.52287... N-Grams are padded left and right by '_', including word-beginning and -ending information in the resulting model.

## Data
For the moment, the format used by the Wortschatz Corpora is supported, i.e. the data must be contained withing one text file containing lines of sentence id and the sentence text, separated by a tab character.

## Related
This module is inspired by and combines aspects of the following two approaches:
http://practicalcryptography.com/miscellaneous/machine-learning/tutorial-automatic-language-identification-ngram-b/
http://cloudmark.github.io/Language-Detection/
