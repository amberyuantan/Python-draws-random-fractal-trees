from turtle import *
from random import *
from math import *

def tree(n,l):
    pd()
    #shadow
    t = cos(radians(heading()+45))/8+0.25
    pencolor(t,t,t)
    pensize(n/3)
    forward(l)#branch

    if n>0:
        b = random()*15+10 #right branch deflection angle
        c = random()*15+10 #left branch deflection angle
        d = l*(random()*0.25+0.7) #next branch length
        #Turn right at an angle and draw the right branch
        right(b)
        tree(n-1,d)
        #Turn left at an angle and draw the left branch
        left(b+c)
        tree(n-1,d)
        #Turn back
        right(c)
    else:
        #leaves
        right(90)
        n=cos(radians(heading()-45))/4+0.5
        pencolor(n,n,n)
        circle(3)
        left(90)
        #Add 0.3 times the falling leaves
        if(random()>0.7):
            pu()
            #falling
            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            #leaves
            pd()
            right(90)
            n = cos(radians(heading()-45))/4+0.5
            pencolor(n,n,n)
            circle(2)
            left(90)
            pu()
            #return
            t=heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)
    
bgcolor(0.5,0.5,0.5)
ht()#hide turtle
speed(0)
tracer(0,0)
pu()
backward(50)
left(90)
pu()
backward(300)
tree(12,100)#Recursion seven levels
done()
