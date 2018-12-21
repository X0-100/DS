'''
This file will print emoji
Unicodes are
\U0001f600

'''

'''
using unicodes
'''

def grinning_face():
    print("\U0001f600")

def grinning_squiting_face(): #Printing on terminal
    print("\U0001F606")

def rofl():
    print("\U0001F923")

'''
using CLDR short Names
'''

def CLDR_grinning_face():
    print('\N{grinning face}')

def CLDR_slightly_smiling_face():
    print('\N{slightly smiling face}')

def CLDR_winking_face(): #printing on terminal
    print('\N{winking face}')




if __name__ == '__main__':
    grinning_face()
    grinning_squiting_face()
    rofl()
    CLDR_grinning_face()
    CLDR_slightly_smiling_face()
    CLDR_winking_face()
