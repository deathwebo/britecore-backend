import unittest
import json
from risker import app


class RiskerTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_risk_types(self):
        response = self.app.get('/risk_types')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(len(data['risk_types']), 3, msg="Amount of risk types don't match the fixtures")
        self.assertEqual(data['risk_types'][0]['name'], 'automobiles')

    def test_single_risk_type(self):
        response = self.app.get('risk_types/1')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data['risk_type']['name'], 'automobiles')


if __name__ == '__main__':
    unittest.main()
