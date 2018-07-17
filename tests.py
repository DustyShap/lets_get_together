import unittest
import os
from app import app, generate_groups, process_list
from file_input import file_to_list

test_list = ['John', 'Jill', 'James', 'Jessica', 'Jackie']
test_list2 = ['Bob', 'Bill', 'Beth', 'Brittney', 'Becky']

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
MY_DATA_PATH = os.path.join(THIS_DIR, 'names.txt')

class BasicTests(unittest.TestCase):
    def test_main_page(self):
        self.app = app.test_client()
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_groups_exist(self):
        self.assertTrue(process_list(test_list, 2))

    def test_process_list_equal(self):
        self.assertEqual(len(process_list(test_list, 2)),
                         len(process_list(test_list2, 2)))

    def test_process_list_not_equal(self):
        self.assertNotEqual(len(process_list(test_list, 2)),
                            len(process_list(test_list2, 3)))


class FileTests(unittest.TestCase):
    def setUp(self):
        self.testdata = open(MY_DATA_PATH)

    def test_does_file_exist(self):
        self.assertTrue(self.testdata)

    def test_file_to_list(self):
        self.assertTrue(isinstance(file_to_list(MY_DATA_PATH),list))

    def test_process_file(self):
        self.assertTrue(process_list(file_to_list(MY_DATA_PATH),3))


if __name__ == '__main__':
    unittest.main()
