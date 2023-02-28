"""This module contains errors raised by the tasks package."""
class TaskException(Exception):
    """The base error of all the errors in this module."""


class TaskError(TaskException):
    """An error occurred while executing a task."""
    def __init__(self, error_msg, additional_info=None):
        """
        Args:
            error_msg (str): message describing the error.
            additional_info (str, optional): message giving more details about the error. It is used for UX purposes,
                to print the additional info on another line or with another format. Defaults to None.
        """
        super().__init__(self)
        self.error_msg = error_msg
        self.additional_info = additional_info

    def __str__(self):
        return self.error_msg
