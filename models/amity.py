"""
Class Amity
"""
import random

from models.room import LivingSpace, Office
from models.person import Fellow, Staff
from clint.textui import colored, puts


class Amity(object):
    """
    Class Amity
    """
    # List of all rooms. Livingspaces snd Offices.
    rooms = []
    # List of all offices.
    offices = []
    # List of all livingspaces.
    livingspaces = []
    # List of all people. Fellows and Staff.
    people = []
    # List of all staff.
    staff = []
    # List of all fellows.
    fellows = []
    # Dictionary containing a list of all occupied rooms and occupants.
    office_allocations = {}
    # Dictionary containing a list of all occupied livingspaces and occupants.
    livingspace_allocations = {}
    # List of all unallocated stuff.
    unallocated_staff = []
    # List of all unallocated fellows.
    unallocated_fellows = []
    # Dictionary containing all rooms.
    room_data = {}
    # Dictionary containing all people.
    person_data = {}

    def create_room(self, room_name, room_type):
        """
        create_room method
        """
        # Convert all inputs to upper case for consistency.
        room_name = room_name.upper()
        room_type = room_type.upper()
        # Test if a room already exists in the list of rooms.
        if room_name in self.rooms:
            return '{} already exists.' .format(room_name)

        else:
            if room_type == 'LIVINGSPACE':
                # Create the new livingspace.
                new_room = LivingSpace(room_name)
                # Add it to the list of rooms.
                self.rooms.append(room_name)
                # Add it to the list of livingspaces.
                self.livingspaces.append(room_name)
                # Add it to the dictionary containing room data.
                self.room_data[room_name] = [new_room.room_type,
                                             new_room.room_capacity]
                # Add it to livingspace allocations dictionary
                # as an empty list indicating that there are no occupants.
                self.livingspace_allocations[room_name] = []
                return '{} created.'.format(room_name)

            elif room_type == 'OFFICE':
                # Create the new office.
                new_room = Office(room_name)
                # Add it to the list of rooms.
                self.rooms.append(room_name)
                # Add it to the list of offices.
                self.offices.append(room_name)
                # Add it to the dictionary containing room data.
                self.room_data[room_name] = [new_room.room_type,
                                             new_room.room_capacity]
                # Add it to office allocations dictionary
                # as an empty list indicating that there are no occupants.
                self.office_allocations[room_name] = []
                return '{} created.'.format(room_name)

            else:
                return 'Invalid room type.'

    def add_person(self, person_name, job_description, wants_accommodation='N'):
        """
        Add person method
        """
        # Check if person name is characters only.
        if person_name.isalpha() is False:
            return 'Invalid person name.'

        else:
            if job_description.upper() == 'FELLOW':
                # Add fellow by name.
                new_person = Fellow(person_name.upper())
                # Assign an ID for unique identification.
                person_id = 'F{}' .format(len(self.people) + 1)
                # Add the fellow to a list containing all fellows.
                self.fellows.append(person_name.upper())
                # Add the fellow to a list containing all people.
                self.people.append(person_name.upper())

                if wants_accommodation.upper() in ['YES', 'Y']:
                    # First add the fellow with their details to the person
                    # data dictionary.
                    self.person_data[person_id] = [new_person.person_name,
                                                   new_person.job_description.upper(),
                                                   wants_accommodation.upper()]
                    # Call the allocate_livingspace method and allocate a
                    # livingspace.
                    allocated_living_space = self.allocate_livingspace(
                        person_name.upper())
                    # Call the allocate_office method and allocate an office.
                    allocated_office = self.allocate_office(
                        person_name.upper())
                    return '{} successfully added! \nAllocated to:\nLivingSpace: {}\nOffice: {}' \
                        .format(person_name.upper(), allocated_living_space, allocated_office)

                elif wants_accommodation.upper() in ['NO', 'N']:
                    # First add the fellow with their details to the person
                    # data dictionary.
                    self.person_data[person_id] = [new_person.person_name,
                                                   new_person.job_description.upper(),
                                                   wants_accommodation.upper()]
                    # Call the allocate_office method and allocate an office.
                    allocated_office = self.allocate_office(
                        person_name.upper())
                    return '{} successfully added! \nAllocated to:\nOffice: {}' \
                        .format(person_name.upper(), allocated_office)

                else:
                    return 'Invalid accommodation input.'

            elif job_description.upper() == 'STAFF':
                # Add staff by name.
                new_person = Staff(person_name.upper())
                # Assign an ID for unique identification.
                person_id = 'S{}' .format(len(self.people) + 1)
                # Add the staff to a list containing all staff.
                self.staff.append(person_name.upper())
                # Add the staff to a list containing all people.
                self.people.append(person_name.upper())

                if wants_accommodation.upper() in ['YES', 'Y']:
                    return 'Staff cannot be allocated a livingspace.'

                elif wants_accommodation.upper() in ['NO', 'N']:
                    # First add the staff with their details to the person data
                    # dictionary.
                    self.person_data[person_id] = [new_person.person_name,
                                                   new_person.job_description.upper(),
                                                   wants_accommodation.upper()]
                    # Call the allocate_office method and allocate an office.
                    allocated_office = self.allocate_office(
                        person_name.upper())
                    return '{} successfully added! \nAllocated to:\nOffice: {}' \
                        .format(person_name.upper(), allocated_office)

                else:
                    return 'Invalid accommodation input.'

            else:
                return "Invalid job description."

    def allocate_livingspace(self, fellow_name):
        """
        allocate a livingspace to a fellow
        """
        # create a list of all vaccant livingspaces.
        vacant_livingspaces = []

        for room in self.livingspaces:
            # Check the length of livingspace allocations by room name.
            # Number of occupants should be less than the room capacity
            # Append the rooms that are not full to a list of vaccant
            # livingspaces.
            if len(self.livingspace_allocations[room]) < self.room_data[room][1]:
                vacant_livingspaces.append(room)
        # Check if the fellow you are trying to reallocate exists.
        if fellow_name not in self.people:
            return '{} does not exist.' .format(fellow_name.upper())
        else:

            if vacant_livingspaces:
                for room in self.livingspace_allocations:
                    # Check that a fellow is not being reallocated to a room they currently occupy.
                    # Do this by checking if their name exists in any room in
                    # the livingspace allocations
                    if fellow_name.upper() in self.livingspace_allocations[room]:
                        return '{} already allocated a livingspace.' \
                            .format(fellow_name.upper())
                # Pick a random room from vaccant livingspaces list.
                random_living_space = random.choice(vacant_livingspaces)
                # Insert the fellow name to the randomly chosen room.
                self.livingspace_allocations[random_living_space].append(
                    fellow_name.upper())
                # Check if the fellow name exists in a room within the
                # vaccant_livingspaces list and remove them.
                if fellow_name in vacant_livingspaces:
                    vacant_livingspaces.remove(fellow_name)

                return '{} allocated to {}.' \
                    .format(fellow_name.upper(), random_living_space)

            else:
                vacant_livingspaces.append(fellow_name.upper())
                return 'No vaccant livingspace.'

    def allocate_office(self, person_name):
        """
        allocate office to staff
        """
        vacant_offices = []
        for room in self.offices:

            if len(self.office_allocations[room]) < self.room_data[room][1]:
                vacant_offices.append(room)

        if person_name not in self.people:
            return '{} does not exist.' .format(person_name.upper())

        else:

            if vacant_offices:
                for room in self.office_allocations:
                    if person_name.upper() in self.office_allocations[room]:
                        return '{} already allocated to an office.' .format(person_name.upper())

                random_office = random.choice(vacant_offices)
                self.office_allocations[random_office].append(
                    person_name.upper())

                if person_name in vacant_offices:
                    vacant_offices.remove(person_name)
                return '{} allocated to {}.' .format(person_name.upper(), random_office)

            else:
                vacant_offices.append(person_name.upper())
                return 'No vaccant office.'

    def reallocate_person(self, person_id, room_name):
        """
        re-locate person method
        """
        person_data_list = self.person_data.get(person_id.upper())
        room_data_list = self.room_data.get(room_name.upper())

        if person_data_list is None:
            return '{} does not exist.' .format(person_id)

        elif room_data_list is None:
            return '{} does not exist.' .format(room_name)

        else:
            person_name = person_data_list[0].upper()
            person_job_type = person_data_list[1]
            room_type = room_data_list[0]
            room_capacity = room_data_list[1]

            if room_type == 'LIVINGSPACE':
                current_number_of_room_occupants = len(
                    self.livingspace_allocations[room_name])

                if person_name in self.livingspace_allocations[room_name]:
                    return "{} already allocated to {}." .format(person_name, room_name)

                elif current_number_of_room_occupants == room_capacity:
                    return '{} is already full.' .format(room_name)

                elif person_job_type == 'STAFF':
                    return 'Cannot reallocate staff member to a livingspace.'

                else:
                    for room in self.livingspace_allocations:
                        for person in self.livingspace_allocations[room]:
                            if person == person_name:
                                self.livingspace_allocations[room].remove(
                                    person_name)
                                self.livingspace_allocations[room_name].append(
                                    person_name)
                                return '{} has been reallocated to {}.' \
                                    .format(person_name, room_name.upper())
                    return '{} is not allocated any livingspace.' .format(person_name)

            if room_type == 'OFFICE':
                current_number_of_room_occupants = len(
                    self.office_allocations[room_name.upper()])

                if person_name in self.office_allocations[room_name.upper()]:
                    return '{} already allocated to {}' .format(person_name, room_name)

                elif current_number_of_room_occupants == room_capacity:
                    return '{} is already full.' .format(room_name)

                else:
                    for room in self.office_allocations:
                        for person in self.office_allocations[room]:
                            if person == person_name:
                                self.office_allocations[room].remove(
                                    person_name)
                                self.office_allocations[room_name.upper()].append(
                                    person_name)
                                return '{} has been reallocated to {}.' \
                                    .format(person_name, room_name.upper())
                    return '{} not yet allocated to any office.' .format(person_name)

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

    def print_staff(self):
        """
        print all staff
        """
        pass

    def print_all_people(self):
        """
        print all people method
        """
        pass

    def print_people_details(self):
        """
        Print everyone in the system starting with their unique ID's
        """
        if not self.person_data:
            return 'No one exists in the system yet.'
        else:
            for people_id, people_details in self.person_data.items():
                puts(colored.green(str(people_id) + ':' + str(people_details)))

            return 'Done.'
