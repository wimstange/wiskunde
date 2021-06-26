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
    lengte = float(self.lengte.text)
    self.voorschrift = self.productie(axioma,schema,iteraties)
    
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
#   lengte =3
#    hoek_gr = int(self.hoek_gr.text)
#    hoek = float(hoek_gr)/180 * m.pi
    x = self.start_x.text
    y = self.start_y.text
    kleur = rood

        
    for k in self.voorschrift:
        x_n, y_n = x+float(self.lengte.text)*m.cos(richting),y+float((self.lengte.text))*m.sin(richting)
        if k == "F":
            c.begin_path()
            c.move_to(x,y)  
            c.line_to(x_n, y_n)
            c.close_path()
  
            c.stroke_style = kleur
            c.line_width = 1
            c.fill_style = kleur
  
            c.fill()
            c.stroke()

            x, y = x_n, y_n
        elif k == "f":
            x, y = x_n, y_n
        elif k == "+":
            richting += float(self.hoek_gr.text)/180 * m.pi
        elif k == "-":
            richting -= float(self.hoek_gr.text)/180 * m.pi

  def axioma_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
#    axioma = self.axioma.text
#    schema = self.schema.text
#    self.voorschrift = self.productie(axioma,schema,2)
#    print(self.voorschrift)
#    self.canvas_1.reset_context
#    self.canvas_1_show

  def button_1_click(self, **event_args):
    """Deze methode wordt uitgevoerd als op de button 'teken fractal' wordt geklikt"""
    if 4 < int(self.iteraties.text) or int(self.iteraties.text) <1:
      antwoord = alert("De iteratiewaarde mag hoogstens 4 zijn.")
      self.iteraties.text = "4"             
    self.voorschrift = self.productie(self.axioma.text,self.schema.text,int(self.iteraties.text))
    self.canvas_1.reset_context()
    self.canvas_1_show()

  def soort_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.soort.selected_value == "lijn van Minkowski":
      self.hoek_gr.text = 90
      self.axioma.text = "F"
      self.schema.text = "F-F+F+FF-F-F+F"
      self.iteraties.text = 3
      self.lengte.text = 10
      self.start_x.text = 50
      self.start_y.text = 100
    elif self.soort.selected_value == "sneeuwvlok van Von Koch":
      self.hoek_gr.text = 60
      self.axioma.text = "F+F+F+F+F+F"
      self.schema.text = "F+F--F+F"
      self.iteraties.text = 4
      self.lengte.text = 5
      self.start_x.text = 300
      self.start_y.text = 50
    elif self.soort.selected_value == "Vierkant Minkowski eiland":
      self.hoek_gr.text = 90
      self.axioma.text = "F+F+F+F"
      self.schema.text = "F-F+F+FF-F-F+F"
      self.iteraties.text = 3
      self.lengte.text = 5
      self.start_x.text = 300
      self.start_y.text = 200
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
      self.lengte.text = 10
      self.start_x.text = 100
      self.start_y.text = 0
    elif self.soort.selected_value == "Kwadratische variant Von Koch lijn":
      self.hoek_gr.text = 90
      self.axioma.text = "F"
      self.schema.text = "F+F-F-F+F"
      self.iteraties.text = 4
      self.lengte.text = 10
      self.start_x.text = 100
      self.start_y.text = 200
    elif self.soort.selected_value == "Archipel van Mandelbrot":
      antwoord = alert("Dit is nog niet geimplementeerd")
#      self.hoek_gr.text = 90
#      self.axioma.text = "F+F+F+F"
#      self.schema.text = "F+F--F+F"
#      self.iteraties.text = 4
#      self.lengte.text = 5
#      self.start_x.text = 300
#      self.start_y.text = 50      
      



