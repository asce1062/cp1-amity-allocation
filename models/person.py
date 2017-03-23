"""
Person
"""


class Person(object):
    """
    Class Person
    """

    def __init__(self, person_name):
        self.person_name = person_name


class Staff(Person):
    """
    class Staff
    """

    def __init__(self, person_name):
        self.person_name = person_name
        self.job_description = "STAFF"


class Fellow(Person):
    """
    Class Fellow
    """

    def __init__(self, person_name):
        self.person_name = person_name
        self.job_description = "FELLOW"
