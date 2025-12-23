#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
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
            return "Error"
        try:
            avg_temp = temp_sum / temp_count
        except ZeroDivisionError:
            return "Error"
        return (
            f"Sensor analysis: {count} readings processed, avg temp: " +
            f"{avg_temp}°C"
        )


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
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
            return "Error"
        return (
            f"Transaction analysis: {count} operations, net flow: " +
            f"{net_flow:+} units"
        )


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
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
            return "Error"
        return (
            f"Event analysis: {events} events, {errors} " +
            f"{'error' if errors == 1 else 'errors'} detected"
        )


class StreamProcessor():
    def __init__(self):
        self.streams: Dict[str, DataStream] = {}

    def add_stream(self, stream: DataStream, stream_id: str):
        self.streams[stream_id] = stream
