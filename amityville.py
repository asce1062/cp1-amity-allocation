#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Usage:
    my_program create_room <room_name> <room_type>
    my_program add_person <person_name> <job_description> [<wants_accommodation>]
    my_program allocate_livingspace <fellow_name>
    my_program allocate_office <person_name>
    my_program reallocate_person <person_id> <room_name>
    my_program load_people [--o=filename]
    my_program load_rooms [--o=filename]
    my_program print_allocations [--o=filename]
    my_program print_specific_room_allocations <room_name>
    my_program print_unallocated [--o=filename]
    my_program print_rooms
    my_program print_fellows
    my_program print_staff
    my_program print_all_people
    my_program print_people_details
    my_program create_db [--db=dbname]
    my_program save_state [--db=dbname]
    my_program load_state [--db=dbname]
    my_program clear_db [--db=dbname]
    my_program delete_person <person_id>
    my_program delete_room <room_name>
    my_program clear
    my_program quit
    my_program (-i | --interactive)
    my_program (-h | --help | --version)

Arguments:
    <room_name> The name of the room
    <room_type> The type of room it can either be an office|living_space
    <person_name> The name of the employee
    <job_description> The employee's job type it can either be fellow|staff
    [<wants_accommodation>] Can either be yes|no if not provided defaults to no
    <fellow_name> The name of a fellow
    <person_id> The ID of the person
    [--o=filename] The name of the text file to write to or read from
    [--db=dbname] The name of the database to write to or read from if not provided defaults to amity.

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import cmd
import os
import sys

from clint.textui import colored, indent, puts
from docopt import DocoptExit, docopt
from pyfiglet import Figlet

from databases.database_models import create_db
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


def startup():
    font_property = Figlet(font='poison')
    with indent(84):
        puts(colored.blue(font_property.renderText('AMITY VILLE')))
    puts(colored.cyan(__doc__))


