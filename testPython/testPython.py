from GUILib import *
this = Application(n="APP",x=100,y=100,w=640,h=480,t="TEET")
this.setBackgroundColor(sf.Color.BLACK)
r = CButton(frame=this.main,n="fd",x=100,y=100,w=100,h=30,c=sf.Color.CYAN)
this.addComponent(r)
r.setRadius(5)
this.run()