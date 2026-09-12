#!/usr/bin/env python3
"""Provide a function for listing every document in a collection."""


def list_all(mongo_collection):
    """Return all documents found in the supplied MongoDB collection."""
    return list(mongo_collection.find())
