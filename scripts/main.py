#!/usr/bin/env python

import numpy as np 
import datastructure as ds
import scipy.stats as ss
from astropy.table import Table
import matplotlib.pyplot as plt


datastructure = ds.DataStructure()

# Note: Software Sequences
# [ G1 , G2 , G3 , G4 , G5 ]
# [ SVG, WOT, TSR, PTN, COW]

A_G1 = [datastructure.SVG.A.temperatureIR,datastructure.SVG.A.noise,datastructure.SVG.A.time]
B_G1 = [datastructure.SVG.B.temperatureIR,datastructure.SVG.B.noise,datastructure.SVG.B.time]
C_G1 = [datastructure.SVG.C.temperatureIR,datastructure.SVG.C.noise,datastructure.SVG.C.time]
D_G1 = [datastructure.SVG.D.temperatureIR,datastructure.SVG.D.noise,datastructure.SVG.D.time]
E_G1 = [datastructure.SVG.E.temperatureIR,datastructure.SVG.E.noise,datastructure.SVG.E.time]

A_G2 = [datastructure.WOT.A.temperatureIR,datastructure.WOT.A.noise,datastructure.WOT.A.time]
B_G2 = [datastructure.WOT.B.temperatureIR,datastructure.WOT.B.noise,datastructure.WOT.B.time]
C_G2 = [datastructure.WOT.C.temperatureIR,datastructure.WOT.C.noise,datastructure.WOT.C.time]
D_G2 = [datastructure.WOT.D.temperatureIR,datastructure.WOT.D.noise,datastructure.WOT.D.time]
E_G2 = [datastructure.WOT.E.temperatureIR,datastructure.WOT.E.noise,datastructure.WOT.E.time]

A_G3 = [datastructure.TSR.A.temperatureIR,datastructure.TSR.A.noise,datastructure.TSR.A.time]
B_G3 = [datastructure.TSR.B.temperatureIR,datastructure.TSR.B.noise,datastructure.TSR.B.time]
C_G3 = [datastructure.TSR.C.temperatureIR,datastructure.TSR.C.noise,datastructure.TSR.C.time]
D_G3 = [datastructure.TSR.D.temperatureIR,datastructure.TSR.D.noise,datastructure.TSR.D.time]
E_G3 = [datastructure.TSR.E.temperatureIR,datastructure.TSR.E.noise,datastructure.TSR.E.time]

A_G4 = [datastructure.PTN.A.temperatureIR,datastructure.PTN.A.noise,datastructure.PTN.A.time]
B_G4 = [datastructure.PTN.B.temperatureIR,datastructure.PTN.B.noise,datastructure.PTN.B.time]
C_G4 = [datastructure.PTN.C.temperatureIR,datastructure.PTN.C.noise,datastructure.PTN.C.time]
D_G4 = [datastructure.PTN.D.temperatureIR,datastructure.PTN.D.noise,datastructure.PTN.D.time]
E_G4 = [datastructure.PTN.E.temperatureIR,datastructure.PTN.E.noise,datastructure.PTN.E.time]

A_G5 = [datastructure.COW.A.temperatureIR,datastructure.COW.A.noise,datastructure.COW.A.time]
B_G5 = [datastructure.COW.B.temperatureIR,datastructure.COW.B.noise,datastructure.COW.B.time]
C_G5 = [datastructure.COW.C.temperatureIR,datastructure.COW.C.noise,datastructure.COW.C.time]
D_G5 = [datastructure.COW.D.temperatureIR,datastructure.COW.D.noise,datastructure.COW.D.time]
E_G5 = [datastructure.COW.E.temperatureIR,datastructure.COW.E.noise,datastructure.COW.E.time]


data_List =  np.array([[A_G1, A_G2, A_G3, A_G4, A_G5],
             [B_G1, B_G2, B_G3, B_G4, B_G5],
             [C_G1, C_G2, C_G3, C_G4, C_G5],
             [D_G1, D_G2, D_G3, D_G4, D_G5],
             [E_G1, E_G2, E_G3, E_G4, E_G5]])


# Note: Mean_Temp_Noise return mean values of data types
# For the current use case, the input "data" has 3 dimensions
# the 1st dimension : no of laptops
# the 2nd dimension : no of Games/Observations
# the last dimension: no of types of data collected (such as temp, noise)
# Therefore, 
# Output : mean value of data in 3 dimensions
def mean_Std(data):
    # check the shape of the data
    data_Shape = data.shape
    data_mean_return = np.zeros(data.shape)
    data_grandMean = np.zeros((data_Shape[0],data_Shape[2]))
    data_std = np.zeros((data_Shape[0],data_Shape[2]))
    for i in range(0,data_Shape[0]):
        for j in range(0,data_Shape[1]):
            for k in range(0,data_Shape[2]):
                data_mean_return[i][j][k] = round(np.mean(data_List[i,j,k]),2)
    for eachLaptop in range(data_Shape[0]):
        for eachData in range(data_Shape[2]):
            data_grandMean[eachLaptop][eachData]=round(np.mean(data_mean_return
                          [eachLaptop,:,eachData]),2) 
            data_std[eachLaptop][eachData]=round(np.std(data_mean_return
                          [eachLaptop,:,eachData],ddof=1),2) 
            
    return data_mean_return, data_grandMean,data_std


