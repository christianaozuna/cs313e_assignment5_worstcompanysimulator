"""
Student information for this assignment:

On my/our honor, Christiana Ozuna and Jessica North, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: cmo2388
UT EID 2: jan3557
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."


# TODO: implement this class. You may delete this comment when you are done.
class Employee(ABC):
    """
    Abstract base class representing a generic employee in the system.
    """

    def __init__(self, name, manager, salary, savings):
        self.relationships = {}
        self.savings = savings
        self.is_employed = True
        self.__name = name
        self.__manager = manager
        self.performance = INITIAL_PERFORMANCE
        self.happiness = INITIAL_HAPPINESS
        self.salary = salary


# TODO: implement this class. You may delete this comment when you are done.
class Manager(Employee):
    """
    A subclass of Employee representing a manager.
    """


# TODO: implement this class. You may delete this comment when you are done.
class TemporaryEmployee(Employee):
    """
    A subclass of Employee representing a temporary employee.
    """


# TODO: implement this class. You may delete this comment when you are done.
class PermanentEmployee(Employee):
    """
    A subclass of Employee representing a permanent employee.
    """
