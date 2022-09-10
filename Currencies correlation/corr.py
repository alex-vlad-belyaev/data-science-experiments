import json
import requests
from array import *
from math import sqrt
import pandas as pd

def data(c1,c2,n,h,v):
    ww1='https://bank.gov.ua/NBU_Exchange/exchange_site?start=20160101&end=20201231&valcode='
    ww2='&sort=exchangedate&order=desc&json'
    w1=ww1+c1+ww2
    w2=ww1+c2+ww2
    x = requests.get(w1)
    j1 = json.loads(x.text)
    y = requests.get(w2)
    j2 = json.loads(y.text)
    la1=[j1[n]['rate']]
    la2=[j2[n]['rate']]
    k=n
    while k<v:
        la1.append(j1[k]['rate'])
        la2.append(j2[k]['rate'])
        k=k+h
    print(la1)
    print(la2)
    # df=pd.DataFrame({'usd':la1,'eur':la2})
    # df.to_excel('D:\\Python\\program\\curr.xlsx')
data('usd','eur',1,10,100)











# x = requests.get('https://bank.gov.ua/NBU_Exchange/exchange_site?start=20160101&end=20201231&valcode=usd&sort=exchangedate&order=desc&json')
# j = json.loads(x.text)
# print(j[0]['rate'])
# print(j[1]['rate'])

# def data(s,n,h,v):
#     w1='https://bank.gov.ua/NBU_Exchange/exchange_site?start=20160101&end=20201231&valcode='
#     w2=s
#     w3='&sort=exchangedate&order=desc&json'
#     w=w1+w2+w3
#     x = requests.get(w)
#     j = json.loads(x.text)
#     la=[j[n]['rate']]
#     k=n
#     while k<v:
#         la.append(j[n]['rate'])
#         k=k+h
#     # print(la)
#     lb={'usd':la}
#     print(lb)
#     df=pd.DataFrame({'usd':lb})
#     df.to_excel('./curr1.xlsx')
# data('usd',1,10,100)













