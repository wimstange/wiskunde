from ._anvil_designer import LevenTemplate
from anvil import *
import random

class Leven(LevenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.N = 80
    # Any code you write here will run when the form opens.
    

  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1
#    N = 80
    wereld = []
    for i in range(self.N):
        r = []
        for j in range(self.N):
            t = random.random()
            if t<0.1:
              r.append(0)
            else:
              r.append(255)
        wereld.append(r)
         
    for i in range(self.N):
      for j in range(self.N):
        if wereld[i][j] == 255:
          kleur = "rgba(255,0,0,1)"
        else: 
          kleur = "rgba(0,0,25,1)"
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
    pass


