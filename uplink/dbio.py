""" Database I/O functions """

import sqlite3

def connect():
    """ Connects to the local SQLite3 database. """
    return sqlite3.connect('db/notes.db')
