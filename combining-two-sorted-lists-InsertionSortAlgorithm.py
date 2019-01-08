'''
This implements combining two sorted lists using Insertion Sort Algorithm
'''
def sort(li):
    print('pointer {} '.format(pointer))
    print(li)
    pointer = 1

    for i in range(1,len(li)-1):
        pointer = pointer + 1
        print('pointer {} '.format(pointer))
        for j in range(i-pointer, i):
            if(li[i] < li[i-1]):
                #Swapping
                iMax = li[i]
                iMin = li[i-1]
                li[i-1] = iMax
                li[i] = iMin
                print(li)

def combine():
    #print('Hello World!')
    emp_li = [12,3,1,5,8]
    return(emp_li)


if __name__ == '__main__':
    emp_li = combine()
    sort(emp_li)
