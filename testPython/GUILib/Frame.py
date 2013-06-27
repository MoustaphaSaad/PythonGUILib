import GUIObject
import sfml as sf
class Container(GUIObject.GUIObject):
    Components = {}
    def __init__(self,n,x,y,w,h):
        return super(Container,self).__init__(n,x,y,w,h)

    def addComponent(self,Component):
        EXCEPTION = Exception
        try:
            self.Components[Component.getName()] = Component
        except EXCEPTION:
            print "[[NOT GUIObject CANNOT BE ADDED]]"
            print EXCEPTION.message

    def Update(self):
        for Component in self.Components :
            self.Components[Component].Update()
        return super(Container,self).Update()
    def Draw(self,Win):
        for Component in self.Components:
            self.Components[Component].Draw(Win)
        return super(Container,self).Draw()

class Frame(GUIObject.GUIObject):
    title = "WINDOW"
    Background = sf.Color.WHITE
    def __init__(self,n,x,y,w,h,t):
        super(Frame,self).__init__(n,x,y,w,h)
        self.title = t
        self.ini()
        return 
    def ini(self):
        self.Cont = Container(self.name,self.Position.x,self.Position.y,self.Size.x,self.Size.y)
        self.Win = sf.RenderWindow(sf.VideoMode(self.getSize().x,self.getSize().y),self.title)
        return
    def EVEHandle(self):
        for event in self.Win.events:
            if type(event) is sf.CloseEvent:
                self.Win.close()
        return
    def addComponent(self,comp):
        self.Cont.addComponent(comp)
        return
    def setBackgroundColor(self,Color):
        self.Background = Color
        return
    def Update(self):
        self.EVEHandle()
        self.Cont.Update()
        return
    def Draw(self):
        self.Win.clear(self.Background)
        self.Cont.Draw(self.Win)
        self.Win.display()
        return





