from ._anvil_designer import Eenvoudige_FractalsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import math as m
from ..Eenvoudige_Fractals.uitleg import uitleg


class Eenvoudige_Fractals(Eenvoudige_FractalsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    axioma = self.axioma.text
    schema = self.schema.text
    schema2 = self.schema2.text
    hoek_gr = int(self.hoek_gr.text)
    hoek = float(hoek_gr)/180 * m.pi
    iteraties = int(self.iteraties.text)
    lengte = float(self.lengte.text)
    self.voorschrift = self.productie(axioma,schema,schema2, iteraties)
    
  def volgende(self, woord, schema, schema2):
    for c in woord:
      if c not in {"F", "f", "+", "-"}:
            alert("ongeldige string")
      result = woord.replace("F", schema)
      if not schema2 == "":
        result = result.replace("f", schema2)
    return result

  def productie(self, woord, schema, schema2,iteraties):
    resultaat = woord
    for i in range(iteraties):
        resultaat = self.volgende(resultaat,schema, schema2)
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

  def button_1_click(self, **event_args):
    """Deze methode wordt uitgevoerd als op de button 'teken fractal' wordt geklikt"""
    if 4 < int(self.iteraties.text) or int(self.iteraties.text) <1:
      antwoord = alert("De iteratiewaarde mag hoogstens 4 zijn.")
      self.iteraties.text = "4"             
    self.voorschrift = self.productie(self.axioma.text,self.schema.text,self.schema2.text,int(self.iteraties.text))
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
      self.start_x.text = 100
      self.start_y.text = 400
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
    self.voorschrift = self.productie(self.axioma.text,self.schema.text,self.schema2.text,int(self.iteraties.text))
    self.canvas_1.reset_context()
    self.canvas_1_show()  

  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    self.canvas_1_show()

  def uitleg_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(content=uitleg.uitleg())





