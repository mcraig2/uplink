""" The command line note-taking tool """

__version__ = '0.0.1'

import sqlite3
import sys

import click

from .add_entry import add_entry
from .remove_entry import remove_entry
from .search_entry import search_entry
from .sync_db import sync_db


@click.group()
@click.option('--debug', default=False)
def main(debug):
    """ This is the main command line tool """
    click.echo('Debug mode is {}'.format(debug))


@main.command()
def add():
    """ This is where you add an entry """
    conn = sqlite3.connect('db/notes.db')
    add_entry(conn=conn)
    sync_db(conn=conn)


@main.command()
@click.argument('prefixes', nargs=-1)
def remove(prefixes):
    """ This is where you remove entry or entries """
    conn = sqlite3.connect('db/notes.db')
    remove_entry(prefixes, conn=conn)
    sync_db(conn=conn)


@main.command()
@click.option('--query', prompt='Entry query',
              help='Free text query to search for')
def search(query):
    """ This is where you search for an entry """
    conn = sqlite3.connect('db/notes.db')
    search_entry(query, conn=conn)
