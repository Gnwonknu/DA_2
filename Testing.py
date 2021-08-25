import requests
import unittest
import Can_rename_ltr as prog

url = 'https://brickset.com/sets/year-1999'
r = requests.get(url)

class Hello(unittest.TestCase):

    def test_login_requests(self):
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
