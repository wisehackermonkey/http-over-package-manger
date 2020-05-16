# http-over-package-manger
### creating http over package manager, a fun experiment



```
send 

    x sub package
    add file to json
        json = {[send: "", user id], [recieve:"", user id]}

    autologin
        npm, python, gem's
        -  npm version patch 
        - commit
        - push

receive
    npm install 
    npm run 

UI
    text box send

    print recieve
```

# send steps
```
- npm login
- 
- >write to json
- cd http-over-packagemaner-v1
- npm version patch 
- npm publish
```

# receive steps
## init
- npm install -i  http-over-packagemaner-v1
## continues
- cd test
- npm update http-over-packagemaner-v1
- ipython 
    > import json
    > json.loads(open("./node_modules/http-over-packagemaner-v1/data.json").read())["username"][-1]



# message schema

- userid int
- username string
- data datestring
- message(s) = array
-     message date
-     message id


# how to use send.py
```
python send.py "<message to be sent>"
EX
python send.py "Friends applaud, the comedy is finished"
```

# how to use receive.py
```
python receive.py "<message to be sent>"
```

# how to use main app
```
>python cli.py

to quit type exit, quit, or q

type some text then hit "enter"

the app will update a npm package named http-over-packagemaner-v1
with the text you just typed

upload the updated npm package

once uploaded, update a local version of the package, and display the text
```
# todo
- polling problem
        x what about using npm update?
- ~~finish semi-automated receive~~
- ~~automate npm * commands~~
- x make script use argv
- two way
-   make script take dynamic user input
-  x display last message send from other user
- add user support