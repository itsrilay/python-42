#!/usr/bin/env python3

"""
Exercise 2: Nexus Integration
This module implements a complete data processing pipeline system.
It demonstrates the use of Protocols for duck typing and Abstract Base Classes
for defining the pipeline structure.
"""

from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    """
    Protocol defining the interface for a processing stage.
    Any class with a process(data) method satisfies this protocol.
    """
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    """
    Abstract base class for a data processing pipeline.
    Manages a sequence of processing stages.
    """
    def __init__(self) -> None:
        """
        Initialize the pipeline with an empty list of stages.
        """
        self.stages: List[Any] = []

    def add_stage(self, stage: Any) -> None:
        """
        Add a processing stage to the pipeline.

        Args:
            stage: An object that adheres to the ProcessingStage protocol.
        """
        self.stages.append(stage)

    def process(self, data: Any) -> Any:
        """
        Process data through all stages in the pipeline sequentially.

        Args:
            data: The initial input data.

        Returns:
            The final processed result after passing through all stages.
        """
        current_data = data
        for stage in self.stages:
            current_data = stage.process(current_data)
        return current_data


class InputStage():
    def process(self, data: Any) -> Any:
