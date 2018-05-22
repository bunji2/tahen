# encoding: utf8

import numpy as np
import pandas as pd

# p35
csvfile = "tab3.1.csv"
data = pd.read_csv(csvfile, index_col=0)
print "----", csvfile, "----"
print data

col_x,col_y = '面接の成績','現在の実力'

def shiki_3_3(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    #print x, y, mean_x, mean_y
    rx = x - mean_x
    ry = y - mean_y
    return np.sum(rx*ry) / np.sqrt(np.sum(rx*rx)*np.sum(ry*ry))

x = data[col_x].values
y = data[col_y].values

print "----"
print col_x.decode('utf8'), '-', col_y.decode('utf8')
print "r =".decode('utf8'), shiki_3_3(x, y)

#P46
csvfile = "tab3.6.csv"
data = pd.read_csv(csvfile, index_col=0)
print "----", csvfile, "----"
print data
col_x,col_y = '結果','予想'
x = data[col_x].values
y = data[col_y].values
print "----"
print col_x.decode('utf8'), '-', col_y.decode('utf8')
print "r =".decode('utf8'), shiki_3_3(x, y)
