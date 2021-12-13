#import for Start
import insertFunct as infu
import numpy as np
import graph as graph
import cmath
from os import path
from platform import system

def rcpath(rel_path):
    iconPath=path.dirname(path.realpath(__file__))+"\\" + rel_path
    if system == "Windows":                #if OS=Windows replace slashes
        iconPath=iconPath.replace("\\","/")
    return iconPath

def getModulus(complex):
    return abs(complex)

def getPhaseElem(complex):
    return cmath.phase(complex)

def getPhase(complexLinSpace):
    phaseRadian=np.vectorize(getPhaseElem)
    return phaseRadian(complexLinSpace)

lastExpr = ""
def lookData():
    global evalLinSpace
    infu.extract_data()
    if infu.num!="" and len(infu.num)>0:
        lastExpr=infu.gStatic+"*"+ "("+ "(" + infu.num + ")" + "/" + "(" + infu.den +")" + ")"      #Ks*((Num)/(Den))
        infu.num=""
        infu.den=""
        infu.gStatic=""
        lastExpr=lastExpr.replace('s','j*w')
        evalLinSpace=(eval(lastExpr, {"w": graph.x*2*cmath.pi, "f": graph.x, "np": np}))

        #calculate Module and Phase:
        modulus=getModulus(evalLinSpace)
        modulusdB=20*np.log10(modulus)

        phaseRadian=getPhase(evalLinSpace)
        phase=np.degrees(phaseRadian)

        graph.modulus=modulusdB
        graph.phase=phase
        graph.axModP.set_ydata(graph.modulus)
        graph.axPhP.set_ydata(graph.phase)
        
    infu.window.after(50, lookData)

# run the gui
infu.plot()
graph.autoScale(0)
infu.window.after(50, lookData)
infu.window.iconbitmap(rcpath('/images/icon.ico'))
infu.window.mainloop()
