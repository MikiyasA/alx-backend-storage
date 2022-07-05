#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """Return an empty list if no document in the collection
    """
    list_doc = []
    results = mongo_collection.find({})
    for r in results:
        list_doc.append(r)

    return list_doc
