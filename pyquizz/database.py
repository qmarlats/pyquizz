#!/usr/bin/env python

"""
.. module:: database
   :platform: Linux, Windows
   :synopsis: Database connector using Peewee module.

.. moduleauthor:: Quentin Marlats <quentin.marlats@qmarlats.com>

"""

import models
from playhouse.sqlite_ext import SqliteExtDatabase

class Database(object):
    def __init__(self, db):
        """Create a Database object.

        :param db: database file name
        :type db: str
        :returns:  Database

        """

        self.db = SqliteExtDatabase('%s.db' % db)

    def connect(self):
        """Connect to the database object."""
        self.db.connect()

    def create(self):
        """Create the database: create the file and the database tables."""
        self.db.create_tables([models.Music, models.Answer])

    def populate(self, model, args):
        model.create(args)
