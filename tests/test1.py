import unittest
from app import app
from io import BytesIO

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log Viewer', response.data)

    def test_upload_txt_file(self):
        data = {'file': (BytesIO(b'This is a test file.'), 'test.txt')}
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'File successfully uploaded and is a .txt file.', response.data)

    def test_upload_non_txt_file(self):
        data = {'file': (BytesIO(b'This is a test file.'), 'test.pdf')}
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid file format. Please upload a .txt file.', response.data)

if __name__ == '__main__':
    unittest.main()
