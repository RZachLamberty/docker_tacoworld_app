import os
import socket

# why not?
import pandas as pd

print('\nHELLO {name}'.format(name=os.getenv("NAME", "world")))
print('my name is {}'.format(socket.gethostname()))
print('these are the results of the tacoworld (tm) model')
print('----------------------\n')
print("I, Zach Lamberty, want tacos more than *anyone*, especially more than Dan!")
print("I, Dan Fein, want tacos, so it's good there are enough to share!")
