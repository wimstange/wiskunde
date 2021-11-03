from ._anvil_designer import Nieuwe_wereldTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Nieuwe_wereld(Nieuwe_wereldTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    c = self.canvas_1
    #c.width = self.parent.N
    #c.height = self.parent.N
    #c.reset_context()