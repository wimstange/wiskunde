from ._anvil_designer import Nieuwe_wereldTemplate
from anvil import *

class Nieuwe_wereld(Nieuwe_wereldTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.