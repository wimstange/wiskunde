from ._anvil_designer import LissajousTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import math

class Lissajous(LissajousTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_box_1.text = "1"
    self.text_box_2.text = "1"
    self.text_box_3.text = "1"
    self.text_box_4.text = "1"
    a=int(self.text_box_1.text)
    b=int(self.text_box_2.text)
    c=int(self.text_box_3.text)
    d=int(self.text_box_4.text)
    
    self.plot_1.data = self.lissajous(a,b,c,d,10000)
    self.plot_1.layout = {'title': 'Kromme van Lissajous'}
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    ### Lissajous figuur zonder gebruik van numpy, met gebruik matplotlib.pyplot

    a=int(self.text_box_1.text)
    b=int(self.text_box_2.text)
    c=int(self.text_box_3.text)
    d=int(self.text_box_4.text)
    
    self.plot_1.data = self.lissajous(a,b,c,d,10000)
    self.plot_1.layout = {'title': 'Kromme van Lissajous'}
    
  def lissajous(self,a,b,c,d,e):
      x, y = [], []
      for i in range(e):
        t = 2*(i)/e*math.pi
        x.append(a*math.sin(c*t))
        y.append(b*math.cos(d*t))
      fig = go.Scatter(x=x, y=y)
      return(fig)




