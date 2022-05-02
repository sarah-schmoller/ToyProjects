import smtplib
import ssl
import yaml
config = yaml.safe_load(open("./clients/config/email_to_sms_config.yaml"))

class EmailToSmsClient:
    def __init__(self):
        self.port = config["email_to_sms_config"]["port"]
        self.smtp_server = config["email_to_sms_config"]["smtp_server"]
        self.sender_email = config["email_to_sms_config"]["sender_email"]
        self.password = config["email_to_sms_config"]["password"]

    def sendViaEmailGateway(self, receiver_emails, message):
        context = ssl.create_default_context()
        for i in receiver_emails:
            with smtplib.SMTP_SSL(self.smtp_server, int(self.port), context=context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, i, message)

