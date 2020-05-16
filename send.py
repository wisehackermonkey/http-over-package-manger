# http over package mananger
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200516


import json

import sys
# custom run command class
from run_command import Command
class Send():
    def __init__(self):
        pass
    def send_text_npm(self):
        Command("npm version patch").run(relative_path="http-over-packagemaner-v1")
        Command("npm publish").run(relative_path="http-over-packagemaner-v1")


    def write_to_disk(self,messages):
        with open("./http-over-packagemaner-v1/data.json", "w") as json_messages:
            json_messages.write(json.dumps(messages))


    def load_from_disk(self):
        messages = json.loads(open("./http-over-packagemaner-v1/data.json").read())
        return messages

    def formater(self, func, param1=None, text=""):
        print(f"{text} ", end="")

        if param1 == None:

            result = func(self)
            print(" [✔]")

            return result

        result = func(self,param1)
        print(" [✔]")
        return result
    def message(self,text):
          # messages schema v1
        # messages = {"john":[],"gale":[]}

        # read the current messages from the data file
        messages = Send().formater(Send.load_from_disk, text="loading messages")


        print("setting message to correct format", end="")
        # add my own message
        messages["john"].append(text)
        print(" [✔]")

        # write message to json package data file    
        Send().formater(Send.write_to_disk, messages, text="saving message to disk")


        Send().formater(Send.send_text_npm, text="Sending message over npm package manager")

if __name__ == "__main__":
    text = sys.argv[-1]
    Send().message(text)
    print(sys.argv)

    # TODO - push changes to npm
    # x cd http-over-packagemaner-v1
    # x npm version patch
    # x npm publish