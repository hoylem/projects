from guizero import App, Slider, Text, Box
import time

time.sleep(2)
#veriables
global milTime, counter, temp4amf, temp4amc, temp4pmf, temp4pmc, temp10amf,\
    temp10amc, temp10pmf, temp10pmc, minf, minc, maxf, maxc, avgf, avgc, lst, boxclear
lst = []
counter = 0
milTime = '00:00'

#mian activity
app = App(title="Daily Temperature Statistics", width=300, height=610, layout="auto", )

#time container
box = Box(app, width=280, height=80)

#to update time
def update():
    global counter, milTime
    counter += 1
    if counter < 10:
        milTime = f"0{counter}:00"
    else:
        milTime = f"{counter}:00"
    if counter == 23:
        counter = -1
    textT.value = milTime
    textT.after(900, update)

textT = Text(box, text="", align="bottom", size=14)
textT.value = milTime
textT.after(900, update)
text = Text(box, text="Military Time", align="bottom", size=14)

#outside temperature container
box2 = Box(app, height=50, width=280)
text = Text(box2, text="Outside temperature(°F)", align="bottom", size=13)

#slider container
box3 = Box(app, height=60, width=280)
slider = Slider(box3, start=(-40), end=140, width=230, height=12)

#4 AM time container
box = Box(app, width=165, height=42, layout="grid", border=1)
box0 = Box(box, width=158, height=20, grid=[0, 0])
text = Text(box0, text="4 AM READING", size=10)
box1 = Box(box, width=160, height=20, grid=[0, 1], layout='grid')
box2 = Box(box1, width=78, height=20, grid=[0, 0])
temp4amf = Text(box2, text="°F", size=9, align="left")
box3 = Box(box1, width=82, height=20, grid=[1, 0])
temp4amc = Text(box3, text="°C", size=9, align="right")
box = Box(app, height=10, width=280)


def updatetemp4amf():
    global temp4amf, lst
    if counter == 4:
        temp4amf.value = str(slider.value) + "°F"
        lst.append(slider.value)
    temp4amf.after(900, updatetemp4amf)
updatetemp4amf()
def updatetemp4amc():
    global temp4amc
    if counter == 4:
        temp4amc.value = str("{:.1f}".format((slider.value-32)/1.8)) + "°C"
    temp4amc.after(900, updatetemp4amc)
updatetemp4amc()

#10 AM time container
box = Box(app, width=165, height=42, layout="grid", border=1)
box0 = Box(box, width=158, height=20, grid=[0, 0])
text = Text(box0, text="10 AM READING", size=10)
box1 = Box(box, width=160, height=20, grid=[0, 1], layout='grid')
box2 = Box(box1, width=78, height=20, grid=[0, 0])
temp10amf = Text(box2, text="°F", size=9, align="left")
box3 = Box(box1, width=82, height=20, grid=[1, 0])
temp10amc = Text(box3, text="°C", size=9, align="right")
box = Box(app, height=10, width=280)

def updatetemp10amf():
    global temp10amf, lst
    if counter == 10:
        temp10amf.value = str(slider.value) + "°F"
        lst.append(slider.value)
    temp10amf.after(900, updatetemp10amf)
updatetemp10amf()
def updatetemp10amc():
    global temp10amc
    if counter == 10:
        temp10amc.value = str("{:.1f}".format((slider.value-32)/1.8)) + "°C"
    temp10amc.after(900, updatetemp10amc)
updatetemp10amc()

#4 PM time container
box = Box(app, width=165, height=42, layout="grid", border=1)
box0 = Box(box, width=158, height=20, grid=[0, 0])
text = Text(box0, text="4 PM READING", size=10)
box1 = Box(box, width=160, height=20, grid=[0, 1], layout='grid')
box2 = Box(box1, width=78, height=20, grid=[0, 0])
temp4pmf = Text(box2, text="°F", size=9, align="left")
box3 = Box(box1, width=82, height=20, grid=[1, 0])
temp4pmc = Text(box3, text="°C", size=9, align="right")
box = Box(app, height=10, width=280)

def updatetemp4pmf():
    global temp4pmf, lst
    if counter == 16:
        temp4pmf.value = str(slider.value) + "°F"
        lst.append(slider.value)
    temp4pmf.after(900, updatetemp4pmf)
updatetemp4pmf()
def updatetemp4pmc():
    global temp4pmc
    if counter == 16:
        temp4pmc.value = str("{:.1f}".format((slider.value-32)/1.8)) + "°C"
    temp4pmc.after(900, updatetemp4pmc)
updatetemp4pmc()