class Amityville(cmd.Cmd):

    """
    docopt comands
    """

    # clear terminal first.

    os.system(('cls' if os.name == 'nt' else 'clear'))
    prompt = colored.blue('(amityville)') + colored.red(' ❯')

    @docopt_cmd
    def do_create_room(self, arg):
        """ Usage: create_room <room_name> <room_type> """

        room_name = arg['<room_name>']
        room_type = arg['<room_type>']
        result = amity.create_room(room_name, room_type)
        if result in ['Invalid room type.']:
            color = colored.red
        elif result in [room_name.upper() + ' already exists.']:
            color = colored.yellow
        else:
            color = colored.green

        puts(color(result))

    @docopt_cmd
    def do_add_person(self, arg):
        """ Usage: add_person <person_name> <job_description> <wants_accommodation> """

        person_name = arg['<person_name>']
        job_description = arg['<job_description>']
        wants_accommodation = arg['<wants_accommodation>']
        result = amity.add_person(person_name, job_description.upper(),
                                  wants_accommodation.upper())
        if result in ['Invalid person name.',
                      'Invalid accommodation input.',
                      'Invalid accommodation input.',
                      'Invalid job description.']:
            color = colored.red
        elif result in ['Staff cannot be allocated a livingspace.']:
            color = colored.yellow
        else:
            color = colored.green

        puts(color(result))

    @docopt_cmd
    def do_allocate_livingspace(self, arg):
        """ Usage: allocate_livingspace <fellow_name> """

        fellow_name = arg['<fellow_name>']
        result = amity.allocate_livingspace(fellow_name.upper())
        if result in [fellow_name.upper() + ' does not exist.',
                      'No vaccant livingspace.']:
            color = colored.red
        else:
            color = colored.green

        puts(color(result))

    @docopt_cmd
    def do_allocate_office(self, arg):
        """ Usage: allocate_office <person_name> """

        person_name = arg['<person_name>']
        result = amity.allocate_office(person_name.upper())
        if result in [person_name.upper() + ' does not exist.',
                      'No vaccant livingspace.']:
            color = colored.red
        else:
            color = colored.green

        puts(color(result))

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """ Usage: reallocate_person <person_id> <room_name> """

        person_id = arg['<person_id>']
        room_name = arg['<room_name>']

        puts(colored.green(amity.reallocate_person(person_id,
                                                   room_name.upper())))

    @docopt_cmd
    def do_load_people(self, arg):
        """ Usage: load_people [--o=filename] """

        filename = arg['--o']
        result = amity.load_people(filename)
        if result in ['People successfully loaded.']:
            color = colored.green
        else:
            color = colored.red

        puts(color(result))

    @docopt_cmd
    def do_load_rooms(self, arg):
        """ Usage: load_rooms [--o=filename] """

        filename = arg['--o']
        result = amity.load_rooms(filename)
        if result in ['Rooms successfully loaded from file.']:
            color = colored.green
        else:
            color = colored.red

        puts(color(result))

    @docopt_cmd
    def do_print_allocations(self, arg):
        """ Usage: print_allocations [--o=filename] """

        filename = arg['--o']

        puts(colored.green(amity.print_allocations(filename)))

    @docopt_cmd
    def do_print_specific_room_allocations(self, arg):
        """ Usage: print_specific_room_allocations <room_name> """

        room_name = arg['<room_name>']
        result = amity.print_specific_room_allocations(room_name)
        if result in ['Invalid input.']:
            color = colored.red
        else:
            color = colored.green
        puts(color(result))

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """ Usage: print_unallocated [--o=filename] """

        filename = arg['--o']

        puts(colored.green(amity.print_unallocated(filename)))

    @docopt_cmd
    def do_print_rooms(self, arg):
        """ Usage: print_rooms """

        puts(colored.green(amity.print_rooms()))

    @docopt_cmd
    def do_print_fellows(self, arg):
        """ Usage: print_fellows """

        puts(colored.green(amity.print_fellows()))

    @docopt_cmd
    def do_print_staff(self, arg):
        """ Usage: print_staff """

        puts(colored.green(amity.print_staff()))

    @docopt_cmd
    def do_print_all_people(self, arg):
        """ Usage: print_all_people """

        puts(colored.green(amity.print_all_people()))

    @docopt_cmd
    def do_print_people_details(self, arg):
        """ Usage: print_people_details """

        result = amity.print_people_details()
        if result in ['No one exists in the system yet.']:
            color = colored.red
        else:
            color = colored.green

        puts(color(result))

    @docopt_cmd
    def do_create_db(self, arg):
        """ Usage: create_db [--db=dbname] """

        dbname = arg['--db']

        create_db(dbname)

    @docopt_cmd
    def do_save_state(self, arg):
        """ Usage: save_state [--db=dbname] """

        if arg['--db']:
            db = arg['--db']
        else:
            db = ''

        puts(colored.green(amity.save_state(dbname=db)))

    @docopt_cmd
    def do_load_state(self, arg):
        """ Usage: load_state [--db=dbname] """

        if arg['--db']:
            db = arg['--db']
        else:
            db = ''

        puts(colored.green(amity.load_state(dbname=db)))

    @docopt_cmd
    def do_clear_db(self, arg):
        """ Usage: clear_db [--db=dbname] """

        if arg['--db']:
            db = arg['--db']
        else:
            db = ''

        puts(colored.green(amity.clear_db(dbname=db)))

    @docopt_cmd
    def do_delete_person(self, arg):
        """ Usage: delete_person <person_id> """

        person_id = arg['<person_id>']
        result = amity.delete_person(person_id.upper())
        if result in [person_id.upper() + ' does not exist.']:
            color = colored.red
        else:
            color = colored.green
        puts(color(result))

    @docopt_cmd
    def do_delete_room(self, arg):
        """ Usage: delete_room <room_name> """

        room_name = arg['<room_name>']
        result = amity.delete_room(room_name.upper())
        if result in [room_name.upper() + ' does not exist.']:
            color = colored.red
        else:
            color = colored.green
        puts(color(result))

    @docopt_cmd
    def do_clear(self, arg):
        """ Usage: clear """

        os.system(('cls' if os.name == 'nt' else 'clear'))

    @docopt_cmd
    def do_quit(self, arg):
        """ Usage: quit """

        puts(colored.red('Goodbye.'))
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    startup()
    Amityville().cmdloop()

print(opt)
