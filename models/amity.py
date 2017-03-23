"""
Class Amity
"""


class Amity(object):
    """
    Class Amity
    """
    rooms = []
    vacant_rooms = []
    offices = []
    vacant_offices = []
    livingspaces = []
    vacant_livingspaces = []
    staff = []
    unallocated_staff = []
    fellows = []
    unallocated_fellows = []

    def create_room(self, room_name, room_type):
        """
        create_room function
        """
        pass

    def add_person(self, person_name, job_description, wants_accommodation):
        """
        Add person Function
        """
        pass

    def reallocate_person(self, person_name, new_room_name):
        """
        re-locate person Function
        """
        pass

    def load_people(self, filename):
        """
        load_people Function
        """
        pass

    def print_allocations(self, filename):
        """
        print_allocations Function
        """
        pass

    def print_unallocated(self, filename):
        """
        print_unallocated function
        """
        pass

    def print_room(self):
        """
        print_room Function
        """
        pass
