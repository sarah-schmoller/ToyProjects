from twilio.rest import Client
import yaml
config = yaml.safe_load(open("./clients/config/twilio_config.yaml"))

class TwilioClient:
    def __init__(self):
        self.account_sid = config["twilio_config"]["account_sid"]
        self.auth_token = config["twilio_config"]["auth_token"]
        self.sender = config["twilio_config"]["purchased_number"]
        self.client = Client(self.account_sid, self.auth_token)

    def createParticipant(self, conversation, number):
        return self.client.conversations \
            .conversations(conversation.sid) \
            .participants \
            .create(
                identity=("+1" + number),
                messaging_binding_address=("+1" + number)
            )

    def createMessage(self, conversation, message):
        return self.client.conversations \
            .conversations(conversation.sid) \
            .messages \
            .create(
                body="\n\n" + message,
                author=self.sender
            )

    def createConversation(self, friendly_name):
        self.client.conversations \
            .conversations \
            .create(friendly_name=friendly_name)

    def deleteConversation(self, conversation):
        self.client.conversations.conversations(conversation.sid) \
            .delete()

    def getCarrierByNumber(self, number):
        return self.client.lookups \
            .v1 \
            .phone_numbers(number) \
            .fetch(type=["carrier"]).carrier["name"]
