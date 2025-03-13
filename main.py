import psycopg2
import pyfirmata
import time

## Setup for Arduino
port = 'COM3'
board = pyfirmata.Arduino(port)

buttonPin = board.get_pin('a:0:i')

it = pyfirmata.util.Iterator(board)
it.start()

## Arduino loop
while True:
    buttonPinInput = buttonPin.read()
    print(buttonPinInput)
    time.sleep(1)

## Setup for database
connection = psycopg2.connect(database="score_system", user="postgres", password="password", host="127.0.0.1", port=5432)

cursor = connection.cursor()

cursor.execute("INSERT INTO public.score (tid, stilling, team) VALUES ('77', '240', 'team4');")

connection.commit()

record = cursor.fetchall()
print("Data from Database:- ", record)
print(len(record), "rows returned")

connection.close()