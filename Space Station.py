#!/bin/python3

import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print("People in Space ", result['number'])
people = result['people']

for p in people:
  print(p['name'], 'in', p['craft'])
  
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
latitude = float(location['latitude'])
longitude = float(location['longitude'])
print('Latitude: ', latitude)
print('Longitude: ', longitude)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(longitude, latitude)

# When Does ISS next pass over me?
#london
lat = 51.5072
lon = 0.1275

# Space Center, Houston
#lat = 29.5502
#lon = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print result
over = result['response'][1]['risetime']
location.write(time.ctime(over))
