#!/usr/bin/env python

"""
.. module:: pyquizz
   :platform: Linux, Windows
   :synopsis: Pyquizz project main file

.. moduleauthor:: Quentin Marlats <quentin.marlats@qmarlats.com>

"""

# from music import Music
# from database import Database

import menus

def main():
    menus.main_menu()

# def test_music():
#     import models
#     music = Music(models.Music.get(id = 16))
#     print(music.is_exists())
#     music.play()
#
# def test_db():
#     db = Database('pyquizz')
#     db.connect()
#     # db.create(force=True)
#     # db.populate("categories")
#     # db.populate("musics")
#     import models
#     categories = models.Category.select()
#     for category in categories:
#         print(category.name)

if __name__ == '__main__':
    # code if script is executed by user (and not imported from another file)
    main()
