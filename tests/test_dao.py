import mongomock
from mock import mock

from complainio.dao import ComplainDAO
from tests import BaseTestCase


class ComplainDAOTestCase(BaseTestCase):

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_save_complain(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
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
        complain_dao.save(complain=complain)
        result = complain_dao.find_by(title='Problema com app do banco')[0]
        result.pop('ObjectId', None)

        self.assertDictEqual(result, complain)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_find_complain_by_specific_field(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        complain = {'title': 'Teste'}
        complain_dao.save(complain=complain)

        result = complain_dao.find_by(title='Teste')[0]
        result.pop('ObjectId', None)

        self.assertDictEqual(result, complain)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_find_all_complains(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
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
        complain_dao.save(complain=complain1)
        complain_dao.save(complain=complain2)

        results = complain_dao.all()
        self.assertEqual(2, len(results))
