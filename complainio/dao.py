from bson import ObjectId
from bson.errors import InvalidId

from complainio import mongo


class ComplainDAO:
    def __init__(self):
        self.collection = self._get_collection()

    def _get_collection(self):
        return mongo.db.complainio

    def save(self, complain):
        result = self.collection.insert_one(complain)
        return str(result.inserted_id)

    def update(self, complain_id, complain_new_body):
        self.collection.update_one({
            '_id': ObjectId(complain_id)},
            {'$set': complain_new_body},
            upsert=False
        )

    def delete(self, complain_id):
        self.collection.delete_one({'_id': ObjectId(complain_id)})

    def get(self, complain_id):
        try:
            return self.collection.find_one({'_id': ObjectId(complain_id)})
        except InvalidId:
            return None

    def find_by(self, **kwargs):
        result = self.collection.find(kwargs)
        return list(result)

    def all(self):
        return list(self.collection.find())
