"""This module implements the tasks related to delete a todo item."""
from scripts.utils.constants import API_URL
from scripts.utils.request import Request


class Delete():
    """Task to delete a todo item."""
    def __init__(self, text):
        self._text = text

    def run(self):
        """Run the task."""
        request = Request(API_URL, timeout=2.5).get()

        for item in request:
            if item['text'] == self._text:
                Request(API_URL, timeout=2.5).delete(id=item['_id'])
                break        
