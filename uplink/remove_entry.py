""" Removes entries from the database """

def remove_entry(prefixes, conn):
    for prefix in prefixes:
        print('Removing "{}"'.format(prefix))
