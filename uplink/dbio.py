""" Database I/O functions """

from configparser import ConfigParser
import glob
import sqlite3

import pandas as pd

def connect():
    """ Connects to the local SQLite3 database. """
    return sqlite3.connect('db/notes.db')


def read_raw_md(fname, cparser=None):
    """ Reads and parses a raw MD file and outputs
        a dictionary with the important bits """
    if not cparser:
        cparser = ConfigParser()

    cparser.read(fname)
    return {'description': cparser['DESCRIPTION']['description'],
            'content': cparser['CONTENT']['content'],
            'keywords': cparser['KEYWORDS']['keywords'].split(' '),
            'processed': cparser['PROCESSED']['processed']}


def load_db(conn):
    """ Load the DB into memory. This should definitely
        be refactored once the DB gets large enough, but
        for now this will work. """
    cfg = ConfigParser()
    files = glob.glob('db/*.md')
    return (pd.DataFrame(read_raw_md(f, cparser=cfg) for f in files)
            .assign(entry_id=files))


def describe_entry(entry_fname):
    """ Take a given entry and make a descriptive string out
        of it for display purposes. """
    contents = read_raw_md(entry_fname, cparser=None)
    return """
{content}
--------------------
Title: {description}
Keywords: {keywords}
Entry_id: {uid}""".format(
        content=contents['content'],
        description=contents['description'],
        keywords=', '.join(contents['keywords']),
        uid=entry_fname[3:-3])
