# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:27:55 2018

@author: msval
"""
difference=[]
error=[]
totalerror=0.0
for acc in range(0,200):
    
    if(y_test[acc]!=0):
        difference.append(prediction1[acc]-float(y_test[acc]))
        error.append(difference[acc]/float(y_test[acc]))
        totalerror+=error[acc]
    else:
        difference.append(0)
        error.append(0)
accuracy=totalerror/200
print("The accuracy of the prediction model = "+str(100-abs(-accuracy*100)));