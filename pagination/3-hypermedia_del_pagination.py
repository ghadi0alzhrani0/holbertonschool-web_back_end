#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination module."""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with empty dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached popular baby names dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by its original sorting position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """Return a deletion-resilient page starting at the given index."""
        index = 0 if index is None else index
        assert isinstance(index, int) and 0 <= index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0

        data = []
        next_index = index
        indexed_data = self.indexed_dataset()

        while (len(data) < page_size and
               next_index < len(self.dataset())):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
