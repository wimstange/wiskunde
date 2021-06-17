from ._anvil_designer import CycloideTemplate
from anvil import *
import plotly.graph_objects as go
import math


class Cycloide(CycloideTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    r = 1
    self.plot_1.data = self.cycloide(r,10000)
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    ### Spiraal van Archimedes zonder gebruik van numpy, met gebruik matplotlib.pyplot
    
    r = float(self.text_box_1.text)
    self.plot_1.data = self.cycloide(r,10000)
    self.plot_1.layout = {'title': 'Cycloide'}
    
  def cycloide(self,r,e):
      x, y = [], []
      for i in range(e):
        t = 8*(i)/e*math.pi
        x.append(r*t-r*math.sin(t))
        y.append(r-r*math.cos(t))
      fig = go.Scatter(x=x, y=y)
      # fig.update_yaxes(scaleanchor = "x",scaleratio = 1)
      return(fig)




