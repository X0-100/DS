# CDAT - April-05-2019
# DESC(1) - Find top K frequent elements from a list of tuples
# DESC(2) - Given a list of tuples with word as first element and its frequency as second element, the task is to find top k frequent element.
# DESC(3) - Initial List of tuple is [[(‘Name’, 151)], [(‘ACe’, 400)], [(‘TURN’, 210)], [(‘RED’, 1113)], [(‘YELLOW’, 1)]]
# DESC(4) - Top ‘K’ elements are [(‘RED’, 1113), (‘ACe’, 400), (‘TURN’, 210)]
# Unfinished Implementation

from collections import defaultdict
def findK():
    
    inpu = [[('Name', 151)], [('ACe', 400)]]
    emp_li = []
    emp_tu = ()
    dfi = defaultdict(list)

    
    for x in inpu:
       
        for y in x:
           
            for k, v in x:
                dfi[k].append(v)
                
                for value in dfi[k]:
                    print(value)
                    
                    
                
                    
                
                
                

                

    





if __name__ == '__main__':
    findK()
