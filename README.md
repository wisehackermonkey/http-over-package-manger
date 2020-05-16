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


# todo
- polling problem
        what about using npm update?
- 