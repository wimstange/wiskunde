from ._anvil_designer import Eenvoudige_FractalsTemplate
from anvil import *
import math as m


class Eenvoudige_Fractals(Eenvoudige_FractalsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    axioma = self.axioma.text
    schema = self.schema.text

    hoek_gr = int(self.hoek_gr.text)
    hoek = float(hoek_gr)/180 * m.pi
    iteraties = int(self.iteraties.text)
    self.voorschrift = self.productie(axioma,schema,iteraties)
    
  def volgende(self, woord, schema):
    for c in woord:
      if c not in {"F", "f", "+", "-"}:
            alert("ongeldige string")
    return woord.replace("F", schema)

  def productie(self, woord, schema, iteratie):
    resultaat = woord
    for i in range(iteratie):
        resultaat = self.volgende(resultaat,schema)
    return resultaat
        
  def teken(self, x,y,voorschrift, kleur):
    c = self.canvas_1
    lengte = 25
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


  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    # Definieer kleuren

    zwart    = (   0,   0,   0)
    wit      = ( 255, 255, 255)
    groen    = (   0, 255,   0)
    rood     = ( 255,   0,   0)
    
    c = self.canvas_1
    richting = 0
    lengte = 25
    hoek_gr = int(self.hoek_gr.text)
    hoek = float(hoek_gr)/180 * m.pi
    x = 150
    y = 150
    kleur = zwart
    print(self.voorschrift)
    for k in self.voorschrift:
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

