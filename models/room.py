#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Class Room
"""


class Room(object):

    """
    Room object
    """

    def __init__(self, room_name):
        self.room_name = room_name


class Office(Room):

    """
    Office
    """

    room_capacity = 6

    def __init__(self, room_name):
        self.room_type = 'OFFICE'


class LivingSpace(Room):

    """
    Living Space
    """

    room_capacity = 4

    def __init__(self, room_name):
        self.room_type = 'LIVINGSPACE'
