#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
All the functions for our Amity Office Space Allocation application.
Currently we support the following functionality:

1. **create_room** - Creates rooms in Amity.
                        (jump to section in [[amity.py#create_room]] )

2. **add_person** - Adds a person to the system and allocates the person to a random room.
                    ( jump to section in [[amity.py#add_person] )

3. **allocate_livingspace** - Called to allocate a livingspace to a fellow who wants/needs one.
                            (jump to section in [[amity.py#allocate_livingspace]])

5. **allocate_office** - Called to allocate an office to both fellows and staff members.
                            (jump to section in [[amity.py#allocate_office]])

6. **reallocate_person** - Reallocate the person.
                            (jump to section in [[amity.py#reallocate_person]])

7. **load_people** - Adds people to rooms from a txt file.
                            (jump to section in [[amity.py#load_people]])

8. **load_rooms** - Adds rooms to amity from a txt file.
                            (jump to section in [[amity.py#load_rooms]])

9. **print_allocations** - Prints a list of allocations onto the screen. Specifying the optional
                            -o  option here outputs the registered allocations to a txt file.
                            (jump to section in [[amity.py#print_allocations]])

10. **print_specific_room_allocations** - Prints a list of allocations
                                            for a specific room onto the screen.
                            (jump to section in [[amity.py#print_specific_room_allocations]])

11. **print_unallocated** - Prints a list of unallocated people to the screen.
                            Specifying the  -o  option here outputs the information
                            to the txt file provided names of all the people in
                            room_name  on the screen
                            (jump to section in [[amity.py#print_specific_room_allocations]])

12. **print_rooms** - Prints a list of all available rooms to the screen.
                            (jump to section in [[amity.py#print_rooms]])

13. **print_fellows** - Prints a list of all fellows to the screen.
                            (jump to section in [[amity.py#print_fellows]])

14. **print_staff** - Prints a list of all staff to the screen.
                            (jump to section in [[amity.py#print_staff]])

15. **print_all_people** - Prints a list of all people to the screen.
                            (jump to section in [[amity.py#print_all_people]])

16. **print_people_details** - Prints a list of all people to the screen with their details.
                                i.e ID, Name, Job Description and Accommodation choice.
                            (jump to section in [[amity.py#print_people_details]])

17. **save_state** - Persists all the data stored in the app to a SQLite database.
                        Specifying the  --db  parameter explicitly stores the data
                        in the sqlite_database  specified.
                        (jump to section in [[amity.py#save_state]])

18. **load_state** - Loads data from a database into the application.
                        (jump to section in [[amity.py#load_state]])

19. **clear_db** - Clears all data from a database.
                        (jump to section in [[amity.py#clear_db]])

20. **delete_person** - Removes a person from our Amity Office Space Allocation application.
                        (jump to section in [[amity.py#delete_person]])

21. **delete_room** - Removes a room from our Amity Office Space Allocation application.
                        (jump to section in [[amity.py#delete_room]])
"""

import os
import random

from clint.textui import colored, puts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# defined in [[database_models.py]]

from databases.database_models import (AmityFellows,
                                       AmityLivingspaceAllocations,
                                       AmityLivingspaces,
                                       AmityOfficeAllocations, AmityOffices,
                                       AmityPeople, AmityPersondata,
                                       AmityRoomdata, AmityRooms, AmityStaff,
                                       AmityUnallocatedlivingspace,
                                       AmityUnallocatedoffice, Base)

# defined in [[person.py]]

from models.person import Fellow, Staff

# defined in [[room.py]]

from models.room import LivingSpace, Office


class Amity(object):

    """
    Class Amity
    """

    # List of all rooms. Livingspaces and Offices.

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

    # === create_room ===
    def create_room(self, room_name, room_type):
        """
        Creates rooms in Amity.

        - Achieve this by first checking if a room exist.
        - Create a new room of type livingspace or office.
        - Append the room to:
                        1. List of rooms.
                        2. List of livingspaces or offices
                        3. Room data dict with [room_name] as the key,
                            and the [room_type] and [room_capacity].
                        4. Also add it to either [livingspace_allocations]
                            or [office_allocations] dict with an empty list.

        Args:
            room_name:   The name of our room.
            room_type:   The room type. Whether office or livingspace.

        Returns:
            {room_name} already exists.
            {room_name} created.
            Invalid room type.
        """

        # Convert all inputs to upper case for consistency.

        room_name = room_name.upper()
        room_type = room_type.upper()

        # Check if a room already exists in the list of rooms.

        if room_name in self.rooms:

            return '{} already exists.'.format(room_name)

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

    # === add_person ===
    def add_person(self, person_name, job_description, wants_accommodation='N'):
        """
        Adds a person to the system and allocates the person to a random room.

        - Achieve this by first checking if the name provided contains non alphabetical chars.
        - Add fellow or staff by name.
        - Assign an ID for unique identification. i.e people count + 1
        - Append the fellow or staff to:
                        1. List of all people.
                        2. List of all fellows or staff.
                        3. Person data dict with [person_id] as the key,
                            and the [person_name], [job_description]
                            and [wants_accommodation].
                        4. Call the [allocate_livingspace] method if the person being added
                             is a fellow and the want accommodation
                             Allocate a livingspace using the name provided.
                        5. Call the [allocate_office] method and allocate an office
                            using the name provided.

        Args:
            person_name:   The name of the person you want to add to amity.
            job_description:   The job description of the person you want to add to amity.
            wants_accommodation:   whether the person wants accommodation.
                                    Defaulted to no if no choice is provided.

        Returns:
            Invalid person name.

            {person_name} successfully added! \n
            Allocated to:\n
            Office: {{No vaccant office.}}

            {person_name} successfully added! \n
            Allocated to:\n
            LivingSpace: {{No vaccant Livingspace.}}\n
            Office: {{No vaccant office.}}

            {person_name} successfully added! \n
            Allocated to:\n
            Office: {{person_name} allocated to {vacant_offices}.}

            {person_name} successfully added! \n
            Allocated to:\n
            LivingSpace: {{fellow_name} allocated to {vacant_livingspaces}.}\n
            Office: {{person_name} allocated to {vacant_offices}.}

            Invalid accommodation input.
            Staff cannot be allocated a livingspace.
            Invalid job description.
        """

        # Check if person name is alphabest only.

        if person_name.isalpha() is False:

            return 'Invalid person name.'

        else:

            if job_description.upper() == 'FELLOW':

                if wants_accommodation.upper() in ['YES', 'Y']:

                    # Add fellow by name.

                    new_person = Fellow(person_name.upper())

                    # Assign an ID for unique identification.

                    person_id = 'F{}'.format(len(self.people) + 1)

                    # Add the fellow to a list containing all people.

                    self.people.append(person_name.upper())

                    # Add the fellow to a list containing all fellows.

                    self.fellows.append(person_name.upper())

                    # Add the fellow with their details to the person
                    # data dictionary.

                    self.person_data[person_id] = \
                        [new_person.person_name,
                         new_person.job_description.upper(),
                         wants_accommodation.upper()]

                    # Call the allocate_livingspace method and allocate a
                    # livingspace.

                    allocated_living_space = \
                        self.allocate_livingspace(person_name.upper())

                    # Call the allocate_office method and allocate an office.

                    allocated_office = \
                        self.allocate_office(person_name.upper())

                    return '{} successfully added! \nAllocated to:\nLivingSpace: {}\nOffice: {}' \
                        .format(person_name.upper(), allocated_living_space, allocated_office)

                elif wants_accommodation.upper() in ['NO', 'N']:

                    # Add fellow by name.

                    new_person = Fellow(person_name.upper())

                    # Assign an ID for unique identification.

                    person_id = 'F{}'.format(len(self.people) + 1)

                    # Add the fellow to a list containing all people.

                    self.people.append(person_name.upper())

                    # Add the fellow to a list containing all fellows.

                    self.fellows.append(person_name.upper())

                    # Add the fellow with their details to the person
                    # data dictionary.

                    self.person_data[person_id] = \
                        [new_person.person_name,
                         new_person.job_description.upper(),
                         wants_accommodation.upper()]

                    # Call the allocate_office method and allocate an office.

                    allocated_office = \
                        self.allocate_office(person_name.upper())

                    return '{} successfully added! \nAllocated to:\nOffice: {}' \
                        .format(person_name.upper(), allocated_office)

                else:

                    return 'Invalid accommodation input.'

            elif job_description.upper() == 'STAFF':

                if wants_accommodation.upper() in ['YES', 'Y']:

                    return 'Staff cannot be allocated a livingspace.'

                elif wants_accommodation.upper() in ['NO', 'N']:

                    # Add staff by name.

                    new_person = Staff(person_name.upper())

                    # Assign an ID for unique identification.

                    person_id = 'S{}'.format(len(self.people) + 1)

                    # Add the staff to a list containing all people.

                    self.people.append(person_name.upper())

                    # Add the staff to a list containing all staff.

                    self.staff.append(person_name.upper())

                    # Add the staff with their details to the person data
                    # dictionary.

                    self.person_data[person_id] = \
                        [new_person.person_name,
                         new_person.job_description.upper(),
                         wants_accommodation.upper()]

                    # Call the allocate_office method and allocate an office.

                    allocated_office = \
                        self.allocate_office(person_name.upper())

                    return '{} successfully added! \nAllocated to:\nOffice: {}' \
                        .format(person_name.upper(), allocated_office)

                else:

                    return 'Invalid accommodation input.'

            else:

                return 'Invalid job description.'

    # === allocate_livingspace ===
    def allocate_livingspace(self, fellow_name):
        """
        Allocates a person to a random livingspace.

        - Achieve this by first checking if there are any rooms that are not full.
            check the length of all rooms in [livingspace_allocation] in comparison
            to the set room capacity for each room type.
        - Add these rooms ((if available)) to a list, [vaccant_livingspaces].
        - verify that the fellow you are trying to allocate a room to exists in amity.
        - Check that the fellow is not being allocated to a room they currently occupy.
        - Pick a random room from the [vaccant_livingspaces] list.
        - Append the fellow to the randomly chosen room.
        - Remove the fellow from the [unallocated_livingspace] list.

        Args:
            fellow_name:   The name of the person you want to add to amity.

        Returns:
            {fellow_name} does not exist.
            {fellow_name} already allocated a livingspace.
            {fellow_name} allocated to {vacant_livingspaces}.
            No vaccant livingspace.
            """

        # create a list of all vaccant livingspaces.

        vacant_livingspaces = []

        for room in self.livingspaces:

            # Check the length of livingspace allocations by room name.
            # Number of occupants should be less than the room capacity
            # Append the rooms that are not full to a list of vaccant
            # livingspaces.

            if len(self.livingspace_allocations[room]) \
                    < self.room_data[room][1]:
                vacant_livingspaces.append(room)

        # Check if the fellow you are trying to reallocate exists.

        if fellow_name not in self.people:

            return '{} does not exist.'.format(fellow_name.upper())

        else:

            if vacant_livingspaces:

                for room in self.livingspace_allocations:

                    # Check that a fellow is not being reallocated to a room they currently occupy.
                    # Do this by checking if their name exists in any room in
                    # the livingspace allocations

                    if fellow_name.upper() \
                            in self.livingspace_allocations[room]:

                        return '{} already allocated a livingspace.'.format(fellow_name.upper())

                # Pick a random room from vaccant livingspaces list.

                random_living_space = random.choice(vacant_livingspaces)

                # Insert the fellow name to the randomly chosen room.

                self.livingspace_allocations[random_living_space].append(
                    fellow_name.upper())

                # Check if the fellow name exists in unallocated_livingspace
                # list and remove them.

                if fellow_name in self.unallocated_livingspace:

                    self.unallocated_livingspace.remove(fellow_name)

                return '{} allocated to {}.'.format(fellow_name.upper(),
                                                    random_living_space)

            else:

                # If there is no empty livingspace add fellow to
                # unallocated_livingspace list

                self.unallocated_livingspace.append(fellow_name.upper())

                return 'No vaccant livingspace.'

    # === allocate_office ===
    def allocate_office(self, person_name):
        """
        Allocates a person to a random office.

        - Achieve this by first checking if there are any rooms that are not full.
            check the length of all rooms in [office_allocation] in comparison
            to the set room capacity for each room type.
        - Add these rooms ((if available)) to a list, [vaccant_offices].
        - verify that the person you are trying to allocate a room to exists in amity.
        - Check that the person is not being allocated to a room they currently occupy.
        - Pick a random room from the vaccant_offices list.
        - Append the person to the randomly chosen room.
        - Remove the person from the unallocated_office list.

        Args:
            person_name:   The name of the person you want to add to amity.

        Returns:
            {person_name} does not exist.
            {person_name} already allocated an office.
            {person_name} allocated to {vacant_office}.
            No vaccant office.
            """

        # create a list of all vaccant offices.

        vacant_offices = []

        for room in self.offices:

            # Check the length of office allocations by room name.
            # Number of occupants should be less than the room capacity
            # Append the rooms that are not full to a list of vaccant
            # offices.

            if len(self.office_allocations[room]) \
                    < self.room_data[room][1]:
                vacant_offices.append(room)

        # Check if the person you are trying to reallocate exists.

        if person_name not in self.people:

            return '{} does not exist.'.format(person_name.upper())

        else:

            if vacant_offices:

                for room in self.office_allocations:

                    # Check that a person is not being reallocated to a room they currently occupy.
                    # Do this by checking if their name exists in any room in
                    # the office allocations

                    if person_name.upper() \
                            in self.office_allocations[room]:

                        return '{} already allocated to an office.'.format(person_name.upper())

                # Pick a random room from vaccant offices list.

                random_office = random.choice(vacant_offices)

                # Insert the person name to the randomly chosen room.

                self.office_allocations[random_office].append(
                    person_name.upper())

                # Check if the person name exists in unallocated_office
                # list and remove them.

                if person_name in self.unallocated_office:

                    self.unallocated_office.remove(person_name)

                return '{} allocated to {}.'.format(person_name.upper(),
                                                    random_office)

            else:

                # If there is no empty office add person to
                # unallocated_office list

                self.unallocated_office.append(person_name.upper())

                return 'No vaccant office.'

    # === reallocate_person ===
    def reallocate_person(self, person_id, room_name):
        """
        Reallocate the person with  [person_identifier]  to  [new_room_name]

        - Get [person_data] dict and search with [person_id] as the key.
        - Get [room_data] dict and search with the [room_name] as the key.
        - Check if the [person_id] and [room_name] exist.
        - Get the [person_name[0]] and [job_description[1]] of the entered ID.
        - Get the [room_type[0]] and [room_capacity[1]] of the entered ID.
        - Check if they are being allocated to the same room they currently reside in.
        - Check that the length of the room being reallocated to is less than the allowed
            capacity.
        - Check if the [job_description] and return that they cannot be allocated to a
            livingspace.
        - Verify that they have been allocated to a room first.
        - Remove them from the currently occupied room.
        - Add them to the new room.

        Args:
            person_id:   The ID of the person you want to re-allocate
            room_name:   The name of the room you want to re-allocate to.

        Returns:
            {person_id} does not exist.
            {room_name} does not exist.
            {person_name} already allocated to {room_name}.
            {room_name} is already full.
            Cannot reallocate staff member to a livingspace.
            {person_name} has been reallocated to {room_name}.
            {person_name} not yet allocated to any livingspace.
            {person_name} already allocated to {room_name}.
            {person_name} not yet allocated to any office.
            """

        # Get person from person_data dict with the ID's as the key.

        person_data_list = self.person_data.get(person_id.upper())

        # Get room by room_name from room_data dict with the name as the
        # key.

        room_data_list = self.room_data.get(room_name.upper())

        # Check if person ID entered exists in our person data list.

        if person_data_list is None:

            return '{} does not exist.'.format(person_id)

        elif room_data_list is None:

            # Check if room name entered exists in our room data list.

            return '{} does not exist.'.format(room_name)

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

                # Current number of room occupants is the length of people
                # allocated to a particular room.

                current_number_of_room_occupants = \
                    len(self.livingspace_allocations[room_name.upper()])

                # Check whether person being reallocated to a room is already
                # residing in that room.

                if person_name \
                        in self.livingspace_allocations[room_name.upper()]:

                    return '{} already allocated to {}.'.format(person_name,
                                                                room_name)

                elif current_number_of_room_occupants == room_capacity:

                    # Check if the length of livingspace allocation by a particular
                    # room name is equal to the allowed room capacity and return
                    # that it is already full.

                    return '{} is already full.'.format(room_name)

                elif person_job_description == 'STAFF':

                    # Also check if the job_description provided is staff and
                    # return that they cannot be allocated to livingspaces.

                    return 'Cannot reallocate staff member to a livingspace.'

                else:

                    for room in self.livingspace_allocations:

                        # First verify that they are allocated a livingspace.

                        for person in \
                                self.livingspace_allocations[room]:

                            if person == person_name:

                                # Remove them from currently occupied room.

                                self.livingspace_allocations[room].remove(
                                    person_name)

                                # Add them to the newly allocated room.

                                self.livingspace_allocations[room_name].append(
                                    person_name)

                                return '{} has been reallocated to {}.'.format(person_name,
                                                                               room_name.upper())

                    return '{} not yet allocated to any livingspace.'.format(person_name)

            if room_type == 'OFFICE':

                # Current number of room occupants id the length of people
                # allocated to a particular room.

                current_number_of_room_occupants = \
                    len(self.office_allocations[room_name.upper()])

                # Check whether person being reallocated to a room is already
                # residing in that room.

                if person_name \
                        in self.office_allocations[room_name.upper()]:

                    return '{} already allocated to {}.'.format(person_name,
                                                                room_name)

                elif current_number_of_room_occupants == room_capacity:

                    # Check if the length of office allocation by a particular
                    # room name is equal to the allowed room capacity and return
                    # that it is already full.

                    return '{} is already full.'.format(room_name)

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

                                return '{} has been reallocated to {}.'.format(person_name,
                                                                               room_name.upper())

                    return '{} not yet allocated to any office.'.format(person_name)

    # === load_people ===
    def load_people(self, filename):
        """
        Adds people to rooms from a txt file.

        - Check that the file entered exits.
        - Read until EOF, return a list of all lines then split the lines at whitespaces.
        - Check if the length of each list and if less than or equal to 2.
        - Join the first and second index to [person_name] and the [job_description]
            to be the third index.
        - If the [job_description] is staff and no accommodation choice is provided
            default the accommodation choice to "NO"
        - Call the[[add_person]] method and pass [person_name], [job_description]
            and [wants_accommodation].
        - Check if the [job_description] is fellow and if accommodation choice is provided.
            If not, default it to "NO". Call [[add_person]] method and pas [person_name],
            [job_description] and [wants_accommodation]

        Args:
            filename:   The name of the file to be loaded.

        Returns:
            File does not exist.
            Invalid number of arguments input.
            Invalid accommodation input.
            Invalid job description.
            People successfully loaded.
            Filename must be provided.
            """

        if filename:

            # Define file directory

            if os.path.isfile('textfiles/' + filename + '.txt') is False:

                return 'File does not exist.'

            else:

                with open('textfiles/' + filename + '.txt') as people_file:

                    # Read until EOF and return a list containing the lines.

                    people = people_file.readlines()

                for person in people:

                    # Return a list of people and split at all whitespaces.

                    person_data = person.split()

                    # Check if person_data length is less than or equal to two.

                    if len(person_data) <= 2:
                        return 'Invalid number of arguments input.'

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

                    elif job_description == 'FELLOW':

                        # Check if person_data length is less than or equal to
                        # three.

                        if len(person_data) <= 3:

                            # If the length is 3 default wants_accommodation to
                            # NO.

                            wants_accommodation = 'NO'

                            # Call add_person method.

                            self.add_person(person_name, job_description,
                                            wants_accommodation)

                        # Check if person_data length is equal to four.

                        elif len(person_data) == 4:

                            # Check if accommodation option is provided.
                            # Accommodation option is the third index since first
                            # name and last name are joined to one.

                            accommodation_option = person_data[3]

                            if accommodation_option == 'Y':

                                # Convert accommodation option to YES for
                                # consistency.

                                wants_accommodation = 'YES'

                                # Call add_person method.

                                self.add_person(person_name,
                                                job_description,
                                                wants_accommodation)

                            elif accommodation_option == 'N':

                                # Convert accommodation option to NO for
                                # consistency.

                                wants_accommodation = 'NO'

                                # Call add_person method.

                                self.add_person(person_name,
                                                job_description,
                                                wants_accommodation)
                            elif accommodation_option not in ['Y', 'N']:

                                # Accommodation option should be either Y or N.

                                return 'Invalid accommodation input.'
                        else:
                            return 'Invalid number of arguments input.'
                    else:
                        return 'Invalid job description.'
            return 'People successfully loaded.'
        else:
            return 'Filename must be provided.'

    # === load_rooms ===
    def load_rooms(self, filename):
        """
        Adds rooms to amity from a txt file.

        - Check that the file entered exits.
        - Read until EOF, return a list of all lines then split the lines at whitespaces.
        - Check if the length of each list is less than 2.
        - Assign [room_name[0]] [room_type[1]] to the indexes in the split data.
        - Call the [[create_room]] and pass thearguments [room_name] and [room_type]

        Args:
            filename:   The name of the file to be loaded.

        Returns:
            File does not exist.
            Invalid number of arguments input.
            Rooms successfully loaded from file.
            Filename must be provided.
            """

        if filename:

            # Define file directory
            if os.path.isfile('textfiles/' + filename + '.txt') is False:

                return 'File does not exist.'

            else:

                with open('textfiles/' + filename + '.txt') as rooms_file:

                    # Read until EOF and return a list containing the lines.

                    rooms = rooms_file.readlines()

                for room in rooms:

                    # Return a list of rooms and split at all whitespaces.

                    rooms_data = room.split()

                    # Check if rooms_data length is less than or equal to two.

                    if len(rooms_data) > 2:
                        return 'Invalid number of arguments input.'

                    # Assign room data and room_type indexes from the split
                    # data.

                    rooms_name = rooms_data[0]
                    rooms_type = rooms_data[1]

                    # Call create_room method.

                    self.create_room(rooms_name, rooms_type)

                return 'Rooms successfully loaded from file.'

        else:

            return 'Filename must be provided.'

    # === print_allocations ===
    def print_allocations(self, filename):
        """
        Prints allocations to a file or the screen.

        - Create a file with the filename entered.
        - Write all room names to the file.
        - Iterate through all [livingspce_allocations and [office_allocations]
            using the [room_name] to search the dict.
        - Join the occupants an write them bellow each room.
        - If no filename is provided print the data to screen.

        Args:
            filename:   The name of the file to write the output to.

        Returns:
            Done.
            """

        if filename:

            # Define filename with the option 'w' to allow writing file
            # permissions.

            file = open('textfiles/' + filename + '.txt', 'w')

            # Write to file.

            file.write('LIVINGSPACE ALLOCATIONS\n')

            for room_name in self.livingspace_allocations:

                # Write room names to file.

                file.write("\n{}\n" .format(room_name))

                file.write('-' * 40)

                file.write('\n')

                # Iterate through all livingspace allocations and get all rooms
                # and their occupants.

                living_space_occupants = \
                    self.livingspace_allocations[room_name]

                # Below the room name write the occupants.

                file.write(', '.join(living_space_occupants))

                file.write('\n')

            file.write("\n\nOFFICE ALLOCATIONS\n")

            for room_name in self.office_allocations:

                # Write room names to file.

                file.write("\n{}\n" .format(room_name))

                file.write('-' * 40)

                file.write('\n')

                # Iterate through all office allocations and get all rooms
                # and their occupants.

                office_occupants = self.office_allocations[room_name]

                # Below the room name write the occupants.

                file.write(', '.join(office_occupants))

                file.write('\n')

            return 'Done.'

        else:

            puts(colored.blue('LIVINGSPACE ALLOCATIONS\n'))

            for room_name in self.livingspace_allocations:

                # Iterate through all livingspace allocations and get all rooms
                # and their occupants.

                livingspace_occupants = \
                    self.livingspace_allocations[room_name]

                # Print out the room name.

                puts(colored.cyan('\n{}'.format(room_name)))

                puts(colored.cyan('-' * 40))

                # Print out the occupants.

                puts(colored.green(', ' .join(livingspace_occupants)))

            puts(colored.blue('\n\nOFFICE ALLOCATIONS\n'))

            for room_name in self.office_allocations:

                # Iterate through all office allocations and get all rooms
                # and their occupants.

                office_occupants = self.office_allocations[room_name]

                # Print out the room name.

                puts(colored.cyan('\n{}'.format(room_name)))

                puts(colored.cyan('-' * 40))

                # Print out the occupants.

                puts(colored.green(', '.join(office_occupants)))

            return 'Done.'

    # === print_specific_room_allocations ===
    def print_specific_room_allocations(self, room_name):
        """
        Prints specific room allocations to the screen.

        - Create a dict [all_allocations]
        - In it store both [livingspace_allocations] and [office_allocations]
        - Write all room names to the file.
        - Iterate through [all_allocations] using the [room_name] provided.
        - Join the occupants an print them bellow the room.

        Args:
            room_name:   The name of the room you want to print the occupants.

        Returns:
            Invalid input.
            Done.
            """

        # Convert room name provided to upper case for consistency.

        room_name = room_name.upper()

        # all_allocations is a dict containing livingspace allocations.

        all_allocations = dict(self.livingspace_allocations)

        # Add office allocations to all_allocations dict.

        all_allocations.update(self.office_allocations)

        # Make sure room name consists of alphabets only.

        if room_name.isalpha() is False:
            return 'Invalid input.'

        # Iterate through all_allocations.

        for room in all_allocations:

            # If the room exists...

            if room_name in room:

                # Print the room name.

                puts(colored.blue('\n{}'.format(room_name)))

                puts(colored.blue('-' * 40))

                # Print all occupants of that room.

                puts(colored.green(' '.join(all_allocations[room_name])))

        return 'Done.'

    # === print_unallocated ===
    def print_unallocated(self, filename):
        """
        Prints all unallocated people to a file or the screen.

        - Create a file with the filename entered.
        - Write all people in [unallocated_livingspaces] and [unallocated_office] to the file.
        - If no filename s provided, print them to the screen.

        Args:
            filename:   The name of the file to write the output to.

        Returns:
            Done.
            """

        if filename:

            # Define filename with the option 'w' to allow writing file
            # permissions.

            file = open('textfiles/' + filename + '.txt', 'w')

            file.write('UNALLOCATED LIVING SPACES\n')

            # Write to file all fellows who have not been allocated any
            # livingspace.

            file.write(', '.join(self.unallocated_livingspace))

            file.write('\n')

            file.write('-' * 40)

            file.write("\n\nUNALLOCATED OFFICES\n")

            # Write to file all fellows who have not been allocated any office.

            file.write(', '.join(self.unallocated_office))

            return 'Done.'

        else:

            puts(colored.blue('UNALLOCATED LIVINGSPACE\n'))

            puts(colored.blue('-' * 40))

            # Print all fellows who have not been allocated any livingspace.

            puts(colored.green(', '.join(self.unallocated_livingspace)))

            puts('\n')

            puts(colored.blue('\n\nUNALLOCATED OFFICE\n'))

            puts(colored.blue('-' * 40))

            # Print all fellows who have not been allocated any office.

            puts(colored.green(', '.join(self.unallocated_office)))

            puts('\n')

            return 'Done.'

    # === print_rooms ===
    def print_rooms(self):
        """
        Prints all room in amity to the screen.

        - Print out all [rooms[]], [offices[]] and [livingspaces[]] to the screen.

        Returns:
            Done.
            """

        puts(colored.blue('ALL ROOMS:\n'))

        puts(colored.blue('-' * 40))

        # Print all rooms.

        puts(colored.green('{}'.format(self.rooms)))

        puts('\n')

        puts(colored.blue('\nLIVINGSPACES:'))

        puts(colored.blue('-' * 40))

        # Print all livingspaces.

        puts(colored.green('{}'.format(self.livingspaces)))

        puts('\n')

        puts(colored.blue('\nOFFICES:'))

        puts(colored.blue('-' * 40))

        # Print all offices.

        puts(colored.green('{}'.format(self.offices)))

        return 'Done.'

    # === print_fellows ===
    def print_fellows(self):
        """
        Prints all fellows in amity to the screen.

        - Print out all [fellows[]] to the screen.

        Returns:
            Done.
            """

        puts(colored.blue('ALL FELLOWS:'))

        puts(colored.blue('-' * 40))

        # Print all fellows.

        puts(colored.green('{}' .format(self.fellows)))

        return 'Done.'

    # === print_staff ===
    def print_staff(self):
        """
        Prints all staff in amity to the screen.

        - Print out all [staff[]] to the screen.

        Returns:
            Done.
            """

        puts(colored.blue('ALL STAFF:'))

        puts(colored.blue('-' * 40))

        # Print all fellows.

        puts(colored.green('{}'.format(self.staff)))

        return 'Done.'

    # === print_all_people ===
    def print_all_people(self):
        """
        Prints all people at amity to the screen.

        - Print out all [people[]] to the screen.

        Returns:
            Done.
            """

        puts(colored.blue('ALL PEOPLE:'))

        puts(colored.blue('-' * 40))

        self.people.sort()

        # Print all people.

        puts(colored.green('{}'.format(self.people)))

        return 'Done.'

    # === print_people_details ===
    def print_people_details(self):
        """
        Prints people details to the screen.

        - Check if [person_data] dict is empty
        - Get person_data (key, value) pairs, as 2-tuples.

        Returns:
            Done.
            """

        # Check if person data dictionary is empty.

        if not self.person_data:

            return 'No one exists in the system yet.'

        else:

            # Get person_data (key, value) pairs, as 2-tuples.

            for (people_id, people_details) in self.person_data.items():

                puts(colored.green(str(people_id) + ':'
                                   + str(people_details)))

            return 'Done.'

    # === save_state ===
    def save_state(self, dbname=''):
        """
        Saves all our data in application memory to the database.

        - If the [dbname] is specified use it, else use amity as the dbname.
        - Clear the database to avoid saving the same data to the database.
        - Create a new session.
        - Create an engine that will be used by our session.
        - Bind the engine to our session.
        - Instantiate db transactions via our session.
        - Get the data from our respectivedata structures.
        - Indext data in dicts to individual columns.
        - Add data to our session pending commit.
        - Commit our data to the database.

        Args:
            dbname:   The name of the database to save the data in application memory.

        Returns:
            Data saved successfully.
            """

        # Application starts

        if dbname:

            name = dbname

        else:

            name = 'amity'

        # Clear database to prevent saving data that already exists.

        self.clear_db(name)

        # new session.   no connections are in use.

        DBSession = sessionmaker()

        # an Engine, which the Session will use for connection resources

        engine = create_engine('sqlite:///' + 'databases/' + name
                               + '.db')

        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        # create a configured "Session" class

        DBSession.configure(bind=engine)

        # instantiate database transactions
        # A Session() instance establishes all conversations with the database
        # and represents a "staging zone" for all the objects loaded into the
        # database session object. Any change made against the objects in the
        # session won't be persisted into the database until you call
        # session.commit(). If you're not happy about the changes, you can
        # revert all of them back to the last commit by calling
        # session.rollback()
        # create a Session

        session = DBSession()

        for room_name in Amity.rooms:

            room_name = room_name

            # Insert room_names into ROOMS table.

            room_details = AmityRooms(room_name)

            session.add(room_details)

        for room_name in Amity.offices:

            room_name = room_name

            # Insert room_names into OFFICES table.

            room_details = AmityOffices(room_name)

            session.add(room_details)

        for room_name in Amity.livingspaces:

            room_name = room_name

            # Insert room_names into LIVINGSPACES table.

            room_details = AmityLivingspaces(room_name)

            session.add(room_details)

        for person_name in Amity.people:

            person_name = person_name

            # Insert person_names into PEOPLE table.

            person_data = AmityPeople(person_name)

            session.add(person_data)

        for person_name in Amity.fellows:

            fellow_name = person_name

            # Insert person_names into FELLOWS table.

            person_data = AmityFellows(fellow_name)

            session.add(person_data)

        for person_name in Amity.staff:

            staff_name = person_name

            # Insert person_names into STAFF table.

            person_data = AmityStaff(staff_name)

            session.add(person_data)

        for fellow_name in Amity.unallocated_livingspace:

            fellow_name = fellow_name

            # Insert person_names into UNALLOCATEDLIVINGSPACE table.

            person_data = AmityUnallocatedlivingspace(fellow_name)

            session.add(person_data)

        for person_name in Amity.unallocated_office:

            person_name = person_name

            # Insert person_names into UNALLOCATEDOFFICE table.

            person_data = AmityUnallocatedoffice(person_name)

            session.add(person_data)

        for room_name in Amity.office_allocations:

            room_name = room_name

            person_name = ','.join(Amity.office_allocations[room_name])

            # Insert room_names and person_names into OFFICEALLOCATIONS table.

            office_allocations = AmityOfficeAllocations(room_name,
                                                        person_name)

            session.add(office_allocations)

        for room_name in Amity.livingspace_allocations:

            room_name = room_name

            person_name = \
                ','.join(Amity.livingspace_allocations[room_name])

            # Insert room_names and person_names into LIVINGSPACEALLOCATIONS
            # table.

            livingspace_allocations = \
                AmityLivingspaceAllocations(room_name, person_name)

            session.add(livingspace_allocations)

        for person_id in Amity.person_data:

            persons_id = person_id

            person_name = Amity.person_data[person_id][0]

            job_description = Amity.person_data[person_id][1]

            wants_accommodation = Amity.person_data[person_id][2]

            # Insert person_id,person_name, job_description,
            # wants_accommodation into PEOPLEDATA table.

            person_data = AmityPersondata(persons_id, person_name,
                                          job_description, wants_accommodation)

            session.add(person_data)

        for room_name in Amity.room_data:

            room_name = room_name

            room_type = Amity.room_data[room_name][0]

            room_capacity = Amity.room_data[room_name][1]

            # Insert room_name, room_type, room_capacity into ROOMDATA table.

            room_data = AmityRoomdata(room_name, room_type,
                                      room_capacity)

            session.add(room_data)

        # commit.
        # The Transaction
        # is committed, the Connection object closed
        # and discarded, the underlying DBAPI connection
        # returned to the connection pool.

        session.commit()

        return 'Data saved successfully.'

    # === load_state ===
    def load_state(self, dbname=''):
        """
        Loads all our data from the application memory.

        - If the [dbname] is specified use it, else use amity as the dbname.
        - Clear the database to avoid saving the same data to the database.
        - Create a new session.
        - Create an engine that will be used by our session.
        - Bind the engine to our session.
        - Instantiate db transactions via our session.
        - Query each database table for their data and store them as objects.
        - Read the data from our objects and append to the various lists.
        - For dicts each column object is represented by an index in the dict.
        - Equate each column to the index they represent in our dict.
        - Populate the dict with the acquired data.

        Args:
            dbname:   The name of the database to save the data in application memory.

        Returns:
            Data has been loaded into the system successfully.
            """

        if dbname:

            name = dbname

        else:

            name = 'amity'

        DBSession = sessionmaker()

        engine = create_engine('sqlite:///' + 'databases/' + name
                               + '.db')

        DBSession.configure(bind=engine)

        session = DBSession()

        rooms = session.query(AmityRooms).all()

        for room in rooms:
            Amity.rooms.append(room.NAME)

        livingspaces = session.query(AmityLivingspaces).all()

        for livingspace in livingspaces:
            Amity.livingspaces.append(livingspace.NAME)

        offices = session.query(AmityOffices).all()

        for office in offices:
            Amity.offices.append(office.NAME)

        people = session.query(AmityPeople).all()

        for person in people:
            Amity.people.append(person.NAME)

        fellows = session.query(AmityFellows).all()

        for fellow in fellows:
            Amity.fellows.append(fellow.NAME)

        staff = session.query(AmityStaff).all()

        for single_staff in staff:
            Amity.staff.append(single_staff.NAME)

        livingspace_unallocations = session.query(
            AmityUnallocatedlivingspace).all()

        for livingspace_unallocation in livingspace_unallocations:
            Amity.unallocated_livingspace.append(livingspace_unallocation.NAME)

        office_unallocations = session.query(AmityUnallocatedoffice).all()

        for office_unallocation in office_unallocations:
            Amity.unallocated_office.append(
                office_unallocation.NAME)

        office_allocations = session.query(AmityOfficeAllocations).all()

        for office_allocation in office_allocations:
            office_name = office_allocation.ROOM_NAME
            allocated_people = office_allocation.PERSON_NAME
            allocated_people = allocated_people.split(',')
            Amity.office_allocations[office_name] = allocated_people

        livingspace_allocations = session.query(
            AmityLivingspaceAllocations).all()

        for livingspace_allocation in livingspace_allocations:
            livingspace_name = livingspace_allocation.ROOM_NAME
            allocated_people = livingspace_allocation.PERSON_NAME
            allocated_people = allocated_people.split(',')
            Amity.livingspace_allocations[livingspace_name] = allocated_people

        person_data = session.query(AmityPersondata).all()

        for single_person in person_data:
            person_id = single_person.PERSON_ID
            person_name = single_person.NAME
            job_description = single_person.JOB_DESCRIPTION
            wants_accommodation = single_person.WANTS_ACCOMMODATION
            Amity.person_data[person_id] = [
                person_name, job_description, wants_accommodation]

        room_data = session.query(AmityRoomdata).all()

        for single_room in room_data:
            room_name = single_room.NAME
            room_type = single_room.ROOM_TYPE
            room_capacity = single_room.ROOM_CAPACITY
            Amity.room_data[room_name] = [room_type, room_capacity]

        return 'Data has been loaded into the system successfully.'

    # === clear_db ===
    def clear_db(self, dbname=''):
        """
        Clears the entire local database.

        - If the [dbname] is specified use it, else use amity as the dbname.
        - Create a new session.
        - Create an engine that will be used by our session.
        - Bind the engine to our session.
        - Drop alltables in the database and re-create them.

        Args:
            dbname:   The name of the database to save the data in application memory.

        Returns:
            Database cleared successfully.
            """

        if dbname:

            name = dbname

        else:

            name = 'amity'

        # automap base
        # The following is what will create the declarative_base base that will be
        # imported to every table.

        DBSession = sessionmaker()

        engine = create_engine('sqlite:///' + 'databases/' + name
                               + '.db')

        DBSession.configure(bind=engine)

        # Drop all tables then recreate them.

        Base.metadata.drop_all(bind=engine)

        Base.metadata.create_all(bind=engine)

        return 'Database cleared successfully.'

    # === delete_person ===
    def delete_person(self, person_id):
        """
        Removes a person from amity.

        - Search the [person_data[person_id]] dict by ID.
        - [person_name] and [person_job_description] are the
            first and second indexes of the acquired data.
        - If [person_job_description] is fellow, delete the person by their id from
            [person_data], [people], [fellows], [unallocated_office], [unallocated_livingspace]
            [livingspace_allocations] and [office_allocation].
        - If [person_job_description] is staff, delete the person by their id from
            [person_data], [people], [staff], [unallocated_office] and [office_allocation].
        - Drop alltables in the database and re-create them.

        Args:
            person_id:   Unique identifier for each person.

        Returns:
            {person_id}: {person_name} who is a {person_job_description}
            has been removed from amity.
            """

        person_data_list = self.person_data.get(person_id.upper())

        if person_data_list is None:

            return '{} does not exist.'.format(person_id.upper())

        else:

            person_name = person_data_list[0].upper()

            person_job_description = person_data_list[1].upper()

            if person_job_description == 'FELLOW':

                del self.person_data[person_id]

                for person in self.people:

                    if person == person_name:

                        self.people.remove(person_name)

                for person in self.fellows:

                    if person == person_name:

                        self.fellows.remove(person_name)

                for unallocatedoffice in self.unallocated_office:

                    if unallocatedoffice == person_name:

                        self.unallocated_office.remove(person_name)

                for unallocatedlivingspace in \
                        self.unallocated_livingspace:

                    if unallocatedlivingspace == person:

                        self.unallocated_livingspace.remove(person_name)

                for room in self.livingspace_allocations:

                    for person in self.livingspace_allocations[room]:

                        if person == person_name:

                            self.livingspace_allocations[room].remove(
                                person_name)

                for roomoffice in self.office_allocations:

                    for person in self.office_allocations[roomoffice]:

                        if person == person_name:

                            self.office_allocations[roomoffice].remove(
                                person_name)

                return '{}: {} who is a {} has been removed from amity.' \
                    .format(person_id.upper(), person_name.upper(), person_job_description.upper())

            else:

                del self.person_data[person_id]

                for person in self.people:

                    if person == person_name:

                        self.people.remove(person_name)

                for person in self.staff:

                    if person == person_name:

                        self.staff.remove(person_name)

                for unallocatedoffice in self.unallocated_office:

                    if unallocatedoffice == person_name:

                        self.unallocated_office.remove(person_name)

                for roomoffice in self.office_allocations:

                    for person in self.office_allocations[roomoffice]:

                        if person == person_name:

                            self.office_allocations[roomoffice].remove(
                                person_name)

                return '{}: {} who is a {} has been removed from amity.' \
                    .format(person_id.upper(), person_name.upper(), person_job_description.upper())

    # === delete_room ===
    def delete_room(self, room_name):
        """
        Removes a room from amity.

        - Search the [room_data[room_name]] dict by room name.
        - [room_name] is the first index of the acquired data.
        - If [room_type] is livingspace, delete the room by the name from
            [room_data], [rooms], [livingspace_allocations] amd [livingspaces]
            [livingspace_allocations] and [office_allocation].
        - If [room_type] is office, delete the person by the name from
            [room_data], [rooms], [office_allocations] and [offices].

        Args:
            room_name:   Room name of the room to be deleted.

        Returns:
            Room {room_name} which is a {room_type} has been removed from amity.
            Room {room_name} which is an {room_type} has been removed from amity.
            """

        room_data_list = self.room_data.get(room_name.upper())

        if room_data_list is None:

            # Check if room name entered exists in our room data list.

            return '{} does not exist.'.format(room_name.upper())

        else:

            # Room type is at index 0 of the room data list.

            room_type = room_data_list[0].upper()

            if room_type == 'LIVINGSPACE':

                del self.room_data[room_name]

                del self.livingspace_allocations[room_name]

                for room in self.rooms:

                    if room == room_name:

                        self.rooms.remove(room_name)

                for livingspaces in self.livingspaces:

                    if livingspaces == room_name:

                        self.livingspaces.remove(room_name)

                return 'Room {} which is a {} has been removed from amity.' \
                    .format(room_name.upper(), room_type.upper())

            else:

                del self.room_data[room_name]

                del self.office_allocations[room_name]

                for room in self.rooms:

                    if room == room_name:

                        self.rooms.remove(room_name)

                for office in self.offices:

                    if office == room_name:

                        self.offices.remove(room_name)

                return 'Room {} which is an {} has been removed from amity.'\
                    .format(room_name.upper(), room_type.upper())
