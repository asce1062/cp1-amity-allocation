#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
"""

from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from clint.textui import colored

# automap base
# The following is what will create the declarative_base base that will be
# imported to every table.

Base = declarative_base()


# The following is the local ROOMS table which will store the
# ROOMS added to amity.

class AmityRooms(Base):

    __tablename__ = 'ROOMS'

    # Here we define columns for the table ROOMS
    # Notice that each column is also a normal Python instance attribute.

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)

    def __init__(self, room_name):

        self.NAME = room_name


class AmityLivingspaces(Base):

    __tablename__ = 'LIVINGSPACES'

    # Here we define columns for the table LIVINGSPACES

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)

    def __init__(self, room_name):

        self.NAME = room_name


class AmityOffices(Base):

    __tablename__ = 'OFFICES'

    # Here we define columns for the table OFFICES

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)

    def __init__(self, room_name):

        self.NAME = room_name


class AmityPeople(Base):

    __tablename__ = 'PEOPLE'

    # Here we define columns for the table PEOPLE

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)

    def __init__(self, person_name):

        self.NAME = person_name


class AmityFellows(Base):

    __tablename__ = 'FELLOWS'

    # Here we define columns for the table FELLOWS

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)

    def __init__(self, fellow_name):

        self.NAME = fellow_name


class AmityStaff(Base):

    __tablename__ = 'STAFF'

    # Here we define columns for the table STAFF

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)

    def __init__(self, staff_name):

        self.NAME = staff_name


class AmityUnallocatedlivingspace(Base):

    __tablename__ = 'UNALLOCATEDLIVINGSPACE'

    # Here we define columns for the table UNALLOCATEDLIVINGSPACE

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)

    def __init__(self, fellow_name):

        self.NAME = fellow_name


class AmityUnallocatedoffice(Base):

    __tablename__ = 'UNALLOCATEDOFFICE'

    # Here we define columns for the table UNALLOCATEDOFFICE

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)

    def __init__(self, person_name):

        self.NAME = person_name


class AmityOfficeAllocations(Base):

    __tablename__ = 'OFFICEALLOCATIONS'

    # Here we define columns for the table UNALLOCATEDOFFICE

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ROOM_NAME = Column(Text)
    PERSON_NAME = Column(Text)

    def __init__(self, room_name, person_name):

        self.ROOM_NAME = room_name
        self.PERSON_NAME = person_name


class AmityLivingspaceAllocations(Base):

    __tablename__ = 'LIVINGSPACEALLOCATIONS'

    # Here we define columns for the table UNALLOCATEDOFFICE

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ROOM_NAME = Column(Text)
    PERSON_NAME = Column(Text)

    def __init__(self, room_name, person_name):

        self.ROOM_NAME = room_name
        self.PERSON_NAME = person_name


class AmityPersondata(Base):

    __tablename__ = 'PEOPLEDATA'

    # Here we define columns for the table PEOPLEDATA
    # Notice that each column is also a normal Python instance attribute.

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PERSON_ID = Column(Text)
    NAME = Column(Text)
    JOB_DESCRIPTION = Column(Text)
    WANTS_ACCOMMODATION = Column(Text)

    def __init__(self, person_id, person_name, job_description, wants_accommodation):

        self.PERSON_ID = person_id
        self.NAME = person_name
        self.JOB_DESCRIPTION = job_description
        self.WANTS_ACCOMMODATION = wants_accommodation


class AmityRoomdata(Base):

    __tablename__ = 'ROOMDATA'

    # Here we define columns for the table ROOMDATA

    ID = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(Text)
    ROOM_TYPE = Column(Text)
    ROOM_CAPACITY = Column(Integer)

    def __init__(self, room_name, room_type, room_capacity):

        self.NAME = room_name
        self.ROOM_TYPE = room_type
        self.ROOM_CAPACITY = room_capacity


def create_db(dbname='amity'):
    """
    create db method
    """

    # Create an engine that stores data in the local directory's
    # amity.db file.

    engine = create_engine('sqlite:///' + 'databases/' + dbname + '.db')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.

    print (colored.green('Database created successfully.'))
    return Base.metadata.create_all(engine)
