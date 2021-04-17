class Rocket():

    def __init__(self):  
        self.__TotalMass=541300
        self.__FuelMass=507500
        self.__EffectiveExhaustVelocity=5544

        self.__FirstStageEngineCombustion=273.6*9
        self.__FirstStageTime=162
        self.__FirstStageThrust=6806*10**3
        self.__FirstStageModuleMass=25600
        self.__FirstStageFuelMass=373309

        self.__SecondStageEngineCombsution=273.6
        self.__SecondStageTime=397
        self.__SecondStageThrust=934*10**3
        self.__SecondStageModuleMass=4000
