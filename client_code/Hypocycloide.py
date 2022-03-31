from ._anvil_designer import HypocycloideTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import math

class Hypocycloide(HypocycloideTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_box_1.text = ".9"
    self.text_box_2.text = "5"
    
    r=float(self.text_box_1.text)
    R=float(self.text_box_2.text)
    
    
    self.plot_1.data = self.hypocycloide(r,R,10000)
    self.plot_1.layout = {'title': 'Hypocycloide'}
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    ### Cycloide zonder gebruik van numpy, met gebruik matplotlib.pyplot

    r=float(self.text_box_1.text)
    R=float(self.text_box_2.text)

    
    self.plot_1.data = self.hypocycloide(r,R,10000)
    self.plot_1.layout = {'title': 'Hypocycloide'}
    
  def hypocycloide(self,r,R,e):
      x, y = [], []
      for i in range(e):
        t = 8*(i)/e*math.pi
        x.append((R-r)*math.cos(t)+r*math.cos((R-r)/r*t))
        y.append((R-r)*math.sin(t)-r*math.sin((R-r)/r*t))
      fig = go.Scatter(x=x, y=y)
      return(fig)




