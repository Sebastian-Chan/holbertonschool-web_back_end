#!/usr/bin/env python3
"FUNCION PY QUE DEVUELVE LA LISTA DE school QUE TIENEN UN TOPIC ESPECÍFICO"


def schools_by_topic(mongo_collection, topic):
    """ mongo_collection will be the pymongo collection object
        topic (string) will be topic searched
    """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [i for i in documents]
    return list_docs
