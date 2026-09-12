#!/usr/bin/env python3
"""Provide a function for inserting a school document into MongoDB."""


def insert_school(mongo_collection, **kwargs):
    """Insert a document from keyword arguments and return its new ID."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
