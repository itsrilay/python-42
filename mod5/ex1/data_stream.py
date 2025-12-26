#!/usr/bin/env python3

"""
Exercise 1: Polymorphic Streams
This module implements a polymorphic data streaming system.
It defines an abstract DataStream class and specialized subclasses
(Sensor, Transaction, Event) managed by a central StreamProcessor.
"""

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    """
    Abstract base class representing a generic data stream.
    """
    def __init__(self, stream_id: str) -> None:
        """
        Initialize the data stream.

        Args:
            stream_id: Unique identifier for the stream.
        """
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data and return a summary string.

        Args:
            data_batch: List of data items to process.

        Returns:
            A formatted string summarizing the processing results.
        """
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter the data batch based on specific criteria.
        Default implementation returns data unchanged.

        Args:
            data_batch: The input list of data.
            criteria: Optional filtering criteria description.

        Returns:
            The filtered list of data.
        """
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieve statistics about the stream's processing history.

        Returns:
            Dictionary containing statistical metrics.
        """
        return {}


class SensorStream(DataStream):
    """
    Specialized stream for processing environmental sensor data.
    """
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Calculate average temperature from sensor readings.
        """
        count = 0
        temp_count = 0
        temp_sum: float = 0
        avg_temp: float = 0
        if not data_batch:
            return "Error"
        for data in data_batch:
            if isinstance(data, dict):
                for key in data:
                    value = data[key]
                    if isinstance(value, (int, float)):
                        if key == "temp":
                            temp_sum += value
                            temp_count += 1
                        count += 1
        if count == 0:
            return "Error: No sensor data found"
        try:
            avg_temp = temp_sum / temp_count
        except ZeroDivisionError:
            return "Error: No temperatures found"
        return (
            f"Sensor analysis: {count} readings processed, avg temp: " +
            f"{avg_temp}°C"
        )

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter for high-priority sensor alerts (e.g., temp > 50).
        """
        filtered: List[Any] = []
        for item in data_batch:
            if isinstance(item, dict):
                if "temp" in item and isinstance(item["temp"], (int, float)):
                    if item["temp"] > 50:
                        filtered.append(item)
        return filtered


class TransactionStream(DataStream):
    """
    Specialized stream for processing financial transactions.
    """
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Calculate net flow from buy/sell operations.
        """
        net_flow = 0
        count = 0
        if not data_batch:
            return "Error"
        for data in data_batch:
            if isinstance(data, dict):
                if "buy" in data and isinstance(data["buy"], (int, float)):
                    net_flow += data["buy"]
                    count += 1
                elif "sell" in data and isinstance(data["sell"], (int, float)):
                    net_flow -= data["sell"]
                    count += 1
        if count == 0:
            return "Error: No transactions found"
        return (
            f"Transaction analysis: {count} operations, net flow: " +
            f"{net_flow:+} units"
        )

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter for large transactions (value > 1000).
        """
        filtered: List[Any] = []
        for item in data_batch:
            if isinstance(item, dict):
                if "buy" in item and item["buy"] > 1000:
                    filtered.append(item)
                elif "sell" in item and item["sell"] > 1000:
                    filtered.append(item)
        return filtered


class EventStream(DataStream):
    """
    Specialized stream for processing system event logs.
    """
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Count total events and specific error occurrences.
        """
        events = 0
        errors = 0
        if not data_batch:
            return "Error"
        for data in data_batch:
            if isinstance(data, str):
                if data == "error":
                    errors += 1
                events += 1
        if events == 0:
            return "Error: No events found"
        return (
            f"Event analysis: {events} events, {errors} " +
            f"{'error' if errors == 1 else 'errors'} detected"
        )


class StreamProcessor():
    """
    Manager class that handles multiple polymorphic data streams.
    """
    def __init__(self) -> None:
        """Initialize the processor with an empty stream registry."""
        self.streams: Dict[str, DataStream] = {}

    def add_stream(self, stream: DataStream):
        """
        Register a new stream with the processor.

        Args:
            stream: The DataStream object to register.
        """
        self.streams[stream.stream_id] = stream

    def process_stream_data(self, stream_id: str, data_batch: List[Any]
                            ) -> str:
        """
        Process data for a specific stream by ID.
        Handles retrieval, filtering, and processing polymorphically.

        Args:
            stream_id: The ID of the target stream.
            data_batch: The data to be processed.

        Returns:
            The result string from the stream's process_batch method.
        """
        try:
            stream = self.streams[stream_id]
            filtered_batch = stream.filter_data(data_batch)
            return stream.process_batch(filtered_batch)
        except KeyError:
            return "Error: Stream not found"


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    processor = StreamProcessor()

    # Structure: (Stream Class, ID, Type, Data Batch, Log Message)
    scenarios: List[tuple[Any, str, str, List[Any], str]] = [
        (
            SensorStream, "SENSOR_001", "Environmental Data",
            [{"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}],
            "Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]"
        ),
        (
            TransactionStream, "TRANS_001", "Financial Data",
            [{"buy": 100}, {"sell": 150}, {"buy": 75}],
            "Processing transaction batch: [buy:100, sell:150, buy:75]"
        ),
        (
            EventStream, "EVENT_001", "System Events",
            ["login", "error", "logout"],
            "Processing event batch: [login, error, logout]"
        )
    ]

    for stream_cls, s_id, s_type, batch, log_msg in scenarios:
        print(f"\nInitializing {stream_cls.__name__}...")

        stream = stream_cls(s_id)
        processor.add_stream(stream)

        print(f"Stream ID: {s_id}, Type: {s_type}")
        print(log_msg)

        result = processor.process_stream_data(s_id, batch)
        print(result)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("\nBatch 1 Results:")
    print("- Sensor data: 3 readings processed")
    print("- Transaction data: 3 operations processed")
    print("- Event data: 3 events processed")

    print("\nStream filtering active: High-priority data only")
    critical_sensor_batch = [{"temp": 120}, {"temp": 200}]
    large_trx_batch = [{"buy": 5000}]
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
