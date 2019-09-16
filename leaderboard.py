import socket
import time
import random
import zmq
import json
import pandas as pd
import sys
DEBUG = True


#***this function can be used for broadcasting for more than one client *****

# wss = [] # Should be globally scoped
#
# def handleConnected(self):
#     print (self.address, 'connected')
#     if self not in wss:
#         wss.append(self)
# Then, when you get a new request, send the message out to each of the clients stored:
#
# def handleMessage(self):
#     if self.data is None:
#         self.data = ''
#
#     for ws in wss:
#         ws.sendMessage(str(self.data))
# Add this to remove if a client disconnects so the array is not full of not connected people
#
# def handleClose(self):
#     wss.remove(self)


class Player:
    def __init__(self,name,score):
        self.name=name
        self.score=score






def result_collector():

    collecter_data =[]
    context = zmq.Context()
    #receive work
    results_receiver = context.socket(zmq.PULL)

    results_receiver.bind("tcp://127.0.0.1:5556")

    # send work
    result_sender = context.socket(zmq.PUSH)
    result_sender.connect("tcp://127.0.0.1:1234")

    for r in range(0,1000):
        re = results_receiver.recv_json()
        player=Player(re['name'], re['score'])
        for item in collecter_data:
            if item.name == player.name:
                player.score = item.score+player.score
                collecter_data.remove(item)
        collecter_data.append(player)
        collecter_data.sort(key=lambda x: x.score,reverse=True)
        first_ten = collecter_data[0:10]

        result=[]
        print("_____________**last updated top 10 players**_____________ :")
        for y in first_ten:

            re={"name":y.name,"score":y.score}
            result.append(re)


        df = pd.DataFrame(result, columns=['name', 'score'])
        print(df)
        r=df.to_json()

        result_sender.send_json(r)







result_collector()
