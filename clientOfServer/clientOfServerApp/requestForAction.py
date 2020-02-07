from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

import  socket
import json
import ast

@csrf_exempt
@api_view(['POST'])
def requestForActionDef(request):
    recipient = request.data["recipient"]
    action = request.data["action"]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((socket.gethostname(), 1234))
    dataObj = {
        "clientType": "serverClient",
        "recipient": recipient,
        "msg": action
    }
    s.send(bytes(json.dumps(dataObj), "utf-8"))

    msg = ast.literal_eval(s.recv(1024).decode("utf-8"))

    return Response(msg)