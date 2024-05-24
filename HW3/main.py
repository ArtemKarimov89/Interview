import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"
    GMAIL_PORT = 587
    MAIL_FORMAT = '(RFC822)'
    EMPTY_BOX = 'There are no letters with current header'

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.header = None

    def send_msg(self, subject, recipients, text_message):
        """
        This is method for send mails!
        """
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(text_message))
        ms = smtplib.SMTP(self.GMAIL_SMTP, self.GMAIL_PORT)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, msg.as_string())
        ms.quit()

    def receive_msg(self):
        """
        This is method for receive mails!
        """
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        if self.header:
            criteria = f'(HEADER Subject {self.header})'
        else:
            criteria = 'ALL'
        data = mail.uid('search', criteria)
        try:
            assert data[0] != self.EMPTY_BOX
        except AssertionError:
            return self.EMPTY_BOX
        latest_email_uid = data[0].split()[-1]
        data = mail.uid('fetch', latest_email_uid, self.MAIL_FORMAT)
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    new_mail = Mail('login@gmail.com', 'qwerty')
    new_mail.send_msg('Subject', ['vasya@email.com', 'petya@email.com'], 'Message')
    message = new_mail.receive_msg()
