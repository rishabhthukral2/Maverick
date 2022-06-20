from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import webbrowser as web
import sys
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
import Main
from MaverickUi import Ui_MainWindow

class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.BestVer()              
          
startFunctions = MainThread()           #variable defined

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.maverick_ui = Ui_MainWindow()
        
        self.maverick_ui.setupUi(self)

        self.maverick_ui.pushButton.clicked.connect(self.startFunc)  # start button to start maverick gui

        self.maverick_ui.pushButton_2.clicked.connect(self.close)   #end maverick predefined in pyqt5

        self.maverick_ui.pushButton_3.clicked.connect(self.YouTubeButton)

        self.maverick_ui.pushButton_6.clicked.connect(self.VsCode)

        self.maverick_ui.pushButton_4.clicked.connect(self.WhatsappButton)

        self.maverick_ui.pushButton_5.clicked.connect(self.ChromeButtom)

    def YouTubeButton(self):
        web.open("https://www.youtube.com/")

    def ChromeButtom(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def WhatsappButton(self):
        web.open("https://web.whatsapp.com/")

    def VsCode(self):
        os.startfile(r"C:\Users\Rishabh\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    def startFunc(self):

        self.maverick_ui.movies_2 = QtGui.QMovie("D:\\mlmaverick\\G.U.I Material\\VoiceReg\\Siri_1.gif")  #path given

        self.maverick_ui.label_2.setMovie(self.maverick_ui.movies_2)        #set the path

        self.maverick_ui.movies_2.start()       #start the gui


        self.maverick_ui.movies_3 = QtGui.QMovie("D:\\mlmaverick\\G.U.I Material\\ExtraGui\\live.gif")

        self.maverick_ui.label_3.setMovie(self.maverick_ui.movies_3)

        self.maverick_ui.movies_3.start()


        self.maverick_ui.movies_5 = QtGui.QMovie("D:\\mlmaverick\\G.U.I Material\\B.G\\Iron_Template_1.gif")

        self.maverick_ui.label.setMovie(self.maverick_ui.movies_5)

        self.maverick_ui.movies_5.start()

        self.maverick_ui.movie = QtGui.QMovie("D:\\mlmaverick\\G.U.I Material\\ExtraGui\\Earth.gif")

        self.maverick_ui.label_7.setMovie(self.maverick_ui.movie)

        self.maverick_ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startFunctions.start()          # it will start the mainThread() function 

    def showtime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        labbel = " Current Time :  " + label_time 
        label_date = now.toString(Qt.ISODate)
        labdsbdh = " Today's Date : " + label_date
        self.maverick_ui.textBrowser_3.setText(labbel)
        self.maverick_ui.textBrowser_2.setText(labdsbdh)

Gui_App = QApplication(sys.argv)
Gui_Maverick = Gui_Start()
Gui_Maverick.show()     #to show the file we created
exit(Gui_App.exec_())   #to exit the app if we want to exit
