import smtplib
to =input("Enter recipient mail:\n")
content =input("Enter body content for the mail:\n")
def SendMail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sendermail@gmail.com','senderPassword')
    server.sendmail('sendmail@gmail.com', to,content)
    server.close()
    
SendMail(to,content)