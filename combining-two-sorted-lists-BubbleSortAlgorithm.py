'''
This file combines two sorted lists
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
    emp_li = [5,2,6,7,3]
    '''
    #emp_li = [5,2,6,7,3]
    '''
    Sorting emp_li by implementing Bubble Sort Algorithm
    '''
    #Count-the-number-of-passes
    n = 1
    while n <= (len(emp_li)-1):
        for y in range(len(emp_li)):
            if(y != (len(emp_li)-1)):
                if( emp_li[y] > emp_li[y+1] ):
                    print('--------------LIST-WILL-BE-TRAVERSED------------------------')
                    temp = emp_li[y]
                    emp_li[y] = emp_li[y+1]
                    emp_li[y+1] = temp
                    print('List Traversed Side Effects - {} '.format(emp_li))
                else:
                    pass
        n = n + 1

if __name__ == '__main__':
    combine()
