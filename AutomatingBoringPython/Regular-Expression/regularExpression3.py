#! python3

import re

'''
Regular Expression Basic #3
Regex Character Class and findall() Method
'''

def findall():
    #return a list of string of valid number
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    matchedAll = phoneNumRegex.findall('111-222-3333 and 333-444-5553 and 444-555-6663 and (444)-222-6777')
    print(matchedAll)
    # return [num, num]

# findall()

def findAllGroup():
    # this will return list of tuple of matched object with multiple value that match the group inside the object
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    matchedAll = phoneNumRegex.findall('111-222-3333 and 333-444-5553 and 444-555-6663 and (444)-222-6777')

    print(matchedAll)
    #return [('areacode', 'num')]

# findAllGroup()

def multiGroup():
    # this will return list of tuple of whole phone number + area code + rest of number
    phoneNumRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
    matchedAll = phoneNumRegex.findall('111-222-3333 and 333-444-5553 and 444-555-6663 and (444)-222-6777')

    print(matchedAll)
    # return [('wholeNumber', 'AreaCode', 'Num')]

# multiGroup()

def charClass():
    '''
    Different Character Class to match complex pattern
    '''

    lyrics = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'

    xmasRegex = re.compile(r'\d+\s\w+')
    matchedAll = xmasRegex.findall(lyrics)

    print(matchedAll)
    #return ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# charClass()

def customCharClass():
    '''
    You can make your own character class by using [] (square bracket)
    [aeiou] will match vowels only (same as r'(a|e|i|o|u)')
    [aeiou]{2} will match double vowel, which mean 2 of those character in a row
    [^aeiou] will make negative characters class, anything will match if its not a vowel
    '''

    vowelRegex = re.compile(r'[aeiouAEIOU]')
    matched = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
    print(matched)

# customCharClass()
