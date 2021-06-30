from vpython import *
from math import cos,sin,nan
l1=int(input('Enter the static link length: '))
l3=int(input('Enter the length of the link opposite to the static link : '))
l2=int(input('Enter the link length of the other link: '))
l4=int(input('Enter the link length of the another link: '))
link1=arrow(pos=vector(0,0,0),axis=vector(l1,0,0),shaftwidth=0.5)
link4=arrow(pos=vector(0,0,0),axis=vector(l4,0,0),shaftwidth=0.5)
k=l1-l4
try:
    theta=acos((k**2+l3**2-l2**2)/(2*k*l3))
except ValueError or ZeroDivisionError:
    theta=nan
link3=arrow(pos=link4.axis,axis=vector(l3,l3,0),shaftwidth=0.5)
link2=arrow(pos=link3.pos+link3.axis,axis=link1.axis-link4.axis-link3.axis,shaftwidth=0.5)
phi=0
while phi<2*pi:
    phi=phi+pi/20
    link4.axis=vector(l4*cos(phi),l4*sin(phi),0)
    k=link1.axis-link4.axis
    try:
        theta=acos((mag(k)**2+l3**2-l2**2)/(2*mag(k)*l3))
    except ValueError:
        theta=nan
    angle=-atan(k.y/k.x)
    link3.pos=link4.axis
    link3.axis=vector(l3*cos(theta-angle),l3*sin(theta-angle),0)
    link2.pos=link3.pos+link3.axis
    link2.axis=link1.axis-link4.axis-link3.axis
    sleep(0.05)
    if isnan(theta)!=1:
        break
    sleep(0.05)
i=1
while True:
    phi=phi+i*pi/60
    link4.axis=vector(l4*cos(phi),l4*sin(phi),0)
    k=link1.axis-link4.axis
    try:
        theta=acos((mag(k)**2+l3**2-l2**2)/(2*mag(k)*l3))
    except ValueError:
        theta=nan   
        i=-i 
        continue
     except ZeroDivisionError:
        theta=0
    try:
        angle=-atan(k.y/k.x)
    except ZeroDivisionError:
            angle=pi/2
    if k.x<0:
        angle=angle-pi
    link3.pos=link4.axis
    link3.axis=vector(l3*cos(theta*i-angle),l3*sin(theta*i-angle),0)
    link2.pos=link3.pos+link3.axis
    link2.axis=link1.axis-link4.axis-link3.axis
    sleep(0.01)
