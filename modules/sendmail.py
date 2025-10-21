import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from modules.talk import talk


def send_email(recipient_email, subject, message):
    try:
        sender_email = "sushilkumardora1290@gmail.com"
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465
        app_password = 'bqjdqsxnkicbhdrc'
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, app_password)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        talk("Sorry, I couldn't send the email. Please try again.")
