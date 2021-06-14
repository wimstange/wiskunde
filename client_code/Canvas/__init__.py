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
    lines = [[0,1],[1,2],
         [0,3],[0,4],[1,4],[1,5],[2,5],[2,6],
         [3,4],[4,5],[5,6],
         [3,7],[3,8],[4,8],[4,9],[5,9],[5,10],[6,10],[6,11],
         [7,8],[8,9],[9,10],[10,11],
         [7,12],[8,12],[8,13],[9,13],[9,14],[10,14],[10,15],[11,15],
         [12,13],[13,14],[14,15],
         [12,16],[13,16],[13,17],[14,17],[14,18],[15,18],
         [16,17],[17,18]]
    
    midPoints = []

    for l in lines:
    
      midPoints.append((int((points[l[0]][0]+points[l[1]][0])/2),
                       int((points[l[0]][1]+points[l[1]][1])/2)))
      
    for line in lines:
      c.begin_path()
      c.move_to(points[line[0]][0],points[line[0]][1])
      x = points[line[1]][0]
      y = points[line[1]][1]
      c.line_to(x,y)
      c.stroke_style = "rgba(255,0,0,1)"
      c.line_width = 3
      c.fill_style = "rgba(255,0,0,1)"
      c.fill()
      c.stroke()    

    for p in points:
      c.begin_path()
      c.arc(p[0],p[1], 20,
            0, 2*math.pi,True)
      c.stroke_style = "#2196F3"
      c.line_width = 3
      c.fill_style = "rgba(0,0,255,1)"
      c.close_path()
      c.fill()
      c.stroke()
      
    for p in midPoints:
      c.begin_path()
      c.arc(p[0],p[1], 5,
            0, 2*math.pi,True)
      c.stroke_style = "rgba(0,0,0,1)"
      c.line_width = 3
      c.fill_style = "rgba(0,0,0,1)"
      c.fill()
      c.stroke()
    

    

  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    self.canvas_1_show()


