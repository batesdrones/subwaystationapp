import csv
import pandas as pd
from geopy.geocoders import Nominatim
import geopy.distance


loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("148 Nelson St, Brooklyn, NY")

starting_point = (getLoc.latitude, getLoc.longitude)

radius_question = input("How far are you willing to go? (in miles): ")
radius = int(radius_question)

####alternative method to create a new df column named Distance.
# Then filter df to sample only rows with values below radius input

def calculateDistance():
    global df
    global distance
    df = pd.read_csv('subwaystation_list.csv')
    df = df.sample()
    ending_point = df['Coordinates']
    distance = geopy.distance.distance(starting_point, ending_point).mi
    if distance > radius:
        calculateDistance()
    else:
        pass
    return df

calculateDistance()
print (df)
print(distance)



# distance = geopy.distance.distance(starting_point, ending_point).mi
#
#
# calculateDistance()

# print("Ending point is:", ending_point)
# print("Distance(in miles) is: ", distance)


# new_spot = df.sample()
#
# print("Your next stop is......", new_spot)