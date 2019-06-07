""" Creates the database table for this app """

import os
import sys

import uplink.dbio as dbio

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS notes (
    id text PRIMARY KEY,
    date_added datetime,
    date_last_updated datetime,
    name text,
    keywords text,
    content text,
    hashed_content text
); """

# Create the connection and create the table!
conn = dbio.connect()
if conn:
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE)
