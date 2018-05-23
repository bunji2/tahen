# encoding: utf8

import numpy as np
import pandas as pd

# p35
csvfile = "tab4.1.csv"
data = pd.read_csv(csvfile, index_col=0)
print "----", csvfile, "----"
print data

#data2 = data.copy()
#data3 = pd.DataFrame(index=data.index, columns=data.columns, dtype='float16')

# 各行の小計を追加
print "----"

sum1 = []
for index in data.index:
    #print index.decode('utf8')
    sum1.append(np.sum(data.loc[index].values))

#print sum1

subtotals1 = pd.DataFrame(sum1, index=data.index, columns=['小計'])
print subtotals1

# 列の追加
#data['小計'] = sum1
#print data

# 各列の小計を追加
print "----"

sum2 = []
for column in data.columns:
    #print column.decode('utf8')
    sum2.append(np.sum(data[column].values))

#print sum2

subtotals2 = pd.DataFrame([sum2], index=['小計'], columns=data.columns)
print subtotals2

# 行の追加
#data.loc['小計'] = sum2
#print data

print "----"
total = np.sum(sum1)
print "合計 =".decode('utf8'), total

# 期待値の計算
print "----"
data2 = data.copy()

for index in data.index:
    print index.decode('utf8')
    subtotal1 = float(subtotals1.loc[index, '小計'])
    for column in data.columns:
        subtotal2 = float(subtotals2.loc['小計', column])
        print subtotal1, subtotal2, total
        data2.loc[index,column] = subtotal1*subtotal2/total

print data2

print "----"

data3 = data2 - data
data3 = data3 * data3 / data2
print data3

print "合計 =".decode('utf8'), np.sum(data3.values)
quit()
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
print "r =", shiki_3_3(x, y)

#P48

def shiki_3_10(x, y):
    sxy = np.sum((x - np.mean(x))*(y - np.mean(y))) / len(x)
    sx = np.sqrt(np.var(x))
    sy = np.sqrt(np.var(y))
    return sxy/(sx*sy)

col_x, col_y = '結果', '予想'
x = data[col_x].values
y = data[col_y].values
print "----"
print col_x.decode('utf8'), '-', col_y.decode('utf8')
print "r =", shiki_3_10(x, y)
