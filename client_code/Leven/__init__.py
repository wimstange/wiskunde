from ._anvil_designer import LevenTemplate
from anvil import *
import random
from ..Nieuwe_wereld import Nieuwe_wereld
class Leven(LevenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.N = 80
    self.wereld = []
    # Any code you write here will run when the form opens.
    self.randomWereld(self.N)
    
#    for i in range(self.N):
#        r = []
#        for j in range(self.N):
#            t = random.random()
#            if t<0.2:
#              r.append(0)
#            else:
#              r.append(255)
#        self.wereld.append(r)
    
  def randomWereld(self, N):
    self.wereld = []
 
    for i in range(self.N):
        r = []
        for j in range(self.N):
            t = random.random()
            if t<0.2:
              r.append(255)
            else:
              r.append(0)
        self.wereld.append(r)

  
  
  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1
         
    for i in range(self.N):
      for j in range(self.N):
        if self.wereld[i][j] == 255:
          kleur = "rgba(255,0,0,1)"
        else: 
          kleur = "rgba(50,200,25,1)"
        c.begin_path()
        c.move_to(i*10,j*10)
        c.line_to(i*10+10,j*10)
        c.line_to(i*10+10,j*10+10)
        c.line_to(i*10,j*10+10)
        c.close_path()
  
        c.stroke_style = kleur
        c.line_width = 1
        c.fill_style = kleur
  
        c.fill()
        c.stroke()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.timer_1.interval=0

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    self.canvas_1.width = str(self.N*10)
    self.canvas_1.height = str(self.N*10)
    self.canvas_1.reset_context()
    self.randomWereld(self.N)
    self.timer_1.interval = 2
    self.canvas_1_show()

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    
    self.N = int(self.text_box_1.text)

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    nieuweWereld = self.wereld.copy()
    for i in range(self.N):
        for j in range(self.N):
            waarde = int((self.wereld[i][(j-1)%self.N]+self.wereld[i][(j+1)%self.N]+
                          self.wereld[(i-1)%self.N][j]+self.wereld[(i+1)%self.N][j]+
                          self.wereld[i-1][(j-1)%self.N]+self.wereld[(i-1)%self.N][(j+1)%self.N]+
                          self.wereld[(i+1)%self.N][(j-1)%self.N]+self.wereld[(i+1)%self.N][(j+1)%self.N])/255)
            if self.wereld[i][j] == 255:
                if waarde < 2 or waarde > 3:
                    nieuweWereld[i][j] = 0
            else:
                if waarde == 3:
                    nieuweWereld[i][j] = 255
                    
    self.wereld[:] = nieuweWereld[:]
    self.canvas_1_show()

  def button_3_click(self, **event_args):

      save_clicked = alert(content=Nieuwe_wereld(),
                           title="Maak nieuwe wereld",
                           large=True,
                           buttons=[("Save",True),("Cancel",False)],
                          )
    # If the alert returned 'True', the save button was clicked.
      if save_clicked:
        print("De wereld is veranderd.")
    






