from ._anvil_designer import Margaret_KepnerTemplate
from anvil import *
import anvil.server

class Margaret_Kepner(Margaret_KepnerTemplate):
   
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Lijst met punten voor je figuur
        self.points = [(100, 100), (150, 150), (200, 100), (250, 150)]
    def canvas_1_show(self, **event_args):
        # Teken de lijnen tussen de punten
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            self.canvas_1.draw_line(x1, y1, x2, y2, color="black", width=2)        