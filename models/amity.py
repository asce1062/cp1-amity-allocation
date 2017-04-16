"""
Class Amity
"""
import random

from clint.textui import colored, puts

from models.room import LivingSpace, Office
from models.person import Fellow, Staff


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
    # List of all fellows not yet allocated to a livingspace.
    unallocated_livingspace = []
    # List of all fellows not yet allocated to an office.
    unallocated_office = []
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
                # with an empty list indicating that there are no occupants.
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
                # with an empty list indicating that there are no occupants.
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
                # Check if the fellow name exists in unallocated_livingspace
                # list and remove them.
                if fellow_name in self.unallocated_livingspace:
                    self.unallocated_livingspace.remove(fellow_name)
                return '{} allocated to {}.' \
                    .format(fellow_name.upper(), random_living_space)
            else:
                # If there is no empty livingspace add fellow to
                # unallocated_livingspace list
                self.unallocated_livingspace.append(fellow_name.upper())
                return 'No vaccant livingspace.'

    def allocate_office(self, person_name):
        """
        allocate office to staff
        """
        # create a list of all vaccant offices.
        vacant_offices = []
        for room in self.offices:
            # Check the length of office allocations by room name.
            # Number of occupants should be less than the room capacity
            # Append the rooms that are not full to a list of vaccant
            # offices.
            if len(self.office_allocations[room]) < self.room_data[room][1]:
                vacant_offices.append(room)
        # Check if the fellow you are trying to reallocate exists.
        if person_name not in self.people:
            return '{} does not exist.' .format(person_name.upper())
        else:
            if vacant_offices:
                for room in self.office_allocations:
                    # Check that a fellow is not being reallocated to a room they currently occupy.
                    # Do this by checking if their name exists in any room in
                    # the office allocations
                    if person_name.upper() in self.office_allocations[room]:
                        return '{} already allocated to an office.' .format(person_name.upper())
                # Pick a random room from vaccant livingspaces list.
                random_office = random.choice(vacant_offices)
                # Insert the fellow name to the randomly chosen room.
                self.office_allocations[random_office].append(
                    person_name.upper())
                # Check if the fellow name exists in unallocated_office
                # list and remove them.
                if person_name in self.unallocated_office:
                    self.unallocated_office.remove(person_name)
                return '{} allocated to {}.' .format(person_name.upper(), random_office)
            else:
                # If there is no empty office add person to
                # unallocated_office list
                self.unallocated_office.append(person_name.upper())
                return 'No vaccant office.'

    def reallocate_person(self, person_id, room_name):
        """
        re-locate person method
        """
        # Get people from person_data dict with their ID's as the key.
        person_data_list = self.person_data.get(person_id.upper())
        # Get rooms by room_name from room_data dict with their names as the
        # key.
        room_data_list = self.room_data.get(room_name.upper())
        # Check if person ID entered exists in our person data list.
        if person_data_list is None:
            return '{} does not exist.' .format(person_id)
        # Check if room name entered exists in our room data list.
        elif room_data_list is None:
            return '{} does not exist.' .format(room_name)
        else:
            # Person name at index 0 of the person data list.
            person_name = person_data_list[0].upper()
            # Person job description is at index 1 of the person data list.
            person_job_description = person_data_list[1]
            # Room type is at index 0 of the room data list.
            room_type = room_data_list[0]
            # Room capacity is at index 1 of the room data list.
            room_capacity = room_data_list[1]

            if room_type == 'LIVINGSPACE':
                # Current number of room occupants id the length of people
                # allocated to a particular room.
                current_number_of_room_occupants = len(
                    self.livingspace_allocations[room_name.upper()])
                # Check whether person being reallocated to a room is already
                # residing in that room.
                if person_name in self.livingspace_allocations[room_name.upper()]:
                    return "{} already allocated to {}." .format(person_name, room_name)
                # Check if the length of livingspace allocation by a particular
                # room name is equal to the allowed room capacity and return
                # that it is already full.
                elif current_number_of_room_occupants == room_capacity:
                    return '{} is already full.' .format(room_name)
                # Also check if the job_description provided is staff and
                # return that they cannot be allocated to livingspaces.
                elif person_job_description == 'STAFF':
                    return 'Cannot reallocate staff member to a livingspace.'
                else:
                    for room in self.livingspace_allocations:
                        # First verify that they are allocated a livingspace.
                        for person in self.livingspace_allocations[room]:
                            if person == person_name:
                                # Remove them from currently occupied room.
                                self.livingspace_allocations[room].remove(
                                    person_name)
                                # Add them to the newly allocated room.
                                self.livingspace_allocations[room_name].append(
                                    person_name)
                                return '{} has been reallocated to {}.' \
                                    .format(person_name, room_name.upper())
                    return '{} not yet allocated to any livingspace.' .format(person_name)
            if room_type == 'OFFICE':
                # Current number of room occupants id the length of people
                # allocated to a particular room.
                current_number_of_room_occupants = len(
                    self.office_allocations[room_name.upper()])
                # Check whether person being reallocated to a room is already
                # residing in that room.
                if person_name in self.office_allocations[room_name.upper()]:
                    return '{} already allocated to {}.' .format(person_name, room_name)
                # Check if the length of livingspace allocation by a particular
                # room name is equal to the allowed room capacity and return
                # that it is already full.
                elif current_number_of_room_occupants == room_capacity:
                    return '{} is already full.' .format(room_name)
                else:
                    for room in self.office_allocations:
                        # First verify that they are allocated an office.
                        for person in self.office_allocations[room]:
                            if person == person_name:
                                # Remove them from currently occupied room.
                                self.office_allocations[room].remove(
                                    person_name)
                                # Add them to the newly allocated room.
                                self.office_allocations[room_name.upper()].append(
                                    person_name)
                                return '{} has been reallocated to {}.' \
                                    .format(person_name, room_name.upper())
                    return '{} not yet allocated to any office.' .format(person_name)

    def load_people(self, filename):
        """
        load_people method
        """

        if filename:
            # Define file directory
            with open("models/" + filename + ".txt") as people_file:
                # Read until EOF and return a list containing the lines.
                people = people_file.readlines()
            for person in people:
                # Return a list of people and split at all whitespaces.
                person_data = person.split()
                # Check if person_data length is less than or equal to two.
                if len(person_data) <= 2:
                    return "Invalid number of arguments input."
                # Join the first and last names to one name.
                person_name = person_data[0] + person_data[1]
                job_description = person_data[2]
                if job_description == 'STAFF':
                    # If the job_description is STAFF default entry for
                    # accommodation is NO.
                    wants_accommodation = 'NO'
                    # Call add_person method.
                    self.add_person(person_name, job_description,
                                    wants_accommodation)
                elif job_description == "FELLOW":
                    # Check the length of each line.
                    if len(person_data) <= 3:
                        # If the length is 3 default wants_accommodation to NO.
                        wants_accommodation = "NO"
                        # Call add_person method.
                        self.add_person(
                            person_name, job_description, wants_accommodation)
                    # Check if accommodation option is provided.
                    elif len(person_data) == 4:
                        # Accommodation option is the third index since first
                        # name and last name are joined to one.
                        accommodation_option = person_data[3]
                        if accommodation_option == "Y":
                            # Convert accommodation option to YES for
                            # consistency.
                            wants_accommodation = "YES"
                            # Call add_person method.
                            self.add_person(
                                person_name, job_description, wants_accommodation)
                        elif accommodation_option == "N":
                            # Convert accommodation option to NO for
                            # consistency.
                            wants_accommodation = "NO"
                            # Call add_person method.
                            self.add_person(
                                person_name, job_description, wants_accommodation)
                            # Accommodation option should be either Y or N.
                        elif accommodation_option not in ['Y', 'N']:
                            return "Invalid accommodation input."
                    else:
                        return "Invalid number of arguments input."
                else:
                    return "Invalid job description."
            return "People successfully loaded."
        else:
            return "Filename must be provided."

    def load_rooms(self, filename):
        """
        load_rooms method
        """
        if filename:
            # Define file directory
            with open("models/" + filename + ".txt") as rooms_file:
                # Read until EOF and return a list containing the lines.
                rooms = rooms_file.readlines()
            for room in rooms:
                # Return a list of rooms and split at all whitespaces.
                rooms_data = room.split()
                # Check if rooms_data length is less than or equal to two.
                if len(rooms_data) > 2:
                    return "Invalid number of arguments input."
                # Assign room data and room_type indexes from the split data.
                rooms_name = rooms_data[0]
                rooms_type = rooms_data[1]
                # Call create_room method.
                self.create_room(rooms_name, rooms_type)
            return "Rooms successfully loaded from file."
        else:
            return "Filename must be provided."

    def print_allocations(self, filename):
        """
        print_allocations method
        """
        if filename:
            # Define file directory with the option 'w' to allow writing file
            # permissions.
            file = open("models/" + filename + ".txt", "w")
            # Write to file.
            file.write("LIVINGSPACE ALLOCATIONS\n")
            for room_name in self.livingspace_allocations:
                # Write room names to file.
                file.write("\n{}\n" .format(room_name))
                file.write("-" * 40)
                file.write("\n")
                # Iterate through all livingspace allocations and get all rooms
                # and their occupants.
                living_space_occupants = self.livingspace_allocations[room_name]
                # Below the room name write the occupants.
                file.write(", ".join(living_space_occupants))
                file.write("\n")
            file.write("\n\nOFFICE ALLOCATIONS\n")
            for room_name in self.office_allocations:
                # Write room names to file.
                file.write("\n{}\n" .format(room_name))
                file.write("-" * 40)
                file.write("\n")
                # Iterate through all office allocations and get all rooms
                # and their occupants.
                office_occupants = self.office_allocations[room_name]
                # Below the room name write the occupants.
                file.write(", ".join(office_occupants))
                file.write("\n")
            return "Done."
        else:
            puts(colored.blue('LIVINGSPACE ALLOCATIONS\n'))
            for room_name in self.livingspace_allocations:
                # Iterate through all livingspace allocations and get all rooms
                # and their occupants.
                livingspace_occupants = self.livingspace_allocations[room_name]
                # Print out the room name.
                puts(colored.cyan('\n{}' .format(room_name)))
                puts(colored.cyan('-' * 40))
                # Print out the occupants.
                puts(colored.green(',' .join(livingspace_occupants)))
            puts(colored.blue('\n\nOFFICE ALLOCATIONS\n'))
            for room_name in self.office_allocations:
                # Iterate through all office allocations and get all rooms
                # and their occupants.
                office_occupants = self.office_allocations[room_name]
                # Print out the room name.
                puts(colored.cyan('\n{}' .format(room_name)))
                puts(colored.cyan('-' * 40))
                # Print out the occupants.
                puts(colored.green(', ' .join(office_occupants)))

            return 'Done.'

    def print_specific_room_allocations(self, room_name):
        """
        print_specific_room_allocations method
        """
        # Convert room name provided to upper case for consistency.
        room_name = room_name.upper()
        # all_allocations is a dict containing livingspace allocations.
        all_allocations = dict(self.livingspace_allocations)
        # Add office allocations to all_allocations dict.
        all_allocations.update(self.office_allocations)
        # Make sure room name consists of alphabets only.
        if room_name.isalpha() is False:
            return "Invalid input."
        # Iterate through all_allocations.
        for room in all_allocations:
            # If the room exists...
            if room_name in room:
                # Print the room name.
                puts(colored.blue('\n{}' .format(room_name)))
                puts(colored.blue('-' * 40))
                # Print all occupants of that room.
                puts(colored.green(', '.join(all_allocations[room_name])))
        return "Done."

    def print_unallocated(self, filename):
        """
        print_unallocated method
        """
        if filename:
            # Define file directory with the option 'w' to allow writing file
            # permissions.
            file = open("models/" + filename + ".txt", "w")
            file.write("UNALLOCATED LIVING SPACES\n")
            # Write to file all fellows who have not been allocated any livingspace.
            file.write(", ".join(self.unallocated_livingspace))
            file.write("\n")
            file.write("-" * 40)
            file.write("\n\nUNALLOCATED OFFICES\n")
            # Write to file all fellows who have not been allocated any office.
            file.write(", ".join(self.unallocated_office))
            return "Done."

        else:
            puts(colored.blue('UNALLOCATED LIVINGSPACE\n'))
            puts(colored.blue('-' * 40))
            # Print all fellows who have not been allocated any livingspace.
            puts(colored.green(', ' .join(self.unallocated_livingspace)))
            puts('\n')
            puts(colored.blue('\n\nUNALLOCATED OFFICE\n'))
            puts(colored.blue('-' * 40))
            # Print all fellows who have not been allocated any office.
            puts(colored.green(', ' .join(self.unallocated_office)))
            puts('\n')
            return "Done."

    def print_rooms(self):
        """
        print_room method
        """
        puts(colored.blue('ALL ROOMS:\n'))
        puts(colored.blue('-' * 40))
        # Print all rooms.
        puts(colored.green('{}' .format(self.rooms)))
        puts('\n')
        puts(colored.blue('\nLIVINGSPACES:'))
        puts(colored.blue('-' * 40))
        # Print all livingspaces.
        puts(colored.green('{}' .format(self.livingspaces)))
        puts('\n')
        puts(colored.blue('\nOFFICES:'))
        puts(colored.blue('-' * 40))
        # Print all offices.
        puts(colored.green('{}' .format(self.offices)))
        return 'Done.'

    def print_fellows(self):
        """
        print all fellows
        """
        puts(colored.blue('ALL FELLOWS:'))
        puts(colored.blue('-' * 40))
        #Print all fellows.
        puts(colored.green('{}' .format(self.fellows)))
        return 'Done.'

    def print_staff(self):
        """
        print all staff
        """
        puts(colored.blue('ALL STAFF:'))
        puts(colored.blue('-' * 40))
        #Print all staff.
        puts(colored.green('{}' .format(self.staff)))
        return "Done."

    def print_all_people(self):
        """
        print all people method
        """
        puts(colored.blue('ALL PEOPLE:'))
        puts(colored.blue('-' * 40))
        self.people.sort()
        # Print all people.
        puts(colored.green('{}' .format(self.people)))
        return "Done."

    def print_people_details(self):
        """
        Print everyone in the system starting with their unique ID's
        """
        # Check if person data dictionary is empty.
        if not self.person_data:
            return 'No one exists in the system yet.'
        else:
            # Get person_data (key, value) pairs, as 2-tuples.
            for people_id, people_details in self.person_data.items():
                puts(colored.green(str(people_id) + ':' + str(people_details)))
            return 'Done.'
