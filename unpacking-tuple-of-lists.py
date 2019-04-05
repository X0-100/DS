# CDAT - April-05-2019
# DESC(1) - Python | Unpacking tuple of lists
# DESC(2) - Given a tuple of lists, write a Python program to unpack the elements of the lists that are packed inside the given tuple.
# DESC(3) - Input  (['a', 'apple'], ['b', 'ball'])
# DESC(4) - Output ['a', 'apple', 'b', 'ball']

def unpack():
    coli = []
    tup1 = (['a', 'apple'], ['b', 'ball'])
    tup2 = ([1, 'sam', 75], [2, 'bob', 39], [3, 'Kate', 87])
    print('Packed tuple of list is ', tup2)
    for x in tup2:
        for y in x:
            coli.append(y)
    return(coli)
    
          
if __name__ == '__main__':
    coli_ = unpack()
    print('Unpacked tuple result is : ', coli_)
