from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
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
        if not data.__class__ == list:
            return False
        for num in data:
            if num.__class__ not in [int, float]:
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
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
        if not data.__class__ == str:
            return False
        return True


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if data.__class__ == str and ":" in data:
            return True
        return False

    def process(self, data: Any) -> str:
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
