import unittest
from app import app, generate_groups, process_list


class BasicTests(unittest.TestCase):
    def test_main_page(self):
        self.app = app.test_client()
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_process_list(self):
        test_list = ['John', 'Jill', 'James', 'Jessica', 'Emily']
        test_list2 = ['Bob', 'Bill', 'Beth', 'Brittney', 'Becky']
        self.assertEqual(len(process_list(test_list, 2)),
                         len(process_list(test_list, 2)))


if __name__ == '__main__':
    unittest.main()
