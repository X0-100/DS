'''
this file converts list to tuple
convert() function : converts list to tuple
convert1() function : converts list to tuple
'''

def convert():
    input_list = []
    rang = int(input('Enter range of numbers to get added to list      '))

    for i in range(rang):
        input_list.append(i)

    tuple = ()
    counter = 0

    for i in input_list:
        tuple = tuple + (i,)

    print('List converted to tuple is  {}'.format(tuple))


def convert1():
    input_list = []
    rang = int(input('Enter range of numbers to get added to the list       '))

    for i in range(rang):
        input_list.append(i)

    print('List converted to tuple is  {}'.format(tuple(input_list)))



if __name__ == '__main__':
    convert()
    convert1()
