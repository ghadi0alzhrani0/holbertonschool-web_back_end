#!/usr/bin/env python3
"""Provide a function for finding schools that teach a topic."""


def schools_by_topic(mongo_collection, topic):
    """Return all school documents containing the requested topic."""
    return mongo_collection.find({"topics": topic})
