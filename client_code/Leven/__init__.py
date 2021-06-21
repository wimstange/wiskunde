from ._anvil_designer import LevenTemplate
from anvil import *
import random

class Leven(LevenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.N = 80
    self.wereld = []
    # Any code you write here will run when the form opens.
    for i in range(self.N):
        r = []
        for j in range(self.N):
            t = random.random()
            if t<0.1:
              r.append(0)
            else:
              r.append(255)
        self.wereld.append(r)

  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1
         
    for i in range(self.N):
      for j in range(self.N):
        if self.wereld[i][j] == 0:
          kleur = "rgba(255,0,0,1)"
        else: 
          kleur = "rgba(50,200,25,1)"
        c.begin_path()
        c.move_to(i*10,j*10)
        c.line_to(i*10+10,j*10)
        c.line_to(i*10+10,j*10+10)
        c.line_to(i*10,j*10+10)
        c.close_path()
  
        c.stroke_style = kleur
        c.line_width = 1
        c.fill_style = kleur
  
        c.fill()
        c.stroke()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    nieuweWereld = self.wereld.copy()
    for i in range(self.N):
        for j in range(self.N):
            waarde = int((self.wereld[i][(j-1)%self.N]+self.wereld[i][(j+1)%self.N]+self.wereld[(i-1)%self.N][j]+
                          self.wereld[(i+1)%self.N][j]+self.wereld[(i-1)%self.N][(j-1)%self.N]+self.wereld[(i-1)%self.N][(j+1)%self.N]+
                          self.wereld[(i+1)%self.N][(j-1)%self.N]+self.wereld[(i+1)%self.N][(j+1)%self.N])/255)
            if self.wereld[i][j] == 255:
                if waarde <2 or waarde > 3:
                    nieuweWereld[i][j] = 0
            else:
                if waarde == 3:
                    nieuweWereld[i][j] = 255
                    
    self.wereld = nieuweWereld
    self.canvas_1_show()
    


