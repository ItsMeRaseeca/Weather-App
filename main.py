import tkinter as tk
import requests
from PIL import Image, ImageTk

#make window using root, and apply toolkit using Tk
root = tk.Tk()

#window title-
root.title("Weather App")

#set window size (geometry)-
root.geometry("600x500")
root.resizable(False, False) #user cannot resize the window.

#API Key:- c6248628ffbf4b6491d1aeb1583e5ff2
#API URL:- https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        feels_like = weather['main']['feels_like']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        pressure = weather['main']['pressure']

        final_string=f"""City: {city} \nCondition: {condition} \nTemperature: {temp}°F \nFeels Like: {feels_like}°F \nHumidity: {humidity}% \nWind Speed: {wind_speed} mph \nPressure: {pressure} hPa"""
    except:
        final_string='There was problem retrieving information'
    return final_string

def get_weather(city):
    weather_key='c6248628ffbf4b6491d1aeb1583e5ff2'
    weather_url='https://api.openweathermap.org/data/2.5/weather'
    params={'appid':weather_key, 'q':city, 'units':'imperial'}
    response=requests.get(weather_url, params)      #create response where the responses will be stored of the requests sent to server
    weather=response.json()

    """print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])"""

    result['text']=format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size=int(frame_two.winfo_height()*0.25)
    # Open and resize image before converting to PhotoImage
    img = Image.open('./img/' + icon + '.png').resize((size, size))
    img = ImageTk.PhotoImage(img)  # Convert after resizing
    weather_icon.delete('all')
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image=img

img = Image.open('./img/weather-bg.jpg')
img = img.resize((600, 500))
img_photo = ImageTk.PhotoImage(img)

bg_label = tk.Label(root, image = img_photo)
bg_label.place(x = 0, y = 0, width = 600, height = 500)

heading_title = tk.Label(bg_label, text="Enter a city name", fg='navy', bg='#8DD3E4', font=('Segoe UI', 18, 'bold'))
heading_title.place(relx=0.5, rely=0.06, anchor='center')

#make a frame
frame_one = tk.Frame(bg_label, bg="#000435", bd = 5)
frame_one.place(x = 80, y = 60, width=450, height=50)

#make entry field-
text_box = tk.Entry(frame_one, font = ('Garamond', 23), width = 19)
text_box.grid(row=0, column=0, sticky = 'w')

btn = tk.Button(frame_one, text="Get Weather", fg='purple', font=('Segoe UI', 14, 'bold'),command=lambda:get_weather(text_box.get()))
btn.grid(row=0, column=1, padx=25)

frame_two = tk.Frame(bg_label, bg="#000435", bd = 5)
frame_two.place(x = 80, y = 130, width=450, height=300)

result = tk.Label(frame_two, font=('Century Gothic', 16), bg='white', justify='left', anchor='nw', padx=15, pady=10)
result.place(relwidth=1, relheight=1)   #relation of width and height w.r.t to parent frame (i.e., frame_two)

weather_icon = tk.Canvas(result, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)   #relwidth/relheight = 1 means 100% of the frame nad 0.5 means 50% of it

root.mainloop()
