#! python3

'''
This program will take a document and extract all Phone Number and Email
'''

import re, pyperclip

# TODO: Create regex for phone number
phoneNumRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                # area code
(\s|-|\.)?                        # separator
(\d{3})                           # first 3 digits
(\s|-|\.)                         # separator
(\d{4})                           # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

# TODO: Create Regex for Email
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+      # username
@                    # the at symbol
[a-zA-Z0-9_.+]+      # domain name
''', re.VERBOSE)



# TODO: Get text off clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from text
extractedPhone = phoneNumRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNum = []
for num in extractedPhone:
    allPhoneNum.append(num[0])


# TODO: Copy and extract email/phone to clipboard

allPhone = '\n'.join(allPhoneNum)
allEmail = '\n'.join(extractedEmail)

print(allEmail)
