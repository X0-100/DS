#https://www.geeksforgeeks.org/python-ways-to-spilt-the-list-by-some-value/
#Implementation


list0 = []
li1 = []
li2 = []
	

def insert_list():
    number = 5
    for x in range(0, number):
        list0.append(input('Enter in List     '))
      


def split_inhalves():
    count = 0
    for x in range(0, len(list0)):
        if count < 1:
            li1.append(list0[x])
            count = count + 1
        else:
            li2.append(list0[x])
    print('li1 -- {} '.format(li1))
    print('li2 -- {} '.format(li2))
    



if __name__ == '__main__':
    insert_list()
    split_inhalves()





