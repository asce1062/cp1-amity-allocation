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

    def test_room_already_exists(self):
        """
        test if a room being created already exists
        """
        self.amityville.create_room("SUN", "OFFICE")
        result = self.amityville.create_room("SUN", "OFFICE")
        self.assertEqual(result, "SUN already exists.")

    def test_create_livingspace(self):
        """
        test if a livingspace is created
        """
        initial_livingspace_count = len(self.amityville.livingspaces)
        self.amityville.create_room("MOON", "LIVINGSPACE")
        final_livingspace_count = len(self.amityville.livingspaces)
        self.assertEqual(final_livingspace_count,
                         initial_livingspace_count + 1)

    def test_create_office(self):
        """
        test if an office is created
        """
        self.amityville.rooms = []
        self.amityville.offices = []

        initial_office_count = len(self.amityville.offices)
        self.amityville.create_room("SUN", "OFFICE")
        final_office_count = len(self.amityville.rooms)
        self.assertEqual(final_office_count, initial_office_count + 1)

    def test_invalid_room_type(self):
        """
        Test for an invalid room type
        """
        result = self.amityville.create_room("SUN", "OFICE")
        self.assertEqual(result, "Invalid room type.")

    def test_invalid_person_name(self):
        """
        test if person name is valid
        """
        result = self.amityville.add_person(
            "asce1062", "FELLOW", "NO")
        self.assertEqual(result, "Invalid person name.")

    def test_add_fellow(self):
        """
        test if a fellow is added
        """
        initial_fellows_count = len(self.amityville.fellows)
        self.amityville.add_person("ALEX", "FELLOW", "NO")
        final_fellows_count = len(self.amityville.people)
        self.assertEqual(final_fellows_count, initial_fellows_count + 1)

    def test_add_staff(self):
        """
        test if a staff member is added
        """
        self.amityville.people = []

        initial_staff_count = len(self.amityville.staff)
        self.amityville.add_person("ALEX", "STAFF", "NO")
        final_staff_count = len(self.amityville.people)
        self.assertEqual(final_staff_count, initial_staff_count + 1)

    def test_invalid_job_description(self):
        """
        test if job description is valid
        """
        result = self.amityville.add_person("ALEX", "FELOW", "NO")
        self.assertEqual(result, "Invalid job description.")

    def test_invalid_accommodation_choice_fellow(self):
        """
        test if accommodation input is valid
        """
        result = self.amityville.add_person("ALEX", "FELLOW", "YEZ")
        self.assertEqual(result, "Invalid accommodation input.")

    def test_invalid_accommodation_choice_staff(self):
        """
        test if accommodation input is valid
        """
        result = self.amityville.add_person("ALEX", "STAFF", "NEIN")
        self.assertEqual(result, "Invalid accommodation input.")

    def test_staff_wants_accommodation(self):
        """
        test if a staff request for accommodation
        """
        result = self.amityville.add_person("ALEX", "STAFF", "YES")
        self.assertEqual(result, "Staff cannot be allocated a livingspace.")

    def test_allocate_livingspace_fellow_does_not_exist(self):
        """
        test allocating a livingspace to a non existant fellow
        """
        self.amityville.rooms = []
        self.amityville.people = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        result = self.amityville.allocate_livingspace("ALEX")
        self.assertEqual(result, "ALEX does not exist.")

    def test_already_allocated_livingspace(self):
        """
        test if a fellow has already been allocated a livingspace
        """
        self.amityville.rooms = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        result = self.amityville.allocate_livingspace("ALEX")
        self.assertEqual(result, "ALEX already allocated a livingspace.")

    def test_allocate_livingspace(self):
        """
        test if a fellow is allocated a living space
        """
        self.amityville.rooms = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.assertIn("ALEX", self.amityville.livingspace_allocations["MOON"])

    def test_no_vaccant_livingspace(self):
        """
        test that there are no vaccant livingspaces
        """
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
        self.assertEqual(result, "No vaccant livingspace.")

    def test_allocate_office_staff_does_not_exist(self):
        """
        test allocating a livingspace to a non existant fellow
        """
        self.amityville.rooms = []
        self.amityville.offices = []
        self.amityville.people = []

        self.amityville.create_room("SUN", "OFFICE")
        result = self.amityville.allocate_office("ALEX")
        self.assertEqual(result, "ALEX does not exist.")

    def test_already_allocated_office(self):
        """
        test if a staff has already been allocated an office
        """
        self.amityville.rooms = []
        self.amityville.offices = []

        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.allocate_office("ALEX")
        self.assertEqual(result, "ALEX already allocated to an office.")

    def test_allocate_office(self):
        """
        test if a staff is allocated an office
        """
        self.amityville.rooms = []
        self.amityville.offices = []

        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        self.assertIn("ALEX", self.amityville.office_allocations["SUN"])

    def test_no_vaccant_office(self):
        """
        test that there are no vaccant offices
        """
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
        self.assertEqual(result, "No vaccant office.")

    def test_no_rooms_to_reallocate_to(self):
        """
        test there are no rooms added in order to reallocate
        """
        self.amityville.room_data = {}

        result = self.amityville.reallocate_person("S1", "SUN")
        self.assertEqual(result, "SUN does not exist.")

    def test_there_are_no_people_to_reallocate(self):
        """
        test there is no one to reallocate
        """
        self.amityville.person_data = {}

        self.amityville.create_room("SUN", "OFFICE")
        result = self.amityville.reallocate_person("S1", "SUN")
        self.assertEqual(result, "S1 does not exist.")

    def test_reallocate_person(self):
        """
        test is persons are reallocated
        """
        self.amityville.rooms = []

        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        self.amityville.create_room("SHINE", "OFFICE")
        result = self.amityville.reallocate_person("S1", "SHINE")
        self.assertEqual(result, "ALEX has been reallocated to SHINE.")

    def test_reallocate_staff_to_livingspace(self):
        """
        test if a staff is reallocated to a living space
        """
        self.amityville.rooms = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.reallocate_person("S1", "MOON")
        self.assertEqual(
            result, "Cannot reallocate staff member to a livingspace.")

    def test_reallocating_to_full_room(self):
        """
        test if room being reallocated to is full
        """
        self.amityville.people = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.amityville.add_person("JOE", "FELLOW", "YES")
        self.amityville.add_person("TINA", "FELLOW", "YES")
        self.amityville.add_person("IBRA", "FELLOW", "YES")
        self.amityville.create_room("LIGHT", "LIVINGSPACE")
        self.amityville.add_person("MILLY", "FELLOW", "YES")
        result = self.amityville.reallocate_person("F5", "MOON")
        self.assertEqual(result, "MOON is already full.")

    def test_reallocating_to_currently_occupied_room(self):
        """
        test if the room being reallocated to is the one they are currently residing in
        """
        self.amityville.people = []

        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.amityville.add_person("JOE", "FELLOW", "YES")
        self.amityville.add_person("TINA", "FELLOW", "YES")
        self.amityville.add_person("IBRA", "FELLOW", "YES")
        result = self.amityville.reallocate_person("F4", "MOON")
        self.assertEqual(result, "IBRA already allocated to MOON.")

    def test_reallocating_and_not_yet_allocated(self):
        """
        test if reallocating a person not yet allocated
        """
        self.amityville.rooms = []

        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("JOE", "FELLOW", "YES")
        self.amityville.add_person("TINA", "FELLOW", "YES")
        self.amityville.add_person("IBRA", "FELLOW", "YES")
        result = self.amityville.reallocate_person("F1", "MOON")
        self.assertEqual(result, "ALEX is not allocated any livingspace.")
