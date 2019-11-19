import smtplib
import email.message


def send_activation_email(subject, message, to):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("softflix.info@gmail.com", "SoftFlix123.")

        msg = email.message.Message()
        msg['Subject'] = subject
        msg['From'] = "softflix.info@gmail.com"
        msg['To'] = to
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(message)

        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.quit()
    except Exception as e:
        print('Mail Send Failed')
        print(e)
