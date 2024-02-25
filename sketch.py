from p5 import *


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