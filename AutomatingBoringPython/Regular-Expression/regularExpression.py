#! python3

'''
Regular Expression Basic #1
Regex Group and Pipe Character
'''

import re

message = 'Call me at 111-222-3333 tomorrow, or at 444-555-6666'

def findingValidNumber(message):
    '''
    Finding if a phone number exist in a string
    '''

    #Phone number in US are typically 3 area code num, follow by - ,follow by 3 num, follow by - ,follow by 4 num.
    #eg. xxx-xxx-xxx
    #Line below will look for this pattern and return it as a regular expression object
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    #regular expression datatype have a search method which we can use to search string for the pattern and return a match object
    matched = phoneNumRegex.search(message)
    #match object have a method call group which will tell you the actual text/strings
    print(matched.group())


    #You can find all of the pattern text by using the find all method returned as a list
    matched1 = phoneNumRegex.findall(message)
    print(matched1)



def subSection(message):
    '''
    More complex pattern matching, finding sub section of a pattern
    '''

    #You can use parenthesis to get area code or just a subsection of the phone numbers
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    matched = phoneNumRegex.search(message)

    #print out the first group (1) in parenthesis
    print(matched.group(1))
    #print out the 2nd group (2) in parenthesis
    print(matched.group(2))

    #You can use '\(' or '\)' to match literal parenthesis



def pipeOperator():
    '''
    Using pipes to match one of many pattern
    '''

    #using pipe character (or operator) to find anything with 'Bat'
    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    matched3 = batRegex.search('Batman is an orphan')

    print(matched3.group()) #You can also pass in group(1) to find out which suffix was found in pattern
