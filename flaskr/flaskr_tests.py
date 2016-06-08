import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
    def tearDown(self):
        pass



    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ),follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in ' in rv.data
        rv = self.logout()
        assert 'You were logged out ' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username ' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data





if __name__ == '__name__':
    unittest.main()
