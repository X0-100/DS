'''
This file combines two sorted lists using Selection Sort Algorithm
== Implementation ==
'''
def combine():
    test_list1 = [1,5,6,9,11]
    test_list2 = [3,4,7,8,10]
    emp_li = []
    for i in test_list1:
        emp_li.append(i)
    for j in test_list2:
        emp_li.append(j)
    '''
    #TEST DATA :
    emp_li = [20,12,10,15,2]
    '''
    emp_li = [20,12,10,15,2]
    print('Resultant List is {} '.format(emp_li))
    '''
    Sorting emp_li by implementing Selection Sort Algorithm
    '''
    pass_ = 1
    swap = 0
    while(pass_ < (len(emp_li)-1)):
        for i in range(len(emp_li)-1):
            for j in range(i, len(emp_li)):
                if(j == (len(emp_li)-1)):
                    print('<<<<<<<<<<<<<<<<<<<<<PASS {} ENDED>>>>>>>>>>>>>>>>>>>>>>>>>>'.format(pass_))
                    pass_ = pass_ + 1
                    break
                print('i {} - '.format(i),'j {} - '.format(j), 'pass {} - '.format(pass_))
                if(emp_li[i] > emp_li[j+1]):
                    iMin = emp_li[j+1]
                    emp_li[j+1] = emp_li[i]
                    emp_li[i] = iMin
                    print('emp_li {} '.format(emp_li))
                    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                else:
                    #print('No Swapping Required; emp_li is {} '.format(emp_li))
                    pass


if __name__ == '__main__':
    combine()
