# Program to count number of lists in a list of lists
# Input : [[1,2,3],[4,5,6,7,8,9],[10,11,12,22,22,34]]
# Output : 3


def process():
    lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9],[10,23,23,34],[45,54,54]]
    count = 0

    for i in lst:
        if(i):
            count = count + 1
    print('Number of lists in a list of lists', count)

if __name__ == '__main__':
    process()
        