# input1 of table function : Table title (string type)
# input2 of table function : dType: 0: temp
#                                   1: noise
def table(title,dType):
    row_names = ['1','2','3','4','5','Mean','Std']
    column_names = ['Observation\Laptop','A','B','C','D','E']
    mean_std = mean_Std(data_List)
    data_Rows = [(row_names[0],mean_std[0][0,0,dType],mean_std[0][1,0,dType],
                  mean_std[0][2,0,dType],mean_std[0][3,0,dType],
                  mean_std[0][4,0,dType]),
                 (row_names[1],mean_std[0][0,1,dType],mean_std[0][1,1,dType],
                  mean_std[0][2,1,dType],mean_std[0][3,1,dType],
                  mean_std[0][4,1,dType]),
                 (row_names[2],mean_std[0][0,2,dType],mean_std[0][1,2,dType],
                  mean_std[0][2,2,dType],mean_std[0][3,2,dType],
                  mean_std[0][4,2,dType]),
                 (row_names[3],mean_std[0][0,3,dType],mean_std[0][1,3,dType],
                  mean_std[0][2,3,dType],mean_std[0][3,3,dType],
                  mean_std[0][4,3,dType]),
                 (row_names[4],mean_std[0][0,4,dType],mean_std[0][1,4,dType],
                  mean_std[0][2,4,dType],mean_std[0][3,4,dType],
                  mean_std[0][4,4,dType]),
                 (row_names[5],mean_std[1][0,dType],mean_std[1][1,dType],
                  mean_std[1][2,dType],mean_std[1][3,dType],
                  mean_std[1][4,dType]),
                 (row_names[6],mean_std[2][0,dType],mean_std[2][1,dType],
                  mean_std[2][2,dType],mean_std[2][3,dType],
                  mean_std[2][4,dType])]
    table = Table(rows = data_Rows, names = column_names)
    print(table)
    print(title)


# input1 of anova_Analysis : data_List(Laptops, Games, data such as temp,noise)
# input2 of anova_Analysis : dType (specify data which you want to analyse )
#                            dType: 0 for Temp, 1 for Noise)
def anova_Analysis(data_list,dType):
    dataType = {0: 'Temperatures', 1: 'Noises'}
    mean_data = mean_Std(data_list)
    F,p = ss.f_oneway(mean_data[0][0,:,dType],mean_data[0][1,:,dType],
                            mean_data[0][2,:,dType],mean_data[0][3,:,dType],
                            mean_data[0][4,:,dType])
    print("\n")
    if(p<0.05):
        print("The mean values of Laptop "+dataType[dType]+""" are 
              statistically significant. Therefore, we reject the null
              hypothesis""")
    elif(p>0.05):
        print("The mean values of Laptop "+dataType[dType]+""" are 
              not statistically significant. Therefore, we failed to reject 
              the null hypothesis""")
    


# plot function plot 
# input 1 : laptop X you would like to observe( you may refer laptopDict in Fn)
# input 2 : game Y you would ike observe (you may refer gameDict in Fn)
# input 3 : data you would like to plot (you may refer axisDict in Fn)
# input 4 : main data you have to put
def multiplot(laptop,game,data,data_list):
    plt.figure()
    x_axis = data[0]
    y_axis = data[1]
    laptopDict = {0:'A',1:'B',2:'C',3:'D',4:'E'}
    gameDict = {0:'G1',1:'G2',2:'G3',3:'G4',4:'G5'}
    axisDict = {0:'Temp',1:'Noise',2:'Time'}
    for i in laptop:
        data_label = ' '
        for j in game:
            data_label = laptopDict[i]+'_'+gameDict[j]
            plt.plot(data_list[i][j][x_axis],data_list[i][j][y_axis],
                     label = data_label)
            plt.xlabel(axisDict[x_axis])
            plt.ylabel(axisDict[y_axis])
            plt.legend(loc='upper right')
            plt.show()
            

def tukeyComparison(data_list,dType):
    k = len(data_List[0])
    n= k**2
    dof = [k,n-k]
    # q table is read from the following link
    #https://www2.stat.duke.edu/courses/Spring98/sta110c/qtable.html
    q_critical_0_05 = 4.23
    mean_std = mean_Std(data_list)
    for each in mean_std[2][:,dType]:
            SSW = (k-1)*each**2 
    MSW = SSW/dof[1]
    T = q_critical_0_05*np.sqrt(MSW/k)
    mean = mean_std[1][:,dType]
    rejected_Dict = {}
    accepted_Dict = {}
    laptop_Dict = {0:'A',1:'B',2:'C',3:'D',4:'E'}
   
    
    for i in laptop_Dict.keys():
        for j in laptop_Dict.keys():
            diff = round(mean[i]-mean[j],2)
           
            key = laptop_Dict.get(i)+laptop_Dict.get(j)
            if(abs(diff)==0):
                pass 
            elif(abs(diff)>T):
                rejected_Dict.update({key:abs(diff)})
               
            elif(abs(diff)<T):
                accepted_Dict.update({key:abs(diff)})
                
    accepted_Tuple = sorted(accepted_Dict.items(), key=lambda diff: abs(diff[1]))
    rejected_Tuple = sorted(rejected_Dict.items(), key=lambda diff: abs(diff[1]))
        
    [print("Accepted Pair",each) for each in accepted_Tuple]
    print("\n")
    [print("Rejected Pair",each) for each in rejected_Tuple]
    return accepted_Tuple, rejected_Tuple
           
            
table("Table 1: Temperature of Laptops across 5 observations",0)
print("\n")
table("Table 2: Noise of Laptops across 5 observations",1)         
anova_Analysis(data_List,0)
anova_Analysis(data_List,1)
multiplot([0,1,2,3,4],[0,1,2,3,4],[2,1],data_List)
result = tukeyComparison(data_List,0)



                
            
                
            
    
    





    



