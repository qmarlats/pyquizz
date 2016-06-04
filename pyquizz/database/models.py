#!/usr/bin/env python

"""
.. module:: models
   :platform: Linux, Windows
   :synopsis: Database models.

.. moduleauthor:: Quentin Marlats

"""

from pyquizz import settings
from peewee import *
from database.database import Database
import datetime

class BaseModel(Model):
    class Meta:
        database = Database(settings.DB_NAME).database

class Category(BaseModel):
    name = CharField(max_length=50, unique=True)

class Music(BaseModel):
    name = CharField(max_length=40, unique=True)
    category = ForeignKeyField(Category, related_name='musics')

class Rating(BaseModel):
    rating = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)

class Score(BaseModel):
    name = CharField(max_length=100)
    gender = CharField(max_length=4)
    age = IntegerField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)
