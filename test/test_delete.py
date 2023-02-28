"""This module test the delete command."""
from faker import Faker
import unittest

from scripts.commands.add.task import Add
from scripts.commands.delete.task import Delete
from scripts.utils.constants import API_URL
from scripts.utils.request import Request


class TestDelete(unittest.TestCase):
    """Test the delete command."""
    def test_delete(self):
        """Test the delete command."""
        name = Faker('es_ES').name()
        
        previous_items = Request(API_URL, timeout=2.5).get()
        Add(name).run()

        Delete(name).run()
        current_items = Request(API_URL, timeout=2.5).get()

        self.assertEqual(len(previous_items), len(current_items))
        self.assertNotIn(name, [item['text'] for item in current_items])

    def test_delete_all(self):
        """Test the delete all command."""
        list_items = Request(API_URL, timeout=2.5).get()

        for item in list_items:
            Delete(item['text']).run()

        current_items = Request(API_URL, timeout=2.5).get()

        self.assertEqual(len(current_items), 0)
