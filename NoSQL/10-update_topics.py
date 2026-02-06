#!/usr/bin/env python3
""" FUNCION PY QUE CAMBIA TODOS LOS topics DE UN documento school CON BASE AL NOMBRE"""
def update_topics(mongo_collection, name, topics):
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)


