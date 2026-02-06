#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a
    collection based on kwarg
"""

def insert_school(mongo_collection, **kwargs):
    document_id = mongo_collection.insert(kwargs)
    return document_id
