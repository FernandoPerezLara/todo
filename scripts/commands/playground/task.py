"""This module implements the tasks related to deploy the playground."""
import random
from faker import Faker

from scripts.commands.add.task import Add
from scripts.commands.delete.task import Delete
from scripts.utils.constants import API_URL
from scripts.utils.request import Request


class GenerateRandom():
    """Task to create a random number of todo items between 10 and 100."""
    def __init__(self):
        pass

    def run(self):
        """Run the task."""
        fake = Faker('es_ES')
        names = [fake.name() for _ in range(random.randint(10, 100))]

        for name in names:
            Add(name).run()


class DeleteAll():
    """Task to delete all the todo items."""
    def __init__(self):
        pass

    def run(self):
        """Run the task."""
        list_items = Request(API_URL, timeout=2.5).get()

        for item in list_items:
            Delete(item['text']).run()
