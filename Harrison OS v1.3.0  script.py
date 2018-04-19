import socketserver
import webbrowser
import tkinter
import turtle
import random
import socket
import time
import os

from socketserver import *
from webbrowser import *
from tkinter import *
from random import *
from socket import *
from os import *

stage = "home"
run = 1
runtest1 = 0
x = 0
y = 0

screen = turtle.Screen()
turtle.hideturtle()
turtle.penup()

screen.addshape('screen 1.gif')
screen.addshape('Screen button 1.gif')
screen.addshape('Screen button home 1.gif')
screen.addshape('Screen button settings 1.gif')
screen.addshape('Settings window 1.gif')
screen.addshape('X button 1.gif')
screen.addshape('Screen button netstats 1.gif')
screen.addshape('Settings netstat warning 1.gif')

screen.bgcolor("Black")

bgnds = turtle.Turtle()
bgnds.penup()
bgnds.speed(10000)
bgnds.shape('screen 1.gif')
bgnds.goto(0, 0)

homebutton = turtle.Turtle()
homebutton.penup()
homebutton.speed(10000)
homebutton.shape('Screen button home 1.gif')
homebutton.goto(-665, -390)

settingbutton = turtle.Turtle()
settingbutton.penup()
settingbutton.speed(10000)
settingbutton.shape('Screen button settings 1.gif')
settingbutton.goto(-545, -390)

settingwindow = turtle.Turtle()
settingwindow.penup()
settingwindow.speed(10000)
settingwindow.shape('Settings window 1.gif')
settingwindow.goto(0, 0)
settingwindow.hideturtle()

xbutton = turtle.Turtle()
xbutton.penup()
xbutton.speed(10000)
xbutton.shape('X button 1.gif')
xbutton.hideturtle()

netstatb = turtle.Turtle()
netstatb.penup()
netstatb.speed(10000)
netstatb.shape('Screen button netstats 1.gif')
netstatb.hideturtle()

m1 = turtle.Turtle()
m1.penup()
m1.speed(10000)
m1.shape('Settings netstat warning 1.gif')
m1.hideturtle()

m2 = turtle.Turtle()
m2.penup()
m2.speed(10000)
m2.hideturtle()

def c1(x, y):
    exit()

def c2(x, y):
    global stage
    stage = "home"

def c3(x, y):
    global stage
    stage = "settings-main"

def c4(x, y):
    global stage
    screen.clear()
    stage = "home"

def c5(x, y):
    global stage
    global runtest1
    stage = "settings-netstat"
    runtest1 = 1

while (run == 1):
    homebutton.onclick(c2)
    settingbutton.onclick(c3)
    xbutton.onclick(c4)
    netstatb.onclick(c5)
    
    if (stage == "home"):
        homebutton.showturtle()
        settingbutton.showturtle()
        settingwindow.hideturtle()
        xbutton.hideturtle()
        m1.hideturtle()
        netstatb.hideturtle()

    if (stage == "settings-main"):
        settingwindow.showturtle()
        xbutton.showturtle()
        xbutton.goto(460, 302.5)
        netstatb.showturtle()
        netstatb.goto(-400, 250)

    if (stage == "settings-netstat"):
        netstatb.hideturtle()
        m1.showturtle()
        m1.goto(0, -250)
        
        if (runtest1 == 1):
            x = (-400)
            m2.goto(x, y)
            m2.showturtle()
            m2.pendown()

            while (x <= 400):
                start = time.time()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                os.getlogin()
                end = time.time()
                total = (float(end) - float(start))
                
                y = (-200 + (float(total) * 200000))
                x = (float(x) + 0.5)
                
                print (x, y, total, end, start)
                
                m2.goto(x, y)
                
            if (x >= 400):
                runtest1 = 0
                m2.penup()
                m2.hideturtle()
                  
        

    
