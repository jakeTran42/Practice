import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587) #connection object (email domain, port num)

conn.ehlo() #start connection, return a reponse code and byte object

conn.starttls() #tls encryption will encrypt your password when sending it

conn.login('email', 'password') #(Username, password)

conn.sendmail('jake.tranheir@gmail.com', #send mail (from, to, body)
 'recipient@gmail.com',
 'Subject: So long...\n\nDear Jake, \nSo long, and thanks for everything.\n\n-Jake'
 ) #The return value is going to a dict of what failed so send, so a blank dict means it succeeded


conn.quit()
