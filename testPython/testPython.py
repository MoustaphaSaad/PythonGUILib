import GUILib
F = GUILib.Frame("moka",0,0,800,600,"jlnkl")
while(F.Win.is_open):
    F.Update()
    F.Draw()
print F.getName()
print "OK\n"