"""
# Michael Hoyle
# ITN160-4C1
# Assignment 6: Agriculture Lab
# 3/9/2022

Create app to monitor times in the day to spread fertilizer onto farm.
"""

# Resources used for assignment:
# https://www.youtube.com/watch?v=NIWwJbo-9_8
# Class material from D2L
# https://lawsie.github.io/guizero/app/
# https://mycourses.dtcc.edu/d2l/le/content/86265/viewContent/3949866/View

# Import for time used in app
import time
from guizero import *

# Global constants
APP_WIDTH = 500
APP_HEIGHT = 500

# Global variables
current_time = 0
sunny_value = 0
temperature = 20
humidity = 20

# Sprayers monitor color
true_color = "green"
false_color = "red"


def main():

    def timer():

        """
           Function associated with time change.
           One second in the app represents one hour in real time.

        """
        app.repeat(1000, time_increase)

    def time_increase():

        global current_time
        current_time += 1
        check()
        update_time()

    def update_time():

        global current_time
        time_string = " "
        if 0 < current_time < 10:
            time_string = "Time  0{}:00".format(current_time)
        elif 10 <= current_time < 24:
            time_string = "Time  {}:00".format(current_time)
        elif current_time == 24:
            current_time = 0
            time_string = "Time  00:00".format(current_time)
        time_text.value = time_string

    def sunny():

        global sunny_value

    def temp_sld(sld_value):

        """
            Function associated with temperature slider.

        """

        global temperature
        temperature = int(sld_value)
        check()

    def humidity_sld(sld_value):

        """
            Function associated with humidity slider.

        """

        global humidity
        humidity = int(sld_value)
        check()

    def monitor_time():

        """
            Function associated with time.
            If time of day is between 07:00 and 18:00, then the text changes colors.

        """

        if 7 <= current_time <= 18:
            time_text_ok.text_color = true_color
            return True
        else:
            time_text_ok.text_color = false_color
            return False

    def monitor_sunny():

        """
            Function associated with sunny.
            If the sunny box is checked, then the text changes colors.
            This means it is not cloudy.

        """

        global sunny_value
        if sunny.value == 1:
            sunny_text.text_color = true_color
            sunny_value = 1
            return True
        else:
            sunny_text.text_color = false_color
            sunny_value = 0
            return False

    def monitor_temperature():

        """
            Function associated with temperature.
            If temperature is between 55° and 75°, then the text changes colors.

        """

        global temperature
        if 55 <= temperature <= 75:
            temp_text.text_color = true_color
            return True
        else:
            temp_text.text_color = false_color
            return False

    def monitor_humidity():

        """
          Function associated with humidity.
          If humidity is less than 50°, then the text changes colors.

        """

        global humidity
        if humidity <= 50:
            humidity_text.text_color = true_color
            return True
        else:
            humidity_text.text_color = false_color
            return False

    def check():

        global current_time, temperature, humidity, sunny_value
        time_check = monitor_time()
        sunny_check = monitor_sunny()
        temperature_check = monitor_temperature()
        humidity_check = monitor_humidity()

        if time_check and sunny_check and temperature_check and humidity_check:
            spray_text.text_color = true_color
            light[(0, 0)].color = true_color
        else:
            spray_text.text_color = false_color
            light[(0, 0)].color = false_color

    try:

        # Main app
        app = App(title='Crop Sprayer Control', layout='auto', width=APP_WIDTH, height=APP_HEIGHT)
        app.bg = '#f5da5f'
        left_box = Box(app, width=270, height=700, align="left", border=True)

        Box(left_box, width=60, height=70, align='top')

        # Time clock box
        box = Box(left_box, width=150, height=30, align='top', border=True)
        time_text = Text(box, text="Time  00:00", align="top")
        time_text.size = 17

        Box(left_box, width=150, height=20, align='top')

        # Sunny box
        box = Box(left_box, width=150, height=30, align='top', border=True)
        sunny = CheckBox(box, ["Sunny"], align="top", command=sunny)
        sunny.text_size = 15

        Box(left_box, width=150, height=20, align='top')

        # Global variables box
        box = Box(left_box, width=180, height=120, align='top', border=True)
        time_text_ok = Text(box, text="Time OK", align="top", size=15)
        sunny_text = Text(box, text="Sunny OK", align="top", size=15)
        temp_text = Text(box, text="Temperature OK", align="top", size=15)
        humidity_text = Text(box, text="Humidity OK", align="top", size=15)

        Box(left_box, width=150, height=20, align='top')

        # Sprayers box
        box = Box(left_box, width=180, height=90, align='top', border=True)
        spray_text = Text(box, text="Sprayers", align="left")
        spray_text.text_size = 16
        light = Waffle(box, height=1, width=1, dim=45, color='black', dotty=True, visible=False, align="left")
        light.visible = True
        light.color = 'red'
        light.pad = 20

        # Humidity slider box
        right_box = Box(app, width=120, height=700, align="right", border=True)
        Box(right_box, width=60, height=40, align='top')
        Text(right_box, text="Humidity", align="top")
        Text(right_box, text="%", align="top")
        Slider(right_box, start=100, end=0, width=35, height=220, horizontal=False, align="top", command=humidity_sld)

        # Temperature slider box
        center_box = Box(app, width=120, height=700, align="right", border=True)
        Box(center_box, width=50, height=40, align='top')
        Text(center_box, text="Temperature", align="top")
        Text(center_box, text="°F", align="top")
        Slider(center_box, start=140, height=220, horizontal=False, align="top", end=-40, width=35, command=temp_sld)

        timer()
        app.display()

    # Defines an argument to the except statement
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
