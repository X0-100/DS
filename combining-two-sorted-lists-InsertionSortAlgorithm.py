'''
This implements combining two sorted lists using Insertion Sort Algorithm
'''
def sort(li):
    for i in range(1,len(li)):
        if(li[i] < li[i-1]):
            #Swapping
            iMax = li[i]
            iMin = li[i-1]
            li[i-1] = iMax
            li[i] = iMin



def combine():
    #print('Hello World!')
    emp_li = [6,5,3,1,8,7,2,4]
    return(emp_li)


if __name__ == '__main__':
    emp_li = combine()
    sort(emp_li)
