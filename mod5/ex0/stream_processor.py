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
        Processes the input data and returns a result string.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validates if the input data is appropriate for this processor.
        Must be implemented by subclasses.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Formats the processing result.
        Default implementation returns the result unchanged.
        """
        return result


class NumericProcessor(DataProcessor):
    """
    Processor for handling lists of numbers (integers and floats).
    """

    def process(self, data: Any) -> str:
        """
        Calculates count, sum, and average of a numeric list.
        Returns a formatted string with these statistics.
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
        Checks if data is a list containing only integers or floats.
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
        Counts characters and words in the text.
        Returns a formatted string with these counts.
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
        Checks if data is a string.
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
        Checks if data is a string and contains a colon separator.
        """
        if data.__class__ == str and ":" in data:
            return True
        return False

    def process(self, data: Any) -> str:
        """
        Parses the log level and message.
        Handles unknown levels gracefully.
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
