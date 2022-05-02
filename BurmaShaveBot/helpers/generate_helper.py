import gpt_2_simple as gpt2

class GenerateHelpers:
    def __init__(self):
        self.sess = gpt2.start_tf_sess()

    def generateMessages(self):
        gpt2.load_gpt2(self.sess, run_name='run')
        results = gpt2.generate(self.sess, run_name='run', return_as_list=True, include_prefix=True)[0]

        return results

    def parseMessages(self, messages):
        split_messages = messages.split("<|endoftext|>\n<|startoftext|>", -1)[3:]
        for message in split_messages:
            discard_flag = False
            lines = message.split('\n', -1)
            lines_as_keys = {}

            # If the poem has more than 7 lines, discard
            if message.count('\n') >= 8:
                discard_flag = True

            # If the last line isn't "Burma-Shave", discard
            if not lines[len(lines)-1] == "Burma-Shave":
                discard_flag = True

            for line in lines:

                # Check whether the line has a length greater than 50 characters; if so, discard
                if len(line) > 50:
                    discard_flag = True

                # Check whether the line has been duplicated elsewhere in the poem; if so, discard
                try:
                    lines_as_keys[line] += 1
                    discard_flag = True
                except:
                    lines_as_keys[line] = 1

            # Clear the dictionary
            lines_as_keys.clear()

            # Use the message if discard flag is not set
            if not discard_flag:
                return message

        return split_messages[0]

