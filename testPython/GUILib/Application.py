import GUIObject
import sfml as sf
from Frame import *
class Application:
    
    def __init__(self,**kwargs):
        n = kwargs.get('n',"app")
        x = kwargs.get('x',0)
        y = kwargs.get('y',0)
        w = kwargs.get('w',0)
        h = kwargs.get('h',0)
        t = kwargs.get('t',"Application")
        self.main = Frame(n,x,y,w,h,t)
        return
    def run(self):
        while(self.main.Win.is_open):
            self.main.Update()
            self.main.Draw()
        return
    def setBackgroundColor(self,x):
        self.main.setBackgroundColor(x)
        return
    def addComponent(self,x):
        self.main.addComponent(x)



