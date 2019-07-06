# https://www.geeksforgeeks.org/python-check-for-spaces-in-string/
# Check the presence of space in string and return "True" if present else "false"

def check_spaces():
    stringtext = str(input("Enter the String to check if space present or not   "))

    stringtext = list(stringtext)

    numberofspaces = 0

    for x in range(0, len(stringtext)):
        if (stringtext[x] == " "):
            numberofspaces = numberofspaces+1
    
            
    if(numberofspaces == 0):
        print("String contains no spaces")
    else:
        print("Space detected {}".format(numberofspaces))



if __name__ == '__main__':
    check_spaces()
