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
df= pd.read_sql_query("SELECT geometry FROM nasa_data;",con=dBCon)
print('read')
df['temp'] = df['geometry'].str.split('(').str[1]
print("REMP")
df['lon'] = df['temp'].str.split(' ').str[0].replace("(","")
print('Lon')
df['lat'] = df['temp'].str.split(' ').str[1]
df['lat'] = df ['lat'].str.replace(")","")
print("Lat")
del df['temp']
del df['geometry']
df.to_csv('help.csv')
print('saved to csv')
df.to_sql('lat_lon', con=dBCon)
print('Fill table')
df2 = pd.read_sql_query("SELECT * from lat_lon LIMIT 5;",con=dBCon)
print(df2)
closeDB(dBCon)
