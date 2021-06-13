from ._anvil_designer import CanvasTemplate
from anvil import *
import math

class Canvas(CanvasTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
   
  def transform(self, points,multp,add):
    result = []
    for point in points:
        result.append((multp*point[0]+add,multp*point[1]+add))
    return result
  
  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1
    MULTP = 64
    ADD = 75
    DISTANCE = 20 
    pointsBase = [(2,0),(4,0),(6,0),
              (1,2),(3,2),(5,2),(7,2),
              (0,4),(2,4),(4,4),(6,4),(8,4),
              (1,6),(3,6),(5,6),(7,6),
              (2,8),(4,8),(6,8)]
    
    points = self.transform(pointsBase,MULTP,ADD)
    
    
    
    for p in points:
      c.begin_path()
      c.arc(p[0],p[1], 20,
            0, 2*math.pi,True)
    
  
      c.stroke_style = "#2196F3"
      c.line_width = 3
      c.fill_style = "rgba(255,0,0,1)"

      c.fill()
      c.stroke()
    
    c.close_path()

