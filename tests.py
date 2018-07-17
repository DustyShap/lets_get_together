import os
import unittest
from app import app, generate_groups, process_list

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
MY_DATA_PATH = os.path.join(THIS_DIR, 'names.txt')


test_list = ['John', 'Jill', 'James', 'Jessica', 'Jackie']
test_list2 = ['Bob', 'Bill', 'Beth', 'Brittney', 'Becky']

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
        self.test_data = open(MY_DATA_PATH).read().splitlines()
        self.file_name_total = len(self.test_data)

    def test_process_file(self):
        self.assertNotEqual(len(process_list(self.test_data,2)),
                         len(process_list(self.test_data,3)))

    def test_group_numbers(self):
        pass






if __name__ == '__main__':
    unittest.main()
