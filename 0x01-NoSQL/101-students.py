#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score
"""
import pymongo


def top_students(mongo_collection):
    return mongo_collection.aggregate([
        { "$addFields":
          {"name": "name",
           "averageScore": {"$avg": "$topics.score"}
          }
        },
        {"$sort": {"averageScore": -1}}
        ])
