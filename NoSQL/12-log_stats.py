#!/usr/bin/env python3
"""Display statistics about Nginx request logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats():
    """Print total, method, and status-check counts for Nginx logs."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print("{} status check".format(status_count))


if __name__ == "__main__":
    log_stats()
