'''
This implements combining two sorted lists using Insertion Sort Algorithm
'''
def sort(li):
    pointer = 1
    print('pointer {}'.format(pointer))
    print('li {} '.format(li))
    while(pointer<len(li)):
        for i in range(1,len(li)-1):
            pointer = pointer + 1
            print('pointer {} '.format(pointer))
            for j in range(i-1, i):
                #break
                if(li[i-1] > li[i]):
                    iMax = li[i-1]
                    iMin = li[i]
                    li[i] = iMax
                    li[i-1] = iMin
                    print(li)
def combine():
    emp_li = [12,3,1,5,8]
    return(emp_li)
if __name__ == '__main__':
    emp_li = combine()
    sort(emp_li)
