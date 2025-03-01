import os
import smtplib
import imghdr
from email.message import EmailMessage

email_sender="phanivikash@gmail.com"
password = os.getenv("PASSWORD")
email_receiver="phanivikash@gmail.com"

def send_email(image_path):
    email_message=EmailMessage()
    email_message["Subject"]= "New object Entered "
    email_message.set_content("Hey New object detected in the frame ")

    with open(image_path , "rb") as file:
        content = file.read()
    email_message.add_attachment(content,maintype = "image",
                                 subtype=imghdr.what(None,content))

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email_sender,password=password)
    gmail.sendmail(email_sender,email_receiver,email_message.as_string())
    gmail.quit()

'''if __name__ is "__main__":
    send_email(image_path="gen2.png")'''






