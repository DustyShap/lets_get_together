import unittest
import os
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
# 
#
# class FileTests(unittest.TestCase):
#     def test_setup(self):
#         name_list = []
#         self.testdata = open(MY_DATA_PATH).readlines()
#         for name in self.testdata:
#             name_list.append(name.replace('\n', ''))
#         self.assertEqual(len(name_list),
#                          len(process_list(name_list,1)))
#     # def test_group_from_list(self):
#     #     self.assertEqual(len(self.testdata),
#     #                     len(process_list))
#     #     print(len(self.testdata))
#
#



if __name__ == '__main__':
    unittest.main()
