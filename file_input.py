from app import process_list

def file_to_list(testFile):
    test_file = open(testFile)
    test_file_list = test_file.read().splitlines()
    test_file.close()
    return test_file_list
if __name__ == '__main__':
    FILE_NAME = input('What is the filename?:  ')
    GROUP_SIZE = int(input('What is the size of the group?:  '))
    try:
        list_of_names = file_to_list(FILE_NAME)
        count = 1
        for group in process_list(list_of_names,GROUP_SIZE):
            print("-----------------------")
            print('Group {}'.format(count))
            for name in group:
                print(name)
            count += 1
    except:
        print("-----------------------")
        print('File doesnt exist')
        print("-----------------------")
