#!/usr/bin/env python

"""
.. module:: pyquizz
   :platform: Linux, Windows
   :synopsis: Pyquizz project main file

.. moduleauthor:: Quentin Marlats

"""

from game.menus import main

def pyquizz():
    """Pyquizz project main function."""

    # Show main menu
    main()

def populate_db():
    """Create database if not exists. To use, replace the pyquizz() function with this one in if __name__ == '__main__'"""

    from pyquizz import settings
    from database import database

    db = database.Database(settings.DB_NAME)
    db.connect()
    db.create(force=True)
    db.populate("categories")
    db.populate("musics")

if __name__ == '__main__':
    # Executed when executing poject from terminal
    pyquizz()
