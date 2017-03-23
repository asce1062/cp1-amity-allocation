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

    def test_create_room(self):
        """
        test create room Function
        """
        all_rooms = len(self.test_amityville.rooms)
        self.test_amityville.create_room("Tsavo", "OFFICE")
        final_all_rooms = len(self.test_amityville.rooms)
        self.assertEqual(final_all_rooms, all_rooms + 1)

    def test_create_livingspace(self):
        """
        test create livingspace function
        """
        living_spaces = len(self.test_amityville.livingspaces)
        self.test_amityville.create_room("MOON", "LIVINGSPACE")
        final_living_spaces = len(self.test_amityville.livingspaces)
        self.assertEqual(final_living_spaces, living_spaces + 1)

    