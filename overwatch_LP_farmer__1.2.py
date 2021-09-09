import datetime
import time
import schedule
import webbrowser
import win32api, win32con


#We indert the dates here // [DAY, HOUR, MONTH]
dates = [[8, 18, 9], [22, 10, 9], [23, 10, 9], [23, 12, 9], [24, 10, 9], [25, 12, 9], [26, 12, 9]]

#This funnction executes the click
def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#THis function executes the task that we gave it, in this case we have make it open the overwatch league channel and click in the pixel position where live videos are dsplays (The program is meant for 1080p monitors, if yours isnt you have to adjust the pixel psotion by yourself)
def job():
    webbrowser.open('https://www.youtube.com/c/overwatchleague') #Overwatch league channel link
    time.sleep(2) #freeze the rpogram for two seconds just in casa
    click(550, 600) #clcik

count = 0
cicle = True

#This cicle willl execute until a valid hour comes in
while (cicle == True):
    count+=1
    date = datetime.datetime.now()# We get the actual date
    for i in dates:
        day = i[0]
        hour = i[1]
        month = i[2]

        #once the moment has come we execute the task
        if(date.day == day and date.month == month):
            if(date.hour == hour and date.minute >= 10):
                job() # Task
                time.sleep(1)
                cicle = False; # We close the program
    if count >= 540:#If the time doesnt come in 9 hours the program closes itself
        cicle = False
    time.sleep(60)
