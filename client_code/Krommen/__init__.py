from ._anvil_designer import KrommenTemplate
from anvil import *
from ..Spiraal_van_Archimedes import Spiraal_van_Archimedes
from ..Hypocycloide import Hypocycloide
from ..Lissajous import Lissajous
from ..Canvas import Canvas

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

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Canvas())

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Spiraal_van_Archimedes())








