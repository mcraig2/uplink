""" A simple search algo that just greps for matches and
    the score is just the number of matches. """

from .preprocess import preprocess_str


def score_doc(doc, query):
    return sum(doc['processed'].count(word)
               for word in query.split(' '))


def score(docs, query):
    query = preprocess_str(query.lower())
    return docs.apply(lambda x: score_doc(x, query), axis=1)
    print('GREP!')
