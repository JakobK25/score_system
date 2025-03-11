import psycopg2
import pyfirmata
import time


## Setup for Arduino
port = 'COM3'
board = pyfirmata.Arduino(port)

button = board.get_pin('d:2:i')

it = pyfirmata.util.Iterator(board)
it.start()

## Setup for database
connection = psycopg2.connect(database="score_system", user="postgres", password="password", host="127.0.0.1", port=5432)

cursor = connection.cursor()

cursor.execute("INSERT INTO public.score (tid, stilling, team) VALUES ('77', '240', 'team4');")

connection.commit()

cursor.execute("SELECT * FROM score;")
record = cursor.fetchall()
print("Data from Database:- ", record)
print(len(record), "rows returned")

connection.close()