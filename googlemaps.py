import pandas as pd
import json
import os
from rich.console import Console

full_path = os.getcwd()

path_db = os.path.join(full_path,'db')
filename_db = os.path.join(path_db,'cities.csv')


console = Console()



class Cities():

    LAT     = "51.177891"
    LON     = "4.835790"

    search = 'herent'

   
    

    def search_city(self,city):
        
 #       console.print(self.df_cities)       
        self.df_cities_search = self.df_cities[self.df_cities.citysearch.str.contains(city,na=False,case=False)]
 #       console.print(self.df_cities_search)       
        self.city_list = self.df_cities_search.city.tolist()
 #       console.print(self.city_list)

        if len(self.df_cities_search['city']) > 0:
            self.city = self.df_cities_search['city'].iloc[0]
            self.lat = self.df_cities_search['lat'].iloc[0]
            self.lon = self.df_cities_search['lon'].iloc[0]
            



    def __init__(self):
                
        self.df_cities = pd.read_csv(filename_db,sep=';',encoding='latin1')
        self.search_city(self.search)



       #self.weather = Weather(**resp_json)

    
if __name__ == "__main__":

    my_maps = Cities()

#    print(my_weather.weather.lat)






