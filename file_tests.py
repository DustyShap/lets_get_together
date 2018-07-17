import os
from app import app, generate_groups, process_list


FILE_NAME = input('What is the file name? ')
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
MY_DATA_PATH = os.path.join(THIS_DIR, FILE_NAME)

print(MY_DATA_PATH)


try:
    with open(MY_DATA_PATH) as file:
        print('there')
except IOError as e:
    print('No file')
