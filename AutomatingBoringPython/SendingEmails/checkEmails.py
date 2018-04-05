import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) #ssl is encryption algorithm

conn.login('email', 'password')

conn.list_folders() # return a list of tuples for email folders

conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE', '01-Jan-2018'])

len(UIDs)

newestMessageID = UIDs[len(UIDs) - 1 ]

newestMessageID

rawMSG = conn.fetch([newestMessage], ['BODY[]', 'FLAGS']) #retrieving the last email

rawMSG

message = pyzmail.PyzMessage.factory(rawMSG[newestMessage][b'BODY[]'])

message.get_subject() #getting the message subject

message.get_addresses('from')

message.get_addresses('to')

message.text_part

message.html_part == None

text = message.text_part.get_payload().decode('UTF-8')

print(text)


'''
TO Delete Emails
'''

conn.select_folder('INBOX', readonly=False)

UID2 = conn.search(['ON', '01-Jan-2018'])

UID2

firstEmailOnUID2 = UID2[0]

conn.delete_messages([firstEmailOnUID2])
