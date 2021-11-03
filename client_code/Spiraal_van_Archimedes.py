from ._anvil_designer import Spiraal_van_ArchimedesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import math

class Spiraal_van_Archimedes(Spiraal_van_ArchimedesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
        
    self.plot_1.data = self.spiraal_van_archimedes(10000)
    self.plot_1.layout = {'title': 'Spiraal van Archimedes'}
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    ### Spiraal van Archimedes zonder gebruik van numpy, met gebruik matplotlib.pyplot
    
    self.plot_1.data = self.spiraal_van_archimedes(10000)
    self.plot_1.layout = {'title': 'Spiraal van Archimedes'}
    #self.plot_1.update_yaxes(scaleanchor = "x",scaleratio = 3,)
    
  def spiraal_van_archimedes(self,e):
      x, y = [], []
      for i in range(e):
        t = 8*(i)/e*math.pi
        x.append(t*math.cos(t))
        y.append(t*math.sin(t))
      fig = go.Scatter(x=x, y=y)
      # fig.update_yaxes(scaleanchor = "x",scaleratio = 1)
      return(fig)




