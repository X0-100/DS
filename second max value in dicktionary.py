# Python program to find second maximum value in Dictionary

def dicktion():
    new_dict ={"google":12, "amazon":9, "flipkart":4, "gfg":13}

    for key, value in new_dict.items():
        #print(key, value)
        pass

    for key,value in new_dict.items():
        #print(value)
        pass

    for key,value in new_dict.items():
        #print(key)
        pass

    for companyname, companyvalue in new_dict.items():
        for i in new_dict.items():
            print(companyname, i)



if __name__ == '__main__':
    dicktion()
