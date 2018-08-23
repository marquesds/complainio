import json

import mock

from complainio.dao import ComplainDAO
from tests import BaseTestCase


class APIV1TestCase(BaseTestCase):
    def test_healthcheck(self):
        response = self.client.get('/api/v1/health')

        self.assertEqual(200, response.status_code)
        self.assertEqual('Everything is fine!', response.data.decode())

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_save_complain(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        body = {
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

        response = self.client.post('/api/v1/complains', data=json.dumps(body), content_type='application/json')
        self.assertEqual(201, response.status_code)

        complain_id = json.loads(response.data).get('id')
        complain_dao = ComplainDAO()
        result = complain_dao.get(complain_id)
        result.pop('_id', None)
        self.assertDictEqual(result, body)

    def test_save_complain_with_an_invalid_body(self):
        body = {
            'title': 'Problema com app do banco',
            'company': {
                'name': 'Itaú'
            },
            'locale': {
                'city': 'São Paulo',
                'state': 'SP'
            }
        }

        response = self.client.post('/api/v1/complains', data=json.dumps(body), content_type='application/json')
        self.assertEqual(400, response.status_code)

        expected = {
            'errors': {
                'description': ['Missing data for required field.']
            }
        }

        self.assertDictEqual(expected, json.loads(response.data))

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_get_complain_by_id(self, mock_get_collection):
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
        response = self.client.get(f'/api/v1/complains/{complain_id}')
        self.assertEqual(200, response.status_code)
        expected = json.loads(response.data)
        complain.pop('_id')
        expected.pop('_id')
        self.assertDictEqual(expected, complain)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_get_complain_by_id_empty_response(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        response = self.client.get('/api/v1/complains/1234')
        self.assertEqual(404, response.status_code)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_get_all_complains(self, mock_get_collection):
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

        response = self.client.get('/api/v1/complains')
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(json.loads(response.data)))

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_get_all_complains_empty_response(self, mock_get_collection):
        mock_get_collection.return_value = self.get_collection()

        response = self.client.get('/api/v1/complains')
        self.assertEqual(404, response.status_code)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_update_complain_by_id(self, mock_get_collection):
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

        response = self.client.put(
            f'/api/v1/complains/{complain_id}',
            data=json.dumps(complain_new_body),
            content_type='application/json'
        )

        self.assertEqual(200, response.status_code)

        result = complain_dao.get(complain_id)
        result.pop('_id')

        self.assertDictEqual(result, complain_new_body)

    @mock.patch('complainio.dao.ComplainDAO._get_collection')
    def test_delete_complain_by_id(self, mock_get_collection):
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
        complain_id1 = complain_dao.save(complain=complain1)
        complain_id2 = complain_dao.save(complain=complain2)

        response = self.client.delete(f'/api/v1/complains/{complain_id1}')
        self.assertEqual(204, response.status_code)

        result = complain_dao.get(complain_id1)
        self.assertIsNone(result)

        result = complain_dao.get(complain_id2)
        self.assertDictEqual(result, complain2)
