"""
Class Amity
"""
from .room import LivingSpace, Office

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
    room_data = {}


    def create_room(self, room_name, room_type):
        """
        create_room method
        """
        room_name = room_name.upper()
        room_type = room_type.upper()

        if room_name in self.rooms:
            return '{} already exists.'.format(room_name)
        else:

            if room_type == 'LIVINGSPACE':
                new_room = LivingSpace(room_name)
                self.rooms.append(room_name)
                self.livingspaces.append(room_name)
                self.room_data[room_name] = [new_room.room_type,
                                             new_room.room_capacity]
                self.livingspace_allocations[room_name] = []
                return '{} created'.format(room_name)
            elif room_type == 'OFFICE':

                new_room = Office(room_name)
                self.rooms.append(room_name)
                self.offices.append(room_name)
                self.room_data[room_name] = [new_room.room_type,
                                             new_room.room_capacity]
                self.office_allocations[room_name] = []
                return '{} created'.format(room_name)
            else:

                return 'Invalid room type.'

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
