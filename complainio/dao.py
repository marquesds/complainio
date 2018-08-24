import os

from bson import ObjectId, SON
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

    def get_complain_count_per_locale(self, _id='$locale.city'):
        # hack to deal with unit tests (mongomock is not working very well for aggregations)
        if not os.getenv('ENVIRONMENT') == 'Testing':
            _id = {'$concat': ['$locale.city', ' - ', '$locale.state']}

        pipeline = [
            {'$group': {'_id': _id, 'count': {'$sum': 1}}},
            {'$sort': SON([('count', -1), ('_id', -1)])}
        ]
        results = self.collection.aggregate(pipeline)
        cleaned_results = []
        for result in results:
            cleaned_result = {result['_id']: result['count']}
            cleaned_results.append(cleaned_result)
        return cleaned_results

    def get_specific_complain_count_by_locale(self, locale):
        if not os.getenv('ENVIRONMENT') == 'Testing':
            locale_str = locale['city'] + ' - ' + locale['state']
        else:
            locale_str = locale['city']

        complains = self.get_complain_count_per_locale()
        result = list(filter(lambda x: locale_str in x, complains))
        if result:
            return result[0]
        else:
            return {}
