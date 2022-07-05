#!/usr/bin/env python3
"""
Python function that changes all topics of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """ name (string) will be the school name to update
    topics (list of strings) will be the list of topics
    """
    nm = {"name": name}
    tp = {"$set": {"topics": topics}}
    mongo_collection.update_many(nm, tp)
