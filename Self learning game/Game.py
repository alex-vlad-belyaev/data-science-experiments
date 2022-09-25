import json
from array import *
import random

def s(a,b,c,k): # поиск выигрышного хода с точностью до перестановки, k - номер записей в файле
    if a<b and a<c:
        u=a
        if b<c:
            v=b
            w=c
            sigma=[1,2,3]
        else:
            v=c
            w=b
            sigma=[1,3,2]
    elif c<b:
        u=c
        if a<b:
            v=a
            w=b
            sigma=[3,1,2]
        else:
            v=b
            w=a
            sigma=[3,2,1]
    else:
        u=b
        if a<c:
            v=a
            w=c
            sigma=[2,1,3]
        else:
            v=c
            w=a
            sigma=[2,3,1]

    if (u-g[k][0])<0 or (v-g[k][1])<0 or (w-g[k][2])<0: # невозможно получить нужную комбинацию в принципе
        res=[3,0]
    else:
        xu=(u-g[k][0])*(u-g[k][1])*(u-g[k][2])
        yu=(v-g[k][0])*(v-g[k][1])*(v-g[k][2])
        zu=(w-g[k][0])*(w-g[k][1])*(w-g[k][2])

        xg=(u-g[k][0])*(v-g[k][0])*(w-g[k][0])
        yg=(u-g[k][1])*(v-g[k][1])*(w-g[k][1])
        zg=(u-g[k][2])*(v-g[k][2])*(w-g[k][2])

        res=[3,1] # невозможно получить нужную комбинацию из-за неполноты файла
        if xu*yu+yu*zu+zu*xu==0 and xg*yg+yg*zg+zg*xg==0:
            if u==g[k][0]:
                if v==g[k][1]:
                    res=[2,w-g[k][2]]
                elif v==g[k][2]:
                    res=[2,w-g[k][1]]
                else:
                    res=[1,v-g[k][1]]
            elif u==g[k][1]:
                if v==g[k][2]:
                   res=[2,w-g[k][0]]
                else:
                    res=[1,v-g[k][0]]
            else:
                res=[0,u-g[k][0]]
    return [res,sigma]    # нужная комбинация вместе с перестановкой 
        
def f(a,b,c,l): # поиск выигрышного хода
    k=0
    m=3
    while k<l:
        t=s(a,b,c,k)
        if t[0][0]<3:
            m=3
            o=t[1][t[0][0]]
            if o==1:
                a-=t[0][1]
                k=l
            if o==2:
                b-=t[0][1]
                k=l
            if o==3:
                c-=t[0][1]
                k=l
        else:
            m=4
        k+=1
    return [a,b,c,m] # выигрышнй ход и указание, есть ли он

with open('key.json', 'r') as file:
    g = json.load(file)
    file.close()


max=5

# p=4
# q=4
# r=0

# игра
d=5 # число записей в файле
p=random.randint(1,max) # максимальное число фишек
q=random.randint(1,max)
r=random.randint(1,max)

log='?'
n=0
print(n,p,q,r)
p0=p
q0=q
r0=r
w=[0,0,0]
while p+q+r>0:
    p1=f(p,q,r,d)[0]
    q1=f(p,q,r,d)[1]
    r1=f(p,q,r,d)[2]
    if p>p1 or q>q1 or r>r1:
        p=p1
        q=q1
        r=r1
        n+=1
        print(n,p,q,r)
        if n==0:
            log='-'
        else:
            if log=='?':
                w=[p0,q0,r0]
                log='+'
    else: 
        if f(p,q,r,d)[3]==3 and n<2:
            log='-'    
        if p*q*r>0:
            e=random.randint(1,3)
            if e>2:
                h=random.randint(1,r)
                r-=h
                n+=1
                print(n,p,q,r)
            else:
                if e<2:
                    h=random.randint(1,p)
                    p-=h
                    n+=1
                    print(n,p,q,r)
                else:
                    h=random.randint(1,q)
                    q-=h
                    n+=1
                    print(n,p,q,r)
        else:
            if p*q>0:
                e=random.randint(1,2)
                if e>1:
                    h=random.randint(1,q)
                    q-=h
                    n+=1
                    print(n,p,q,r)
                else:
                    h=random.randint(1,p)
                    p-=h
                    n+=1
                    print(n,p,q,r)
            elif q*r>0:
                e=random.randint(2,3)
                if e>2:
                    h=random.randint(1,r)
                    r-=h
                    n+=1
                    print(n,p,q,r)
                else:
                    h=random.randint(1,q)
                    q-=h
                    n+=1
                    print(n,p,q,r)
            elif p*r>0:
                e=random.randint(1,2)
                if e>1:
                    h=random.randint(1,r)
                    r-=h
                    n+=1
                    print(n,p,q,r)
                else:
                    h=random.randint(1,p)
                    p-=h
                    n+=1
                    print(n,p,q,r)
            else:
                if p>0:
                    h=random.randint(1,p)
                    p-=h
                    n+=1
                    print(n,p,q,r)
                elif q>0:
                    h=random.randint(1,q)
                    q-=h
                    n+=1
                    print(n,p,q,r)
                elif r>0:
                    h=random.randint(1,r)
                    r-=h
                    n+=1
                    print(n,p,q,r)
                else:
                    n+=1
                    print(n,p,q,r)
    if n>1:
        p0=p1
        q0=q1
        r0=r1
    p1=p
    q1=q
    r1=r
                      
if n-2*(n//2)==0:
    print('второй проиграл')
else:
    print('первый проиграл')
print(log,w)


if log=='+':

    p=w[0]
    q=w[1]
    r=w[2]

    log='записать'
    i=1
    while p-i>=0:
        p1=p-i
        if f(p1,q,r,d)[3]==4:
            log='нет записи'
            print(p1,q,r)
            i=p
        i+=1
    if log=='записать':
        i=1
        while q-i>=0:
                q1=q-i
                if f(p,q1,r,d)[3]==4:
                    log='нет записи'
                    print(p,q1,r)
                    i=q
                i+=1
    if log=='записать':
        i=1
        while r-i>=0:
                r1=r-i
                if f(p,q,r1,d)[3]==4:
                    log='нет записи'
                    print(p,q,r1)
                    i=r
                i+=1
else:
    log='нет записи'
print(log)

if log=='записать':
    g.append(w)
    with open("key.json", "w") as h:
        json.dump(g, h)
    h.close()









# cd D:\Python\program12