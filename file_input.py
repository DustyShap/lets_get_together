from app import process_list


def file_to_list(file):
    try:
        with open(file) as name_file:
            return name_file.read().splitlines()
    except:
        print('No file found')


def file_list_to_groups(file_list,group_size):
    return process_list(file_list,group_size)

def total_number_of_people_in_groups(processed_list):
    count = 0
    for group in processed_list:
        for person in group:
            count+=1
    return count
