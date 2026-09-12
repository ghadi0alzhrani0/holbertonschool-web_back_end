#!/usr/bin/env python3
"""Provide a function for updating topics of matching schools."""


def update_topics(mongo_collection, name, topics):
    """Replace the topics of every school document matching a name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
