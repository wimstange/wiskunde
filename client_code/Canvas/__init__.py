from ._anvil_designer import CanvasTemplate
from anvil import *
import math

class Canvas(CanvasTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1
  
    c.begin_path()
    c.move_to(100,100)
    c.line_to(100,200)
    c.line_to(200,200)
    c.close_path()
    c.stroke_style = "#2196F3"
    c.line_width = 3
    c.fill_style = "#E0E0E0"
  
    c.fill()
    c.stroke()
    
    
    c.begin_path()
    c.arc(500, 200, 10, 0, 2*math.pi,True)
    c.close_path()
  
    c.stroke_style = "#2196F3"
    c.line_width = 3
    c.fill_style = "rgba(255,0,0,1)"
  
    c.fill()
    c.stroke()
    
    

