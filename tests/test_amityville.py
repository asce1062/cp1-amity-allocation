"""
test for amityville
"""
import unittest
from models.amity import Amity

class TestAmityville(unittest.TestCase):
    """
    Class test Amity
    """
    def setUp(self):
        self.test_amityville = Amity()
