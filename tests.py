import unittest
import os
from app import app, generate_groups, process_list
from file_input import file_to_list

test_list = ['John', 'Jill', 'James', 'Jessica', 'Jackie']
test_list2 = ['Bob', 'Bill', 'Beth', 'Brittney', 'Becky']

FILE_NAME = 'names.txt'

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
        self.test_file = open(FILE_NAME)

    def tearDown(self):
        self.test_file.close()

    def test_file_exists(self):
        self.assertTrue(self.test_file)

    def test_file_opens(self):
        open_file = open(FILE_NAME)
        open_file.close()

    def test_list_function(self):
        self.assertTrue(isinstance(file_to_list(FILE_NAME),list))

    def test_processed_groups_are_list(self):
        name_list = file_to_list(FILE_NAME)
        self.assertTrue(isinstance(process_list(name_list,2),list))

    def test_correct_group_sizes(self):
        GROUP_SIZE = 2





if __name__ == '__main__':
    unittest.main()
