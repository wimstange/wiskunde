import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.mpl_util
import matplotlib.pyplot as plt

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
anvil.server.callable
def say_hello(name):
  print("Hello, " + name + "!")
  return 42




@anvil.server.callable
def make_plot(x,y):
  
  # Plot it in the normal Matplotlib way
  plt.figure(1, figsize=(10,5))
  plt.plot(x, y, 'crimson')  
  
  # Return this plot as a PNG image in a Media object
  return anvil.mpl_util.plot_image()
