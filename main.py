import psycopg2
import pyfirmata
import time
from datetime import datetime
import random

## Setup for Arduino
#port = 'COM3'
#board = pyfirmata.Arduino(port)
#button = board.get_pin('d:2:i')

#it = pyfirmata.util.Iterator(board)
#it.start()

## Setup for database
connection = psycopg2.connect(database="scoredb", user="postgres", password="postgres", host="127.0.0.1", port=5432)
db = connection.cursor()

## Setup time
startTime = datetime.now()
print("Start running at: ", startTime)

## Generate random data and time

for i in range(10):
    score = random.randint(1, 5)
    timestamp = datetime.now()

    db.execute("INSERT INTO score_system.scoretb (time, score) VALUES (%s, %s)", (timestamp, score))
    connection.commit()
    
    delay = random.randint(1, 5)
    time.sleep(delay)

## Read data from database
db.execute("SELECT * FROM score_system.scoretb ORDER BY time DESC LIMIT 10")
record = db.fetchall()
print("Data from Database:- ", record)
print(len(record), "rows returned")

connection.close()