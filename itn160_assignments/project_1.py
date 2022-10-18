"""
Michael Hoyle
ITN160-4C1
Project 1: Spelling Bee Scoring Control Panel
02/17/2022

Create app with game controller, name entry boxes,
and scores cards to score spelling bee competition.

"""

# Resources used for project:
# https://lawsie.github.io/guizero/alerts/
# ITN160 learning modules and class recordings
# Instructor notes/feedback
# https://stackoverflow.com/questions/57736941/textbox-not-showing-up-in-my-game-tic-tac-toe-python

from guizero import *

# Global constants
APP_WIDTH = 400
APP_HEIGHT = 250


def main():

    def new_round():
        """

        Event handler for starting and restarting
         the Spelling Bee game
        :return: None
        """
        # clears player 1 score app
        if new_round_button:
            name_player1.value = ""
            counter1.value = 0
            champ_1_txt.value = ""
            lose_txt.value = ""

            # clears player 2 score app
            name_player2.value = ""
            counter2.value = 0
            champ_2_txt.value = ""
            lose_txt_2.value = ""

        # Pop-up app for player 1 name entry
        name_1 = app.question('Spelling Bee', 'Enter Player 1 name')
        if name_1 is not None:
            name_player1.value = 'Welcome, ' + name_1
            new_round_button.disable()

        # Pop-up app for player 2 name entry
        name_2 = app.question('Spelling Bee', 'Enter Player 2 name')
        if name_2 is not None:
            name_player2.value = 'Welcome, ' + name_2
            button_1.enable()
            button_2.enable()


    # Increase Player 1 score - reveal win or loss
    def score_player_1(value):

        new_score = int(counter1.value) + value
        if 0 <= new_score <= 10:
            counter1.value = new_score
        if counter1.value == '10':
            champ_1_txt.value = 'Champion!'
        if counter1.value == '10':
            lose_txt_2.value = 'Game Over, you lose!'
            new_round_button.enable()

    # Increase Player 2 score - reveal win or loss
    def score_player_2(value):

        new_score_2 = int(counter2.value) + value
        if 0 <= new_score_2 <= 10:
            counter2.value = new_score_2
        if counter2.value == '10':
            champ_2_txt.value = 'Champion!'
        if counter2.value == '10':
            lose_txt.value = 'Game Over, you lose!'
            new_round_button.enable()

    # Main app layout
    app = App('Spelling Bee Controller', bg='light gray',
              width=APP_WIDTH, height=APP_HEIGHT, layout='grid')
    app.text_size = 15
    new_round_button = PushButton(app, text='Begin New Round',
                                  command=new_round, width=35, height=1, grid=[1, 0, 2, 1])

    # Player 1 box details
    display_box1 = Box(app, border=True, height=185, width=200,
                       grid=[1, 2])
    text1 = Text(display_box1, text='Player 1')
    text1.text_color = 'navy blue'
    button_1 = PushButton(display_box1, command=score_player_1, text='Correct',
                          width=10, height=2, args=[+1])
    button_1.text_color = 'navy blue'
    button_1.disable()

    # Player 2 box details
    display_box2 = Box(app, border=True, height=185, width=200,
                       grid=[2, 2])
    p2_text = Text(display_box2, text='Player 2')
    p2_text.text_color = 'maroon'
    button_2 = PushButton(display_box2, command=score_player_2, text='Correct',
                          width=10, height=2, args=[+1])
    button_2.text_color = 'maroon'
    button_2.disable()

    # Window to display player 1 score
    p1_score_window = Window(app, title='Player 1 Score')

    # Displays Player 1's name inputted into textbox
    name_player1 = Text(p1_score_window, size=10, color='navy blue')

    # Displays score of player 1
    counter1 = Text(p1_score_window, text='0', color='navy blue', size=125,
                    width='fill', height='fill')

    # Displays winner and losing message for player 1
    champ_1_txt = Text(p1_score_window, size=50, color='red')
    lose_txt = Text(p1_score_window, size=35, color='red')

    # Window to display player 2 score
    p2_score_window = Window(app, title='Player 2 Score')

    # Displays Player 2's name inputted into textbox
    name_player2 = Text(p2_score_window, size=30, color='maroon')

    # Displays score of player 2
    counter2 = Text(p2_score_window, text="0", color='maroon',
                    size=125, width='fill', height='fill')

    # Displays winner and losing message for player 2
    champ_2_txt = Text(p2_score_window, size=50, color='red')
    lose_txt_2 = Text(p2_score_window, size=35, color='red')

    app.display()


if __name__ == '__main__':
    main()
