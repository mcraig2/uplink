""" The command line note-taking tool """

__version__ = '0.0.1'

import sqlite3
import sys

import click

from .add_entry import add_entry
from .remove_entry import remove_entry
from .search_entry import search_entry


@click.group()
@click.option('--debug', default=False)
def main(debug):
    """ This is the main command line tool """
    click.echo('Debug mode is {}'.format(debug))
    conn = sqlite3.connect('db/notes.db')


@main.command()
@click.argument('inputfile', type=click.File('rb'))
def add(inputfile):
    """ This is where you add an entry """
    add_entry(inputfile, conn=conn)


@main.command()
@click.argument('prefixes', nargs=-1)
def remove(prefixes):
    """ This is where you remove entry or entries """
    remove_entry(prefixes, conn=conn)


@main.command()
@click.option('--query', prompt='Entry query',
              help='Free text query to search for')
def search(query):
    """ This is where you search for an entry """
    search_entry(query, conn=conn)
