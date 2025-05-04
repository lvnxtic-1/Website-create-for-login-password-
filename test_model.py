import unittest
from app import app

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_login_success(self):
        response = self.client.post('/login', data=dict(
            username='admin',
            password='password123'
        ))
        self.assertIn(b"Welcome", response.data)

    def test_login_failure(self):
        response = self.client.post('/login', data=dict(
            username='wrong',
            password='user'
        ))
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
