""" Search the database with the given query """

import pandas as pd

from .dbio import describe_entry
from .dbio import load_db
from .grep_scorer import score


def format_entry(entry):
    """ Take an entry and format it for output """
    separator = '-' * 80
    return """
{separator}
{entry}
{separator}""".format(separator=separator, entry=describe_entry(entry))


def search_entry(query, conn):
    db = load_db(conn=conn)
    scores = score(db, query)
    most_relevant = db.iloc[scores.idxmax(), :]['entry_id']

    print(format_entry(most_relevant))
