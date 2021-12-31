import smtplib
import email.message

def email_sender(url):
    email_content = url
    msg = email.message.Message()

    msg["Subject"] = "Preço da câmera baxou"
    msg["From"] # = Email do remetente
    msg["To"] # = Email do destinatário
    password # = Senha
    msg.add_header("Content-type", "text/html")
    msg.set_payload(email_content)

    sender = smtplib.SMTP("smtp.gmail.com", 587)
    sender.starttls()
    sender.login(msg["From"], password)
    sender.sendmail(msg["From"], msg["To"], msg.as_string())

    print("Email enviado com sucesso!!!")
