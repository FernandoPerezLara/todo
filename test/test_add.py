"""This module test the add command."""
from faker import Faker
import random
import unittest

from scripts.commands.add.task import Add
from scripts.utils.constants import API_URL
from scripts.utils.request import Request


class TestAdd(unittest.TestCase):
    """Test the add command."""
    def test_add(self):
        """Test the add command."""
        fake = Faker('es_ES')
        names = [fake.name() for i in range(random.randint(10, 100))]

        for name in names:
            Add(name).run()

        list_items = Request(API_URL, timeout=2.5).get()

        for name in names:
            self.assertIn(name, [item['text'] for item in list_items])
