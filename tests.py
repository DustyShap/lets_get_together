import unittest
import os
from app import app, generate_groups, process_list
from extension import group_by_location, get_group_size

test_list = ['John', 'Jill', 'James', 'Jessica', 'Jackie']
test_list2 = ['Bob', 'Bill', 'Beth', 'Brittney', 'Becky']

NUM_CITIES = 5
GROUP_SIZE = 2

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


class LocationTests(unittest.TestCase):
    def setUp(self):
        self.name_file = open('names.txt')

    def tearDown(self):
        self.name_file.close()

    def test_to_see_if_file_exists(self):
        self.assertTrue(self.name_file)

    def test_to_see_if_groups_by_unique_city(self):
        self.assertEqual(NUM_CITIES, len(group_by_location('names.txt').keys()))

    def test_to_ensure_group_size(self):
        oversize = False
        #Assert that any of the groups generated didn't exceed group number
        records = group_by_location('names.txt')
        # self.assertTrue(get_group_size(records,GROUP_SIZE) <= GROUP_SIZE)
        lists = get_group_size(records, GROUP_SIZE)
        print(lists)
        for list in lists:
            for i in list:
                if len(i) > GROUP_SIZE:
                    oversize = True
        self.assertFalse(oversize)


if __name__ == '__main__':
    unittest.main()
