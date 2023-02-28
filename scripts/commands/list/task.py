"""This module implements the tasks related to display a list of todo."""

class List():
    """Task to list all todo items."""
    def __init__(self, output):
        self._output = output

    def run(self):
        """Run the task."""
        print(f"Output: {self._output}")
