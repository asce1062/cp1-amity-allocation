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
        self.amityville = Amity()

    def test_create_room(self):
        """
        test if a room is created
        """
        rooms = len(self.amityville.rooms)
        self.amityville.create_room("Tsavo", "OFFICE")
        final_rooms = len(self.amityville.rooms)
        self.assertEqual(final_rooms, rooms + 1)

    def test_create_livingspace(self):
        """
        test if a living space is created
        """
        living_spaces = len(self.amityville.livingspaces)
        self.amityville.create_room("MOON", "LIVINGSPACE")
        final_living_spaces = len(self.amityville.livingspaces)
        self.assertEqual(final_living_spaces, living_spaces + 1)

    def test_create_office(self):
        """
        test if an office is created
        """
        offices = len(self.amityville.offices)
        self.amityville.create_room("SUN", "OFFICE")
        final_offices = len(self.amityville.rooms)
        self.assertEqual(final_offices, offices + 1)

    def test_room_already_exists(self):
        """
        test if a room being created already exist
        """
        self.amityville.create_room("NARNIA", "OFFICE")
        result = self.amityville.create_room("NARNIA", "OFFICE")
        self.assertEqual(result, "NARNIA already exists")

    def test_invalid_room_type(self):
        """
        Test if an invalid room type
        """
        result = self.amityville.create_room("NARNIA", "OFICE")
        self.assertEqual(result, "Invalid room type.")

    def test_add_person(self):
        """
        test is a person is added
        """
        people = len(self.amityville.people)
        self.amityville.add_person("ALEX", "FELLOW", "NO")
        final_people = len(self.amityville.people)
        self.assertEqual(final_people, people + 1)

    def test_add_staff(self):
        """
        test if a staff member is added
        """
        staff = len(self.amityville.staff)
        self.amityville.add_person("ALEX", "STAFF", "NO")
        final_staff = len(self.amityville.people)
        self.assertEqual(final_staff, staff + 1)

    def test_add_fellow(self):
        """
        test if a fellow is added
        """
        fellows = len(self.amityville.fellows)
        self.amityville.add_person("ALEX", "FELLOW", "NO")
        final_fellows = len(self.amityville.people)
        self.assertEqual(final_fellows, fellows + 1)

    def test_invalid_person_name(self):
        """
        test if person name is valid
        """
        result = self.amityville.add_person(
            "asce1062", "FELLOW", "NO")
        self.assertEqual(result, "Invalid person name")

    def test_invalid_job_description(self):
        """
        test if job description is valid
        """
        result = self.amityville.add_person("ALEX", "FELOW", "NO")
        self.assertEqual(result, "Invalid job description")

    def test_staff_wants_accommodation(self):
        """
        test if a staff request for accommodation
        """
        result = self.amityville.add_person("ALEX", "STAFF", "YES")
        self.assertEqual(result, "Staff cannot be allocated living spaces")

    def test_allocate_livingspace(self):
        """
        test if a fellow is allocated a living space
        """
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.assertIn("ALEX", self.amityville.livingspace_allocations["MOON"])

    def test_allocate_office(self):
        """
        test if a staff is allocated an office
        """
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        self.assertIn("ALEX", self.amityville.office_allocations["SUN"])

    def test_already_allocated_livingspace(self):
        """
        test if a fellow has already been allocated a livingspace
        """
        self.amityville.rooms = []
        self.amityville.offices = []
        self.amityville.livingspaces = []
        self.amityville.people = []
        self.amityville.staff = []
        self.amityville.fellows = []
        self.amityville.office_allocations = {}
        self.amityville.livingspace_allocations = {}
        self.amityville.vacant_offices = []
        self.amityville.vacant_livingspaces = []
        self.amityville.unallocated_staff = []
        self.amityville.unallocated_fellows = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        result = self.amityville.allocate_livingspace("ALEX")
        self.assertEqual(result, "ALEX already allocated a livingspace")

    def test_no_vaccant_livingspace(self):
        """
        test that there are no vaccant livingspaces
        """
        self.amityville.rooms = []
        self.amityville.offices = []
        self.amityville.livingspaces = []
        self.amityville.people = []
        self.amityville.staff = []
        self.amityville.fellows = []
        self.amityville.office_allocations = {}
        self.amityville.livingspace_allocations = {}
        self.amityville.vacant_offices = []
        self.amityville.vacant_livingspaces = []
        self.amityville.unallocated_staff = []
        self.amityville.unallocated_fellows = []

        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.amityville.add_person("JOE", "FELLOW", "YES")
        self.amityville.add_person("TINA", "FELLOW", "YES")
        self.amityville.add_person("IBRA", "FELLOW", "YES")
        self.amityville.add_person("MILLY", "FELLOW", "YES")
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.allocate_livingspace("MILLY")
        self.amityville.allocate_livingspace("IBRA")
        self.amityville.allocate_livingspace("TINA")
        self.amityville.allocate_livingspace("JOE")
        result = self.amityville.allocate_livingspace("ALEX")
        self.assertEqual(result, "No vaccant livingspace")

    def test_already_allocated_office(self):
        """
        test if a staff has already been allocated an office
        """
        self.amityville.rooms = []
        self.amityville.offices = []
        self.amityville.livingspaces = []
        self.amityville.people = []
        self.amityville.staff = []
        self.amityville.fellows = []
        self.amityville.office_allocations = {}
        self.amityville.livingspace_allocations = {}
        self.amityville.vacant_offices = []
        self.amityville.vacant_livingspaces = []
        self.amityville.unallocated_staff = []
        self.amityville.unallocated_fellows = []

        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.allocate_office("ALEX")
        self.assertEqual(result, "ALEX already allocated an office")

    def test_no_vaccant_office(self):
        """
        test that there are no vaccant offices
        """
        self.amityville.rooms = []
        self.amityville.offices = []
        self.amityville.livingspaces = []
        self.amityville.people = []
        self.amityville.staff = []
        self.amityville.fellows = []
        self.amityville.office_allocations = {}
        self.amityville.livingspace_allocations = {}
        self.amityville.vacant_offices = []
        self.amityville.vacant_livingspaces = []
        self.amityville.unallocated_staff = []
        self.amityville.unallocated_fellows = []

        self.amityville.add_person("ALEX", "STAFF", "NO")
        self.amityville.add_person("JOE", "STAFF", "NO")
        self.amityville.add_person("TINA", "STAFF", "NO")
        self.amityville.add_person("IBRA", "STAFF", "NO")
        self.amityville.add_person("MILLY", "STAFF", "NO")
        self.amityville.add_person("PAU", "STAFF", "NO")
        self.amityville.add_person("JONA", "STAFF", "NO")
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.allocate_office("JONA")
        self.amityville.allocate_office("PAU")
        self.amityville.allocate_office("MILLY")
        self.amityville.allocate_office("IBRA")
        self.amityville.allocate_office("TINA")
        self.amityville.allocate_office("JOE")
        result = self.amityville.allocate_office("ALEX")
        self.assertEqual(result, "No vaccant office")

    def test_reallocate_person(self):
        """
        test is persons are reallocated
        """
        self.amityville.rooms = []
        self.amityville.offices = []
        self.amityville.livingspaces = []
        self.amityville.people = []
        self.amityville.staff = []
        self.amityville.fellows = []
        self.amityville.office_allocations = {}
        self.amityville.livingspace_allocations = {}
        self.amityville.vacant_offices = []
        self.amityville.vacant_livingspaces = []
        self.amityville.unallocated_staff = []
        self.amityville.unallocated_fellows = []

        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "FELLOW", "NO")
        self.amityville.create_room("SHINE", "OFFICE")
        result = self.amityville.reallocate_person("S1", "SHINE")
        self.assertEqual(result, "ALEX has been reallocated to SHINE")

    def test_reallocate_staff_to_livingspace(self):
        """
        test if a staff is reallocated to a living space
        """
        self.amityville.rooms = []
        self.amityville.offices = []
        self.amityville.livingspaces = []
        self.amityville.people = []
        self.amityville.staff = []
        self.amityville.fellows = []
        self.amityville.office_allocations = {}
        self.amityville.livingspace_allocations = {}
        self.amityville.vacant_offices = []
        self.amityville.vacant_livingspaces = []
        self.amityville.unallocated_staff = []
        self.amityville.unallocated_fellows = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.reallocate_person("S1", "MOON")
        self.assertEqual(
            result, "Cannot allocate staff member to a livingspace")

    def test_reallocating_to_full_room(self):
        """
        test if room being reallocated to is full
        """
        self.amityville.rooms = []
        self.amityville.offices = []
        self.amityville.livingspaces = []
        self.amityville.people = []
        self.amityville.staff = []
        self.amityville.fellows = []
        self.amityville.office_allocations = {}
        self.amityville.livingspace_allocations = {}
        self.amityville.vacant_offices = []
        self.amityville.vacant_livingspaces = []
        self.amityville.unallocated_staff = []
        self.amityville.unallocated_fellows = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.amityville.add_person("JOE", "FELLOW", "YES")
        self.amityville.add_person("TINA", "FELLOW", "YES")
        self.amityville.add_person("IBRA", "FELLOW", "YES")
        self.amityville.create_room("LIGHT", "LIVINGSPACE")
        self.amityville.add_person("MILLY", "FELLOW", "YES")
        result = self.amityville.reallocate_person("F5", "MOON")
        self.assertEqual(result, "MOON is already full")
