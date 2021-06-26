from ._anvil_designer import Eenvoudige_FractalsTemplate
from anvil import *

class Eenvoudige_Fractals(Eenvoudige_FractalsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.