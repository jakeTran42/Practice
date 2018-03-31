#! python3

import re

'''
Regular Expression Basic #2
Matching specific num of repetition
? This symbol means it can appear once or none (optional)
'''

def batGender():

    # batRegex = re.compile(r'Batman|Batwoman')
    batRegex = re.compile(r'Bat(wo)?man') #the code above can be written like this, the group 'wo' can appear 0 or 1 time to match the pattern

    matched = batRegex.search('The Batman Saga')
    matched1 = batRegex.search('The Batwoman Saga')

    print(matched.group())
    print(matched1.group())

# batGender()

'''
Finding if phone number will have an area code
'''

def optionalAreaCode():
    #you can separate area code by group and add a ? to see if it appear 1 or 0 times
    phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    matched = phoneNumRegex.search('My phone number is 222-3333')
    print(matched.group())

    #if you ever need to match a literal ? then you can use '\?'

# optionalAreaCode()

'''
* (asterisk) means match it if it appear 0 or more times
'''

def ZeroOrMore():
    #similar to ? but it can match the pattern if it appear more than once
    batRegex = re.compile(r'Bat(wo)*(man)*')

    matched = batRegex.search('The Batmanmanman Saga')
    matched1 = batRegex.search('The Batwowowowowoman Saga')

    print(matched.group())
    print(matched1.group())

    print(matched == None)
    print(matched1 == None)

    #if you need to match a literal * then use '\*'

# ZeroOrMore()

'''
+ symbol means the pattern must appear once or more
'''

def oneOrMore():
    batRegex = re.compile(r'Bat(wo)+man')
    matched = batRegex.search('The Batman Saga')
    matched1 = batRegex.search('The Batwoman Saga')

    print(matched == None) # return True if nothing match
    print(matched1 == None)

    #if you need to match a literal + then use '\+'

# oneOrMore()


'''
{Num} symbol will match the exact number that is in the curly braces
eg. regex = re.compile(r'(Ha){3}')
'''
