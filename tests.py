from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure sure Flask was correctly set up
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that login page loads correctly
    def test_login_page_exists(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure login page responds appropriately to correct credentials
    def test_login_credentials_correct(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="bardia", password="lol"),
         follow_redirects=True)
        self.assertIn(b'Successful login', response.data)

    # Ensure login page responds appropriately to incorrect credentials
    def test_login_credentials_incorrect(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="meanie", password="ugly"),
        follow_redirects=True)
        self.assertIn(b'Invalid username/password. Please try again.', response.data)

    # Ensure logout page works correctly.
    def test_logout_page_exists(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="bardia", password="lol"),
         follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'Successfully logged out.', response.data)

    # Ensure that posts appear on home page
    def test_posts_show(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="bardia", password="lol"),
         follow_redirects=True)
        self.assertIn(b'Beautiful', response.data)

    # Ensure that the about page loads
    def test_about_page(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/txt')
        self.assertTrue(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
