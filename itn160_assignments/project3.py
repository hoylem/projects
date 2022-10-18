from guizero import *



boxes = []
items = ['Burger', 'Frank', 'Fries', 'Soda']
prices = [4.95, 1.99, 2.50, 2.00]
count = [0] * len(items)
inc_buttons = []
dec_buttons = []
counters = []
total = []
totals = [0] * len(items)


def main():
    def calc_total():
        global total_amount
        total_amount.clear()
        total_amount.append("Order Total  ${:.2f}".format(sum(totals)))

    def increment(btn):
        count = int(counters[btn].value) + 1
        if count <= 10:
            counters[btn].clear()
            counters[btn].append(str(count))

            prod = count * prices[btn]
            total[btn].clear()
            total[btn].append("${:.2f}".format(prod))
            totals[btn] = prod
            calc_total()

    def decrement(btn):
        count = int(counters[btn].value) - 1
        if count >= 0:
            counters[btn].clear()
            counters[btn].append(str(count))

            prod = count * prices[btn]
            total[btn].clear()
            total[btn].append("${:.2f}".format(prod))
            totals[btn] = prod
            calc_total()

    def clear_order():
        global totals, total_amount
        for i in range(len(items)):
            count = [0] * len(items)
            totals = [0] * len(items)
            counters[i].clear()
            counters[i].append("0")
            total[i].clear()
            total[i].append("${:.2f}".format(totals[len(boxes) - 1]))
            total_amount.clear()
            total_amount.append("Order Total  ${:.2f}".format(0))

    def order():
        order_final = app.yesno(title, "OK to place order ?")
        if order_final == True:
            listbox.clear()
            for i in range(len(items)):
                listbox.append(
                    "{: <15} {} @ ${:5.2f} ${:5.2f}".format(items[i], counters[i].value, prices[i], totals[i]))
            listbox.append("")
            listbox.append("Order Total ${:.2f}".format(sum(totals)))
            listbox.append("")
            listbox.append("Thanks for eating at Joe's")
            clear_order()
        else:
            clear_order()

    for item in items:
        boxes.append(Box(app, border=True))
        dec_buttons.append(
            PushButton(boxes[len(boxes) - 1], command=decrement, args=[len(boxes) - 1], text="-", align="left"))
        counters.append(Text(boxes[len(boxes) - 1], text="0", align="left", width=5))
        inc_buttons.append(
            PushButton(boxes[len(boxes) - 1], command=increment, args=[len(boxes) - 1], text="+", align="left"))
        Text(boxes[len(boxes) - 1], text=items[len(boxes) - 1], align="left", width=10)
        Text(boxes[len(boxes) - 1], text="${:.2f}".format(prices[len(boxes) - 1]), align="left", width=7)
        total.append(
            Text(boxes[len(boxes) - 1], text="${:.2f}".format(totals[len(boxes) - 1]), align="left", width=7))







    app = App(title="Eat at Mike's", width=400, height=400)
    reciept_app = App(title="Customer Receipt", width=400, height=300)
    top_pad = Box(reciept_app, height=50)
    listbox = ListBox(reciept_app, width=300, height=200, items=[])

    top_pad = Box(app, height=20)
    order_box = Box(app)
    order_btn = PushButton(order_box, command=order, text="Place Order", align="left")
    left_pad = Box(order_box, align="left", height="fill", width=30)
    total_box = Box(order_box, align="right", border=True, height=40, width=175)
    total_amount = Text(total_box, text="Order Total  ${:.2f}".format(0), align="bottom")

    top_pad = Box(app, height=30)
    Text(app, text="Enter Your Order")
    top_pad = Box(app, height=30)

    app.display()


if __name__ == '__main__':
    main()