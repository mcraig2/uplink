""" The command line note-taking tool """

__version__ = '0.0.1'

import sys
import click
from .stuff import Stuff


@click.group()
@click.option('--debug', default=False)
def main(debug):
    """ This is the main command line tool """
    click.echo('Debug mode is {}'.format(debug))


@main.command()
@click.argument('input', type=click.File('rb'))
def add():
    """ This is where you add an entry """
    click.echo('Adding')


@main.command()
@click.argument('prefixes', nargs=-1)
def remove(prefixes):
    """ This is where you remove entry or entries """
    for prefix in prefixes:
        click.echo('Removing {}'.format(prefix))


@main.command()
@click.option('--query', prompt='Entry query',
              help='Free text query to search for')
def search(query):
    """ This is where you search for an entry """
    click.echo('Searching using query: {}'.format(query))
