#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    create_room <room_name> <room_type>
    add_person <person_name> <job_type> <want_accommodation>
    allocate_living_space <person_name>
    allocate_office <person_name>
    reallocate_person <person_id> <room_name>

Arguments:
    <room_name> The name of the room
    <room_type> The type of room it can either be an office|living_space
    <person_name> The name of the employee
    <person_id> The ID of the person
    <job_description> The employee's job type it can either be fellow|staff
    <wants_accommodation> can either be yes|no

Options:
    -h , --help , Show this screen and exit
"""

import os
import cmd

from docopt import docopt, DocoptExit
from clint.textui import colored, puts

from models.amity import Amity

amity = Amity()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            puts(colored.red('Invalid Command!'))
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Amityville(cmd.Cmd):
    """
    docopt comands
    """
    # clear terminal first.
    os.system('cls' if os.name == 'nt' else 'clear')
    prompt = '(amityville)' + (colored.red(' ❯'))

    @docopt_cmd
    def do_create_room(self, arg):
        """ Usage: create_room <room_name> <room_type> """
        room_name = arg['<room_name>']
        room_type = arg['<room_type>']

        puts(colored.green(amity.create_room(room_name, room_type)))

    @docopt_cmd
    def do_add_person(self, arg):
        """ Usage: add_person <person_name> <job_description> <wants_accommodation> """
        person_name = arg['<person_name>']
        job_description = arg['<job_description>']
        wants_accommodation = arg['<wants_accommodation>']

        puts(colored.green(amity.add_person(person_name,
                                            job_description.upper(), wants_accommodation.upper())))

    @docopt_cmd
    def do_allocate_livingspace(self, arg):
        """ Usage: allocate_livingspace <fellow_name> """
        fellow_name = arg['<fellow_name>']

        puts(colored.green(amity.allocate_livingspace(fellow_name.upper())))

    @docopt_cmd
    def do_allocate_office(self, arg):
        """ Usage: allocate_office <person_name> """
        person_name = arg['<person_name>']

        puts(colored.green(amity.allocate_office(person_name.upper())))

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """ Usage: reallocate_person <person_id> <room_name> """
        person_id = arg['<person_id>']
        room_name = arg['<room_name>']

        puts(colored.green(amity.reallocate_person(person_id, room_name.upper())))

    @docopt_cmd
    def do_print_people_details(self, arg):
        """ Usage: print_identifiers """

        puts(colored.green(amity.print_people_details()))

    @docopt_cmd
    def do_clear(self, arg):
        """ Usage: clear """
        os.system('cls' if os.name == 'nt' else 'clear')

    @docopt_cmd
    def do_quit(self, arg):
        """ Usage: quit """
        exit()


if __name__ == "__main__":
    Amityville().cmdloop()
