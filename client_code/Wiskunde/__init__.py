from ._anvil_designer import WiskundeTemplate
from anvil import *
from ..Spiraal_van_Archimedes import Spiraal_van_Archimedes
from ..Hypocycloide import Hypocycloide
from ..Lissajous import Lissajous
from ..Cycloide import Cycloide
from ..Kat_en_muis import Kat_en_muis
from ..Boom_van_Pythagoras import Boom_van_Pythagoras
from ..Leven import Leven
from ..Eenvoudige_Fractals import Eenvoudige_Fractals

class Wiskunde(WiskundeTemplate):
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
    self.content_panel.add_component(Kat_en_muis())

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Spiraal_van_Archimedes())

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Cycloide())

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Boom_van_Pythagoras())

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Leven())

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Eenvoudige_Fractals())











