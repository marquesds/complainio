from complainio import mongo


class ComplainDAO:
    def __init__(self):
        self.collection = self._get_collection()

    def _get_collection(self):
        return mongo.db.complainio

    def save(self, complain):
        self.collection.insert_one(complain)

    def update(self):
        pass

    def delete(self):
        pass

    def find_by(self, **kwargs):
        result = self.collection.find(kwargs)
        return list(result)

    def all(self):
        return list(self.collection.find())
