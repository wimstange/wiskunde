from ._anvil_designer import Form1Template
from anvil import *
from ..Form1_detail import Form1_detail
from Pillow import Image

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    print(self.item)
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    item_copy = dict(list(self.item))
    save_clicked = alert(
      content=Form1_detail(item=item_copy),
      title="Het detail formulier",
      large=True,
      buttons=[("Save",True),("Cancel",False)],
    )
    if save_clicked:
    

      self.refresh_data_bindings()

    
    
 
