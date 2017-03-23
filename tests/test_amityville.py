"""
test for amityville
"""
import unittest
from models.amity import Amity
from models.person import Person, Staff, Fellow
from models.room import Room, Office, LivingSpace

class TestAmityville(unittest.TestCase):
    """
    Class test Amity
    """
    def setUp(self):
        self.test_amityville = Amity()
