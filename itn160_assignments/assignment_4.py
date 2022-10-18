"""
Michael Hoyle
ITN160-4C1
Assignment 4: Daily Temperature Statistics
2/22/2022
"""

# Resources:
# https://youtu.be/csuTz38di8A
# https://www.geeksforgeeks.org/python-list/
# https://mycourses.dtcc.edu/d2l/le/content/86265/viewContent/3952818/View
# https://youtu.be/h0zOCbyoHIE
# https://youtu.be/Ptb1Ut6ZCYY

# Import library
from guizero import *
import time

# Global variables
military_time = '00:00'
timer = 0
list = []

# Time and temperature variables
global f_4am, c_4am, f_4pm, c_4pm, f_10am, c_10am, \
    f_10pm, c_10pm, min_f, min_c, max_f, max_c, avg_f, avg_c, reset_box

# Two second sleep
time.sleep(2)

# Main app layout
app = App(title='Daily Temperature Analysis', width=330, height=675, layout='auto', )



def main():
    def update():
        """
        Event handler for military timer.
        One hour is increased each second.
        """
        global timer, military_time, box
        timer += 1
        if timer < 10:
            military_time = f'0{timer}:00'
        else:
            military_time = f'{timer}:00'
        if timer == 23:
            timer = -1
        text_1.value = military_time
        text_1.after(1000, update)

    # Displays timer text
    text_1 = Text(app, text="", align='bottom', size=15)
    text_1.value = military_time
    text_1.after(1000, update)
    text = Text(app, text='Timer', color='orange', align='bottom', size=17)

    # Box with text
    box_3 = Box(app, height=50, width=280)
    Text(box_3, text='Outside Weather(°F)', color='blue', align='bottom', size=18)

    # Function for slider
    box_4 = Box(app, height=60, width=280)
    slider = Slider(box_4, start=(-40), end=140, width=230, height=20)

    # 4am time values
    box = Box(app, width=175, height=50, layout='grid', border=1)
    box_1 = Box(box, width=165, height=23, grid=[0, 0])
    Text(box_1, text='04:00 Scan', color='red', size=10)
    box_2 = Box(box, width=170, height=23, grid=[0, 1], layout='grid')
    box_3 = Box(box_2, width=85, height=23, grid=[0, 0])
    f_4am = Text(box_3, text='°F', size=10, color='red', align='left')
    box_4 = Box(box_2, width=90, height=23, grid=[1, 0])
    c_4am = Text(box_4, text='°C', size=10, color='red', align='right')
    box = Box(app, height=15, width=275)

    def update_f_4am():

        """
        Event handler for the slider.
        Temperature is converted to fahrenheit at 04:00.
        """
        global f_4am, list
        if timer == 4:
            f_4am.value = str(slider.value) + '°F'
            list.append(slider.value)
        f_4am.after(1000, update_f_4am)


    def update_c_4am():

        """
        Event handler for the slider.
        Temperature is converted to celsius at 04:00.
        """

        global c_4am
        if timer == 4:
            c_4am.value = str('{:.1f}'.format((slider.value - 32) * 5 / 9)) + '°C'
        c_4am.after(1000, update_c_4am)


    # 10am time values
    box = Box(app, width=175, height=50, layout="grid", border=1)
    box_1 = Box(box, width=165, height=23, grid=[0, 0])
    text = Text(box_1, text='10:00 Scan', color='red', size=10)
    box_2 = Box(box, width=170, height=23, grid=[0, 1], layout='grid')
    box_3 = Box(box_2, width=85, height=23, grid=[0, 0])
    f_10am = Text(box_3, text='°F', color='red', size=9, align='left')
    box_4 = Box(box_2, width=90, height=23, grid=[1, 0])
    c_10am = Text(box_4, text='°C', color='red', size=9, align='right')
    box = Box(app, height=15, width=275)

    def update_f_10am():

        """
        Event handler for the slider.
        Temperature is converted to fahrenheit at 10:00.
        """

        global f_10am, list
        if timer == 10:
            f_10am.value = str(slider.value) + '°F'
            list.append(slider.value)
        f_10am.after(1000, update_f_10am)


    def update_c_10am():

        """
        Event handler for the slider.
        Temperature is converted to celsius at 10:00.
        """

        global c_10am
        if timer == 10:
            c_10am.value = str('{:.1f}'.format((slider.value - 32) * 5 / 9)) + '°C'
        c_10am.after(1000, update_c_10am)


    # 4pm time values
    box = Box(app, width=175, height=50, layout='grid', border=1)
    box_1 = Box(box, width=165, height=23, grid=[0, 0])
    text = Text(box_1, text='16:00 Scan', color='red', size=10)
    box_2 = Box(box, width=170, height=23, grid=[0, 1], layout='grid')
    box_3 = Box(box_2, width=85, height=23, grid=[0, 0])
    f_4pm = Text(box_3, text='°F', color='red', size=9, align='left')
    box_4 = Box(box_2, width=90, height=23, grid=[1, 0])
    c_4pm = Text(box_4, text='°C', color='red', size=9, align='right')
    box = Box(app, height=15, width=275)

    def update_f_4pm():

        """
        Event handler for the slider.
        Temperature is converted to fahrenheit at 16:00.
        """

        global f_4pm, list
        if timer == 16:
            f_4pm.value = str(slider.value) + '°F'
            list.append(slider.value)
        f_4pm.after(1000, update_f_4pm)


    def update_c_4pm():

        """
        Event handler for the slider.
        Temperature is converted to celsius at 16:00.
        """

        global c_4pm
        if timer == 16:
            c_4pm.value = str('{:.1f}'.format((slider.value - 32) * 5 / 9)) + '°C'
        c_4pm.after(1000, update_c_4pm)


    # 10pm time values
    box = Box(app, width=175, height=50, layout='grid', border=1)
    box_1 = Box(box, width=165, height=23, grid=[0, 0])
    text = Text(box_1, text='22:00 Scan', color='red', size=10)
    box_2 = Box(box, width=170, height=23, grid=[0, 1], layout='grid')
    box_3 = Box(box_2, width=85, height=23, grid=[0, 0])
    f_10pm = Text(box_3, text='°F', color='red', size=9, align='left')
    box_4 = Box(box_2, width=90, height=23, grid=[1, 0])
    c_10pm = Text(box_4, text='°C', color='red', size=9, align='right')
    box = Box(app, height=15, width=275)

    def update_f_10pm():

        """
        Event handler for the slider.
        Temperature is converted to fahrenheit at 22:00.
        """

        global f_10pm, list
        if timer == 22:
            f_10pm.value = str(slider.value) + '°F'
            list.append(slider.value)
        f_10pm.after(1000, update_f_10pm)


    def update_c_10pm():

        """
        Event handler for the slider.
        Temperature is converted to celsius at 22:00.
        """

        global c_10pm
        if timer == 22:
            c_10pm.value = str('{:.1f}'.format((slider.value - 32) * 5 / 9)) + '°C'
        c_10pm.after(1000, update_c_10pm)


    # Minimum temperature
    box = Box(app, width=175, height=50, layout='grid', border=1)
    box_1 = Box(box, width=165, height=23, grid=[0, 0])
    text = Text(box_1, text='Minimum Scan', color='red', size=10)
    box_2 = Box(box, width=170, height=23, grid=[0, 1], layout='grid')
    box_3 = Box(box_2, width=85, height=23, grid=[0, 0])
    min_f = Text(box_3, text='°F', color='red', size=9, align='left')
    box_4 = Box(box_2, width=90, height=23, grid=[1, 0])
    min_c = Text(box_4, text='°C', color='red', size=9, align='right')
    box = Box(app, height=15, width=275)

    def update_min_f():

        """
        Event handler for the temperature conversion.
        When timer reaches 22:00, the minimum temp in
        fahrenheit is displayed.
        """
        global list, min_f
        if timer == 22:
            min_f.value = str(min(list)) + '°F'
        min_f.after(1000, update_min_f)

        update_min_f()


    def update_min_c():

        """
        Event handler for the temperature conversion.
        When timer reaches 22:00, the minimum temp in
        celsius is displayed.
        """

        global list, min_c
        if timer == 22:
            min_c.value = str('{:.1f}'.format((slider.value - 32) * 5 / 9)) + '°C'
        min_c.after(1000, update_min_c)


    # Maximum temperature
    box = Box(app, width=175, height=50, layout='grid', border=1)
    box_1 = Box(box, width=165, height=23, grid=[0, 0])
    text = Text(box_1, text='Maximum Scan', color='red', size=10)
    box_2 = Box(box, width=170, height=23, grid=[0, 1], layout='grid')
    box_3 = Box(box_2, width=85, height=23, grid=[0, 0])
    max_f = Text(box_3, text='°F', color='red', size=9, align='left')
    box_4 = Box(box_2, width=90, height=23, grid=[1, 0])
    max_c = Text(box_4, text='°C', color='red', size=9, align='right')
    box = Box(app, height=15, width=275)

    def update_max_f():

        """
        Event handler for the temperature conversion.
        When timer reaches 22:00, the maximum temp in
        fahrenheit is displayed.
        """

        global list, max_f
        if timer == 22:
            max_f.value = str(max(list)) + '°F'
        max_f.after(1000, update_max_f)


    def update_max_c():

        """
        Event handler for the temperature conversion.
        When timer reaches 22:00, the maximum temp in
        celsius is displayed.
        """

        global list, max_c
        if timer == 22:
            max_c.value = str('{:.1f}'.format((max(list) - 32) * 5 / 9)) + '°C'
        max_c.after(1000, update_max_c)


    # Mean temperature
    box = Box(app, border=1, width=175, height=50, layout='grid', )
    box_1 = Box(box, width=165, height=23, grid=[0, 0])
    text = Text(box_1, text='Average Scan', color='red', size=10)
    box_2 = Box(box, width=170, height=23, grid=[0, 1], layout='grid')
    box_3 = Box(box_2, width=85, height=23, grid=[0, 0])
    avg_f = Text(box_3, text='°F', color='red', size=9, align='left')
    box_4 = Box(box_2, width=90, height=23, grid=[1, 0])
    avg_c = Text(box_4, text='°C', color='red', size=9, align='right')
    reset_box = Box(app, height=15, width=275)

    def update_avg_f():

        """
        Event handler for the temperature conversion.
        When timer reaches 22:00, the average temp in
        fahrenheit is displayed.
        """

        global list, avg_f
        if timer == 22:
            average = sum(list) / len(list)
            avg_f.value = str('{:.1f}'.format(average)) + '°F'
        avg_f.after(1000, update_avg_f)


    def update_avg_c():

        """
        Event handler for the temperature conversion.
        When timer reaches 22:00, the average temp in
        celsius is displayed.
        """

        global list, avg_c, c_4am, f_4am
        if timer == 22:
            average = sum(list) / len(list)
            avg_c.value = str('{:.1f}'.format((average - 32) * 5 / 9)) + '°C'
        avg_c.after(1000, update_avg_c)


    def reset():
        """
        Event handler for the timer. When all
        temperature values have completed,
        the timer pauses for 2 seconds, and
        then the values reset.
        """

        if timer == -1:
            time.sleep(2)

            min_f.value = ""
            min_c.value = ""
            max_f.value = ""
            max_c.value = ""
            avg_c.value = ""
            avg_f.value = ""
            f_4am.value = ""
            c_4am.value = ""
            f_4pm.value = ""
            c_4pm.value = ""
            f_10am.value = ""
            c_10am.value = ""
            f_10pm.value = ""
            c_10pm.value = ""

    def update_reset_box():

        """

        Event handler to reset box. Global
        variable is called to reset box after
        one second.
        """

        global reset_box
        reset()
        reset_box.after(1000, update_reset_box)


    # Displays app
    app.display()




if __name__ == '__main__':
    main()
