'''
this file shows the possible iteartion methods
0. a simple iteartion
1. iterating using range
2. iterating using enumerate
'''

def process0():
    string = input('enter string to iterate     ')
    for element in string:
        print(element, end='')
    print('\n')

def process1():
    string = input('enter string to iterate     ')
    for element in range(len(string)):
        print(string[element], end='')
    print('\n')

def process2():
    string = input('enter string to iterate       ')
    for key, value in enumerate(string):
        print(value, end='')
    print('\n')

if __name__ == '__main__':
    process0()
    process1()
    process2()
