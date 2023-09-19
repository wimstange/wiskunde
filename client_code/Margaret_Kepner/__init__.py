from ._anvil_designer import Margaret_KepnerTemplate
from anvil import *
import anvil.server

class Margaret_Kepner(Margaret_KepnerTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.N = 80
        self.wereld = []

        # Any code you write here will run when the form opens.
    def canvas_1_show(self, **event_args):
        """This method is called when the Canvas is shown on the screen"""
        c = self.canvas_1
         
        kleur = "rgba(255,0,0,1)"
        i=3
        j=4
        c.begin_path()
        c.move_to(i*10,j*10)
        c.line_to(i*10+10,j*10)
        c.line_to(i*10+10,j*10+10)
        c.line_to(i*10,j*10+10)
        c.close_path()
  
        c.stroke_style = kleur
        c.line_width = 1
        c.fill_style = kleur
  
        c.fill()
        c.stroke()