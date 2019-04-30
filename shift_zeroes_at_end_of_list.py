# Shift zeroes at end of list
# test_list = [1, 4, None, "Manjeet", False, 0, False, 0, "Nikhil"]


def get():
    
    test_list = [1, 4, 0, 0, 0, None, "Manjeet", False, 0, False, 0, "Nikhil", True]
    empty1 = []
    empty2 = []
    final_list = []

    for x in test_list:
        if (x == 0 and x is not False):
            empty1.append(x)
        else:
            empty2.append(x)

    print('empty1 list for appending zeroes only', '=', empty1)
    print('empty2 for rest of others ', '=', empty2)

    for x in empty1:
        empty2.append(x)


    print('Modified List  ',empty2)
        
            
    
            


if __name__ == '__main__':
    get()
