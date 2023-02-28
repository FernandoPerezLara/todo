"""This module implements the tasks related to display a list of todo."""
import json

from scripts.utils.constants import API_URL
from scripts.utils.request import Request


class List():
    """Task to list all todo items."""
    def __init__(self, output):
        self._output = output

    def run(self):
        """Run the task."""
        request = Request(API_URL, timeout=2.5).get()

        if self._output == 'table':
            if len(request) == 0:
                col_widths = [0, 0]
            else:
                col_widths = [
                    max(len(item['_id']) for item in request),
                    max(len(item['text']) for item in request)
                ]

            print(
                "ID".ljust(col_widths[0]) + ' ' +
                "ITEM".ljust(col_widths[1])
            )

            for item in request:
                print(
                    item['_id'].ljust(col_widths[0]) + ' ' +
                    item['text'].ljust(col_widths[1])
                )
        elif self._output == 'txt':
            for item in request:
                print(item['text'])
        else:
            print(json.dumps(request, indent=2, sort_keys=True))
