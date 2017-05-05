# CP1A - Office Space Allocation

![amityville](https://i.imgur.com/qcifTAr.png)

#

##### Requirements

To complete this checkpoint you must have completed Modules 1, 2, 3 and 4.

##### Problem Description

In this exercise you will be required to model a room allocation system for one of Andela’s facilities called Amity.

##### Constraints

Amity has rooms which can be offices or living spaces. An office can accommodate a maximum of 6 people. A living space can accommodate a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

#

##### Task 0 - Model the system

For this task you are required to model the entire system using class definitions. Create the following classes and implement the required functionality within them - `Person`, `Fellow`, `Staff`, `Amity`, `Room`, `Office`, `Living Space`.

Ensure that you are properly structuring your class files and using easily navigable folder structures.

You should have [UML Class Diagrams](http://www.tutorialspoint.com/uml/uml_class_diagram.htm) for your system. Keep the diagrams in a /designs folder.

#

##### Task 1 - Write Tests for the models

Create tests for the models you just created in the previous exercise that ensure the functionality created in the classes are working.

You are then advised to schedule a Test-Cases review with your Simulations Facilitator before you can proceed with Task 2.

#

##### Task 2 - Create a command line interface

After reading through this task, jump to task 2.5 and then come back here.

For this task you are required to create a command line interface using [docopt](http://docopt.org/) that does the following using your models.

1. `create_room <room_name>`... - Creates rooms in Amity. Using this command I should be able to create as many rooms as possible by specifying multiple room names after the create_room command.


2. `add_person <person_name> <FELLOW|STAFF> [wants_accommodation]` - Adds a person to the system and allocates the person to a random room. `wants_accommodation` here is an optional argument which can be either `Y` or `N`. The default value if it is not provided is `N`.


3. `reallocate_person <person_identifier> <new_room_name>` - Reallocate the person with `person_identifier` to `new_room_name`.


4. `load_people` - Adds people to rooms from a txt file. See Appendix 1A for text input format.


5. `print_allocations [-o=filename]`  - Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered allocations to a txt file. See Appendix 2A for format.


6. `print_unallocated [-o=filename]` - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.


7. `print_room <room_name>` - Prints  the names of all the people in `room_name` on the screen.


8. `save_state [--db=sqlite_database]` - Persists all the data stored in the app to a SQLite database. Specifying the `--db` parameter explicitly stores the data in the `sqlite_database` specified.

9. `load_state <sqlite_database>` - Loads data from a database into the application.

#

##### Task 2.5 - Write Tests for all functionality created

For this project you are expected to use TDD. What this means is that you will be writing tests before you create functionality. Just as a rule of thumb before creating any function in the previous task, ensure you have written at the very least, an empty test for it.

Ensure you have test coverage of over 70% at the end of the project.

_You may now proceed with Task 2._

#

##### Appendix 1A - Sample Input Format

`OLUWAFEMI SULE FELLOW Y`

`DOMINIC WALTERS STAFF`

`SIMON PATTERSON FELLOW Y`

`MARI LAWRENCE FELLOW Y`

`LEIGH RILEY STAFF`

`TANA LOPEZ FELLOW Y`

`KELLY McGUIRE STAFF`

#

##### Appendix 2A - Sample Output Format

`ROOM NAME`

`-------------------------------------`

`MEMBER 1, MEMBER 2, MEMBER 3`

`ROOM NAME`

`-------------------------------------`

`MEMBER 1, MEMBER 2`
#

##### Task 3 - Have any ideas?

You are free to add on extra functionality beyond what’s specified in the specifications. You are encouraged to do this to exceed expectations.

#

#### GETTING STARTED:

1. Clone Repo:

    ```
    $ git clone git@github.com:asce1062/cp1-amity-allocation.git
    ```
2. Navigate to local directory.

    ```
    $ cd cp1-amity-allocation
    ```
3. Install virtualenv via pip:

    ```
    $ pip install virtualenv
    ```
4. Install virtualenvwrapper via pip:

    ```
    $ pip install virtualenvwrapper
    $ export WORKON_HOME=$HOME/.virtualenvs
    $ export PROJECT_HOME=$HOME/Devel
    $ source /usr/local/bin/virtualenvwrapper.sh
    $ source ~/.bashrc
    $ mkvirtualenv amity
    $ workon amity
    ```
5. Install requiremets

    ```
    $ pip install -r requirements.txt
    ```
6. Start the application

    ```
    $ python amityville.py -i
    ```
#### USAGE:
[![amityville](https://asciinema.org/a/117745.png)](https://asciinema.org/a/117745)

- ```create_room <room_name> <room_type>```
_Usage_ : `create_room moon livingspace` - Creates a room `moon` which is a `livingspace`.

- ```add_person <person_name> <job_description> [<wants_accommodation>]```
_Usage_ : `add_person aleximmer fellow yes` - Adds a person `aleximmer` who is a `fellow` and wants a `livingspace`.

- ```allocate_livingspace <fellow_name>```
_Usage_ : `allocate_livingspace aleximmer` - Allocates a `random livingspace` from a list of `livingspaces` that have not reached the `maximum capacity`.

- ```allocate_office <person_name>```
_Usage_ : `allocate_office aleximmer`- Allocates a `random office` from a list of `offices` that have not reached the `maximum capacity`.

- ```reallocate_person <person_id> <room_name>```
_Usage_ : `reallocate_person f1 moon` - Re-allocates a person by `person_id` to a `room` who's name is specified. Print `people_ids` using the `print_people_details` command.

- ```load_people [--o=filename]```
_Usage_ : `load_people --o=people` - loads people from a text file who's name is specified. You must have the text file created first before using this command.

- ```load_rooms [--o=filename]```
_Usage_ : `load_rooms --o=rooms` - `loads rooms` from a text file who's `name` is specified. You must have the text file created first before using this command.

- ```print_allocations [--o=filename]```
_Usage_ : `print_allocations --o=allocations` - Prints `all allocations` to a text file if the `filename` option is provided. Else it prints out to screen.

- ```print_specific_room_allocations <room_name>```
_Usage_ : `print_specific_room_allocations moon` - Prints all people allocated to the specified `room_name`

- ```print_unallocated [--o=filename]```
_Usage_ : `print_unallocated --o=unallocations` - Prints `all unallocations` to a text file if the `filename` option is provided. Else it prints out to screen.

- ```print_rooms```
_Usage_ : `print_rooms` - Prints all `offices` and `livingspaces` available in amity.

- ```print_fellows```
_Usage_ : `print_fellows` - Prints all `fellows` at amity.

- ```print_staff```
_Usage_ : `print_staff` - Prints all `staff` at amity.

- ```print_all_people```
_Usage_ : `print_all_people` - Prints all `staff` and `fellows` at amity.

- ```print_people_details```
_Usage_ : `print_people_details` - Prints all `people_details` of `people` at amity. Format being `ID`: `name`, `job_description`, `accommodation_choice`

- ```create_db [--db=dbname]```
_Usage_ : `create_db --db=cp1` - Creates a `database` named `cp1` and populates it with all the tables specified in `database_models`

- ```save_state [--db=dbname]```
_Usage_ : `save_state --db=cp1` - Saves tha program's `state` to the databse `cp1` if no database name is provided, a database named `amity` is created and the program `state` is saved to it.

- ```load_state [--db=dbname]```
-_Usage_ : `load_state --db=cp1` - Loads the `saved` program `state` back to the application. If no database name is provided, it will use a database named `amity`.

- ```clear_db [--db=dbname]```
_Usage_ : `clear_db --db=cp1` - `Clears` the database for a fresh start. If no database name is provided, the database named `amity` is cleared.

- ```delete_person <person_id>```
_Usage_ : `delete_person f1` - `Deletes` a `person` with the `ID` `F1` from amity allocation system.

- ```delete_room <room_name>```
_Usage_ : `delete_room moon` - `Deletes` the `room` `moon` from amoty.

- ```clear```
_Usage_ : `clear` - Clears the terminal output for a cleaner environmet to work on.

- ```quit```
_Usage_ : `quit` - Exits the application.

- ```(-i | --interactive)```
_Usage_ : `python amityville.py -i` - Start amityville in `interactive` mode.

- ```(-h | --help | --version)```
_Usage_ : `python amityville.py -h` - Prints out the `Usage`, `Arguments` and `Options` and exits the application.

#

#### ARGUMENTS:

- ```<room_name>```  The name of the room
- ```<room_type>``` The type of room it can either be an office|living_space
- ```<person_name>``` The name of the employee
- ```<job_description>``` The employee's job type it can either be fellow|staff
- ```[<wants_accommodation>]``` Can either be yes|no if not provided defaults to no
- ```<fellow_name>``` The name of a fellow
- ```<person_id>``` The ID of the person
- ```[--o=filename]``` The name of the text file to write to or read from
- ```[--db=dbname]``` The name of the database to write to or read from if not provided defaults to amity.

#
#### Options:

    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
