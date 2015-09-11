import smtplib
import os
from email_auth import gmail_user, gmail_pwd
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage
from email.header         import Header    


def send_email(recipient, imgDir, extension = ".jpg"):
    msg = MIMEMultipart('contents and more contents')
    msg['Subject'] = 'Twitter Stats for the day'
    msg['From'] = gmail_user
    msg['To'] = recipient
    
    msg_text = MIMEText('From josh with love :D')
    msg.attach(msg_text)

    # send all jpg files in dir as attachments
    for img in [f for f in os.listdir(imgDir) if f.endswith(extension)]:
        with open(imgDir+img, 'rb') as file:
            msg_image = MIMEImage(file.read(), name='image',  _subtype="jpeg")
            msg.attach(msg_image)
        # throw away jpgs so as not to clutter
        os.remove(imgDir+img)
        
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
    imgDir = sys.argv[2]
    send_email(recipient, imgDir)
