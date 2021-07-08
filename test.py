import unittest
from app import flask_app
from flask import session

class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = flask_app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # def test_login(self):
    #     tester = flask_app.test_client(self)
    #     response = tester.get('login', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)

    def test_report(self):
        tester = flask_app.test_client(self)
        response = tester.get('report', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # def test_create_flight(self):
    #     tester = flask_app.test_client(self)
    #     response = tester.get('createflight', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)

    def test_unknown(self):
        tester = flask_app.test_client(self)
        response = tester.get('test', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # def test_register_validate_input(self):
    #     response = flask_app.test_client(self).post('login', {username: 'James', password: '007'})
    #     self.assertEquals(response, 'James')
    #     #
    #     # response = flask_app.test_client(self).post('login', data={'Username': 'admin', 'Password': 'admin'})
    #     # self.assertEqual(response.data, 'message')

    # def test_input_login(self):
    #     with flask_app.test_client() as temp:
    #         rv = temp.get('/')
    #         assert session['foo'] == 42

if __name__ == '__main__':
    unittest.main()