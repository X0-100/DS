# Merge two list
# lst1 = [1,2,3]
# lst2 = ['a','b','c']
# output = [1,'a',2,'b',3,'c']


def process():
    lst1 = [1,2,3]
    lst2 = ['a','b','c']
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
