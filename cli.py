# interactive console for sending messages
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200516
from send import Send
from display import Display

try:
    text = ""
    print("Type <quit> or <exit> to close program")
    while text != "quit":
        Display().messages()
        text = input("--> ")
        if text == "":
            continue
        if text in ["quit","exit","q",""]:
            break
        Send().message(text)

        
except KeyboardInterrupt as error:
    print("Program closed")
    exit()