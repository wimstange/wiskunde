from ._anvil_designer import peanolijnTemplate
from anvil import *
import math as m


class peanolijn(peanolijnTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    

  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    q = self.canvas_1
    def teken(c, x,y, richting, voorschrift, kleur):
    
      x = x
      y = y
      for c in voorschrift:
        if c == "F":
          x_n, y_n = x+lengte*m.cos(richting),y+lengte*m.sin(richting)
          q.begin_path()
          q.move_to(x,y)  
          q.line_to(x_n, y_n)
          q.close_path()
  
          q.stroke_style = kleur
          q.line_width = 1
          q.fill_style = kleur
  
          q.fill()
          q.stroke()
          x, y = x_n, y_n
        elif c == "f":
          x+=lengte
          y+=lengte
        elif c == "+":
          richting += hoek
        elif c == "-":
          richting -= hoek
      return (x, y), richting
  
  
    nmax = 7#antal iteraties
    x, y = 175, 30 #beginpositie
    richting = 0
    hoek =  -m.pi/2 #verandering van richting bij commando + of -
    lengte =  17# stapgrootte bij commando F of f
    axioma = "X" # startfiguur. Wordt bij eerste generatie gevuld met schema1
    schema1 = "-YF+XFX+FY-"
    schema2 = "+XF-YFY-FX+"
    l1 = len(schema1)
    l2 = len(schema2)
    lp = max(l1,l2)
    p = []
    n = []
    for i in range(lp*nmax):
      p.append("")
      n.append(0)

    s, k = 1, 0
    p[0], n[0] = "X", 0

    while s>0:
      while k < nmax:
        c = p[s]
        k = n[s] + 1
        s -= 1
        if c == "X":
            for i in range(lp):
                s += 1
                p[s] = schema1[lp - i-1]
                n[s] = k
        elif c == "Y":
            for i in range(lp):
                s += 1
                p[s] = schema2[lp - i-1]
                n[s] = k
        elif c == "F" or c == "+" or c == "-":
            s += 1
            p[s] = c
            n[s] = k
      c = p[s]
      (x,y), richting = teken(q, x, y, richting, c, "rgba(255,0,0)") # tekenen
      s -= 1
      k = n[s]

  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    self.canvas_1_show()


