from complainio import mongo


def get_mongodb_client_mock():
    pass


class ComplainDAO:
    def __init__(self, collection=None):
        self.collection = collection
        if not self.collection:
            self.collection = mongo.db.complainio

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
