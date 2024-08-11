import os
import eel
from Backend.features import *
from Backend.speak import *

eel.init("Frontend")

# function for starting sound
playStartSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"') # opennig in app window -> we can use any browser for it chrome (Here, msedge)
eel.start('index.html', mode=None, host='localhost', block=True)