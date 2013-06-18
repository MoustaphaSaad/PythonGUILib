import sfml as sf
import abc
class GUIObject(object):
    Position = sf.Vector2()
    Size = sf.Vector2()
    name=""

    def __init__(self,n,x,y,w,h):
        self.Position.x = x
        self.Position.y = y
        self.Size.x = w
        self.Size.y = h
        self.name = n

    def setName(self,val):
        self.name = val
    def getName(self):
        return self.name
    def setPosition(self,x,y):
        self.Position.x=x
        self.Position.y=y

    def setSize(self,w,h):
        self.Size.x=w
        self.Size.y=h

    def getPosition(self):
        return self.Position

    def getSize(self):
        return self.Size
    @abc.abstractmethod
    def Update(self):
        """the update function"""
        return
    @abc.abstractmethod
    def Draw(self):
        """the draw function"""

