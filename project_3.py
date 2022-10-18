


from guizero import *


def main():



    def place(window_1):
        window_1.show()

    food_list = []

    food = {
        ['Burger', 4.95]
        ['Cheese Fries', 2.50]
        ['Hot Dog', 2.95]
        ['Water', 1.99]
    }

    window_1 = App(title="Eat at Mike's", bg="light yellow", width=500,
                   height=500, layout="auto")
    window_2 = App(title="Customer Receipt", bg="royal blue",
                   width=400, height=350, layout="auto")
    Text(window_1)  # spacer
    Text(window_1, 'Enter Your Order', size=15)
    Text(window_1)  # spacer
    box_1 = Box(window_1, width=400, height=65, border=1)
    box_2 = Box(window_1, width=400, height=65, border=1)
    box_3 = Box(window_1, width=400, height=65, border=1)
    box_4 = Box(window_1, width=400, height=65, border=1)
    PushButton(box_1, align='left', text='-', width=4)
    PushButton(box_1, align='left', text='+', width=4)
    PushButton(box_2, align='left', text='-', width=4)
    PushButton(box_2, align='left', text='+', width=4)
    PushButton(box_3, align='left', text='-', width=4)
    PushButton(box_3, align='left', text='+', width=4)
    PushButton(box_4, align='left', text='-', width=4)
    PushButton(box_4, text='+', align='left', width=4)
    Text(box_1, text='0')
    Text(box_2, text='0')
    Text(box_3, text='0')
    Text(box_4, text='0')
    Text(box_1, text='Burger', align='left')
    Text(box_2, text='Cheese Fries', align='left')
    Text(box_3, text='Hot Dog', align='left')
    Text(box_4, text='Water', align='left')
    Text(box_1, text='$4.95')
    Text(box_2, text='$1.99')
    Text(box_3, text='$2.50')
    Text(box_4, text='$2.00')
    Text(window_1)  # spacer
    Text(window_1)  # spacer
    PushButton(window_1, text='Place Order', width=20, height=2, align='left', command=place(window_1))
    order_total_box = Box(window_1, width=210, height=75, border=1)

    Text(order_total_box, text='Order Total')

    window_1.display()
    window_2.display()



if __name__ == '__main__':
    main()


