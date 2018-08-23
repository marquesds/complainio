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

        complain_dao = ComplainDAO()
        result = complain_dao.find_by(title='Problema com app do banco')[0]
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
