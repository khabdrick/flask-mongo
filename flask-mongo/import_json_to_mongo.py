
from pymongo import MongoClient
import json

def import_json_to_mongo(db_name, collection_name, json_path):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]

    with open(json_path, 'r') as f:
        data = json.load(f)
        db[collection_name].insert_many(data)

    client.close()

if __name__ == "__main__":
    db_name = 'blogdb'
    collection_name = 'posts'
    json_path = 'post.json'
    import_json_to_mongo(db_name, collection_name, json_path)
