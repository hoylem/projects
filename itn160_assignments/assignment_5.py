"""

Michael Hoyle
ITN160-4C1
Assignment 5: Temperature Notification
2/25/2022
"""

# Resources used for program:
# https://mycourses.dtcc.edu/d2l/le/content/86265/viewContent/3952818/View
# https://youtu.be/JOqAcGdSPMc
# Instructor feedback
# https://youtu.be/WtjnDbzhTHI

# import library
from guizero import *


def main():

    def flash_message():

        """
        Event handler for text to flash
        """

        if txt_message.visible and sld_temp.value <= 32:
            txt_message.hide()

        elif txt_message.visible and sld_temp.value >= 101:
            txt_message.hide()
        else:
            txt_message.show()

    def change_temp(value):

        temperature = int(value)

        if temperature <= 32:
            txt_message.value = 'Extreme Cold'
            txt_message.text_color = 'blue'

        elif 33 <= temperature < 50:
            txt_message.value = 'Cold'
            txt_message.text_color = 'blue'

        elif 51 < temperature <= 70:
            txt_message.value = 'Mild'
            txt_message.text_color = 'Orange'

        elif 71 < temperature <= 90:
            txt_message.value = 'Beautiful'
            txt_message.text_color = 'green'

        elif 91 <= temperature <= 100:
            txt_message.value = 'Hot'
            txt_message.text_color = 'red'

        elif temperature >= 101:
            txt_message.value = 'Extreme Heat'
            txt_message.text_color = 'red'

    # closes app when 'Exit' button is pushed
    def exit_button():

        app.destroy()

    # Main app layout
    app = App(title='Temperature Notification Panel', width=400, height=350, bg='light yellow', layout="auto")
    app.text_size = 18

    # App text and layout
    Text(app)  # creates space
    Text(app, text='Outside Temperature °F')
    sld_temp = Slider(app, command=change_temp, start=-50, end=150, width=250, height=25)
    Text(app)  # creates space
    txt_message = Text(app, size=18, font='Comic Sans MS')
    Text(app)  # creates space
    PushButton(app, text='Exit', width=8, height=1, command=exit_button)

    # Repeats code every second
    txt_message.repeat(1000, flash_message)

    # Displays full app
    app.display()


if __name__ == '__main__':
    main()
