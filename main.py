
import requests
import os
from twilio.rest import Client
sid = ""
token = ""
fromNo = +15076525665
lat = 12.774270
lon = 79.474602
Api = ""

connection = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={Api}")
connection.raise_for_status()
rain = False
info = ""
abt_info =""
for i in range(0,8):
    id = connection.json()['list'][i]['weather'][0]['id']
    print(id)
    if(id>=500 and id<=530):
        rain = True
        abt_info = connection.json()['list'][i]['weather'][0]['main']
        if(abt_info == 'Clouds'):
            info = "Domesan Here:  Cloudy climate is expected... Happy day ahead"
        else:
            info = f"Domesan Here:  {abt_info} is expected🌧️.. Take your Umbrella ☔ "
        break
    elif(id>=300 and id<=331):
        abt_info = connection.json()['list'][i]['weather'][0]['description']
        if (abt_info == 'Clouds'):
            info = "Domesan Here:  Cloudy climate is expected... Happy day ahead"
        else:
            info =f"Domesan Here:  {abt_info} is Expected🌧️... Don't forget to take your Umbrella ☔ "
        rain = True
        break
    elif(id>=200 and id<=232):
        abt_info = connection.json()['list'][i]['weather'][0]['description']
        if (abt_info == 'Clouds'):
            info = "Domesan Here:  Cloudy climate is expected... Happy day ahead"
        else:
            info = f"Domesan Here:  {abt_info} is Expected⛈... Don't forget to take your Umbrella☔ "
        rain = True
        break

if(not rain):
    info = "Domesan Here:  Sunny climate🌞... Don't forget to carry water with you🥤"
numbers = ["no1", "no2","no3"]
print(info)
client = Client(sid,token)
# for i in range(len(numbers)):
#     message = client.messages.create(
#         body= info,
#         from_= fromNo,
#         to= numbers[i]
#
#     )