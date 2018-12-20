# Find all the numbers in a string using regular expression in Python
# Given a string str containing numbers and alphabets, the task is to find all the numbers in str using regular expression.
# Input: abcd11gdf15hnnn678hh4           Output: 11 15 678 4

def reg_ex():

    str_n = input('Enter Input Charcaters  -  String&numbers mayBe....')
    reg_ex_simulation_1 = '0123456789'
    ar = []
    p = 0

    ar1 = []
    p1 = 0


    for i in str_n:
        for j in reg_ex_simulation_1:
            if(i == j):
                ar.append([])
                ar[p] = (i)
                p = p + 1
            else:
                pass


    print('EXTRACTED NUMBERS IN STRING FORMAT  '   , ar)

    print('RESULTANT EXTRACTED NUMBERS',list(map(int, ar)))


    for i in ar:
        for j in ar:
            ar1.append([])
            ar1[p1] = (i)





if __name__ == '__main__':
    reg_ex()
