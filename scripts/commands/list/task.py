"""This module implements the tasks related to display a list of todo."""
from scripts.utils.constants import API_URL
from scripts.utils.request import Request

class List():
    """Task to list all todo items."""
    def __init__(self, output):
        self._output = output

    def run(self):
        """Run the task."""
        request = Request(API_URL, timeout=2.5).get()
        print(f"Output: {request}")
