import  socket
import ast
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 1234))

s.listen(5)

userObj = {}

while True:
    clienSocket, address = s.accept()
    print("Connection from {address} has been etablished!",address, clienSocket)
    
    clientMsg = ast.literal_eval(clienSocket.recv(1024).decode("utf-8"))
    # userObj[email] = clienSocket
    #print(clientMsg, type(clientMsg))
    if(clientMsg["clientType"] == "raspiClient"):
        userObj[clientMsg["email"]] = clienSocket
    elif(clientMsg["clientType"] == "serverClient"):
        if clientMsg["recipient"] in userObj:
            userObj[clientMsg["recipient"]].send(bytes(clientMsg["msg"], "utf=8"))
            response = {
                "status": 200,
                "message": "success"
            }
            clienSocket.send(bytes(json.dumps(response), "utf=8"))
        else:
            response = {
                "status": 404,
                "message": "User No Found"
            }
            clienSocket.send(bytes(json.dumps(response), "utf=8"))

