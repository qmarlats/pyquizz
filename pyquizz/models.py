#!/usr/bin/env python

"""
.. module:: models
   :platform: Linux, Windows
   :synopsis: Database models.

.. moduleauthor:: Quentin Marlats <quentin.marlats@qmarlats.com>

"""

from peewee import *

class Music(Model):
    identifier = CharField(max_length=40, unique=True)

class Answer(Model):
    value = CharField(max_length=100)
    is_right_answer = BooleanField()
    music = ForeignKeyField(Music, related_name='answers')
