from ._anvil_designer import Kat_en_muisTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import math
import random

class Kat_en_muis(Kat_en_muisTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.MULTP = 64
    self.ADD = 75
    self.DISTANCE = 20 
#    running = True
    self.muisBeurt = True
    self.muisPoint = None
    self.katPoints = []
    self.katComputer = False
    self.muisComputer = False
    self.katWinst = False
    self.muisWinst = False
    
    self.pointsBase = [(2,0),(4,0),(6,0),
              (1,2),(3,2),(5,2),(7,2),
              (0,4),(2,4),(4,4),(6,4),(8,4),
              (1,6),(3,6),(5,6),(7,6),
              (2,8),(4,8),(6,8)]
    
    self.points = self.transform(self.pointsBase,self.MULTP,self.ADD)
    self.lines = [[0,1],[1,2],
         [0,3],[0,4],[1,4],[1,5],[2,5],[2,6],
         [3,4],[4,5],[5,6],
         [3,7],[3,8],[4,8],[4,9],[5,9],[5,10],[6,10],[6,11],
         [7,8],[8,9],[9,10],[10,11],
         [7,12],[8,12],[8,13],[9,13],[9,14],[10,14],[10,15],[11,15],
         [12,13],[13,14],[14,15],
         [12,16],[13,16],[13,17],[14,17],[14,18],[15,18],
         [16,17],[17,18]]
    
    self.midPoints = []

    for l in self.lines:
    
      self.midPoints.append((int((self.points[l[0]][0]+self.points[l[1]][0])/2),
                       int((self.points[l[0]][1]+self.points[l[1]][1])/2)))
   
  def afstand(self,p,q):
    return math.sqrt((p[0]-q[0])*(p[0]-q[0])+(p[1]-q[1])*(p[1]-q[1]))

  def midden(self,p,q):
    return (int((p[0]+q[0])/2),int((p[1]+q[1])/2))
  
  def pointSelected(self,points, loc, distance):
    result = None
    for e in points:
        if self.afstand(e,loc) < distance:
            result = e
    return result
  
  def transform(self, points,multp,add):
    result = []
    for point in points:
        result.append((multp*point[0]+add+175,multp*point[1]+add))
    return result
  
  def midden(self,p,q):
    return (int((p[0]+q[0])/2),int((p[1]+q[1])/2))
  
  def burenPoints(self,p):
    result = []
    for point in self.points:
        if self.afstand(point,p) < (self.MULTP*2.3) and point != p:
            result.append(point)
    return result

  def burenMidPoints(self,p):
    result = []
    for point in self.points:
        if self.midden(point,p) in self.midPoints and self.afstand(point,self.midden(point,p)) < (self.MULTP*1.2):
            result.append(self.midden(point,p))
    return result
  
  def drawboard(self):
    c = self.canvas_1
    c.fill("rgba(223,246,142,1)")
    for line in self.lines:
      c.begin_path()
      c.move_to(self.points[line[0]][0],self.points[line[0]][1])
      x = self.points[line[1]][0]
      y = self.points[line[1]][1]
      c.line_to(x,y)
      c.stroke_style = "rgba(255,0,0,1)"
      c.line_width = 3
      c.fill_style = "rgba(255,0,0,1)"
      c.fill()
      c.stroke()    

    for p in self.points:
      if p == self.muisPoint:
        kleur = "rgba(255,255,255,1)"
      else:
        kleur = "rgba(0,0,255,1)"
      c.begin_path()
      c.arc(p[0],p[1], 20,
            0, 2*math.pi,True)
      c.stroke_style = kleur
      c.line_width = 3
      c.fill_style = kleur
      c.close_path()
      c.fill()
      c.stroke()
      
    for p in self.midPoints:
      if p in self.katPoints:
        kleur = "rgba(255,0,0,1)"
      else:
        kleur = "rgba(0,0,0,1)"
      
      c.begin_path()
      c.arc(p[0],p[1], 5,
            0, 2*math.pi,True)
      c.stroke_style = kleur
      c.line_width = 3
      c.fill_style = kleur
      c.fill()
      c.stroke()
  
  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    self.drawboard()
    
  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    self.canvas_1_show()

  def canvas_1_mouse_down(self, x, y, button, **event_args):
    """This method is called when a mouse button is pressed on this component"""

    c = self.canvas_1
    p = self.pointSelected(self.points, (x,y), 20)
    q = self.pointSelected(self.midPoints,(x,y),10)
    
    if self.muisBeurt and not p == None:
      old_p = self.muisPoint
      if self.muisPoint == None or (p in self.points and p in self.burenPoints(self.muisPoint) and not self.midden(old_p,p) in self.katPoints):
        self.muisPoint = p
        self.muisBeurt = not self.muisBeurt

    if not self.muisBeurt and not q == None and not q in self.katPoints:
      self.katPoints.append(q)
      self.muisBeurt = not self.muisBeurt


    self.drawboard()      
      
    if len(self.katPoints) == 19:
      muisWinst = True
      c.clear_rect(100,250,575,75)
      c.fill_style = 'rgba(255,255,255,1)'
      c.fill_rect(100,250,575,75)

      c.fill_style = "rgba(0,0,255,1)"
      c.line_width = 2
      c.font = '72px montserrat'
      c.fill_text("De muis wint!!",100,300)
    
    buren = self.burenMidPoints(self.muisPoint)
    if buren != []:
      self.katWinst = True
      for b in buren:
        if b not in self.katPoints:
          katWinst = False
      if self.katWinst:
        c.clear_rect(100,250,575,75)
        c.fill_style = 'rgba(255,255,255,1)'
        c.fill_rect(100,250,575,75)
        
        c.fill_style = "rgba(255,0,0,1)"
        c.line_width = 2
        c.font = '72px montserrat'
        c.fill_text("De katten winnen!!",100,300)
        
    if not self.katWinst and not self.muisWinst:
      if self.muisBeurt == True and self.muisComputer == True:
        print("Muis aan zet en door de computer")
        print("Muispunt is nu:")
        print(self.muisPoint)
        self.muisPoint = random.choice(self.points)
        print("de computer heeft gekozen:")
        print(self.muisPoint)
      if self.katBeurt == True and self.katComputer == True:
        print("Katten aan zet en door de computer")
        print("Katpunten zijn nu:")
        print(self.katPoints)
        self.katPoints.append(random.choice(self.midPoints))
        print("de computer heeft gekozen:")
        print(self.katPoints)
        
        
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_2.text = "De computer speelt muis"
    self.muisComputer = not self.muisComputer
    

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_2.text = "De computer speelt katten"
    self.katComputer = not self.katComputer

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.muisPoint = None
    self.katPoints = []
    self.muisBeurt = False
    self.background = "rgba(223,246,142,1)"
    self.drawboard()






