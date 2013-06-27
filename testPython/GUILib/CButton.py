import AbstractButton
import RoundRect
import sfml as sf
class CButton(AbstractButton.AbstractButton):
    def __init__(self, **kwargs):
        x = kwargs.get('x',0)
        y = kwargs.get('y',0)
        w = kwargs.get('w',0)
        h = kwargs.get('h',0)
        frame = kwargs.get('frame',0)
        r = kwargs.get('r',0)
        n = kwargs.get('n',0)
        c = kwargs.get('c',sf.Color.GREEN)
        self.ButtonLabel = kwargs.get('label',n)
        self.body = RoundRect.RoundRect(x,y,w,h,r,c)
        return super(CButton, self).__init__(frame,n,x,y,w,h)
    def setRadius(self,r):
        self.body.setRadius(r)
        return
    def Update(self):
        self.body.Update()
        return super(CButton, self).Update()
    def Draw(self,win):
        self.body.draw(win)
        return super(CButton, self).Draw()



