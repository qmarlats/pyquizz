#!/usr/bin/env python

"""
.. module:: pyquizz
   :platform: Linux, Windows
   :synopsis: Pyquizz project main file

.. moduleauthor:: Quentin Marlats <quentin.marlats@qmarlats.com>

"""

from music import Music
from database import Database

def test_music():
    music = Music("6e759f6da358f4a36421af5006c5dbcd6ccabbdb")
    print(music.is_exists())
    music.play()

def test_db():
    db = Database('pyquizz')
    db.connect()
    db.create_database()

if __name__ == '__main__':
    # code if script is executed by user (and not imported from another file)
    test_db()
