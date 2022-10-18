

from guizero import *

# Global Constant
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 250
WINDOW_WIDTH2 = 700
WINDOW_HEIGHT2 = 200
lanes = 6






def main():
    def operate_lane(operators1, indicators):
        if checkbox_1.value: 
            indicators.value
            indicators.text_color
        else:
            indicators.value
            indicators.text_color

    window_1 = App(title="Lane Display", bg="orange", width=WINDOW_WIDTH,
                    height=WINDOW_HEIGHT, layout="grid")
    window_2 = App(title="Lane Operator", bg="green",
                    width=WINDOW_WIDTH2, height=WINDOW_HEIGHT2, layout="grid")

    Text(window_1, size=45, grid=[0, 0])
    Text(window_2, size=45, grid=[0, 0])

    operators1 = []
    indicators = []

    lane1 = Text(window_1, text='1', width=4, size=35, grid=[1, 0])
    lane2 = Text(window_1, text='2', width=4, size=35, grid=[2, 0])
    lane3 = Text(window_1, text='3', width=4, size=35, grid=[3, 0])
    lane4 = Text(window_1, text='4', width=4, size=35, grid=[4, 0])
    lane5 = Text(window_1, text='5', width=4, size=35, grid=[5, 0])
    lane6 = Text(window_1, text='6', width=4, size=35, grid=[6, 0])

    indicator1 = Text(window_1, text='X', width=4, color='red', size=35, grid=[1, 1])
    indicator2 = Text(window_1, text='X', width=4, color='red', size=35, grid=[2, 1])
    indicator3 = Text(window_1, text='X', width=4, color='red', size=35, grid=[3, 1])
    indicator4 = Text(window_1, text='X', width=4, color='red', size=35, grid=[4, 1])
    indicator5 = Text(window_1, text='X', width=4, color='red', size=35, grid=[5, 1])
    indicator6 = Text(window_1, text='X', width=4, color='red', size=35, grid=[6, 1])

    lane2 = Text(window_2, text='1', width=4, size=35, grid=[1, 0])
    lane2 = Text(window_2, text='2', width=4, size=35, grid=[2, 0])
    lane2 = Text(window_2, text='3', width=4, size=35, grid=[3, 0])
    lane2 = Text(window_2, text='4', width=4, size=35, grid=[4, 0])
    lane2 = Text(window_2, text='5', width=4, size=35, grid=[5, 0])
    lane2 = Text(window_2, text='6', width=4, size=35, grid=[6, 0])

    checkbox_1 = CheckBox(window_2, grid=[1, 2], command=operate_lane, args=[operators1, indicators])
    checkbox_2 = CheckBox(window_2, grid=[2, 2], command=operate_lane, args=[operators1, indicators])
    checkbox_3 = CheckBox(window_2, grid=[3, 2], command=operate_lane, args=[operators1, indicators])
    checkbox_4 = CheckBox(window_2, grid=[4, 2], command=operate_lane, args=[operators1, indicators])
    checkbox_5 = CheckBox(window_2, grid=[5, 2], command=operate_lane, args=[operators1, indicators])
    checkbox_6 = CheckBox(window_2, grid=[6, 2], command=operate_lane, args=[operators1, indicators])

    window_1.display()
    window_2.display()



if __name__ == '__main__':
    main()





