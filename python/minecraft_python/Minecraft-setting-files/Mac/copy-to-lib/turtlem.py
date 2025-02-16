from math import sin, cos, atan, pi
from minecraft import *

#coordinate : [ x, y, z ]

class Turtle() :
        def __init__(self, pos = [0, 0, 0], head = 0) :
                self.pos = pos
                self.head = head

        def forward(self, distance) :
                self.pos[0] +=  distance * cos(self.head/57.296)
                self.pos[2] += distance * sin(self.head/57.296)

        def backward(self, distance) :
                self.pos[0] -=  distance * cos(self.head/57.296)
                self.pos[2] -= distance * sin(self.head/57.296)

        def sethead(self, degree) :
                self.head = degree

        def setpos(self, pos) :
                self.pos = pos
        
        def right(self, degree) :
                self.head -= degree

        def left(self, degree) :
                self.head += degree

        def up(self, distance) :
                self.pos[1] += distace
        
        def down(self, distance) :
                self.pos[1] -= distace

        def setx(self, x) :
                self.pos[0] = x

        def sety(self, y) :
                self.pos[1] = y

        def setz(self, z) :
                self.pos[2] = z


class Turtlem() :
        def __init__(self, pb = 41, th = 2, pd = True) :
                self.turtle = Turtle()
                self.track = list()
                self.pb = pb
                self.th = th - 1
                self.pd = pd

        def getpos(self) :
                x = self.turtle.pos[0]
                y = self.turtle.pos[1]
                z = self.turtle.pos[2]
                return [x, y, z]

        def getroundpos(self) :
                x = round(self.turtle.pos[0])
                y = round(self.turtle.pos[1])
                z = round(self.turtle.pos[2])
                return [x, y, z]
        
        def forward(self, distance) :
                for count in range(distance) :
                        self.track.append([self.getroundpos(), self.pb, self.th, self. pd])
                        self.turtle.forward(1)
                self.show()
                
        def backward(self, distance) :
                for count in range(distance) :
                        self.track.append([self.getroundpos(), self.pb, self.th, self. pd])
                        self.turtle.backward(1)
                self.show()

        def right(self, degree) :
                self.turtle.right(degree)

        def left(self, degree) :
                self.turtle.left(degree)

        def backjump(self, distance) :
                self.turtle.backward(distance)

        def frontjump(self, distance) :
                self.turtle.forward(distance)

        def up(self, distance) :
                for count in range(distance) :
                        self.track.append([self.getroundpos(), self.pb, self.th, self. pd])
                        self.turtle.up(1)
                self.show()

        def down(self, distance) :
                for count in range(distance) :
                        self.track.append([self.getroundpos(), self.pb, self.th, self. pd])
                        self.turtle.down(1)
                self.show()

        def circle(self, rad, flag = 'left') :
                temp = self.turtle.head
                junk = rad*8
                for i in range(junk) :
                        self.track.append([self.getpos(), self.pb, self.th, self. pd])
                        self.turtle.right(360/junk)
                        self.turtle.forward(2*rad*sin((180/junk)/57.296))
                self.turtle.sethead(temp)
                self.turtle.setx(round(self.turtle.pos[0]))
                self.turtle.setz(round(self.turtle.pos[2]))
                self.show()
                        
        def penup(self) :
                self.pd = False

        def pendown(self) :
                self.pd = True

        def pensize(self, size) :
                self.th = size - 1

        def penblock(self, _id) :
                self.pb = _id

        def spawnturtle(self, size = 1) :
                px = getpos().x
                py = getpos().y
                pz = getpos().z
                shell = [
                        [0, 1, 0, 0, 1, 0],
                        [-2, 1, 1, 2, 1, 5],
                        [-1, 2, 2, 1, 2, 5] ]
                body = [
                        [-2, 1, 1, -2, 0, 1],
                        [2, 1, 1, 2, 0, 1],
                        [-2, 1, 5, -2, 0, 5],
                        [2, 1, 5, 2, 0, 5],
                        [0, 1, 6, 0, 1, 6]]
                for  p in shell :
                        setblocks(px + p[0], py + p[1], pz + p[2],
                                  px + p[3], py + p[4], pz + p[5], 35, 5)
                for  p in body :
                        setblocks(px + p[0], py + p[1], pz + p[2],
                                  px + p[3], py + p[4], pz + p[5], 35, 4)
        
        def show(self) :
                px = getpos().x
                py = getpos().y-1
                pz = getpos().z
                for t in self.track :
                        if t[3] :
                                setblocks(
                                        px + t[0][0], py + t[0][1], pz + t[0][2],
                                        px + t[0][0] + t[2], py + t[0][1],
                                        pz + t[0][2] + t[2], t[1])
                self.track = list()

turtle = Turtlem()           
