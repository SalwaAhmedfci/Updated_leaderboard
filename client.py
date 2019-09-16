import time
import zmq
import random
import json
import pandas as pd


def consumer():

    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5000")

    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5556")

    #recieve results
    results_receiver1 = context.socket(zmq.PULL)
    results_receiver1.bind("tcp://127.0.0.1:1234")
    collecter_data =[]
    while True:
        work = consumer_receiver.recv_json()

        result = {"score": work['score'], "name":work['name']}


        consumer_sender.send_json(result)
        work1 = results_receiver1.recv_json()


        print("_____________**last updated top 10 players**_____________ :")

        df=pd.read_json(work1)
        print(df)


consumer()

