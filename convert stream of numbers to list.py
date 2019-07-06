# cONVERT sTREAM oF nUMBERS tO lIST
# The original string is : 10 12 3 54 6 777 443
# The list of stream of numbers : ['10', '12', '3', '54', '6', '777', '443']


def conversion(arg1):
    originalstring = arg1
    lioriginalstring1 = originalstring[0]
    li = []
    
    

    for x in range(1, len(originalstring)):
        if(originalstring[x] == " "):
            li.append(lioriginalstring1)
            break
        
        else:
            lioriginalstring1 = originalstring[x] + lioriginalstring1
            print(lioriginalstring1)
            
            
            
    return(li)

   

    


if __name__ == '__main__':
    result = conversion("10 12 3 54 6 777 443")
    print(result)
                         
