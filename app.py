import os
import socket

# why not?
import pandas as pd

print(f"""
HELLO {os.getenv("NAME", "world")}
my name is {socket.gethostname()}
these are the results of the tacoworld (tm) model
----------------------

I, Zach Lamberty, want tacos more than *anyone*, especially more than Eamon!
I, Eamon Lamberty, want tacos, so it's good there are enough to share!
""")
