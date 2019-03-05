'''
This file combines two sorted lists using Bubble Sort Algorithm
'''
def combine():
    test_list1 = [1,5,6,9,11]
    test_list2 = [3,4,7,8,10]
    emp_li = []
    for i in test_list1:
        emp_li.append(i)
    for j in test_list2:
        emp_li.append(j)

    #print('Resultant List is {} '.format(emp_li))

    '''
    #TEST DATA :
    emp_li = [5,2,6,7,3]
    
    emp_li = [5,2,6,7,3]
    print('Resultant List is {} '.format(emp_li))
    '''
    '''
    Sorting emp_li by implementing Bubble Sort Algorithm
    '''
    #Count-the-number-of-passes
    pass_ = 1
    swap = 0
    while pass_ <= (len(emp_li)-1):
        for y in range(len(emp_li)):
            if(y != (len(emp_li)-1)):
                if( emp_li[y] > emp_li[y+1] ):
                    swap = swap + 1
                    print('--------------At Pass {} --------------------------  '.format(pass_))
                    temp = emp_li[y]
                    emp_li[y] = emp_li[y+1]
                    emp_li[y+1] = temp
                    print('List SORTED - {} '.format(emp_li))
                else:
                    pass
        print('***************************PASS TAKEN {} **********************'.format(pass_))
        pass_ = pass_ + 1
    print('Total swaps taken is {}  '.format(swap))


if __name__ == '__main__':
    combine()
