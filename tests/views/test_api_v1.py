from tests import BaseTestCase


class APIV1TestCase(BaseTestCase):
    def test_healthcheck(self):
        response = self.client.get('/api/v1/health')

        self.assertEqual(200, response.status_code)
        self.assertEqual('Everything is fine!', response.data.decode())
