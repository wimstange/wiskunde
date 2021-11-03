from ._anvil_designer import peanolijnTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import math as m


class peanolijn(peanolijnTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.axioma  = "X"
    self.schema1 = "-YF+XFX+FY-"
    self.schema2 = "+XF-YFY-FX+"

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
  
  
    nmax = 7 #antal iteraties
    x, y = 150, 30 #beginpositie
    richting = 0
    hoek =  -m.pi/2 #verandering van richting bij commando + of -
    lengte =  5 # stapgrootte bij commando F of f
#    axioma = "X" # startfiguur. Wordt bij eerste generatie gevuld met schema1
#    schema1 = "-YF+XFX+FY-"
#    schema2 = "+XF-YFY-FX+"
    l1 = len(self.schema1)
    l2 = len(self.schema2)
    lp = max(l1,l2)
    p = []
    n = []
    for i in range(lp*nmax):
      p.append("")
      n.append(0)

    s, k = 1, 0
    p[0], n[0] = self.axioma, 0

    while s>0:
      while k < nmax:
        c = p[s]
        k = n[s] + 1
        s -= 1
        if c == "X":
            for i in range(lp):
                s += 1
                p[s] = self.schema1[lp - i-1]
                n[s] = k
        elif c == "Y":
            for i in range(lp):
                s += 1
                p[s] = self.schema2[lp - i-1]
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

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.soort.selected_value == "Hilbert versie":
      self.hoek_gr.text = 90
      self.axioma.text = "F"
      self.schema.text = "F-F+F+FF-F-F+F"
      self.iteraties.text = 3
      self.lengte.text = 10
      self.start_x.text = 100
      self.start_y.text = 400
    elif self.soort.selected_value == "Tweede versie":
      self.hoek_gr.text = 60
      axiomaext = "F+F+F+F+F+F"
      self.schema.text = "F+F--F+F"
      self.iteraties.text = 4
      self.lengte.text = 5
      self.start_x.text = 300
      self.start_y.text = 50
    elif self.soort.selected_value == "Gosper versie":
      self.axioma = "XF"
      self.schema1 = "X+YF++YF-FX--FXFX-YF+"
      self.schema2 = "-FX+YFYF++YF+FX--FX-Y"
    elif self.soort.selected_value == "Variant Minkowski lijn":
      self.hoek_gr.text = 90
      self.axioma.text = "+F"
      self.schema.text = "F+F-F-FFF+F+F-F"
      self.iteraties.text = 3
      self.lengte.text = 5
      self.start_x.text = 300
      self.start_y.text = 200
    elif self.soort.selected_value == "Vierkant van Sierpinski":
      self.hoek_gr.text = 90
      self.axioma.text = "F+F+F+F"
      self.schema.text = "FF+F+F+F+FF"
      self.iteraties.text = 3
      self.lengte.text = 25
      self.start_x.text = 100
      self.start_y.text = 50
    elif self.soort.selected_value == "Kwadratische variant Von Koch lijn":
      self.hoek_gr.text = 90
      self.axioma.text = "F"
      self.schema.text = "F+F-F-F+F"
      self.iteraties.text = 4
      self.lengte.text = 10
      self.start_x.text = 100
      self.start_y.text = 200
    elif self.soort.selected_value == "Archipel van Mandelbrot":
      self.hoek_gr.text = 90
      self.axioma.text = "F+F+F+F"
      self.schema.text = "F-f+FF-F-FF-Ff-FF+f-FF+F+FF+Ff+FF"
      self.schema2.text = "ffffff"
      self.iteraties.text = 3
      self.lengte.text = 5
      self.start_x.text = 300
      self.start_y.text = 50      
    self.canvas_1.reset_context()
    self.canvas_1_show()  



