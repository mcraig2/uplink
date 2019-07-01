""" Search the database with the given query """

import pandas as pd

from .dbio import describe_entry
from .dbio import load_db
from .grep_scorer import score


def search_entry(query, conn):
    db = load_db(conn=conn)
    scores = score(db, query)
    most_relevant = db.iloc[scores.idxmax(), :]['entry_id']

    print(describe_entry(most_relevant))
