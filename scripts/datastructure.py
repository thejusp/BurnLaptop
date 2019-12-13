#!/usr/bin/env python

import filehandle as fh
import syshandle as sysH


class DataStructure:
    
    def __init__(self):


        self.COW = Game("COW")
        self.PTN = Game("PTN")
        self.SVG = Game("SVG")
        #self.TRA = Game("TRA")
        #self.TRB = Game("TRB")
        self.TSR = Game("TSR")
        self.WOT = Game("WOT")


class Game:
    def __init__(self,game):

        self.A = Laptop("A", game)
        self.B = Laptop("B", game)
        self.C = Laptop("C", game)
        self.D = Laptop("D", game)
        self.E = Laptop("E", game)


class Laptop:
    
    def __init__(self, model, gametype):

        data = fh.parseData(self.filenameGenerator(model,gametype))
        self.temperature   = data[1]
        self.time          = data[0]
        self.temperatureIR = data[2]
        self.noise         = data[3]
     
        


    
    def filenameGenerator(self,model, gametype):            
        LinuxDelimiter =   '/'
        game = model + '_' + gametype.lower() + '.csv'
        fname = str(fh.getConfig("config.yaml")[1]) + LinuxDelimiter + 'RM_Experiments' + LinuxDelimiter + gametype + LinuxDelimiter + model + LinuxDelimiter + game
        print(fname)
        return fname


