'''
Sort all sublists in given list of strings
Input:
lst = [['Machine', 'London', 'Canada', 'France'],
       ['Spain', 'Munich'],
       ['Australia', 'Mandi']]

Output:
flist = [['Canada', 'France', 'London', 'Machine'],
         ['Munich', 'Spain'],
         ['Australia', 'Mandi']]

Implementation - unfinished
'''

class App:
    lst = []
    lst1 = []
    dict = {}

    def __init__(self, lst):
        self.lst = lst

    def process(self):
        for x in range(0,len(self.lst)):
            print(x)
            for y in self.lst[x]:
                print(y, '', y[0])
                dict = {self.lst1.append(ord(y[0])): y}
                print(self.lst1)
                for z in y:
                    print(z)
                    if dict['self.lst1.append(ord(y[0]))'] >











if __name__ == '__main__':
    app = App([['Machine','London','Canada','France'],['Spain','Munich'],['Australia','Mandi']])
    app.process()
