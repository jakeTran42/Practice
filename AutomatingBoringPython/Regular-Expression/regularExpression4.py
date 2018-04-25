#! python3

'''
Regex Dot-Star, Caret/Dollar Sign
sub() method and Verbose Mode
'''

import re

'''
Using ^ (Caret) indicate that the regex must begin with the specify pattern
eg. re.compile(r'^Hello') #Hello must occur beginning of string

Using $ indicate the regex must ends with the patterns
eg. re.compile(r'$Hello') #Hello must occur at the end of string

Using . (dot character) means any character except for new line (to match new line then use re.DOTALL as second argument in your compile method)
eg. re.compile(r'.at') will return any string that have any 1 character follow by 'at'
    findall('The Cat is wearing a hat') ---> return ---> ['Cat', 'hat'] #Cat and Hat have 1 character follow by 'at'

Using .* means any pattern (Dot Star will use greedy match so use a ? if you want non-greedy)
    >>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    >>> mo = nameRegex.findall('First Name: Al Last Name: Sweigart')
    >>> [('Al', 'Sweigart')]

Using re.IGNORECASE or re.I will ignore casing as 2nd argument

Find and replace will use the sub() method (substitude)

Using re.VERBOSE will make your pattern more readable as a 2nd argument
'''
