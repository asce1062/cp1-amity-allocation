"""
tests for amityville.
"""
import os
import unittest

from models.amity import Amity


class TestAmityville(unittest.TestCase):
    """
    Class test Amity
    """

    def setUp(self):
        self.amityville = Amity()

    def tearDown(self):
        """
        provide cleanup for all
        clear list data for each test.
        """
        # remove all entries in dict
        self.amityville.office_allocations.clear()
        self.amityville.livingspace_allocations.clear()
        self.amityville.room_data.clear()
        self.amityville.person_data.clear()
        # remove all entries in list
        del self.amityville.rooms[:]
        del self.amityville.offices[:]
        del self.amityville.livingspaces[:]
        del self.amityville.people[:]
        del self.amityville.staff[:]
        del self.amityville.fellows[:]
        del self.amityville.unallocated_livingspace[:]
        del self.amityville.unallocated_office[:]

    def test_create_room_already_exists(self):
        """
        test if a room being created already exists
        """
        self.amityville.create_room("SUN", "OFFICE")
        result = self.amityville.create_room("SUN", "OFFICE")
        self.assertEqual(result, "SUN already exists.")

    def test_create_room_livingspace(self):
        """
        test if a livingspace is created
        """
        result = self.amityville.create_room("MOON", "LIVINGSPACE")
        self.assertEqual(result, "MOON created.")

    def test_create_roomoffice(self):
        """
        test if an office is created
        """
        result = self.amityville.create_room("SUN", "OFFICE")
        self.assertEqual(result, "SUN created.")

    def test_create_room_invalid_room_type(self):
        """
        Test for an invalid room type
        """
        result = self.amityville.create_room("SUN", "OFICE")
        self.assertEqual(result, "Invalid room type.")

    def test_add_person_invalid_person_name(self):
        """
        test if person name is valid
        """
        result = self.amityville.add_person(
            "asce1062", "FELLOW", "NO")
        self.assertEqual(result, "Invalid person name.")

    def test_add_person_fellow(self):
        """
        test if a fellow is added
        """
        result = self.amityville.add_person("ALEX", "FELLOW", "NO")
        self.assertEqual(
            result, 'ALEX successfully added! \nAllocated to:\nOffice: No vaccant office.')

    def test_add_person_staff(self):
        """
        test if a staff member is added
        """
        result = self.amityville.add_person("ALEX", "STAFF", "NO")
        self.assertEqual(
            result, "ALEX successfully added! \nAllocated to:\nOffice: No vaccant office.")

    def test_add_person_invalid_job_description(self):
        """
        test if job description is valid
        """
        result = self.amityville.add_person("ALEX", "FELOW", "NO")
        self.assertEqual(result, "Invalid job description.")

    def test_add_person_invalid_accommodation_choice_fellow(self):
        """
        test if accommodation input is valid
        """
        result = self.amityville.add_person("ALEX", "FELLOW", "YEZ")
        self.assertEqual(result, "Invalid accommodation input.")

    def test_add_person_invalid_accommodation_choice_staff(self):
        """
        test if accommodation input is valid
        """
        result = self.amityville.add_person("ALEX", "STAFF", "NEIN")
        self.assertEqual(result, "Invalid accommodation input.")

    def test_add_person_staff_wants_accommodation(self):
        """
        test if a staff request for accommodation
        """
        result = self.amityville.add_person("ALEX", "STAFF", "YES")
        self.assertEqual(result, "Staff cannot be allocated a livingspace.")

    def test_allocate_livingspaceallocate_livingspace_to_nonexistent_fellow(self):
        """
        test allocating a livingspace to a non existant fellow
        """
        result = self.amityville.allocate_livingspace("ALEX")
        self.assertEqual(result, "ALEX does not exist.")

    def test_allocate_livingspace_already_allocated_livingspace(self):
        """
        test if a fellow has already been allocated a livingspace
        """
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        result = self.amityville.allocate_livingspace("ALEX")
        self.assertEqual(result, "ALEX already allocated a livingspace.")

    def test_allocate_livingspace(self):
        """
        test if a fellow is allocated a living space
        """
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "NO")
        result = self.amityville.allocate_livingspace("ALEX")
        self.assertEqual(result, "ALEX allocated to MOON.")

    def test_allocate_livingspace_no_vaccant_livingspace(self):
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

    def test_allocate_office_to_nonexistent_staff(self):
        """
        test allocating a livingspace to a non existant fellow
        """
        result = self.amityville.allocate_office("ALEX")
        self.assertEqual(result, "ALEX does not exist.")

    def test_allocate_office_already_allocated_office(self):
        """
        test if a staff has already been allocated an office
        """
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.allocate_office("ALEX")
        self.assertEqual(result, "ALEX already allocated to an office.")

    def test_allocate_office(self):
        """
        test if a staff is allocated an office
        """
        self.amityville.add_person("ALEX", "STAFF", "NO")
        self.amityville.create_room("SUN", "OFFICE")
        result = self.amityville.allocate_office("ALEX")
        self.assertEqual(result, "ALEX allocated to SUN.")

    def test_allocate_office_no_vaccant_office(self):
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

    def test_reallocate_person_nonexistent_rooms_to_reallocate_to(self):
        """
        test there are no rooms added in order to reallocate
        """
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.reallocate_person("S1", "SUN")
        self.assertEqual(result, "SUN does not exist.")

    def test_reallocate_person_nonexistent_people_to_reallocate(self):
        """
        test there is no one to reallocate
        """
        self.amityville.create_room("SUN", "OFFICE")
        result = self.amityville.reallocate_person("S1", "SUN")
        self.assertEqual(result, "S1 does not exist.")

    def test_reallocate_person_livingspace(self):
        """
        test if person is reallocated to a livingspace
        """
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "NO")
        self.amityville.allocate_livingspace("ALEX")
        self.amityville.create_room("LIGHT", "LIVINGSPACE")
        result = self.amityville.reallocate_person("F1", "LIGHT")
        self.assertEqual(result, "ALEX has been reallocated to LIGHT.")

    def test_reallocate_person_office(self):
        """
        test if person is reallocated to an office.
        """
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        self.amityville.create_room("SHINE", "OFFICE")
        result = self.amityville.reallocate_person("S1", "SHINE")
        self.assertEqual(result, "ALEX has been reallocated to SHINE.")

    def test_reallocate_person_staff_to_livingspace(self):
        """
        test if a staff is reallocated to a living space
        """
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.reallocate_person("S1", "MOON")
        self.assertEqual(
            result, "Cannot reallocate staff member to a livingspace.")

    def test_reallocate_person_to_full_livingspace(self):
        """
        test if room being reallocated to is already full
        """
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.amityville.add_person("JOE", "FELLOW", "YES")
        self.amityville.add_person("TINA", "FELLOW", "YES")
        self.amityville.add_person("IBRA", "FELLOW", "YES")
        self.amityville.create_room("LIGHT", "LIVINGSPACE")
        self.amityville.add_person("MILLY", "FELLOW", "YES")
        result = self.amityville.reallocate_person("F5", "MOON")
        self.assertEqual(result, "MOON is already full.")

    def test_reallocate_person_to_full_office(self):
        """
        test if room being reallocated to is already full
        """
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        self.amityville.add_person("JOE", "STAFF", "NO")
        self.amityville.add_person("TINA", "STAFF", "NO")
        self.amityville.add_person("IBRA", "STAFF", "NO")
        self.amityville.add_person("MILLY", "STAFF", "NO")
        self.amityville.add_person("PAU", "STAFF", "NO")
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("JONA", "STAFF", "NO")
        result = self.amityville.reallocate_person("s7", "SUN")
        self.assertEqual(result, "SUN is already full.")

    def test_reallocate_person_to_currently_occupied_livingspace(self):
        """
        test if the room being reallocated to is the one they are currently residing in
        """
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        result = self.amityville.reallocate_person("F1", "MOON")
        self.assertEqual(result, "ALEX already allocated to MOON.")

    def test_reallocate_person_to_currently_occupied_office(self):
        """
        test if the room being reallocated to is the one they are currently residing in
        """
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.reallocate_person("S1", "SUN")
        self.assertEqual(result, "ALEX already allocated to SUN.")

    def test_reallocate_person_to_a_livingspace_and_not_yet_allocated_a_livingspace(self):
        """
        test reallocating a person who is not yet allocated.
        """
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        self.amityville.create_room("MOON", "LIVINGSPACE")
        result = self.amityville.reallocate_person("F1", "MOON")
        self.assertEqual(result, "ALEX not yet allocated to any livingspace.")

    def test_reallocate_person_to_a_livingspace_and_not_yet_allocated_an_office(self):
        """
        test reallocating a person who is not yet allocated.
        """
        self.amityville.add_person("ALEX", "STAFF", "NO")
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.create_room("SHINE", "OFFICE")
        result = self.amityville.reallocate_person("S1", "SHINE")
        self.assertEqual(result, "ALEX not yet allocated to any office.")

    def test_print_people_details_no_data_yet(self):
        """
        test print people details and no people added to the system yet.
        """
        result = self.amityville.print_people_details()
        self.assertEqual(result, 'No one exists in the system yet.')

    def test_load_people(self):
        """
        test if people are loaded from a file.
        """
        filename = "people"
        result = self.amityville.load_people(filename)
        self.assertEqual(result, "People successfully loaded.")

    def test_load_people_no_filename(self):
        """
        test if no file name is provided.
        """
        result = self.amityville.load_people("")
        self.assertEqual(result, "Filename must be provided.")

    def test_load_people_invalid_accommodation(self):
        """
        Test if invalid accommodation input is handled.
        """
        filename = "invalid_accommodation"
        result = self.amityville.load_people(filename)
        self.assertEqual(result, "Invalid accommodation input.")

    def test_load_people_invalid_number_of_arguments(self):
        """
        test if there are more than 4 arguments.
        """
        filename = "invalid_number_of_arguments"
        result = self.amityville.load_people(filename)
        self.assertEqual(result, "Invalid number of arguments input.")

    def test_load_people_invalid_job_description(self):
        """
        test for invalid job description.
        """
        filename = "invalid_job_description"
        result = self.amityville.load_people(filename)
        self.assertEqual(result, "Invalid job description.")

    def test_load_rooms_from_file(self):
        """
        test if rooms are loaded from file.
        """
        filename = "rooms"
        result = self.amityville.load_rooms(filename)
        self.assertEqual(result, "Rooms successfully loaded from file.")

    def test_load_rooms_from_file_no_filename(self):
        """
        test if no file name is provided.
        """
        filename = ""
        result = self.amityville.load_rooms(filename)
        self.assertEqual(result, "Filename must be provided.")

    def test_load_rooms_from_file_invalid_input(self):
        """
        test if there are more than 2 arguments.
        """
        filename = "rooms_invalid_input"
        result = self.amityville.load_rooms(filename)
        self.assertEqual(result, "Invalid number of arguments input.")

    def test_print_allocations_to_screen(self):
        """
        test if allocations are successfully printed to the screen.
        """
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        filename = ""
        result = self.amityville.print_allocations(filename)
        self.assertEqual(result, "Done.")

    def test_print_allocations_to_file(self):
        """
        test if allocations are successfully printed out to a file.
        """
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.create_room("MOON", "LIVINGSPACE")
        self.amityville.add_person("ALEX", "FELLOW", "YES")
        filename = "allocations"
        result = self.amityville.print_allocations(filename)
        self.assertTrue(os.path.isfile("models/allocations.txt"))
        self.assertEqual(result, "Done.")

    def test_print_specific_room_allocations(self):
        """
        test if specific room allocations are printed to the screen.
        """
        self.amityville.create_room("SUN", "OFFICE")
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.print_specific_room_allocations("SUN")
        self.assertEqual(result, "Done.")

    def test_print_specific_room_allocations_invalid_input(self):
        """
        test if invalid input is handled.
        """
        result = self.amityville.print_specific_room_allocations("SUN(1)")
        self.assertEqual(result, "Invalid input.")

    def test_print_unallocated_to_screen(self):
        """
        test if un-allocations are printed to the screen.
        """
        filename = ""
        result = self.amityville.print_unallocated(filename)
        self.assertEqual(result, "Done.")

    def test_print_unallocated_to_file(self):
        """
        test if un-allocations are printed into a file.
        """
        filename = "unallocated"
        result = self.amityville.print_unallocated(filename)
        self.assertTrue(os.path.isfile("models/unallocated.txt"))
        self.assertEqual(result, "Done.")

    def test_print_rooms(self):
        """
        test if existing rooms are printed to the screen.
        """
        result = self.amityville.print_rooms()
        self.assertEqual(result, "Done.")

    def test_print_fellows(self):
        """
        test if existing fellows are printed to the screen.
        """
        result = self.amityville.print_fellows()
        self.assertEqual(result, "Done.")

    def test_print_staff(self):
        """
        test if existing staff are printed to the screen.
        """
        result = self.amityville.print_staff()
        self.assertEqual(result, "Done.")

    def test_print_all_people(self):
        """
        test if all existing people are printed to the screen.
        """
        result = self.amityville.print_all_people()
        self.assertEqual(result, "Done.")

    def test_print_people_details(self):
        """
        test print people details.
        """
        self.amityville.person_data = {}
        self.amityville.add_person("ALEX", "STAFF", "NO")
        result = self.amityville.print_people_details()
        self.assertEqual(result, 'Done.')
