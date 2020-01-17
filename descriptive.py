#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:29:51 2020

@author: yash
"""
#import numpy as np
#from statistics import mode,stdev
import csv

with open('iris.csv','r') as file:
    
    def mean(data):
        addition = 0.0
        for i in range(0,len(data)-1):
            addition += float(data[i][0])
        mean = addition/len(data)
        return mean
        
    def median(data):
        list1 = []
        for i in range(0,len(data)-1):
            list1.append(float(data[i][0]))
        list1.sort()
        mid = len(data)//2
        return list1[mid]
        #l  = variance(list1)
        #print(l)
        
    def mode1(data):
        count = {}
        for i in range(len(data)-1):
            check = data[i][0]
            if check in count:
                count[check] +=1
            else:
                count[check] =1
        a = max(count.values())
        for k,values in count.items():  
            if values == a:
                return k
                
    def Std_D(data):
        avg = mean(data)
        sd = 0.0        
        for i in range(len(data)-1):
            val = float(data[i][0])
            #print(val)
            sd += (avg - val) **2 
            #print(sd)
        s = sd/len(data)
        std = s ** 0.5
        return std;

    def variance(data):
        a = Std_D(data)
        var = a**2
        return var
    
    def rangee(data):
        list1 = []
        for i in range(0,len(data)-1):
            list1.append(float(data[i][0]))
        list1.sort()
        rang = list1[-1] - list1[0]
        return rang        


    read = list(csv.reader(file, delimiter = ','))
    
    m = mean(read)
    print("MEAN IS : ",m)
    
    s = Std_D(read)
    print("Standard Deviation : ",s)    
    
    mi = median(read)
    print("MEDIAN IS : ",mi)  
    
    mo = mode1(read)
    print("MODE IS : ",mo)
    
    v = variance(read)
    print("Variance is : ",v)
    
    r = rangee(read)
    print("Range is : ",r)
    
    
"""    a = np.median(list1)
    print(a)
    b = mode(list1)
    print(b)
    c = stdev(list1)
    print(c)
""" 