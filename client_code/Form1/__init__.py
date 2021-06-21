from ._anvil_designer import Form1Template
from anvil import *
import random

class Form1(Form1Template):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)



  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    pass

  def canvas_1_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    self.N = 80
    self.D = 10
    self.AAN = 255
    self.UIT = 0
    self.waarden = [self.AAN, self.UIT]


  def randomWereld(self,N):
   
    wereld = []
    for i in range(N):
        r = random.choices(waarden, weights = [0.2, 0.8], k = N)
        wereld.append(r)
    return wereld

    def volgendeGen(wereld):
    
      nieuweWereld = wereld.copy()
      N = len(wereld)
      for i in range(N):
        for j in range(N):
            waarde = int((wereld[i][(j-1)%N]+wereld[i][(j+1)%N]+wereld[(i-1)%N][j]+
                          wereld[(i+1)%N][j]+wereld[(i-1)%N][(j-1)%N]+wereld[(i-1)%N][(j+1)%N]+
                          wereld[(i+1)%N][(j-1)%N]+wereld[(i+1)%N][(j+1)%N])/255)
            if wereld[i][j] == AAN:
                if waarde <2 or waarde > 3:
                    nieuweWereld[i][j] = self.UIT
            else:
                if waarde == 3:
                    nieuweWereld[i][j] = self.AAN
                    
    return nieuweWereld

    def toonWereld(wereld,N):
      for i in range(N):
        for j in range(N):
            if wereld[i][j] == self.UIT:
                kleur = "rgba(0,0,50,1)"
            else:
                kleur = "rgba(255,0,0,1)"
            x, y = self.D*i, self.D*j
            c.begin_path()
            c.move_to(x,y)
            c.line_to(x+self.D,y)
            c.line_to(x+self.D,y+self.D)
            c.line_to(x,y+self.D)
            c.close_path()
  
            c.stroke_style = kleur
            c.line_width = 3
            c.fill_style = kleur
  
            c.fill()
            c.stroke()
        # pygame.draw.rect(screen,kleur,Rect((D*i,D*j),(D,D)))

    wereld = self.randomWereld(self.N)
    print(wereld)
    self,toonWereld(wereld,self.N)






