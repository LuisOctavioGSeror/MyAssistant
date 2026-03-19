import numpy as np
import smtplib
import email.message

def get_list_of_emails() -> list:

    list_of_emails = np.loadtxt("../data/notes/e-mails.txt", delimiter=',', dtype=str)
    list_of_emails = list_of_emails.tolist()
    return list_of_emails
def send_email(to: str, subject: str, email_body: str) -> str:

    message = email.message.Message()
    password = "yjensohwfhqqnfma"
    s = smtplib.SMTP('smtp.gmail.com: 587')

    message['Subject'] = subject
    message['From'] = "luisoctavioluis4@gmail.com"
    message['To'] = to
    message.add_header('Content-Type', 'text/html')
    message.set_payload(email_body)

    s.starttls()
    s.login(message['From'], password)
    s.sendmail(message['From'], [message['To']], message.as_string().encode('utf-8'))

    return "E-mail sent"


if __name__ == "__main__":

    #send_email("luisoctavioluis4@gmail.com", "Test", "This is a test")
    get_list_of_emails()