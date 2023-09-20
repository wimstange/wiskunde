from ._anvil_designer import Margaret_KepnerTemplate
from anvil import *
import anvil.server

class Margaret_Kepner(Margaret_KepnerTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.kleur = "rgba(255,0,0,1)"
        self.a=300
        self.b=400
        # Any code you write here will run when the form opens.
    def canvas_1_show(self, **event_args):
        """This method is called when the Canvas is shown on the screen"""
        self.maak_vierkant()
         
    def maak_vierkant(self):
        c = self.canvas_1
        c.begin_path()
        c.move_to(self.a,self.b)
        c.line_to(self.a+10,self.b)
        c.line_to(self.a+10,self.b+10)
        c.line_to(self.a,self.b+10)
        c.close_path()
  
        c.stroke_style = self.kleur
        c.line_width = 1
        c.fill_style = self.kleur
  
        c.fill()
        c.stroke()
        