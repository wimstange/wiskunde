from ._anvil_designer import Eenvoudige_FractalsTemplate
from anvil import *
import math as m


class Eenvoudige_Fractals(Eenvoudige_FractalsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.axioma = "F+F+F+F"
    self.schema = "FF+F+F+F+FF"
    self.lengte = 25
    self.hoek_gr = 60
    self.hoek = self.hoek_gr/180 * m.pi
    self.iteraties = 8
    self.productie = self.productie(self.axioma,self.schema,self.iteraties)
    
    c = self.canvas_1

  def volgende(self, woord, schema):
    for c in woord:
      if c not in {"F", "f", "+", "-"}:
            alert("ongeldige string")
    return woord.replace("F", schema)

  def productie(self, woord, schema, iteratie):
    resultaat = woord
    for i in range(iteratie):
        resultaat = volgende(resultaat,schema)
    return resultaat
        
  def teken(self, x,y,voorschrift, kleur):
    richting = 0
    x = x
    y = y
    for k in voorschrift:
        x_n, y_n = x+lengte*m.cos(richting),y+lengte*m.sin(richting)
        if k == "F":
            c.begin_path()
            c.line_to(x_n, y_n)
            c.close_path()
  
            c.stroke_style = kleur
            c.line_width = 3
            c.fill_style = kleur
  
            c.fill()
            c.stroke()

            x, y = x_n, y_n
        elif k == "f":
            x, y = x_n, y_n
        elif k == "+":
            richting += hoek
        elif k == "-":
            richting -= hoek
    
# Definieer kleuren

  zwart    = (   0,   0,   0)
  wit      = ( 255, 255, 255)
  groen    = (   0, 255,   0)
  rood     = ( 255,   0,   0)
  teken(150,150,self.voorschrift, zwart)
