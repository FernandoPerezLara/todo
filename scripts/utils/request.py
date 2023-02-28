"""This module contains all the requests to the API."""
import requests

from scripts.utils.errors import TaskError


class Request():
    """This class contains all the requests to the API."""
    def __init__(self, url, timeout=2.5):
        self._url = url
        self._timeout = timeout
    
    def get(self):
        """Get the response from the API."""
        try:
            return requests.get(self._url, timeout=self._timeout).json()
        except requests.exceptions.HTTPError as e:
            raise TaskError("An HTTP error occurred", additional_info=e) from None
        except requests.exceptions.ConnectionError as e:
            raise TaskError("A Connection error occurred", additional_info=e) from None
        except requests.exceptions.Timeout as e:
            raise TaskError("The request timed out", additional_info=e) from None
        except requests.exceptions.RequestException as e:
            raise TaskError("An unknown error occurred", additional_info=e) from None
