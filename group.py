import os, json, random

class Group():

    def sanitize_filename(self,file):
        return file.strip()

    def load_names(self,file):
        name_list = records = open(file,"r").read().splitlines()
        return name_list



    def process_list(self,participant_list, group_size):
        groups = []
        new_list = list(set(participant_list))  # Remove duplicates
        random.shuffle(new_list)
        for i in range(0, len(new_list), group_size):
            groups.append(new_list[i:i+group_size])
        return groups


if __name__ == '__main__':
    print('Welcome to the Lets Get Together Group Generator')
    print('------------------------------------------------')
    group = Group()
    while True:
        try:
            filename = group.sanitize_filename(input("What is the name of the input file? "))
            group_list = group.load_names(filename)
            group_numbers = int(input("How many people per group? "))
            print(group.process_list(group_list,group_numbers))
            break
        except:
            print('Invalid')
            break
