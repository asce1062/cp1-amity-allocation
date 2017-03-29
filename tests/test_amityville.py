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
        created_room = self.test_amityville.create_room("NARNIA", "OFFICE")
        self.assertEqual(created_room, "NARNIA already exists")

    def test_invalid_room_type(self):
        """
        Test if an invalid room type
        """
        created_room = self.test_amityville.create_room("NARNIA", "OFICE")
        self.assertEqual(created_room, "Invalid room type.")

    def test_add_person(self):
        """
        test add person Function
        """
        all_people = len(self.test_amityville.people)
        self.test_amityville.add_person("ALEX", "FELLOW", "NO")
        final_all_people = len(self.test_amityville.people)
        self.assertEqual(final_all_people, all_people + 1)

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
        all_people = self.test_amityville.add_person("asce1062", "FELLOW", "NO")
        self.assertEqual(all_people, "Invalid person name")

    def test_invalid_job_description(self):
        """
        test if invalid job description
        """
        all_people = self.test_amityville.add_person("ALEX", "FELOW", "NO")
        self.assertEqual(all_people, "Invalid job description")

    def test_staff_wants_accommodation(self):
        """
        test if a staff request for accommodation
        """
        all_people = self.test_amityville.add_person("TONI", "STAFF", "YES")
        self.assertEqual(all_people, "Staff cannot be allocate living spaces")

