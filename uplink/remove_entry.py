""" Removes entries from the database """

import glob
import os


def remove_entry(prefixes, conn):
    for prefix in prefixes:
        matches = glob.glob('db/{}*.md'.format(prefix))
        if not matches:
            print('Could not find prefix {}!'.format(prefix))
        for match in matches:
            print('Deleting {}'.format(match))
            os.remove(match)
