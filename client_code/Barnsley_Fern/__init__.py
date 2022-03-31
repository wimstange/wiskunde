from ._anvil_designer import Barnsley_FernTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import plotly.graph_objects as go

class Barnsley_Fern(Barnsley_FernTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.draw_fern(int(self.text_box_1.text))

        
        

    def transformation_1(self,p):
        x = p[0]
        y = p[1]
        x1 = 0.85*x + 0.04*y
        y1 = -0.04*x + 0.85*y + 1.6
        return x1, y1

    def transformation_2(self, p):
        x = p[0]
        y = p[1]
        x1 = 0.2*x - 0.26*y
        y1 = 0.23*x + 0.22*y + 1.6
        return x1, y1

    def transformation_3(self, p):
        x = p[0]
        y = p[1]
        x1 = -0.15*x + 0.28*y
        y1 = 0.26*x  + 0.24*y + 0.44
        return x1, y1

    def transformation_4(self, p):
        x = p[0]
        y = p[1]
        x1 = 0
        y1 = 0.16*y
        return x1, y1
    
    def get_index(self, probability):
        r = random.random()
        c_probability = 0
        sum_probability = []
        for p in probability:
            c_probability += p
            sum_probability.append(c_probability)
        for item, sp in enumerate(sum_probability):
            if r <= sp:
                return item
        return len(probability)-1
    
    def transform(self, p):
        # list of transformation functions
        transformations = [self.transformation_1, self.transformation_2,
                            self.transformation_3, self.transformation_4]
        probability = [0.85, 0.07, 0.07, 0.01]
        # pick a random transformation function and call it
        tindex = self.get_index(probability)
        t = transformations[tindex]
        x, y = t(p)
        return x, y
    
    def draw_fern(self, n):
        # We start with (0, 0)
        x_rij = [0]
        y_rij = [0]
        x1, y1 = 0, 0
        for i in range(n):
            x1, y1 = self.transform((x1, y1))
            x_rij.append(x1)
            y_rij.append(y1)
        
        # Plot the points
        media_obj = anvil.server.call('make_plot')
        self.image_1.source = media_obj
        self.download_link.url = media_obj
        
        
        fig = go.Scatter(x=x_rij, y=y_rij, mode="markers")  
    
    
        self.plot_1.data = fig
        self.plot_1.layout = {'title': 'Barnsley Fern'}

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.draw_fern(int(self.text_box_1.text))

