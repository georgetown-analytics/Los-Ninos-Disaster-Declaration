import pandas as pd
import numpy as np
import psycopg2

pgHost = 'localhost'
pgUn = 'bill'
pgPw = 'password'
pgDb = 'victoria'

def connectDB():
	dBCon = psycopg2.connect(host = pgHost, user = pgUn, password = pgPw, database=pgDb)
	cursor = dBCon.cursor()
	print("DB Connected")
	return dBCon, cursor

def closeDB(dBCon):
	dBCon.close()
	print("DB Close")

dBCon, cursor = connectDB()
disaster = pd.read_csv('DisasterDeclarationsSummaries2.csv')
print(list(disaster))
disaster.to_sql('disaster', con = dBCon)
closeDB(dBCon)
