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
        rooms = len(self.test_amityville.rooms)
        self.test_amityville.create_room("Tsavo", "OFFICE")
        final_rooms = len(self.test_amityville.rooms)
        self.assertEqual(final_rooms, rooms + 1)

    def test_create_livingspace(self):
        """
        test create livingspace function
        """
        living_spaces = len(self.test_amityville.livingspaces)
        self.test_amityville.create_room("MOON", "LIVINGSPACE")
        final_living_spaces = len(self.test_amityville.livingspaces)
        self.assertEqual(final_living_spaces, living_spaces + 1)

    def test_create_office(self):
        """
        test create office function
        """
        offices = len(self.test_amityville.offices)
        self.test_amityville.create_room("SUN", "OFFICE")
        final_offices = len(self.test_amityville.rooms)
        self.assertEqual(final_offices, offices + 1)

    def test_room_already_exists(self):
        """
        test if a room being created already exist
        """
        self.test_amityville.create_room("NARNIA", "OFFICE")
        response = self.test_amityville.create_room("NARNIA", "OFFICE")
        self.assertEqual(response, "NARNIA already exists")

    def test_invalid_room_type(self):
        """
        Test if an invalid room type
        """
        response = self.test_amityville.create_room("NARNIA", "OFICE")
        self.assertEqual(response, "Invalid room type.")

    def test_add_person(self):
        """
        test add person Function
        """
        people = len(self.test_amityville.people)
        self.test_amityville.add_person("ALEX", "FELLOW", "NO")
        final_people = len(self.test_amityville.people)
        self.assertEqual(final_people, people + 1)

    def test_add_staff(self):
        """
        test add staff function
        """
        staff = len(self.test_amityville.staff)
        self.test_amityville.add_person("ALEX", "STAFF", "NO")
        final_staff = len(self.test_amityville.people)
        self.assertEqual(final_staff, staff + 1)

    def test_add_fellow(self):
        """
        test add fellow Function
        """
        fellows = len(self.test_amityville.fellows)
        self.test_amityville.add_person("ALEX", "STAFF", "NO")
        final_fellows = len(self.test_amityville.people)
        self.assertEqual(final_fellows, fellows + 1)

    def test_invalid_person_name(self):
        """
        test if invalid person name()
        """
        response = self.test_amityville.add_person(
            "asce1062", "FELLOW", "NO")
        self.assertEqual(response, "Invalid person name")

    def test_invalid_job_description(self):
        """
        test if invalid job description
        """
        response = self.test_amityville.add_person("ALEX", "FELOW", "NO")
        self.assertEqual(response, "Invalid job description")

    def test_staff_wants_accommodation(self):
        """
        test if a staff request for accommodation
        """
        response = self.test_amityville.add_person("TONI", "STAFF", "YES")
        self.assertEqual(response, "Staff cannot be allocated living spaces")
