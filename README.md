Code Challenge: Scoreboard
==========================

A simple network application using ZeroMQ to keep a live leaderboard 
of a multiplayer video game.


**Getting Started**
-

-To run the code on your local machine:

1-clone the project : open the terminal and paste the following command:
    
    https://gitlab.com/SalwaAhmed/leaderboard.git

2-run this command to install the requirements :

    pip3 install requirements.txt  
    
3-open three tabs in the terminal(so you can see the results separately ) and type consecutively :
  terminal  1:  
    python3   game.py   5000
  terminal  2:  
    python3   client.py
  terminal  3:
    python3   leaderboard.py    


4-To terminate press ctrl+C



**Prerequisites**
-

1-[python3](https://docs.python.org/)
2-[pandas](https://pandas.pydata.org/pandas-docs/stable/)
3-[pyzmq](https://pyzmq.readthedocs.io/en/latest/)
4-[pytz](http://pytz.sourceforge.net/)
5-[setuptools](https://setuptools.readthedocs.io/en/latest/)
6-[NumPy](https://numpy.org/)
7-[JSON](https://docs.python.org/3/library/json.html)




**outputs**
-

At game.py:
-
-the output will be like this :

{'score': 20, 'name': 'Lickitung}


At the leaderboard.py:
-

_____________**last updated top 10 players**_____________ :
        name  score
0   Magikarp     65
1     Cubone     60
2     Meowth     55
3   Cloyster     40
4    Machamp     35
5   Nidorina     35
6     Weedle     35
7    Starmie     35
8    Venonat     35
9  Hitmonlee     30

At the client.py:
-

_____________**last updated top 10 players**_____________ :
        name  score
0   Magikarp     65
1     Cubone     60
2     Meowth     55
3   Cloyster     40
4    Machamp     35
5   Nidorina     35
6     Weedle     35
7    Starmie     35
8    Venonat     35
9  Hitmonlee     30

 
which represent the current player that is sent by the (producer) to the (consumer)
game.py--> client.py 

Then forward by the client.py to the (resultcollector) Leaderboard.py which keep tracking
for the players and get the submission of their scores ,getting the top 10 players , sending it back 
to the client.py to view it.

**this cycle is built using**:
 
 [PULL Socket](https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pushpull.html)
 [PUSH Socket](https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pushpull.html) 

-you will see a live updated list  players scores .




