from ._anvil_designer import SymmetrieTemplate
from anvil import *
import anvil.server
import math


class Symmetrie(SymmetrieTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.X = []
        self.Y = []

        # Any code you write here will run when the form opens.


    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        print("Ik klik")
        c = self.canvas_1
        c.stroke_style = "rgba(100,100,100,1)"
        c.line_width = 1
        c.fill_style = "rgba(100,100,100,1)"
        c.begin_path()
        c.move_to(0,0)
        for k in range(400):
            t = 2 * k * math.pi / 400
            r = 1 + 1.5 * math.cos(7*t+math.cos(7*t))
            c.line_to(r*math.cos(t),r*math.sin(t))
        c.close_path()
        c.fill()
        c.stroke()
        print("Ik heb geklikt!")

    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.link_1_click()



        

