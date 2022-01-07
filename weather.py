import openweather as ow
import googlemaps as gm 
import PySimpleGUI as sg      
import os
from rich.console import Console


LAYOUT = True

console = Console()
city = gm.Cities()


my_weather = ow.OpenWeather()

#my_weather.LAT="123"
my_weather.update_weather()

temp = my_weather.weather.current.temp - 273
weather_description = my_weather.weather.current.weather_description
weather_main = my_weather.weather.current.weather_main
weather_icon = my_weather.weather.current.weather_icon


console.print(my_weather.weather.hourly_forcasts)
for i in range(24):
    console.print(my_weather.weather.hourly[i].time)
    console.print(round(my_weather.weather.hourly[i].temp-273))


'''

temp = 100
weather_description = 'scattered clouds'
weather_main = 'Clouds'
weather_icon = '03d'
'''

console.print(temp)
console.print(weather_main)
console.print(weather_icon)
console.print(weather_description)

full_path = os.getcwd()

path_icons = os.path.join(full_path,'icons')
filename_icon = os.path.join(path_icons,weather_icon + '@2x.png')

console.print(filename_icon)

def layout():
    
    choices = ['11','12','135','146','1597','kl','kla','klaaa']
    IGNORE_CASE = True
    '''
    START LAYOUT
    '''

    WINDOW_WIDTH = 160
    WINDOW_HEIGHT = 350
    ICON_SIZE = 100
    

    TEXT_WIDTH = 30
    TEXT_HEIGHT = 1 
    
    ALPHA = 0.8
    IMAGE = 'test.jpg'

    right_click_menu = ['&Right', ['E&xit','Test']]
    

    layout = [[sg.Image(filename_icon,size=(ICON_SIZE,ICON_SIZE),key='Icon')],
        [sg.Text(str(round(temp)) + '°C',justification='c',size=(TEXT_WIDTH,TEXT_HEIGHT),key='txtTemp',background_color='red')],      
        [sg.Text(weather_main,justification='c',size=(TEXT_WIDTH,TEXT_HEIGHT),key='txtMain')],
        [sg.Text(weather_description,justification='c',size=(TEXT_WIDTH,TEXT_HEIGHT),key='txtDescription')],      
        ###autocomplete
        [sg.Input(size=(TEXT_WIDTH, TEXT_HEIGHT),justification='c', enable_events=True, key='-IN-')],
        [sg.pin(sg.Col([[sg.Listbox(values=['test','2'],size=(TEXT_WIDTH, 5), enable_events=True, key='-BOX-', select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]], key='-BOX-CONTAINER-', pad=(0, 0), visible=False ))],
        ###autocomplete
        [sg.Exit(key='Exit')]]

    layout2 = [[sg.Image(filename_icon,size=(ICON_SIZE,ICON_SIZE),key='Icon')],
        [sg.Text(str(round(temp)) + '°C',justification='c' ,size=(TEXT_WIDTH,TEXT_HEIGHT),key='txtTemp',background_color='purple')]]      
   

    layout_window = [[sg.Column(layout, element_justification='c'),sg.Column(layout2, element_justification='c')]]



    window = sg.Window('My weather app', layout_window, size=(WINDOW_WIDTH*4,WINDOW_HEIGHT),location=(100,100),
        alpha_channel=ALPHA,
        grab_anywhere=True,
        no_titlebar=True,
        right_click_menu=right_click_menu)    




    list_element:sg.Listbox = window.Element('-BOX-')           # store listbox element for easier access and to get to docstrings
    prediction_list, input_text, sel_item = [], "", 0

    while True:  
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Test':
            print('test')


        ###autocomplete
        if event.startswith('Escape'):
            window['-IN-'].update('')
            window['-BOX-CONTAINER-'].update(visible=False)

        if event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        if event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) - 1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        if event == '\r':
            if len(values['-BOX-']) > 0:
                window['-IN-'].update(value=values['-BOX-'])
                window['-BOX-CONTAINER-'].update(visible=False)



        if event == '-IN-':
            text = values['-IN-'] if not IGNORE_CASE else values['-IN-'].lower()
            if text == input_text:
                continue
            else:
                input_text = text
            prediction_list = []
            if text:
                if IGNORE_CASE:
                    prediction_list = [item for item in choices if item.lower().startswith(text)]
                else:
                    prediction_list = [item for item in choices if item.startswith(text)]
                search = city.search_city(text)
                prediction_list = city.city_list


            list_element.update(values=prediction_list)
            sel_item = 0
            list_element.update(set_to_index=sel_item)

            if len(prediction_list) > 0:
                window['-BOX-CONTAINER-'].update(visible=True)
            else:
                window['-BOX-CONTAINER-'].update(visible=False)
        if event == '-BOX-':
            window['-IN-'].update(value=values['-BOX-'])
            window['-BOX-CONTAINER-'].update(visible=False)
             
            search = city.search_city(values['-BOX-'][0])
            console.print(city.city)
            console.print(city.lat)
            console.print(city.lon)
                            
            my_weather.LAT=city.lat
            my_weather.LON=city.lon

            my_weather.update_weather()

            my_temp = str(round(my_weather.weather.current.temp - 273))
            

            my_weather_description = my_weather.weather.current.weather_description
            my_weather_main = my_weather.weather.current.weather_main
            my_weather_icon = my_weather.weather.current.weather_icon

            my_filename_icon = os.path.join(path_icons,my_weather_icon + '@2x.png')

            window['txtTemp'].update(my_temp)
            window['txtMain'].update(my_weather_main)
            window['txtDescription'].update(my_weather_description)
            window['Icon'].update(my_filename_icon)
        ###autocomplete

    window.close()

if LAYOUT == True:
    layout()

