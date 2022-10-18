"""
# Michael Hoyle
"""
# resources used:
# https://lawsie.github.io/guizero/pushbutton/
# https://easycodebook.com/2020/03/python-gui-program-temperature-conversion-fahrenheit-to-celsius/
# https://www.youtube.com/watch?v=YvZBNuSEoA8
# https://mycourses.dtcc.edu/d2l/le/content/86265/viewContent/3940026/View
# https://mycourses.dtcc.edu/d2l/le/content/86265/viewContent/3936967/View
# https://stackoverflow.com/questions/56095177/how-do-i-pass-parameters-to-a-function-from-a-guizero-object

# import 2 function from convert.py file
import convert
from convert import celsius_to_fahrenheit, fahrenheit_to_celsius
from guizero import *

# Global constants
APP_WIDTH = 350
APP_HEIGHT = 500

ROW_WIDTH = APP_WIDTH
ROW_HEIGHT = 60

def main():

    def c2f_button_clicked(self):
        """
        Event handler for c2f button:
        Receive an int value and convert to fahrenheit
        :return: Convert celsius temperature to fahrenheit
        """
        c2f_button_clicked = int(f'{tbx_celsius.value}')
        fahrenheit = convert.celsius_to_fahrenheit(celsius)
        txt_celsius.value = (f'{celsius} = {fahrenheit:.3f}')
        


    # Main app layout
    app = App(layout='auto', title='Celsius and Fahrenheit Conversions', width=APP_WIDTH, height=APP_HEIGHT)
    app.text_size = 18

    # Celsius to Fahrenheit conversion text, text box, and pushbutton
    Text(app, text='Enter °F', align='top', color='blue')
    tbx_celsius = TextBox(app, command=c2f_button_clicked)
    PushButton(app, text='Convert °C to °F')
    txt_celsius = Text(app, color='red')
    

    def f2c_button_clicked(fahrenheit):
        """
        Event handler for f2c button:
        Receive an int value and convert to celsius
        :return: Convert fahrenheit temperature to celsius
        """

        fahrenheit = int(tbx_fahrenheit.value)
        celsius = convert.fahrenheit_to_celsius(fahrenheit)
        txt_fahrenheit.value = f'{fahrenheit} = {celsius:.3f}'
        tbx_fahrenheit.clear()

    # Fahrenheit to Celsius conversion text, text box, and pushbutton
    Text(app, text='Enter °C', align='top', color='blue')
    tbx_fahrenheit = TextBox(app,command=f2c_button_clicked)
    PushButton(app, text='Convert °F to °C', command=f2c_button_clicked)
    txt_fahrenheit = Text(app, color='red')

    # Displays the main app and everything inside it
    app.display()

if __name__ == '__main__':
    main()