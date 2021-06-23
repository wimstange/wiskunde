from ._anvil_designer import Form1_detailTemplate
from anvil import *

class Form1_detail(Form1_detailTemplate, item=new_items):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.