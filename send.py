# http over package mananger
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200516


import json

import sys

# text = sys.argv[2]
text = "hi gale"

# messages schema v1
# messages = {"john":[],"gale":[]}

# read the current messages from the data file
messages = json.loads(open("./http-over-packagemaner-v1/data.json").read())


# add my own message
messages["john"].append(text) 


# write message to json package data file
with open("./http-over-packagemaner-v1/data.json","w") as json_messages:
    json_messages.write(json.dumps(messages))


#TODO - push changes to npm
# cd http-over-packagemaner-v1
# npm version patch 
# npm publish