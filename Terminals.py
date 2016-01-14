import os
from datetime import time
import datetime

x = 0
hour =str(datetime.datetime.now().hour)
Time = datetime.datetime.now()

while x < 2:
        os.system("gnome-terminal")
        x = x + 1
#os.system("google-chrome www.arstechnica.co.uk")
os.system("clear")
os.system("gnome-terminal --window-with-profile=Unnamed -e '/usr/bin/newsbeuter'")
if (int(hour) >= 12) :
       print"Good Afternoon Sir, the current date and time is"
       print str(Time)  
else:
        print "Good Morning Sir, the current date and time is"
        print str(Time)
#os.system("xchat")
~                                                                  
~                            
