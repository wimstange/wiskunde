from ._anvil_designer import KrommenTemplate
from anvil import *
from ..Hypocycloide import Hypocycloide
from ..Lissajous import Lissajous

class Krommen(KrommenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Hypocycloide())

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Lissajous())


