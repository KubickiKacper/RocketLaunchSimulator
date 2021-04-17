import rocket as R
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Functions(R.Rocket):
    """ Klasa dziedzicząca klase Rocket. Klasa zawiera wszystkie niezbędne funkcje slużące do przeprowadzenia symulacji startu rakiety Falcon F9FT"""


    def Velocity(self,fig,ax):
        """Funkcja sluzy stworzeniu animacji, przedstawiającej wykres prędkości od czasu rakiety. 
      Funkcja oblicza predkość rakiety ze wzoru Ideal Rocket Equiation: V= Ve *ln(m0/mf), gdzie V to aktualna prędkość, Ve to impuls właściwy silników, m0 to masa początkowa rakiety,
      mf masa końcowa rakiety."""
        def VelocityAnimation(time):

            V=self._Rocket__EffectiveExhaustVelocity*np.log(self._Rocket__TotalMass/Functions.ActuallMass(self,time))
            y_data.append(V) 
            x_data.append(time)

            line.set_xdata(x_data)
            line.set_ydata(y_data)
            line.set_color('#03DAC6')

            if x_data[-1] > self._Rocket__FirstStageTime+self._Rocket__SecondStageTime-2:
                ani._stop()
                
            
            return line,

            
        x_data=[]
        y_data=[]

       
        line,= ax.plot(0,0)
        ax.set_facecolor('#e9ecef')

        ani=FuncAnimation(fig,func=VelocityAnimation,frames=np.arange(0,self._Rocket__FirstStageTime+self._Rocket__SecondStageTime,1),interval=100)

        return ani

    def ActuallMass(self,time):
        """Funkcja zwracajaca aktualna mase rakiety, sluży głownie do pracy z funkcjami rysującymi wykresy. """
        Array=time<=self._Rocket__FirstStageTime
        Result=np.zeros_like(time)
        Result[Array==True]=(self._Rocket__TotalMass-(self._Rocket__FirstStageEngineCombustion*time[Array==True]))
        Result[Array==False]=((self._Rocket__TotalMass-self._Rocket__FirstStageFuelMass-self._Rocket__FirstStageModuleMass)-(self._Rocket__SecondStageEngineCombsution*(time[Array==False]-self._Rocket__FirstStageTime)))
        return Result
   
    def FirstStagePlot(self):
        """Funkcja zapisująca wykres przyspieszenia od czasu pierwszego etapu startu rakiety."""
        def FirstStageAcceleration(time):
            return (self._Rocket__FirstStageThrust-(Functions.ActuallMass(self,time)*9.81))/(self._Rocket__TotalMass-(self._Rocket__FirstStageEngineCombustion*time))
   
        FirstStageTime=np.arange(0,self._Rocket__FirstStageTime,1)      
        plt.plot(FirstStageTime,FirstStageAcceleration(FirstStageTime))
        plt.title("First Stage Acceleration")
        plt.xlabel("Seconds")
        plt.ylabel('m/s^2')
        plt.xlim(0)
        plt.ylim(0)
        plt.grid()
        plt.savefig("FirstStageAcceleration.png")
        plt.cla()
        

    def SecondStagePlot(self):
        """Funkcja zapisująca wykres przyspieszenia od czasu drugiego etapu startu rakiety."""
        def SecondStageAcceleration(time):     
            return (self._Rocket__SecondStageThrust-(Functions.ActuallMass(self,time)*9.81))/((self._Rocket__TotalMass-self._Rocket__FirstStageFuelMass-self._Rocket__FirstStageModuleMass)-(self._Rocket__SecondStageEngineCombsution*(time-self._Rocket__FirstStageTime)))

        SecondStageTime=np.arange(self._Rocket__FirstStageTime,self._Rocket__SecondStageTime+self._Rocket__FirstStageTime,1)      
        plt.plot(SecondStageTime,SecondStageAcceleration(SecondStageTime))
        plt.title("Second Stage Acceleration")
        plt.xlabel("Seconds")
        plt.ylabel('m/s^2')
        plt.xlim(self._Rocket__FirstStageTime+1)
        plt.grid()
        plt.savefig("SecondStageAcceleration.png")
        plt.cla()

    def VelocityPlot(self):
        """Funkcja zapisująca wykres prędkosci od czasu całej symulacji."""
        def VelocityPlot(time):
            return self._Rocket__EffectiveExhaustVelocity*np.log(self._Rocket__TotalMass/Functions.ActuallMass(self,time))

        VelocityTime=np.arange(0,self._Rocket__FirstStageTime+self._Rocket__SecondStageTime,1)
        plt.plot(VelocityTime,VelocityPlot(VelocityTime))
        plt.title("Velocity")
        plt.xlabel("Seconds")
        plt.ylabel('km/h')
        plt.xlim(0)
        plt.ylim(0)
        plt.grid()
        plt.savefig("Velocity.png")
        plt.cla()

    

    def Acceleration(self,fig,ax):
        """Funkcja sluzy stworzeniu animacji, przedstawiającej wykres przyspieszenia od czasu rakiety. """

        def FirstStageAcceleration(time):
            return (self._Rocket__FirstStageThrust-(Functions.ActuallMass(self,time)*9.81))/(self._Rocket__TotalMass-(self._Rocket__FirstStageEngineCombustion*time))
   
        def SecondStageAcceleration(time):
            return (self._Rocket__SecondStageThrust-(Functions.ActuallMass(self,time)*9.81))/((self._Rocket__TotalMass-self._Rocket__FirstStageFuelMass-self._Rocket__FirstStageModuleMass)-(self._Rocket__SecondStageEngineCombsution*(time-self._Rocket__FirstStageTime)))


        x_data=[]
        y_data=[]

       
        line,= ax.plot(0,0)
        ax.set_facecolor('#e9ecef')

        def AccelerationAnimation(time):
            Array1=time<=self._Rocket__FirstStageTime
           
            
        
            if Array1==True:
                y_data.append(FirstStageAcceleration(time))             
            else:
                 y_data.append(SecondStageAcceleration(time))

            x_data.append(time)
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            line.set_color('#03DAC6')
            if x_data[-1] > self._Rocket__FirstStageTime+self._Rocket__SecondStageTime-2:
                ani._stop()
                
            
            return line,

        time=np.arange(0,self._Rocket__FirstStageTime+self._Rocket__SecondStageTime,1)
        ani=FuncAnimation(fig,func=AccelerationAnimation,frames=time,interval=100)
        

        return ani
       
