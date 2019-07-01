""" Contains functions for preprocessing document strings """

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from stemming.porter2 import stem


def preprocess_str(docstr):
    """ Given the string, removes punctuation, stopwords,
        and stems the words. """
    tokenizer = RegexpTokenizer(r'\w+')
    stop = set(stopwords.words('english'))
    tokens = (stem(word) for word in tokenizer.tokenize(docstr.lower())
              if word not in stop)
    return ' '.join(tokens)
