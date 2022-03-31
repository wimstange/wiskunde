from ._anvil_designer import Boom_van_PythagorasTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import random


class Boom_van_Pythagoras(Boom_van_PythagorasTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    def transf(x,y):
      return a*x-b*y-1+a, b*x+a*y+b

    a, b, c, d = .5, .5, .5, -.5
    d1, d2 = a*a+b*b, c*c+d*d
    q = d1/(d1+d2)
    max_n = 60000

    x, y = 0, 0
    x_rij, y_rij = [], []

    for n in range(max_n):
      r = random.random()
    
      if r <= q:
        x1, y1 = a*x-b*y-1+a, b*x+a*y+b
      else:
        x1, y1 = c*x-d*y+1-c, d*x+c*y-d
      x, y = x1, y1    
      x_rij.append(x)
      y_rij.append(y)
    fig = go.Scatter(x=x_rij, y=y_rij, mode="markers")  
    
    
    self.plot_1.data = fig
    self.plot_1.layout = {'title': 'Boom van Pythagoras'}
        
