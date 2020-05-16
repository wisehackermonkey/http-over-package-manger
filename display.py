# receive text from package data json
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200516

import itertools
import json 
from run_command import Command
# get newest messages stored in package data.json

class Display():
    def messages(self):
        Command("npm update http-over-packagemaner-v1").run(relative_path="test")
        with open("./test/node_modules/http-over-packagemaner-v1/data.json") as file:
            messages = json.loads(file.read())

            zipped = itertools.zip_longest(messages["john"][-3:],messages["gale"][-3:])

            print(f"{'--john--':<50}---gale---")
            for user1,user2 in zipped:
                user1 = "" if user1 == None else user1
                user2 = "" if user2 == None else user2
                print(f"#{user1:<50}##{user2}#")
if __name__ == "__main__":
    Display().messages()