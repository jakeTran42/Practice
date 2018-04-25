#! python3

'''
This simple program will take in sys arg for an address and google map itself.
If there are no argument then it will take whatever is in the clipboard.
This can be run with the command mapit by using batch files.
'''


import webbrowser, sys, pyperclip

address = sys.argv #sys.argv will return a list of something like this ['mapit.py', 'street', 'City', 'Zip Code']

if len(address) > 1:
    fullAddress = ' '.join(sys.argv[1:])

else:
    fullAddress = pyperclip.paste()


# https://www.google.com/maps/place/<Address>

webbrowser.open('https://www.google.com/maps/place/%s' % (fullAddress))
