from app import process_list
import csv

# file = open('names.txt', 'r').read().splitlines()


# print(file)

# infoHash = {
#     'Chicago': ['Dustin','Kathryn'],
#     'SF':['Paul']
# }
# recordHash = {}
# for item in file:
#     # print(item.split(', '))
#     records = item.split(', ')
#     name,location = item.split(', ')
#     # print(location)
#     if location not in recordHash:
#         recordHash[location] = [name]
#     else:
#         recordHash[location].append(name)
# # print(recordHash)
#
# # print(my_list)
#
#
# for key in recordHash:
#     print(process_list(recordHash[key],2))


def group_by_location(file):
    records = open(file,"r").read().splitlines()
    recordHash = {}
    for item in records:
        name,location = item.split(', ')
        if location not in recordHash:
            recordHash[location] = [name]
        else:
            recordHash[location].append(name)
    # for key in recordHash:
    #     # print(process_list(recordHash[key],2))
    return recordHash


def get_group_size(hash, group_size):
    namelist = []
    for key in hash:
        # print(process_list(hash[key],group_size))
        namelist.append(process_list(hash[key],group_size))
    return namelist

print(group_by_location('names.txt'))
