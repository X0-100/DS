# Find elements of a list by indices
# Given two lists with elements and indices, find elements of list 1 at indices present in list 2.
# list1 = [10,20,30,40,50]
# list2 = [0,2,4]
# find_list = [10,30,50]


def get():
    list1 = ['Hello', 'geeks', 'for', 'geeks']
    list2 = [1,2,3]
    find_list_by_indices = []
    for y in list2:
        find_list_by_indices.append(list1[y])
    print(find_list_by_indices)


if __name__ == '__main__':
    get()
        
