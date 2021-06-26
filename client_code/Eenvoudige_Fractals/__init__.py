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
    self.hoek = 60
    self.iteraties = 8

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
    for c in voorschrift:
        if c == "F":
            x_n, y_n = x+lengte*m.cos(richting),y+lengte*m.sin(richting)
            p.draw.line(screen, kleur, (x,y), (x_n, y_n),3)
            x, y = x_n, y_n
        elif c == "f":
            x+lengte,y+lengte
        elif c == "+":
            richting += hoek
        elif c == "-":
            richting -= hoek
    



# Definieer kleuren

zwart    = (   0,   0,   0)
wit      = ( 255, 255, 255)
groen    = (   0, 255,   0)
rood     = ( 255,   0,   0)

    