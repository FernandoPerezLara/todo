"""This module test the list command."""
import unittest

from scripts.commands.list.task import List


class TestList(unittest.TestCase):
    """Test the list command."""
    def test_list_txt(self):
        """Test the list command in txt format."""
        List('txt').run()

    def test_list_json(self):
        """Test the list command in json format."""
        List('json').run()

    def test_list_table(self):
        """Test the list command in table format."""
        List('table').run()
