from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import math

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    ### Lissajous figuur zonder gebruik van numpy, met gebruik matplotlib.pyplot

    
    self.plot_1.data = self.lissajous(5,14,32,7,1000)
    
  def lissajous(self,a,b,c,d,e):
      x, y = [], []
      for i in range(e):
        t = 2*(i)/e*math.pi
        x.append(a*math.sin(c*t))
        y.append(b*math.cos(d*t))
      fig = go.Scatter(x=x, y=y)
      return(fig)




