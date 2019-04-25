# CDAT - April-O5-06-2019
# DESC(1) - Find top K frequent elements from a list of tuples
# DESC(2) - Given a list of tuples with word as first element and its frequency as second element, the task is to find top k frequent element.
# DESC(3) - Initial List of tuple is [[(‘Name’, 151)], [(‘ACe’, 400)], [(‘TURN’, 210)], [(‘RED’, 1113)], [(‘YELLOW’, 1)]]
# DESC(4) - Top ‘K’ elements are [(‘RED’, 1113), (‘ACe’, 400), (‘TURN’, 210)]
# Unfinished

import sys

def findK():
    
    input_li =[[('Name', 151)], [('ACe', 400)],]

    emp_li = []
    dict_ = {}
    tup = ()


    for x in input_li:
        emp_li.append(x)
        for y in x:
            for z in y:
                print(z)
                dict_[z] = 0
                print(dict_)
        


    

    

    

    

    

    





if __name__ == '__main__':
    findK()
