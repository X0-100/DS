# Merge two list
# lst1 = [1,2,3]
# lst2 = ['a','b','c']
# output = [1,'a',2,'b',3,'c']
# provided the two lists are of equal length


def process():
    lst1 = [1,2,3,4,5,6]
    lst2 = ['a','b','c',7,8,9]
    count = 0
    out = []

    for x in lst1:
        for x1 in range(0,len(lst2)):
            out.append(x)
            out.append(lst2[x1+count])
            count = count + 1
            print('count', count)
            print('out', out)
            break
                        
            
    print(out)
    

if __name__ == '__main__':
    process()
