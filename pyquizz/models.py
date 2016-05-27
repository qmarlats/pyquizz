#!/usr/bin/env python

"""
.. module:: models
   :platform: Linux, Windows
   :synopsis: Database models.

.. moduleauthor:: Quentin Marlats <quentin.marlats@qmarlats.com>

"""

from peewee import *

class Category(Model):
    name = CharField(max_length=50, unique=True)

class Music(Model):
    name = CharField(max_length=40, unique=True)
    category = ForeignKeyField(Category, related_name='musics')
