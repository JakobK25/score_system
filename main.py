import psycopg2
import pyfirmata
import time

connection = psycopg2.connect(database="score_system", user="postgres", password="password", host="127.0.0.1", port=5432)

cursor = connection.cursor()

cursor.execute("INSERT INTO public.score (tid, stilling, team) VALUES ('77', '240', 'team4');")

connection.commit()

cursor.execute("SELECT * FROM score;")
record = cursor.fetchall()
print("Data from Database:- ", record)
print(len(record), "rows returned")

connection.close()