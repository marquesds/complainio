import mongomock

from complainio.dao import ComplainDAO
from tests import BaseTestCase


class ComplainDAOTestCase(BaseTestCase):
    def setUp(self):
        mongoclient = mongomock.MongoClient()
        database = mongoclient.complainio
        collection = database.complains
        self.complain_dao = ComplainDAO(collection=collection)

    def test_save_complain(self):
        complain = {
            'title': 'Problema com app do banco',
            'description': 'Tento abrir o app, mas não consigo.',
            'company': {
                'name': 'Itaú'
            },
            'locale': {
                'city': 'São Paulo',
                'state': 'SP'
            }
        }
        self.complain_dao.save(complain=complain)
        result = self.complain_dao.find_by(title='Problema com app do banco')[0]
        result.pop('ObjectId', None)

        self.assertDictEqual(result, complain)

    def test_find_complain_by_specific_field(self):
        complain = {'title': 'Teste'}
        self.complain_dao.save(complain=complain)

        result = self.complain_dao.find_by(title='Teste')[0]
        result.pop('ObjectId', None)

        self.assertDictEqual(result, complain)

    def test_find_all_complains(self):
        complain1 = {
            'title': 'Problema com app do banco',
            'description': 'Tento abrir o app, mas não consigo.',
            'company': {
                'name': 'Itaú'
            },
            'locale': {
                'city': 'São Paulo',
                'state': 'SP'
            }
        }

        complain2 = {
            'title': 'Meu livro não chegou',
            'description': 'Encomendei um livro há 40 dias e ainda não chegou.',
            'company': {
                'name': 'Amazon'
            },
            'locale': {
                'city': 'São Paulo',
                'state': 'SP'
            }
        }
        self.complain_dao.save(complain=complain1)
        self.complain_dao.save(complain=complain2)

        results = self.complain_dao.all()
        self.assertEqual(2, len(results))
