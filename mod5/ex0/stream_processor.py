#!/usr/bin/env python3

"""
Exercise 0: Data Processor Foundation
This module establishes the foundation for the data processing system.
It defines an abstract DataProcessor class and specialized subclasses
(Numeric, Text, Log) to demonstrate method overriding and basic polymorphism.
"""

from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Abstract base class for processing different types of data streams.

    Defines the interface that all specialized processors must follow.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the input data and return a result string.
        Must be implemented by subclasses.

        Args:
            data: The input data to be processed.

        Returns:
            A formatted string containing the processing results.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate if the input data is appropriate for this processor.
        Must be implemented by subclasses.

        Args:
            data: The input data to check.

        Returns:
            True if the data is valid for this processor, False otherwise.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the processing result.
        Default implementation returns the result unchanged.

        Args:
            result: The raw result string from the process method.

        Returns:
            The formatted output string.
        """
        return result


class NumericProcessor(DataProcessor):
    """
    Processor for handling lists of numbers (integers and floats).
    """

    def process(self, data: Any) -> str:
        """
        Calculate count, sum, and average of a numeric list.

        Args:
            data: A list of numbers (integers or floats).

        Returns:
            A formatted string with count, sum, and average stats.
            Returns "Error" if the data is empty or invalid.
        """
        if not data:
            return "Error"
        count = 0
        total = 0
        for num in data:
            total += num
            count += 1
        avg = total / count
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        """
        Check if data is a list containing only integers or floats.

        Args:
            data: The input data to validate.

        Returns:
            True if data is a list of numbers, False otherwise.
        """
        if not data.__class__ == list:
            return False
        for num in data:
            if num.__class__ not in [int, float]:
                return False
        return True


class TextProcessor(DataProcessor):
    """
    Processor for handling text strings.
    """

    def process(self, data: Any) -> str:
        """
        Count characters and words in the text.

        Args:
            data: The input string to analyze.

        Returns:
            A formatted string with character and word counts.
        """
        char_count = 0
        word_count = 0
        in_word = False
        for char in data:
            if char == " ":
                in_word = False
            else:
                if not in_word:
                    word_count += 1
                    in_word = True
            char_count += 1
        return f"Processed text: {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        """
        Check if data is a valid string.

        Args:
            data: The input data to validate.

        Returns:
            True if data is a string, False otherwise.
        """
        if not data.__class__ == str:
            return False
        return True


class LogProcessor(DataProcessor):
    """
    Processor for handling log entries in 'LEVEL: Message' format.
    """

    def validate(self, data: Any) -> bool:
        """
        Check if data is a string and contains a colon separator.

        Args:
            data: The input data to validate.

        Returns:
            True if data is a string containing ':', False otherwise.
        """
        if data.__class__ == str and ":" in data:
            return True
        return False

    def process(self, data: Any) -> str:
        """
        Parse the log level and message.

        Args:
            data: A log string in the format "LEVEL: Message".

        Returns:
            A formatted string with a tag (e.g., [ALERT]) and the message.
        """
        level_dict = {
            "ERROR": "[ALERT]",
            "INFO": "[INFO]"
        }
        level = ""
        message = ""
        found_sep = False
        for char in data:
            if found_sep:
                if char == " " and message == "":
                    continue
                message += char
            else:
                if char == ":":
                    found_sep = True
                else:
                    level += char
        tag = ""
        try:
            tag = level_dict[level]
        except KeyError:
            tag = f"[{level}]"
        return f"{tag} {level} level detected: {message}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")

    test_list = [1, 2, 3, 4, 5]
    num_processor = NumericProcessor()
    print(f"Processing data: {test_list}")
    if num_processor.validate(test_list):
        print("Validation: Numeric data verified")
    else:
        print("Validation: Error")
    print(f"Output: {num_processor.process(test_list)}")

    print("\nInitializing Text Processor...")
    test_str = "Hello Nexus World"
    text_processor = TextProcessor()
    print(f'Processing data: "{test_str}"')
    if text_processor.validate(test_str):
        print("Validation: Text data verified")
    else:
        print("Validation: Error")
    print(f"Output: {text_processor.process(test_str)}")

    print("\nInitializing Log Processor...")
    test_log = "ERROR: Connection timeout"
    log_processor = LogProcessor()
    print(f'Processing data: "{test_log}"')
    if log_processor.validate(test_log):
        print("Validation: Log entry verified")
    else:
        print("Validation: Error")
    print(f"Output: {log_processor.process(test_log)}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    polymorphic_data: List[Any] = [
        (num_processor, [1, 2, 3]),
        (text_processor, "Hello, world"),
        (log_processor, "INFO: System ready")
    ]
    i = 1
    for processor, data in polymorphic_data:
        print(f"Result {i}: {processor.process(data)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
