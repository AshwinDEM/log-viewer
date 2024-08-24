import unittest
from app import app
from io import BytesIO

'''
Root
├── Home Page
│   └── test_home
│       ├── Status Code: 200
│       └── Contains: 'Log Viewer'
│
├── Upload File
    ├── File Type: .txt
    │   ├── Starts with .LOG
    │   │   ├── Valid Time and Date Format
    │   │   │   └── test_upload_txt_file_with_log_and_datetime
    │   │   │       ├── Status Code: 200
    │   │   │       └── Contains: 'File successfully uploaded and is a .txt file.'
    │   │   └── Invalid Time and Date Format
    │   │       └── test_upload_txt_file_with_log_and_invalid_datetime
    │   │           ├── Status Code: 200
    │   │           └── Contains: 'Invalid file content. The second line must be in the format HH:MM DD-MM-YYYY.'
    │   └── Does Not Start with .LOG
    │       └── test_upload_txt_file_without_log
    │           ├── Status Code: 200
    │           └── Contains: 'Invalid file content. The file must start with .LOG.'
    └── File Type: Not .txt
        └── test_upload_non_txt_file
            ├── Status Code: 200
            └── Contains: 'Invalid file format. Please upload a .txt file.
'''


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the home page
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log Viewer', response.data)

    # Test that uploaded file is a .txt file and starts with .LOG and has a valid time and date format
    def test_upload_txt_file_with_log_and_datetime(self):
        data = {'file': (BytesIO(b'.LOG\n21:30 31-10-2004\nThis is a test file.'), 'test.txt')}
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'File successfully uploaded and is a .txt file.', response.data)

    # Test that uploaded file is a .txt file but starts with .LOG and has an invalid time and date format
    def test_upload_txt_file_with_log_and_invalid_datetime(self):
        data = {'file': (BytesIO(b'.LOG\n21:30 31-10-04\nThis is a test file.'), 'test.txt')}
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid file content. The second line must be in the format HH:MM DD-MM-YYYY.', response.data)

    # Test that uploaded file is a .txt file but does not start with .LOG
    def test_upload_txt_file_without_log(self):
        data = {'file': (BytesIO(b'This is a test file.'), 'test.txt')}
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid file content. The file must start with .LOG.', response.data)

    # Test that uploaded file is not a .txt file
    def test_upload_non_txt_file(self):
        data = {'file': (BytesIO(b'This is a test file.'), 'test.pdf')}
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid file format. Please upload a .txt file.', response.data)

if __name__ == '__main__':
    unittest.main()
