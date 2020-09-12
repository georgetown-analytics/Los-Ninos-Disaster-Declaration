from flask import Flask
import folium
import pickle
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def index():
	model = pickle.load(open('finalized_model.sav','rb'))
	data =pd.read_csv('Data4Bill.csv')
	data = data[data['Time']==18190]	#10/21/19
#	data = data[data['Time']==15919]	#8/2/13
	data = data[['Month','latitude','longitude','day_1_Precip','day_2_Precip', 'day_3_Precip', 'day_4_Precip', 'day_5_Precip', 'day_6_Precip', 'day_7_Precip']]
	data['predict_disaster']=model.predict(data)
	start_coords = (28, -82)
	folium_map = folium.Map(location = start_coords, zoom_start=7)
	for index, row, in data.iterrows():
		if row['predict_disaster']==1:
			folium.Marker(location=(row['latitude'],row['longitude']), popup=str(row['latitude'])+', '+str(row['longitude'])).add_to(folium_map)
	return folium_map._repr_html_()

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
