&quot;&quot;&quot;
Michael Hoyle
ITN160-4C1
Create app to score spelling bee competition.
&quot;&quot;&quot;
# Global constants
APP_WIDTH = 525
APP_HEIGHT = 275
from guizero import *
def main():
def file_function(): # Menu function
print(&quot;File option&quot;)

app = App(title=&#39;Spelling Bee Control Panel&#39;, bg=&#39;light gray&#39;,
width=APP_WIDTH, height=APP_HEIGHT, layout=&#39;auto&#39;)
win1 = Window(app, title=&quot;Contestant 1 Score&quot;, width=250, height=275)
win2 = Window(app, title=&quot;Contestant 2 Score&quot;)
round = PushButton(app, text=&#39;Start New Round&#39;, width=25, height=2,
align=&#39;top&#39;)
round.text_size = 20
round.text_color = &#39;green&#39;
display_box1 = Box(app, border=True, height=100, width=200, align=&#39;left&#39;)
Text(display_box1, text=&#39;Contestant 1&#39;, size=20, color=&#39;navy blue&#39;)
correct1 = PushButton(display_box1, text=&quot;Correct&quot;)
correct1.text_size = 15
correct1.text_color = &#39;navy blue&#39;
correct1.disable()
display_box2 = Box(app, border=True, height=100, width=200,
align=&#39;right&#39;)
Text(display_box2, text=&#39;Contestant 2&#39;, size=20, color=&#39;maroon&#39;)
correct2 = PushButton(display_box2, text=&#39;Correct&#39;)
correct2.text_size = 15
correct2.text_color = &#39;maroon&#39;
correct2.disable()
Text(win1, text=&quot;Welcome Mike&quot;)
Text(win2, text=&quot;Welcome Elizabeth&quot;)
MenuBar(app,
toplevel=[&quot;File&quot;],
options=[
[[&quot;Exit Program&quot;, exit]]])

app.display()

if __name__ == &#39;__main__&#39;:
main()