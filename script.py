import csv
import time
import pandas as pd
import urllib.request
import geocoder
import geopy.distance
import gmplot
import folium
import webbrowser

###get location of starting point
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

ip = geocoder.ip(f'{external_ip}')
starting_point = ip.latlng


"""
ask the user for length willing to travel. Create the circle radius. Test.
"""
#todo: raise exceptions if not an integer
radius_question = input("How many miles are you willing to travel: ")
radius = int(radius_question)

"""
alternative method to create a new df column named Distance- then
filter df to sample only rows with values below radius input
"""

def filterDistance():
    global df
    global distance
    global ending_point
    global destination
    global line
    df = pd.read_csv('subwaystation_list.csv')
    df = df.sample()
    ending_point = df['Coordinates']
    destination = df['NAME']
    line = df['LINE']
    distance = geopy.distance.distance(starting_point, ending_point).mi
    if distance > radius:
        filterDistance()
    else:
        pass
    return df

filterDistance()

#todo: convert distance to less decimals for display
"""
removes object number from variables with item method
"""
ending_point = ending_point.item()
destination = destination.item()
line = line.item()

print(f"Your next stop is: {destination} on the {line} line.")
print(f"It is {distance} miles away.")

#convert coordinates to float to use for mapping
def convert_float(inp):
    splitted_data = inp.split(",")
    return float(splitted_data[-2]), float(splitted_data[-1])

lat, long = convert_float(ending_point)
coords = [lat, long]

def generate_map():
    my_map = folium.Map(location = coords, zoom_start=10)
    folium.Marker(coords, popup = f"Your destination: {destination} station. Have fun!").add_to(my_map)
    my_map.save('map.html')

generate_map()
time.sleep(5)
webbrowser.open('./map.html')
