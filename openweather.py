import requests
import json
from rich.console import Console
from datetime import datetime
from collections.abc import Mapping
from enum import Enum

console = Console()

class Units_Temp(Enum):
    KELVIN = 'K'
    CELSIUS = '°C'

class Weather_summary():
    def set_key(self, key, kwargs):
        if key in kwargs:
            return(kwargs[key])
        else:
            return(None)



    def __init__(self,**kwargs):

        self.main = self.set_key('main',kwargs)            
        self.description = self.set_key('description',kwargs)            
        self.icon = self.set_key('icon',kwargs)            


class Temp():
    def set_key(self, key, kwargs):
        if key in kwargs:
            return(kwargs[key])
        else:
            return(None)



    def __init__(self,**kwargs):

        self.day = self.set_key('day',kwargs)            
        self.min = self.set_key('min',kwargs)            
        self.max = self.set_key('max',kwargs)            
        self.night = self.set_key('night',kwargs)            
        self.eve = self.set_key('eve',kwargs)            
        self.morn = self.set_key('morn',kwargs)            

class Weather_current():
    def set_key(self, key, kwargs):
        if key in kwargs:
            return(kwargs[key])
        else:
            return(None)


    def __init__(self,**kwargs):
        
        self.dt = self.set_key('dt',kwargs)            
        self.sunrise = self.set_key('sunrise',kwargs)            
        self.temp = self.set_key('temp',kwargs)
        self.sunset = self.set_key('sunset',kwargs)            
        self.feels_like = self.set_key('feels_like',kwargs)            
        self.pressure = self.set_key('pressure',kwargs)            
        self.humidity = self.set_key('humidity',kwargs)            
        self.dew_point = self.set_key('dew_point',kwargs)            
        self.uvi = self.set_key('uvi',kwargs)            
        self.clouds = self.set_key('clouds',kwargs)            
        self.visibility = self.set_key('visibility',kwargs)            
        self.wind_speed = self.set_key('wind_speed',kwargs)            
        self.wind_deg = self.set_key('wind_deg',kwargs)            
        self.wind_gust = self.set_key('wind_gust',kwargs)            
        self.pop = self.set_key('pop',kwargs)            
        self.rain = self.set_key('rain',kwargs)            
        self.weather = kwargs['weather'][0]

        self.datetime = datetime.fromtimestamp(self.dt)
        self.date = self.datetime.strftime('%d-%m-%Y')
        self.time = self.datetime.strftime('%H:%M')

        if isinstance(self.temp, Mapping):
            self.temp = Temp(**self.temp)

        if isinstance(self.feels_like, Mapping):
            self.feels_like = Temp(**self.feels_like)

        if isinstance(self.weather, Mapping):
            self.weather = Weather_summary(**self.weather)
            self.weather_description = self.weather.description
            self.weather_icon = self.weather.icon
            self.weather_main = self.weather.main


    def temp_kelvin_to_degrees(self,temp):
        if temp:    
            return(temp-273.15)
        else:
            return(None)

class Weather():

    def __init__(self,lat,lon,timezone,timezone_offset,current,hourly,daily,**kwargs):
    

        self.lat = lat
        self.lon = lon
        self.timezone = timezone

        self.current = Weather_current(**current)
        self.hourly = []
        for obj in hourly:
            self.hourly.append(Weather_current(**obj))
        self.daily = []
        for obj in daily:
            self.daily.append(Weather_current(**obj))


        self.hourly_forcasts = len(hourly)
        self.daily_forcasts = len(daily)
       



class OpenWeather():

    API_KEY = "26b905fee7c99b97779736b9df95fecb"
    LAT     = "51.177891"
    LON     = "4.835790"
    EXCLUDE = "minutely"


    '''
    https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
    '''

    



    def update_weather(self):

        url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(self.LAT) + "&exclude=" + self.EXCLUDE + "&lon=" + str(self.LON) + "&appid=" + self.API_KEY
        
        print(url)

        resp = requests.get(url)
        resp_json = resp.json()

        self.weather = Weather(**resp_json)
#        console.print(resp_json)

#        return(resp_json)



    def __init__(self):
        pass
#        resp_json = self.get_weather()
#        self.weather = Weather(**resp_json)

    
if __name__ == "__main__":

    my_weather = OpenWeather()
    my_weather.update_weather()
    print(my_weather.weather.lat)



    print(my_weather.weather.current.sunrise)
    print(my_weather.weather.current.temp)
    print(my_weather.weather.current.temp)


    console.print(my_weather.weather.current.date)
    console.print(my_weather.weather.current.time)

    console.print(my_weather.weather.current.weather.main)
    console.print(my_weather.weather.current.weather.description)
    console.print(my_weather.weather.current.weather.icon)

    console.print(my_weather.weather.hourly[1].time)
    console.print(my_weather.weather.hourly[1].temp)


    console.print(my_weather.weather.hourly[2].time)
    console.print(my_weather.weather.hourly[2].temp)
    console.print(my_weather.weather.hourly[2].sunrise)
    console.print(my_weather.weather.hourly_forcasts)




    print(my_weather.weather.hourly[1].rain)


    console.print(my_weather.weather.daily_forcasts)

    print(my_weather.weather.daily[1].rain)
    print(my_weather.weather.daily[1].temp)
    print(my_weather.weather.daily[1].temp.min)
    print(my_weather.weather.daily[1].temp.max)



