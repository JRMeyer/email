# Import smtplib for the actual sending function
import smtplib
from email_auth import gmail_user, gmail_pwd
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage
from email.header         import Header    


def send_email(recipient):
    msg = MIMEMultipart('contents and more contents')
    msg['Subject'] = 'What a subject line!'
    msg['From'] = gmail_user
    msg['To'] = recipient
    
    msg_text = MIMEText('foo foo foo bar bar bar')
    msg.attach(msg_text)

    with open('img.jpg', 'rb') as file:
        msg_image = MIMEImage(file.read(), name='image',  _subtype="jpeg")
        msg.attach(msg_image)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(gmail_user, [recipient], msg.as_string())
        server.close()
        print 'successfully sent mail'
    except:
        print 'failed to send mail'




if __name__ == '__main__':
    import sys
    recipient = sys.argv[1]
    send_email(recipient)
