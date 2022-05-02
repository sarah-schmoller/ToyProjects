import helpers.generate_helper
import helpers.send_helper
import yaml
config = yaml.safe_load(open("./config/launch_config.yaml"))

def main():
    send_type = config["launch_config"]["send_type"]
    receiver_numbers = config["launch_config"]["receiver_numbers"]

    generate_helper = helpers.generate_helper.GenerateHelpers()
    send_helper = helpers.send_helper.SendHelpers()

    generated_messages = generate_helper.generateMessages()

    parsed_message = generate_helper.parseMessages(generated_messages)

    if send_type == "email_gateway":
        send_helper.sendViaEmailGateway(receiver_numbers, parsed_message)
    elif send_type == "twilio":
        send_helper.sendViaTwilio(receiver_numbers, parsed_message)

if __name__ == "__main__":
    main()
