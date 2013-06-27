import sfml as sf
import GUIObject
import math
class RoundRect():
    body1 = sf.RectangleShape()
    body2 = sf.RectangleShape()
    c1 = sf.CircleShape()
    c2 = sf.CircleShape()
    c3 = sf.CircleShape()
    c4 = sf.CircleShape()
    COLOR = sf.Color.GREEN
    Position = sf.Vector2()
    Size= sf.Vector2()
    Radius =0
    def __init__(self, x,y,w,h,r,C):
        self.Position = sf.Vector2(x,y)
        self.Size=sf.Vector2(w,h)
        self.Radius=r
        self.COLOR=C
        self.init()
        return
    def init(self):
        self.body1.position = sf.Vector2(100,100+self.Radius)
        self.body2.position = sf.Vector2(100+self.Radius,100)
        self.body1.size = sf.Vector2(self.Size.x+2*self.Radius,self.Size.y)
        self.body2.size = sf.Vector2(self.Size.x,self.Size.y+2*self.Radius)
        self.body1.fill_color = self.COLOR
        self.body2.fill_color = self.COLOR
        self.c1.fill_color = self.COLOR
        self.c2.fill_color = self.COLOR
        self.c3.fill_color = self.COLOR
        self.c4.fill_color = self.COLOR
        self.c4.radius = self.Radius
        self.c1.radius = self.Radius
        self.c2.radius = self.Radius
        self.c3.radius = self.Radius
        self.c4.position = sf.Vector2(self.body1.position.x+self.body1.size.x-2*self.Radius,self.body2.position.y+self.body2.size.y-2*self.Radius)
        self.c3.position= sf.Vector2(self.body1.position.x,self.body2.position.y+self.body2.size.y-2*self.Radius)
        self.c2.position = sf.Vector2(self.body1.position.x+self.body1.size.x-2*self.Radius,self.body2.position.y)
        self.c1.position = sf.Vector2(self.body1.position.x,self.body2.position.y)
        return
    def Update(self):
        self.init()
        return
    def setRadius(self,r):
        self.Radius = r
        return
    def draw(self,win):
        win.draw(self.body2)
        win.draw(self.body1)
        win.draw(self.c2)
        win.draw(self.c1)
        win.draw(self.c3)
        win.draw(self.c4)
        return



