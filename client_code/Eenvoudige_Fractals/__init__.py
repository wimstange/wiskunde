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
    self.voorschrift = self.productie(axioma,schema,4)
    
  def volgende(self, woord, schema):
    for c in woord:
      if c not in {"F", "f", "+", "-"}:
            alert("ongeldige string")
    return woord.replace("F", schema)

  def productie(self, woord, schema, iteraties):
    resultaat = woord
    for i in range(iteraties):
        resultaat = self.volgende(resultaat,schema)
    return resultaat
        
  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    # Definieer kleuren

    zwart    = "rgba(   0,   0,   0)"
    wit      = "rgba( 255, 255, 255)"
    groen    = "rgba(   0, 255,   0)"
    rood     = "rgba(255,   0,   0)"
    
    c = self.canvas_1
    richting = 0
    lengte = 10
    hoek_gr = int(self.hoek_gr.text)
    hoek = float(hoek_gr)/180 * m.pi
    x = 0
    y = 0
    kleur = rood

        
    for k in self.voorschrift:
        x_n, y_n = x+lengte*m.cos(richting),y+lengte*m.sin(richting)
        if k == "F":
            c.begin_path()
            c.move_to(x,y)  
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

  def axioma_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    axioma = self.axioma.text
    schema = self.schema.text
    self.voorschrift = self.productie(axioma,schema,2)
    print(self.voorschrift)
#    self.canvas_1.reset_context
    self.canvas_1_show


