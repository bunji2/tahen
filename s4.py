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

#p59
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

#p61
print "----"

data3 = data2 - data
data3 = data3 * data3 / data2
print data3

print "合計 =".decode('utf8'), np.sum(data3.values)

#p63
print "----"

#print data3.shape, np.min(data3.shape), np.max(data3.shape)
Nmin = np.min(data3.shape)
N = total

q = np.sqrt(np.sum(data3.values)/(N*(Nmin-1)))
print "q =", q

# p64
csvfile = "tab4.5.csv"
data = pd.read_csv(csvfile, index_col=0)
print "----", csvfile, "----"
print data

def calc_every_means_and_total_mean(data):
    d = []
    mean1 = []
    for index in data.index:
        #print index.decode('utf8')
        mean1.append(np.mean(data.loc[index].values))
        d.extend(data.loc[index].values)
    means = pd.DataFrame(mean1, index=data.index, columns=['平均'])
    return means, np.sum(d), np.mean(d)

# 各行の平均を計算
print "----"


#print sum1

means, total_sum, total_mean = calc_every_means_and_total_mean(data)

print means
print '全平均 ='.decode('utf8'), total_mean

print "----", "tab4.6", "----"
data2 = data - total_mean
print data2
_, total_sum, _ = calc_every_means_and_total_mean(data2)
print '合計 ='.decode('utf8'), total_sum

data2 = data2 * data2
print data2
_, total_sum, _ = calc_every_means_and_total_mean(data2)
print '合計 ='.decode('utf8'), total_sum

print "----", "kitai", "----"
kitai = data.copy()
for column in data.columns:
    kitai[column] = means['平均'].values
print kitai

# p67
print "----", "tab4.8", "----"
data3 = kitai - total_mean
print data3
data3 = data3 * data3
print data3

_, total_sum2, _ = calc_every_means_and_total_mean(data3)

print '合計 ='.decode('utf8'), total_sum2

# p68
print 'p =', np.sqrt(total_sum2 / total_sum)

def shiki_4_1(data):
    d = []
    means = []
    for index in data.index:
        #print index.decode('utf8')
        means.append(np.mean(data.loc[index].values))
        d.extend(data.loc[index].values)
    total_sum = np.sum(d)
    total_mean = np.mean(d)
    kitai = data.copy()
    for column in data.columns:
        kitai[column] = means
    #print "kitai =", kitai
    data2 = kitai - total_mean
    #print "data2 =", data2
    data2 = data2 * data2
    d = []
    for column in data2.columns:
        d.extend(data2[column])
    #a = np.sum(d) * len(data.columns)
    a = np.sum(d)
    #print "a =", a
    data3 = data - total_mean
    data3 = data3 * data3
    d = []
    for column in data3.columns:
        d.extend(data3[column])
    b = np.sum(d)
    #print "b =", b
    return np.sqrt(a/b)

print 'p =', shiki_4_1(data)