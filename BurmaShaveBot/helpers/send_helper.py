import clients.email_to_sms_client
import clients.twilio_client
import yaml
config = yaml.safe_load(open("./helpers/config/send_config.yaml"))

class SendHelpers:
    def __init__(self):
        self.sender_email = config["send_config"]["email_to_sms_sender"]
        self.sender_number = config["send_config"]["twilio_purchased_number"]
        self.email_suffix_dict = config["send_config"]["email_suffixes"]

    def sendViaEmailGateway(self, receiver_numbers, message):
        twilio_client = clients.twilio_client.TwilioClient()
        email_to_sms_client = clients.email_to_sms_client.EmailToSmsClient()

        receiver_emails = []
        for i in receiver_numbers:
            provider = twilio_client.getCarrierByNumber(i)
            receiver_emails.append(i + self.email_suffix_dict[str(provider)])
        email_to_sms_client.sendViaEmailGateway(receiver_emails, message)

    def sendViaTwilio(self, numbers_list, message):
        twilio_client = clients.twilio_client.TwilioClient()

        conversation = twilio_client.createConversation("BurmaShave")

        participants = []
        for i in numbers_list:
            participants.add(twilio_client.createParticipant(conversation, i))

        participants.add(twilio_client.createParticipant(conversation, self.sender_number))

        twilio_client.createMessage(conversation, message, self.sender_number)

        twilio_client.deleteConversation(conversation)

    def getCarrierByNumber(self, number):
        twilio_client = clients.twilio_client.TwilioClient()

        phone_number = twilio_client.getCarrierByNumber(number)
        return phone_number.carrier


