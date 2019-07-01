""" Adds entries to the database """

import uuid

from .preprocess import preprocess_str


def read_template():
    with open('db/__template__.md', 'r') as template:
        data = template.read()

    return data


def get_input():
    description = input('Description: ')
    content = input('Content: ')
    keywords = input('Keywords: ')
    return {'description': description,
            'content': content,
            'keywords': keywords}


def add_entry(conn):
    entry_id = uuid.uuid1()
    entry = get_input()
    entry['processed'] = preprocess_str(' '.join(entry.values()))

    print('Adding entry {}'.format(entry_id))
    with open('db/{}.md'.format(entry_id), 'w') as outfile:
        outfile.write(read_template().format(**entry))
