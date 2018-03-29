#! python3

'''
Regular Expression Basic #1
'''

import re

#Phone number in US are typically 3 area code num, follow by - ,follow by 3 num, follow by - ,follow by 4 num.
#eg. xxx-xxx-xxx
message = 'Call me at 111-222-3333 tomorrow, or at 444-555-6666'
#Line below will look for this pattern and return it as a regular expression object
phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d\-\d\d\d\d')
#regular expression datatype have a search method which we can use to search string for the pattern and return a match object
matched = phoneNumRegex.search(message)
#match object have a method call group which will tell you the actual text/strings
print(matched.group())


#You can find all of the pattern text by using the find all method returned as a list
matched2 = phoneNumRegex.findall(message)
print(matched2)
