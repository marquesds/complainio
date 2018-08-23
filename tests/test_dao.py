from bson import ObjectId
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

        self.assertDictEqual(result, complain)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_get_complain_by_id(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        complain = {
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

        complain_id = complain_dao.save(complain=complain)
        result = complain_dao.get(complain_id)

        self.assertDictEqual(result, complain)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_get_complain_by_id_empty_result(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        complain_id = str(ObjectId())
        result = complain_dao.get(complain_id)

        self.assertIsNone(result)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_find_complain_by_specific_field(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        complain = {'title': 'Teste'}
        complain_dao.save(complain=complain)

        result = complain_dao.find_by(title='Teste')[0]

        self.assertDictEqual(result, complain)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_find_complain_by_specific_field_empty_result(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        results = complain_dao.all()

        self.assertListEqual([], results)

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

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_find_all_complains_empty_result(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        results = complain_dao.all()

        self.assertListEqual([], results)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_update_complain(self, mock_get_collection):
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
        complain_id = complain_dao.save(complain=complain)
        result = complain_dao.get(complain_id)
        self.assertDictEqual(result, complain)

        complain_new_body = {
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

        complain_dao.update(complain_id, complain_new_body)
        result = complain_dao.get(complain_id)
        result.pop('_id')

        self.assertDictEqual(result, complain_new_body)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_try_update_nonexistent_complain(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()

        complain_new_body = {
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

        complain_id = str(ObjectId())
        complain_dao.update(complain_id, complain_new_body)

        result = complain_dao.get(complain_id)
        self.assertIsNone(result)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_delete_complain(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        complain = {
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

        complain_id = complain_dao.save(complain=complain)
        result = complain_dao.get(complain_id)

        self.assertDictEqual(result, complain)

        complain_dao.delete(complain_id)
        result = complain_dao.get(complain_id)

        self.assertIsNone(result)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_try_delete_nonexistent_complain(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_id = str(ObjectId())
        complain_dao = ComplainDAO()

        results = complain_dao.all()
        self.assertListEqual([], results)

        complain_dao.delete(complain_id)

        results = complain_dao.all()
        self.assertListEqual([], results)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_get_complain_count_by_locale(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        complain_dao.save({'locale': {'city': 'São Paulo', 'state': 'SP'}})
        complain_dao.save({'locale': {'city': 'São Paulo', 'state': 'SP'}})
        complain_dao.save({'locale': {'city': 'São Paulo', 'state': 'SP'}})
        complain_dao.save({'locale': {'city': 'São Paulo', 'state': 'SP'}})

        complain_dao.save({'locale': {'city': 'Fortaleza', 'state': 'CE'}})
        complain_dao.save({'locale': {'city': 'Fortaleza', 'state': 'CE'}})

        complain_dao.save({'locale': {'city': 'Curitiba', 'state': 'PR'}})

        results = complain_dao.get_complain_count_by_locale('$locale.city')

        # the real results will be something like [{'São Paulo - SP': 4}, {'Fortaleza - CE': 2}, ...]
        expected = [{'São Paulo': 4}, {'Fortaleza': 2}, {'Curitiba': 1}]
        self.assertListEqual(expected, results)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_get_complain_count_by_locale_empty_result(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        complain_dao = ComplainDAO()
        results = complain_dao.get_complain_count_by_locale('$locale.city')

        self.assertListEqual([], results)
