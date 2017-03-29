"""
Class Amity
"""


class Amity(object):
    """
    Class Amity
    """
    rooms = []
    offices = []
    livingspaces = []
    people = []
    staff = []
    fellows = []
    office_allocations = {}
    livingspace_allocations = {}
    vacant_offices = []
    vacant_livingspaces = []
    unallocated_staff = []
    unallocated_fellows = []

    def create_room(self, room_name, room_type):
        """
        create_room method
        """
        pass

    def add_person(self, person_name, job_description, wants_accommodation):
        """
        Add person method
        """
        pass

    def allocate_livingspace(self, fellow_name):
        """
        allocate a livingspace to a fellow
        """
        pass

    def allocate_office(self, staff_name):
        """
        allocate office to staff
        """
        pass

    def reallocate_person(self, person_id, room_name):
        """
        re-locate person method
        """
        pass

    def load_people(self, filename):
        """
        load_people method
        """
        pass

    def load_rooms(self, filename):
        """
        load_rooms method
        """
        pass

    def print_allocations(self, filename):
        """
        print_allocations method
        """
        pass

    def print_unallocated(self, filename):
        """
        print_unallocated method
        """
        pass

    def print_room(self):
        """
        print_room method
        """
        pass

    def print_fellows(self):
        """
        print all fellows
        """
        pass

    def print_staf(self):
        """
        print all staff
        """
        pass

    def print_all_people(self):
        """
        print all people
        """
        pass
