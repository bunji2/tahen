# encoding: utf8

import numpy as np

def shiki_2_6(x, y):
    n = len(x)
    #print "n =", n
    d = x - y
    #print "d =", d
    dd = d * d
    #print "dd =", dd
    #print "sum dd =", np.sum(dd)
    #print 6.0*np.sum(dd)/(n*(n*n-1))
    return 1.0 - 6.0*np.sum(dd)/(n*(n*n-1))

# p28
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 5, 1, 2, 4])
print a
print b
print shiki_2_6(a, b)

# p31
import pandas as pd

data = pd.read_csv("tab2.6.csv", index_col=0)
print data

# boo: str -> list(int)
# name: インデックス名
def boo(name):
    #     1, 2, 3, 4, 5, 6
    #結果,神,中,横,ヤ,巨,広
    #S記者,ヤ,神,巨,中,広,横
    # ==> [2, 4, 6, 1, 3, 5]
    # 結果の並びで該当する列名のリストを作成する。
    if not name in data.index:
        raise IndexError("unknown index: "+ name)
    bar = {}
    for column in data.columns:
        #print column, data.loc[name, column].decode('utf8')
        bar[data.loc[name, column]] = int(column)

    return [bar[data.loc['結果', column]] for column in data.columns]

print "----"
kekka  = np.array(boo('結果'))
for name in ['S記者','T記者','H記者','M記者','Y予報士']:
    value = np.array(boo(name))
    print name.decode('utf8'), " =", shiki_2_6(kekka, value)

#print boo('予報士')
# ==> IndexError
