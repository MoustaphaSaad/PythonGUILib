import Clickable
import GUIObject
class AbstractButton(GUIObject.GUIObject,Clickable.Clickable):
    ButtonLabel=""
    def __init__(self,frame):
        self.Frame = frame
        return
    def setLabel(self,val):
        self.ButtonLabel=val
    def getLabel(self):
        return self.ButtonLabel

    def Clicked(self,event):
        event()
        return
    def Hoverred(self,event):
        event()
        return
    def Update(self):
        if(self.isClicked):
            self.Clicked(getattr(self.Frame,self.name+"Clicked"))
        if(self.isHoverred):
            self.Hoverred(getattr(self.Frame,self.name+"Hoverred"))
        return
    
