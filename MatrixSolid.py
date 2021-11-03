import time
import math
from random import seed
from random import random
from samplebase import SampleBase
from rgbmatrix import graphics

seed(time)
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
def CartesianToMatrix(pos,flag):
    if(flag == 0):
        return ((xSize/2)+pos)
    else:
        return((ySize/2)-pos)

def perspective(x,z):
    return(x/(abs(z)+1))
    








class GraphicsTest(SampleBase):
    def __init__(self,*args,**kwargs):
        super(GraphicsTest,self).__init__(*args,**kwargs)
    def run(self):
        print("In run")
        canvas = self.matrix
        red = graphics.Color(255,0,0)
        green = graphics.Color(0,255,0)
        blue = graphics.Color(0,0,255)
        
        rCol = 255
        bCol = 255
        gCol = 255
        rColFlag = 0
        bColFlag = 0
        gColFlag = 0

        multi = graphics.Color(rCol,bCol,gCol)
        icol = ico()
        while(True):
            if(rColFlag == 0):
                rCol = rCol + 2
                if(rCol > 255):
                    rCol = rCol - 2
                    rColFlag = 1
            else:
                rCol = rCol - 2
                if(rCol <= 0):
                    rCol = rCol +2

            if(bColFlag == 0):
                bCol = bCol + 7
                if(bCol > 255):
                    bCol = bCol - 7
                    bColFlag = 1
            else:
                bCol = bCol -7
                if(bCol <= 0):
                    bCol = bCol + 7
                    bColFlag = 0
            if(gColFlag == 0):
                gCol = gCol +11
                if(gCol > 255):
                    gCol = gCol -11
                    gColFlag = 1
            else:
                gCol = gCol - 11
                if(gCol <= 0):
                    gCol = gCol + 11
                    gColFlag = 0
            multi = graphics.Color(rCol,bCol,gCol)

            canvas.Clear()
            """graphics.DrawLine(canvas,CartesianToMatrix(cube1.point1[0],0),CartesianToMatrix(cube1.point1[1],1),CartesianToMatrix(cube1.point2[0],0),CartesianToMatrix(cube1.point2[1],1),red)
            """

            for tri in icol.triArr:
                """print(CartesianToMatrix(tri.point1.y,1))"""
                """ without Perspective
                graphics.DrawLine(canvas,CartesianToMatrix(tri.point1.x,0),CartesianToMatrix(tri.point1.y,1),CartesianToMatrix(tri.point2.x,0),CartesianToMatrix(tri.point2.y,1),multi)
                graphics.DrawLine(canvas,CartesianToMatrix(tri.point2.x,0),CartesianToMatrix(tri.point2.y,1),CartesianToMatrix(tri.point3.x,0),CartesianToMatrix(tri.point3.y,1),multi)
                graphics.DrawLine(canvas,CartesianToMatrix(tri.point3.x,0),CartesianToMatrix(tri.point3.y,1),CartesianToMatrix(tri.point1.x,0),CartesianToMatrix(tri.point1.y,1),multi)
                """
                """With Perspective"""
                graphics.DrawLine(canvas,CartesianToMatrix(perspective(tri.point1.x,tri.point1.z),0),CartesianToMatrix(perspective(tri.point1.y,tri.point1.z),1),CartesianToMatrix(perspective(tri.point2.x,tri.point2.z),0),CartesianToMatrix(perspective(tri.point2.y,tri.point2.z),1),multi)
                graphics.DrawLine(canvas,CartesianToMatrix(perspective(tri.point2.x,tri.point2.z),0),CartesianToMatrix(perspective(tri.point2.y,tri.point2.z),1),CartesianToMatrix(perspective(tri.point3.x,tri.point3.z),0),CartesianToMatrix(perspective(tri.point3.y,tri.point3.z),1),multi)
                graphics.DrawLine(canvas,CartesianToMatrix(perspective(tri.point3.x,tri.point3.z),0),CartesianToMatrix(perspective(tri.point3.y,tri.point3.z),1),CartesianToMatrix(perspective(tri.point1.x,tri.point1.z),0),CartesianToMatrix(perspective(tri.point1.y,tri.point1.z),1),multi)
                


             
            icol.rotateZ(0.1/3)
            icol.rotateY(0.1/3)
            icol.rotateX(0.1/3)
            time.sleep(1/30)
            
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if(not graphics_test.process()):
        graphics_test.print_help()



            
        
        
        
    
    

        
    
    
    
        
        
    


