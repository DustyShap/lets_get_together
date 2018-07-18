import unittest
import os
from app import app, generate_groups, process_list
from file_input import file_to_list, file_list_to_groups,total_number_of_people_in_groups

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
        self.file_name = 'names.txt'
        self.name_list = file_to_list(self.file_name)

    def tearDown(self):
        pass

    def test_to_see_if_file_exists(self):
        name_file = open(self.file_name)
        self.assertTrue(name_file)
        name_file.close()

    def test_file_to_list_function(self):
        name_list = file_to_list(self.file_name)
        self.assertTrue(isinstance(name_list,list))

    def test_file_to_groups_function(self):
        name_list = file_to_list(self.file_name)
        # print(file_list_to_groups(name_list,4))
        self.assertTrue(isinstance(file_list_to_groups(name_list,4),list))

    def test_length_of_list_vs_total_groups(self):
        list_length = len(file_to_list(self.file_name))
        processed_groups_length = total_number_of_people_in_groups(file_list_to_groups(self.name_list,4))
        self.assertEqual(list_length,processed_groups_length)



if __name__ == '__main__':
    unittest.main()
