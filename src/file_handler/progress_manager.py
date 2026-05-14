"""
Progress file handler for the Python Core Lessons Study CLI.

This module manages reading and writing progress records using a JSON file.
"""

import json
import os


class ProgressFile:
    """Context manager for safely handling progress data.

    Attributes:
        file_path (str): Path to the progress JSON file.
        data (list): List of progress records.
    """

    def __init__(self, file_path):
        """Initializes the progress file manager.

        Args:
            file_path (str): Path to the JSON file.
        """
        self.file_path = file_path
        self.data = []

    def __enter__(self):
        """Loads progress data when entering the context.

        Returns:
            ProgressFile: Current file manager object.
        """
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except json.JSONDecodeError:
            self.data = []

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Saves progress data when exiting the context."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

    def add_record(self, record):
        """Adds one progress record.

        Args:
            record (dict): Study or quiz record.
        """
        self.data.append(record)

    def get_records(self):
        """Returns all progress records.

        Returns:
            list: Saved progress records.
        """
        return self.data
