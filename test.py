from guizero import *
NUMBER_OF_LANES = 8
def main():
    def controls_one(i, controls, signals):
        if controls[i].value:
            signals[i].value = 'O'
            signals[i].text_color = 'green'
        else:
            signals[i].value = 'X'
            signals[i].text_color = 'red'
    win1 = App(title='Toll Booths', height=200, width=850,
               layout='grid')
    win1.text_size = 20

    win2 = App(title='Control Room', height=170, width=500, layout='grid')
    win1.text_size = 14

    Text(win1, text=' ' * 8, grid=[0,0])
    Text(win2, text=' ' * 8, grid=[0,0])

    lanes_1 = []
    signal_1 = []
    lanes_2 = []
    controls_2 = []


    for i in range(NUMBER_OF_LANES):
        lanes_1.append(Text(win1, text=str(i + 1), width=3, size=40, grid=[i + 1, 1]))
        signal_1.append(Text(win1, text='X', width=3, color='red', size=40, grid=[i + 1, 2]))
        lanes_2.append(Text(win2, text=str(i + 1) + ' ', align='left', width=3, size=20, grid=[i + 1, 1]))
        controls_2.append(CheckBox(win2, command=controls_one, args=[i, controls_2, signal_1], grid=[i + 1, 2]))



    win1.display()



main()

