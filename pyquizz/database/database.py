"""
.. module:: database
   :platform: Linux, Windows
   :synopsis: Database connector using Peewee module.

.. moduleauthor:: Quentin Marlats

"""

import os
from pyquizz import settings
from database import models
from utils import csv
from playhouse.sqlite_ext import SqliteExtDatabase
from peewee import *

class Database(object):
    def __init__(self, database):
        """Create a Database object.

        :param database: database file name
        :type database: str
        :returns:  Database

        """

        self.database = SqliteExtDatabase('%s.db' % database)
        self.models = models

    def create(self, force = False, verbose = True):
        """Create the database: create the file and the database tables.

        :param force: force the creation of a database even if another with the same name already exists
        :type db: bool

        """

        if not os.path.isfile(self.database.database) or force == True: # self.database.database corresponds to the database file
            try:
                self.database.create_tables([self.models.Category, self.models.Music, self.models.Rating, self.models.Score])
            except Exception:
                print("Une erreur est survenue lors de la création de la base de données.")
        else:
            if verbose:
                print("La base de données existe déjà.")

    def connect(self):
        """Connect to the database."""

        try:
            self.database.connect()
        except Exception:
            print("Une erreur est survenue lors de la connexion à la base de données.")

    def populate(self, what):
        """ Populate database with CSV files"""

        if what == "categories":
            csv_data = csv.get_csv_data("%s/categories" % settings.POPULATE_FILES_DIR)
            for data in csv_data:
                try:
                    models.Category.create(name=data[0])
                except Exception:
                    print("Une erreur est survenue lors du remplissage de la base de données.")
        elif what == "musics":
            csv_data_files = csv.get_csv_data("%s/musics" % settings.POPULATE_FILES_DIR, 7) # Hardcoded number of musics CSV file should be fixed
            for csv_data in csv_data_files:
                for data in csv_data:
                    try:
                        models.Music.create(name=data[0], category=data[1])
                    except Exception:
                        print("Une erreur est survenue lors du remplissage de la base de données.")
