#!/usr/bin/env python3
"""FUNCION PY QUE INSERTA UN NUEVO DOC EN COLECCION BASADA EN kwargs """
def insert_school(mongo_collection, **kwargs):
    document_id = mongo_collection.insert(kwargs)
    return document_id
