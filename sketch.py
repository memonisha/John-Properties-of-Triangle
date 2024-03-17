from p5 import *
#import math  #library in python to do math stuff like sqrt, etc.


def setup():
  createCanvas(windowWidth,windowHeight)
  global a, b, c, angleA, angleB, angleC
  a=createMovableCircle(100,100,20)
  b=createMovableCircle(150,150,20)
  c=createMovableCircle(200,100,20)
  angleA=angleB=angleC=0
  

def draw():
  global a, b, c
  global ab, bc, ac
  background('black')
  drawTickAxes()

  
  
  

  
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
  angles()


def distance():
  global ab, bc, ac
  global angleA, angleB, angleC
  ab= round(sqrt((a.x-b.x)**2+(a.y-b.y)**2))
  bc= round(sqrt((b.x-c.x)**2+(b.y-c.y)**2))
  ac= round(sqrt((a.x-c.x)**2+(a.y-c.y)**2))

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
  
  #displaying angles
  fill("black")
  noStroke()
  rect(a.x-25,a.y-20,15,15)
  rect(b.x-5, b.y+20, 15, 15)
  rect(c.x+25,c.y-20,15,15)
  textSize(13)
  fill("orange")
  textStyle(BOLD)
  text(angleB, a.x -25 ,a.y-20)
  text(angleC, b.x -5  ,b.y+20)
  text(angleA, c.x +25, c.y -20)

  #displaying triangle type
  textSize (20)
  if angleA==90 or angleB==90 or angleC==90:
    text("This is a right angled triangle",width/6,height -125)
  elif angleA<90 and angleB<90 and angleC<90:
    text("This is a acute angled triangle" ,width/6,height -125)
  else:
    text("This is a obtuse angled triangle" ,width/6,height -125)
  


def angles():
  global angleA, angleB, angleC,ab, bc, ac
  #local variables which are telling us just the distances
  a=ab
  b=bc
  c=ac
  a2= a**2
  b2= b**2
  c2= c**2

  angleA=round(acos((c2+b2-a2)/(2*b*c)))
  angleB=round(acos((a2+c2-b2)/(2*a*c)))
  angleC=180-(angleA+angleB)


  
  
  

  #print(angleA,angleB,angleC)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  