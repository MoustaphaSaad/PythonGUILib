
import abc
class Clickable(object):
    isClicked=False
    isHoverred=False
    @abc.abstractmethod
    def Clicked(self,f):
        """the abstract clicked function"""
        return
    @abc.abstractmethod
    def Hoverred(self):
        """the abstract hovered function"""
        return
