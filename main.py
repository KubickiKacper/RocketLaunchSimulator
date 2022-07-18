import rocket as R
import calculations as C
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow, QVBoxLayout,QHBoxLayout,QLabel
from PyQt5.QtGui import  QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

class MainWindow(QWidget):

    def Start(self):
        F9FT=R.Rocket()
        axA=self.AccelerationFigure.subplots()
        axA.grid()
        axA.set_title("Acceleration")
        axA.set_xlabel("seconds")
        axA.set_ylabel("m/s^2")
        
        axA.set_xlim(0,F9FT._Rocket__FirstStageTime+F9FT._Rocket__SecondStageTime+10)
        axA.set_ylim(-10,40)
        lineA=C.Functions.Acceleration(F9FT,self.AccelerationFigure,axA)
        
        self.canvasA.draw()
       

        axV=self.VelocityFigure.subplots()    
        axV.grid()
        axV.set_title("Velocity")
        axV.set_xlabel("seconds")
        axV.set_ylabel("km/h")
        axV.set_xlim(0,F9FT._Rocket__FirstStageTime+F9FT._Rocket__SecondStageTime+10)
        axV.set_ylim(0,20000)
        lineV=C.Functions.Velocity(F9FT,self.VelocityFigure,axV)
    
        
        self.canvasV.draw()

        C.Functions.FirstStagePlot(F9FT)
        C.Functions.SecondStagePlot(F9FT)
        C.Functions.VelocityPlot(F9FT)



    def __init__(self, app):
        super().__init__()
        
        self.setFixedSize(1300, 875)
        self.setStyleSheet("background-color:white ")

        self.layout=QVBoxLayout()
        self.blankspace1=QWidget()
        self.blankspace1.setFixedHeight(10)
        self.blankspace2=QWidget()
        self.blankspace2.setFixedHeight(10)


        self.ButttonLayout=QHBoxLayout()
        self.StartButton=QPushButton("START")
        self.StartButton.clicked.connect(self.Start)
        self.StartButton.setStyleSheet("QPushButton{background-color:#03DAC6 ;font-size:35px;border-radius: 10px; min-width: 10em; padding: 6px}"
                                       "QPushButton:pressed { background-color:#e9ecef ;font-size:32px;border-radius: 10px; min-width: 10em; padding: 6px }" )
        self.StartButton.setFixedHeight(100)
        self.ButttonLayout.addWidget(self.blankspace1)
        self.ButttonLayout.addWidget(self.StartButton)
        self.ButttonLayout.addWidget(self.blankspace2)
        self.layout.addLayout(self.ButttonLayout)

        self.MenuLayout=QHBoxLayout()
        self.Plots=QVBoxLayout()
        self.RocketImageLayout=QVBoxLayout()
        
       
        self.AccelerationFigure=Figure()  
        self.VelocityFigure=Figure()
        
        
        
        self.canvasA = FigureCanvas(self.AccelerationFigure)
        
        self.canvasV = FigureCanvas(self.VelocityFigure)
        
      
        self.VelocityPlot=QWidget()
        
        self.RocketImage=QLabel()
       
        self.RocketPixmap=QPixmap('RocketImage1.png')
        self.RocketImage.setPixmap(self.RocketPixmap)
        self.RocketImage.setFixedWidth(100)
        
        self.RocketImageLayout.addWidget(self.RocketImage)

       
        self.Plots.addWidget(self.canvasA)
        self.Plots.addWidget(self.canvasV)

        self.MenuLayout.addLayout(self.Plots)
        self.MenuLayout.addLayout(self.RocketImageLayout)
        self.layout.addLayout(self.MenuLayout)

        self.setLayout(self.layout)
        self.show()


app=QApplication([])
new=MainWindow(app)
app.exec_()

#ChangeToTestActions1

