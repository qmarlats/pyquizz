#!/usr/bin/env python

"""
.. module:: database
   :platform: Linux, Windows
   :synopsis: Database connector using Peewee module.

.. moduleauthor:: Quentin Marlats <quentin.marlats@qmarlats.com>

"""

import os, models, populate
from playhouse.sqlite_ext import SqliteExtDatabase

class Database(object):
    def __init__(self, db):
        """Create a Database object.

        :param db: database file name
        :type db: str
        :returns:  Database

        """

        self.db = SqliteExtDatabase('%s.db' % db)
        self.models = models

    def connect(self):
        """Connect to the database object."""
        self.db.connect()

    def create(self, force = False, verbose = True):
        """Create the database: create the file and the database tables.

        :param force: force the creation of a database even if another with the same name already exists
        :type db: bool

        """
        if not os.path.isfile(self.db.database) or force == True:
            self.db.create_tables([models.Music, models.Answer])
        else:
            if verbose:
                print("The specified database already exists")

    def populate(self, what, model = None):
        if what == "category":
            csv_data = populate.get_csv("categories")
            models.Category(*csv_data)
