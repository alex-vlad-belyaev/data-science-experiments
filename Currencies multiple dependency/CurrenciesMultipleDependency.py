import json
from unittest import result
import requests
from array import *
from math import sqrt
import pandas as pd

V=10 # длина векторов
H=10 # шаг
N=5 # номер первого числа


def data(c,n,h,v): # c - валюта, n - номер первого числа < h, h - шаг, v - длина вектора
    w1='https://bank.gov.ua/NBU_Exchange/exchange_site?start=20160101&end=20201231&valcode='
    w2='&sort=exchangedate&order=desc&json'
    w=w1+c+w2
    x = requests.get(w)
    j = json.loads(x.text)
    l=[j[n]['rate']]
    k=n
    while k<v*h:
        l.append(j[k]['rate'])
        k=k+h
    return l
t1=data('usd',0,H,V)
t2=data('eur',0,H,V)
t3=data('jpy',0,H,V)

print(t1)
print(t2)
print(t3)

# df=pd.DataFrame({'usd':t1,'eur':t2})
# df.to_excel('D:\\Python\\program\\currel02.xlsx')

def dr(z,v): # v>0 - длина вектора
    k=0
    d=[(z[1]-z[0])/(z[0]//1)]
    while k<v-1:
        d.append((z[k+2]-z[k+1])/(z[0]//1))
        k=k+1
    return d

d1=dr(t1,V) 
d2=dr(t2,V)
d3=dr(t3,V)
# print(d1)
# print(d2)

def corr(u,v,n): # n - длина векторов
    t=0
    a=[0]
    b=[0]
    sa=0
    sb=0
    i = 0
    while i<n:
        sa+=u[i]
        sb+=v[i]
        a.append(u[i])
        b.append(v[i])
        i=i+1
    sa/=n
    sb/=n
    p = 0
    q = 0
    r = 0
    l = 0
    while l<n: 
        p=p+(u[l]-sa)*(v[l]-sb)
        q=q+(u[l]-sa)**2
        r=r+(v[l]-sb)**2
        l =l + 1
    t = p/(sqrt(q) * sqrt(r))
    return t
  
T1=corr(d1,d3,V)
T2=corr(d2,d3,V)

print([T1,T2])



























