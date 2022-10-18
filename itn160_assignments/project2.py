""" 
Michael Hoyle
ITN160-4C1
Project 2
3/26/2022

Quiz game app that allows players to buzz in with answers, led by a Host
"""

# Resources used:
# https://lawsie.github.io/guizero/app/
# https://mycourses.dtcc.edu/d2l/le/content/86265/viewContent/3853060/View

# import library
from guizero import *


def main():

    """Functions for the host and players button.
    Changes host and players light. Player buttons are enabled and disabled."""

    def host():

        circle_1.oval(125, 125, 25, 25, color="blue", outline=True)
        circle_2.oval(125, 125, 25, 25, color="black", outline=True)
        circle_3.oval(125, 125, 25, 25, color="black", outline=True)
        circle_4.oval(125, 125, 25, 25, color="black", outline=True)
        txt_2.value = "Buzz in first to answer the question"
        button_a.enable()
        button_b.enable()
        button_c.enable()
        button_d.enable()

    def player1():

        circle_1.oval(125, 125, 25, 25, color="black", outline=True)
        circle_2.oval(125, 125, 25, 25, color="green", outline=True)
        circle_3.oval(125, 125, 25, 25, color="black", outline=True)
        circle_4.oval(125, 125, 25, 25, color="black", outline=True)
        txt_2.value = "Player 1 buzzed in first"
        button_b.disable()
        button_c.disable()
        button_d.disable()

    def player2():

        circle_1.oval(125, 125, 25, 25, color="black", outline=True)
        circle_2.oval(125, 125, 25, 25, color="black", outline=True)
        circle_3.oval(125, 125, 25, 25, color="green", outline=True)
        circle_4.oval(125, 125, 25, 25, color="black", outline=True)
        txt_2.value = "Player 2 buzzed in first"
        button_b.disable()
        button_c.disable()
        button_d.disable()

    def player3():

        circle_1.oval(125, 125, 25, 25, color="black", outline=True)
        circle_2.oval(125, 125, 25, 25, color="black", outline=True)
        circle_3.oval(125, 125, 25, 25, color="black", outline=True)
        circle_4.oval(125, 125, 25, 25, color="green", outline=True)
        txt_2.value = "Player 3 buzzed in first"
        button_b.disable()
        button_c.disable()
        button_d.disable()

    # App layout - Grid manager used to position widgets
    app = App("Are You Smarter Than Mr. Sciallo?", bg="orange", width=450, height=800,
              layout="grid")  # using grid layout

    tbox = Box(app, border=1, grid=[1, 1, 2, 1], width=450, height=35)
    Text(app, size=20, grid=[1, 0, 2, 1])
    txt_2 = Text(tbox, "Wait for the host to start the round", size=20)
    Text(app, size=20, grid=[1, 2, 2, 1])

    circle_1 = Drawing(app, width=125, height=125, grid=[1, 3])
    circle_1.oval(125, 125, 25, 25, color="light yellow", outline=True)  # Using oval for the circle drawing
    circle_2 = Drawing(app, width=125, height=125, grid=[1, 4])
    circle_2.oval(125, 125, 25, 25, color="light yellow", outline=True)
    circle_3 = Drawing(app, width=125, height=125, grid=[1, 5])
    circle_3.oval(125, 125, 25, 25, color="light yellow", outline=True)
    circle_4 = Drawing(app, width=125, height=125, grid=[1, 6])
    circle_4.oval(125, 125, 25, 25, color="light yellow", outline=True)

    button_a = PushButton(app, command=host, text="Host", grid=[2, 3], padx=27, pady=7)
    button_a.text_size = 22
    button_b = PushButton(app, command=player1, text="Player 1", grid=[2, 4], padx=7, pady=7)
    button_b.text_size = 22
    button_b.disable()
    button_c = PushButton(app, command=player2, text="Player 2", grid=[2, 5], padx=7, pady=7)
    button_c.text_size = 22
    button_c.disable()
    button_d = PushButton(app, command=player3, text="Player 3", grid=[2, 6], padx=7, pady=7)
    button_d.text_size = 22
    button_d.disable()

    # Display the app
    app.display()


if __name__ == '__main__':
    main()
