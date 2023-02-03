import time
import math
from random import seed
from random import random
#from samplebase import SampleBase
#from rgbmatrix import graphics
import tkinter

seed(1)
xSize = 64
ySize = 64

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class tri():
    def __init__(self,point1,point2,point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
class ico():
    multiplier = 55
    golden = (1+math.sqrt(5))/2
    a = (1/2) * multiplier
    b = (1/(2*golden)) * multiplier
    triArr = []
    triArr.append(tri(point(0,b,-a),point(b,a,0),point( -b,a,0)))
    triArr.append(tri(point(0,b,a),point(-b,a,0),point(b,a,0)))
    triArr.append(tri(point(0,b,a),point(0,-b,a),point(-a,0,b)))
    triArr.append(tri(point(0,b,a),point(a,0,b),point(0,-b,a)))
    triArr.append(tri(point(0,b,-a),point(0,-b,-a),point(a,0,-b)))
    triArr.append(tri(point(0,b,-a),point(-a,0,-b),point(0,-b,-a)))
    triArr.append(tri(point(0,-b,a),point(b,-a,0),point(-b,-a,0)))
    triArr.append(tri(point(0,-b,-a),point(-b,-a,0),point(b,-a,0)))
    triArr.append(tri(point(-b,a,0),point(-a,0,b),point(-a,0,-b)))
    triArr.append(tri(point(-b,-a,0),point(-a,0,-b),point(-a,0,b)))
    triArr.append(tri(point(b,a,0),point(a,0,-b),point(a,0,b)))
    triArr.append(tri(point(b,-a,0),point(a,0,b),point(a,0,-b)))
    triArr.append(tri(point(0,b,a),point(-a,0,b),point(-b,a,0)))
    triArr.append(tri(point(0,b,a),point(b,a,0),point(a,0,b)))
    triArr.append(tri(point( 0,b,-a),point(-b,a,0),point(-a,0,-b)))
    triArr.append(tri(point(0,b,-a),point(a,0,-b),point(b,a,0)))
    triArr.append(tri(point(0,-b,-a),point(-a,0,-b),point(-b,-a,0)))
    triArr.append(tri(point(0,-b,-a),point(b,-a,0),point(a,0,-b)))
    triArr.append(tri(point(0,-b,a),point(-b,-a,0),point(-a,0,b)))
    triArr.append(tri(point(0,-b,a),point(a,0,b),point(b,-a,0)))
    
    def rotateZ(self, degree):
        sinTheta = math.sin(degree)
        cosTheta = math.cos(degree)
        for triangle in self.triArr:
            
            x = triangle.point1.x
            y = triangle.point1.y
            triangle.point1.x = x*cosTheta -y*sinTheta
            triangle.point1.y = y*cosTheta + x*sinTheta
            x = triangle.point2.x
            y = triangle.point2.y
            triangle.point2.x = x*cosTheta -y*sinTheta
            triangle.point2.y = y*cosTheta + x*sinTheta
            x = triangle.point3.x
            y = triangle.point3.y
            triangle.point3.x = x*cosTheta -y*sinTheta
            triangle.point3.y = y*cosTheta + x*sinTheta
    
    def rotateX(self, degree):
        sinTheta = math.sin(degree)
        cosTheta = math.cos(degree)
        for triangle in self.triArr:

            x = triangle.point1.y
            y = triangle.point1.z
            triangle.point1.y = x*cosTheta -y*sinTheta
            triangle.point1.z = y*cosTheta + x*sinTheta
            x = triangle.point2.y
            y = triangle.point2.z
            triangle.point2.y = x*cosTheta -y*sinTheta
            triangle.point2.z = y*cosTheta + x*sinTheta
            x = triangle.point3.y
            y = triangle.point3.z
            triangle.point3.y = x*cosTheta -y*sinTheta
            triangle.point3.z = y*cosTheta + x*sinTheta
    
    def rotateY(self, degree):
        sinTheta = math.sin(degree)
        cosTheta = math.cos(degree)
        for triangle in self.triArr:
            x = triangle.point1.x
            y = triangle.point1.z
            triangle.point1.x = x*cosTheta -y*sinTheta
            triangle.point1.z = y*cosTheta + x*sinTheta
            x = triangle.point2.x
            y = triangle.point2.z
            triangle.point2.x = x*cosTheta -y*sinTheta
            triangle.point2.z = y*cosTheta + x*sinTheta
            x = triangle.point3.x
            y = triangle.point3.z
            triangle.point3.x = x*cosTheta -y*sinTheta
            triangle.point3.z = y*cosTheta + x*sinTheta




        

"""
This function tranforms a cartesian coordinate to it's representative matrix position
pos = position

Flag represents different directions (x or y):

flag = 0 -> x dir
flag = 1 -> y dir


"""

def perspective(x,z):
    return(x/(abs(z)+1))

class canvas:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.triArr = []
        self.top = tkinter.Tk()
        self.c = tkinter.Canvas(self.top,bg="white",height=y,width=x)
        self.xOffset = 0
        self.yOffset = 0
    
    def readPoints(self,fileLoc,mul):
        f = open(fileLoc,"r")
        
        points = []
        point1 = 0
        point2 = 0
        point3 = 0
        count = 0
        for x in f:
            #print("in readPointsLoop")
            spl = x.split(' ',4)
            #print(spl)
            points.append(point(float(spl[0])*mul,float(spl[1])*mul,float(spl[2])*mul))
            #print(spl[0])
            if(float(spl[0]) == 3):
                #print("In faces")
                #print(spl[3])
                self.triArr.append(tri(points[int(spl[1])],points[int(spl[2])],points[int(spl[3])]))
                
            
        
    def drawTri(self,tri,mul):
        self.c.create_line(self.CartesianToMatrix(tri.point1.x*mul,0),self.CartesianToMatrix(tri.point1.y*mul,1),self.CartesianToMatrix(tri.point2.x*mul,0),self.CartesianToMatrix(tri.point2.y*mul,1),self.CartesianToMatrix(tri.point3.x*mul,0),self.CartesianToMatrix(tri.point3.y*mul,1),self.CartesianToMatrix(tri.point1.x*mul,0),self.CartesianToMatrix(tri.point1.y*mul,1))
    
    def updateCanvas(self):
        self.c.pack()
        self.top.update()
    def clearCanvas(self):
        self.c.delete('all')
    def CartesianToMatrix(self,pos,flag):
        if(flag == 0):
            return ((self.x/2)+pos+self.xOffset)
        else:
            return((self.y/2)-pos+self.yOffset)

    def drawAll(self,mul):
        for tr in self.triArr:
            self.drawTri(tr,mul)
    def translateAllDown(self,pixels):
        for tr in self.triArr:
            self.translateTri(tr,pixels)
    
    def translateTri(self,tri,pixels):
        tri.point1.y = tri.point1.y - pixels
        tri.point2.y = tri.point2.y - pixels
        tri.point3.y = tri.point2.y - pixels

    def rotateY(self,theta):
        sinTheta = math.sin(theta)
        cosTheta = math.cos(theta)
        for tr in self.triArr:
            tr.point1.x = tr.point1.x * cosTheta + tr.point1.z * sinTheta
            tr.point1.y = tr.point1.z * cosTheta - tr.point1.x * sinTheta

            tr.point2.x = tr.point2.x * cosTheta + tr.point2.z * sinTheta
            tr.point2.y = tr.point2.z * cosTheta - tr.point2.x * sinTheta

            tr.point2.x = tr.point2.x * cosTheta + tr.point2.z * sinTheta
            tr.point2.y = tr.point2.z * cosTheta - tr.point2.x * sinTheta


            
if __name__ == "__main__":
    can = canvas(900,900)
    #can.triArr.append(tri(point(1,1,1),point(5,50,50),point(70,70,70)))
    print("Before readPoints")
    can.readPoints("happy_vrip.ply",1)
    print("After readPoints")
    """
    while(True):
        can.clearCanvas()
        can.drawAll()
        can.updateCanvas()
        can.rotateZ(0.2)
        time.sleep(0.1)
    """
    #can.translateAllDown(100)
    can.yOffset = 600
    can.clearCanvas()
    #1000 represents the multiplier

    print("Starting draw")
    can.drawAll(6000)
    can.updateCanvas()

    time.sleep(20)
    
    """time.sleep(1)
    print("translating down:")
    
    can.clearCanvas()
    can.drawAll()
    can.updateCanvas()
    """
    
    """
    print("rotating")
    can.clearCanvas()
    can.rotateZ(0.1)
    print("drawing")
    can.drawAll
    print("updating")
    can.updateCanvas()
    """
    print("Done")
    #time.sleep(5)
    
    #can.drawTri(can.triArr[0])
    #can.updateCanvas()



            
        
        
        
    
    

        
    
    
    
        
        
    



