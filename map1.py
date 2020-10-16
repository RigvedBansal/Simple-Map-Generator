import folium
import os
mumbai = [19.0760,72.8777]
nyc = [40.7128, -74.0060]
london = [51.5074,-0.1278]
dubai =[25.2048,55.2708]
while location1 not in ["Mumbai","New York","London","Dubai"]:
	location1=input("Enter a location: ")
		if location1 =="Mumbai":
			m = folium.Map(location=mumbai)
		elif location1 == "New York":
			m = folium.Map(location=nyc)
		elif location1 == "London":
			m = folium.Map(location=london)
		elif location1 == "Dubai":
			m = folium.Map(location=dubai)
m.save('index.html')


