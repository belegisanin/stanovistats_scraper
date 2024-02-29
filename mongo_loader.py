from pymongo import MongoClient
from model.listing import Listing
from pymongo.operations import UpdateMany


class MongoLoader:
    client: MongoClient = None

    def __init__(self, client: MongoClient):
        self.client = client

    def insert_all_listings(self, listings: list[Listing], db_name: str,
                            collection_name: str, logs=False) -> int | None:
        db = self.client[db_name]
        collection = db[collection_name]

        try:
            operations = [UpdateMany({"_id": l.id}, {"$set": l.to_dict()}, upsert=True) for l in listings]
            result = collection.bulk_write(operations)

            if logs:
                print(f'Total of {result.inserted_count} listings inserted into MongoDB database')

            return result.inserted_count

        except Exception as e:
            print(e)

        return None