#10 PM time container
box = Box(app, width=165, height=42, layout="grid", border=1)
box0 = Box(box, width=158, height=20, grid=[0, 0])
text = Text(box0, text="10 PM READING", size=10)
box1 = Box(box, width=160, height=20, grid=[0, 1], layout='grid')
box2 = Box(box1, width=78, height=20, grid=[0, 0])
temp10pmf = Text(box2, text="°F", size=9, align="left")
box3 = Box(box1, width=82, height=20, grid=[1, 0])
temp10pmc = Text(box3, text="°C", size=9, align="right")
box = Box(app, height=30, width=280)

def updatetemp10pmf():
    global temp10pmf, lst
    if counter == 22:
        temp10pmf.value = str(slider.value) + "°F"
        lst.append(slider.value)
    temp10pmf.after(900, updatetemp10pmf)
updatetemp10pmf()
def updatetemp10pmc():
    global temp10pmc
    if counter == 22:
        temp10pmc.value = str("{:.1f}".format((slider.value-32)/1.8)) + "°C"
    temp10pmc.after(900, updatetemp10pmc)
updatetemp10pmc()

#minimum reading container
box = Box(app, width=165, height=42, layout="grid", border=1)
box0 = Box(box, width=158, height=20, grid=[0, 0])
text = Text(box0, text="Minimum reading", size=10)
box1 = Box(box, width=160, height=20, grid=[0, 1], layout='grid')
box2 = Box(box1, width=78, height=20, grid=[0, 0])
minf = Text(box2, text="°F", size=9, align="left")
box3 = Box(box1, width=82, height=20, grid=[1, 0])
minc = Text(box3, text="°C", size=9, align="right")
box = Box(app, height=10, width=280)

def updateminf():
    global lst, minf
    if counter == 22:
        minf.value = str(min(lst)) + "°F"
    minf.after(900, updateminf)
updateminf()
def updateminc():
    global lst, minc
    if counter == 22:
        minc.value = str("{:.1f}".format((slider.value-32)/1.8)) + "°C"
    minc.after(900, updateminc)
updateminc()



#max reading container
box = Box(app, width=165, height=42, layout="grid", border=1)
box0 = Box(box, width=158, height=20, grid=[0, 0])
text = Text(box0, text="Maximum reading", size=10)
box1 = Box(box, width=160, height=20, grid=[0, 1], layout='grid')
box2 = Box(box1, width=78, height=20, grid=[0, 0])
maxf = Text(box2, text="°F", size=9, align="left")
box3 = Box(box1, width=82, height=20, grid=[1, 0])
maxc = Text(box3, text="°C", size=9, align="right")
box = Box(app, height=10, width=280)

def updatemaxf():
    global lst, maxf
    if counter == 22:
        maxf.value = str(max(lst)) + "°F"
    maxf.after(900, updatemaxf)
updatemaxf()
def updatemaxc():
    global lst, maxc
    if counter == 22:
        maxc.value = str("{:.1f}".format((max(lst)-32)/1.8)) + "°C"
    maxc.after(900, updatemaxc)
updatemaxc()

#average container
box = Box(app, width=165, height=42, layout="grid", border=1)
box0 = Box(box, width=158, height=20, grid=[0, 0])
text = Text(box0, text="Average reading", size=10)
box1 = Box(box, width=160, height=20, grid=[0, 1], layout='grid')
box2 = Box(box1, width=78, height=20, grid=[0, 0])
avgf = Text(box2, text="°F", size=9, align="left")
box3 = Box(box1, width=82, height=20, grid=[1, 0])
avgc = Text(box3, text="°C", size=9, align="right")
boxclear = Box(app, height=10, width=280)

def updateavgf():
    global lst, avgf
    if counter == 22:
        average = sum(lst) / len(lst)
        avgf.value = str("{:.1f}".format(average)) + "°F"
    avgf.after(900, updateavgf)
updateavgf()

def updateavgc():
    global lst, avgc, temp4amc, temp4amf
    if counter == 22:
        average = sum(lst) / len(lst)
        avgc.value = str("{:.1f}".format((average-32)/1.8)) + "°C"
    avgc.after(900, updateavgc)
updateavgc()

#to clear previous day data
def clear():
    global milTime, counter, temp4amf, temp4amc, temp4pmf, temp4pmc, temp10amf, \
        temp10amc, temp10pmf, temp10pmc, minf, minc, maxf, maxc, avgf, avgc, lst
    if counter == -1:
        time.sleep(1)
        lst = []
        avgc.value = ""
        avgf.value = ""
        minf.value = ""
        minc.value = ""
        maxf.value = ""
        maxc.value = ""
        temp4amf.value = ""
        temp4amc.value = ""
        temp4pmf.value = ""
        temp4pmc.value = ""
        temp10amf.value = ""
        temp10amc.value = ""
        temp10pmf.value = ""
        temp10pmc.value = ""
def updateboxclear():
    global boxclear
    clear()
    boxclear.after(900, updateboxclear)
updateboxclear()



app.display()