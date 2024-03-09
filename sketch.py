from p5 import *
import math  #library in python to do math stuff like sqrt, round


def setup():
  createCanvas(windowWidth,windowHeight)
  global a, b, c
  a=createMovableCircle(100,100,20)
  b=createMovableCircle(150,150,20)
  c=createMovableCircle(200,100,20)
  

def draw():
  global a, b, c
  background('black')
  drawTickAxes()

  
  
  

  c.draw()
  
  textSize(22)
  fill("green")
  a.draw()
  text(f"({a.x},{a.y})",200,400)
  fill("magenta")
  b.draw()
  text(f"({b.x},{b.y})",200,350)
  fill("cyan")
  c.draw()
  text(f"({c.x},{c.y})",200,300)

  push()
  stroke("yellow")
  strokeWeight(4)
  line(a.x,a.y,b.x,b.y)
  stroke(51, 74, 245)
  line(b.x,b.y,c.x,c.y)
  stroke(51, 245, 61)
  line(c.x,c.y, a.x, a.y)
  pop()

  distance()

#distances
#p1=(20,30)    p2=(100,230)
# return ----> p1 and p2 distance
#    formula= sqrt()
def distance():
  
  ab= round(math.sqrt((a.x-b.x)**2+(a.y-b.y)**2))
  bc= round(math.sqrt((b.x-c.x)**2+(b.y-c.y)**2))
  ac= round(math.sqrt((a.x-c.x)**2+(a.y-c.y)**2))

  midXab=(a.x+b.x)/2 - 25
  midYab=(a.y+b.y)/2
  textSize(13)
  fill("plum")
  textStyle(BOLD)
  text(ab,midXab,midYab)
  midXbc =(b.x+c.x)/2 +15
  midYbc =(b.y+c.y)/2 
  text(bc,midXbc,midYbc)
  midXac =(a.x+c.x)/2 -10
  midYac =(a.y+c.y)/2 -15
  text(ac,midXac,midYac)
  textSize (20)
  if ab==bc==ac :
    
    text("This triangle is Equilateral",width/6,height -100)

  elif ab==bc or bc==ac or ab==ac :
    
    text("This triangle is Isosceles",width/6,height -100)

  else:
    
    text("This triangle is Scalene",width/6,height -100)
  
  print(ab,bc,ac)