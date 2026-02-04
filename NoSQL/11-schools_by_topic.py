"FUNCION PY QUE DEVUELVE LA LISTA DE school QUE TIENEN UN TOPIC ESPECÍFICO"

def schools_by_topic(mongo_collection, topic):
    documents = mongo_collection.find({"topics": topic})
    list_docs = [i for i in documents]
    return list_docs
