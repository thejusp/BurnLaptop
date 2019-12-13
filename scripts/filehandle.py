#!/usr/bin/env python

import os
import pandas
import yaml
from fnmatch import fnmatch  

def fetchFile(root,pattern):
    filelist = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                filelist.append(os.path.join(path, name))
    return filelist 


def getConfig(filename):

    with open(filename) as f:
        docs = yaml.load_all(f)
        dat = []
        for doc in docs:
            for k, v in doc.items():
                dat.append(v)
    return dat


def printList(in_list):
    for i in in_list:
        print (i)

def parseData(file_name):

    try:    
        df          = pandas.read_csv(file_name)
        array_frame = df.values
        time        = df.values[:,0]/1000
        temp        = df.values[:,3]
        temp_ir     = df.values[:,4]
        noise       = df.values[:,5]

    except:

        print ("Error: Filehandle: " +  file_name + "does not exist")



    # plt.plot(time, temp_ir)
    # plt.show()

    return [time, temp, temp_ir, noise]


