from cmu_112_graphics import *
from tkinter import *
from VideoClient import *
from VideoServer import *
from threading import Thread

class HomeMode(Mode):

    def redrawAll(mode, canvas):
        rectWidth = 100
        rectHeight = 50
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text='Welcome to the video streamer!', font=font)
        canvas.create_text(mode.width/2, 200, text='This application will allow you to stream video:', font=font)
        canvas.create_rectangle(mode.width/3,300, (mode.width/3)+rectWidth,300 + rectHeight)
        canvas.create_rectangle(mode.width-(mode.width / 3), 300, mode.width-(mode.width / 3)-rectWidth, 300+rectHeight)
        canvas.create_text((mode.width/3)+rectWidth/2,300+rectHeight/2, text='Watch', font=20)
        canvas.create_text((mode.width-(mode.width / 3))-(rectWidth)/2, 300+rectHeight/2, text='Stream', font="15")

    def mousePressed(mode, event):
        rectWidth = 100
        rectHeight = 50
        if event.x > mode.width/3 and event.x < mode.width/3 + rectWidth:
            if event.y < 350 and event.y > 300:
                HOST = mode.getUserInput('What is the server IP?')
                ConnectingClientThread = Thread(target=runVideoClient, args = (HOST,))
                ConnectingClientThread.start()

        if event.x < (mode.width-(mode.width / 3)) and event.x >(mode.width-(mode.width / 3)-rectWidth):
            if event.y < 350 and event.y > 300:
                HOST = mode.getUserInput('What is the server your IP?')
                ServerThread = Thread(target=runVideoServer, args = (HOST,))
                HostingClientThread = Thread(target=runVideoClient, args = (HOST,))
                ServerThread.start()
                HostingClientThread.start()

class watchMode(Mode):
    def appStarted(mode):
        pass

    def redrawAll(mode, canvas):
        canvas.create_text(mode.width/2, 150, text='What is the server IP?', font=10)

class hostMode(Mode):
    def redrawAll(mode, canvas):
        canvas.create_text(mode.width / 2, 150, text='What is the your server IP?', font=10)

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = HomeMode()
        app.watchMode = watchMode()
        app.hostMode = hostMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=1000, height=500)