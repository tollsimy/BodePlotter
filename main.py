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

expr = ""
lastExpr="1*((1)/(1+1j*f))"
def lookData():
    global evalLinSpace
    global lastExpr
    infu.extract_data()
    if infu.num!="" and len(infu.num)>0:
        expr=infu.gStatic+"*"+ "("+ "(" + infu.num + ")" + "/" + "(" + infu.den +")" + ")"      #Ks*((Num)/(Den))
        infu.num=""
        infu.den=""
        infu.gStatic=""
        expr=expr.replace('s','j*w')
        try:
            evalLinSpace=(eval(expr, {"w": graph.x*2*cmath.pi, "f": graph.x, "np": np}))
            lastExpr=expr
            infu.text_stringDebug.configure(state="normal")
            infu.text_stringDebug.delete("1.0", "end")
            infu.text_stringDebug.insert("end", "Valid expression")
            infu.text_stringDebug.configure(state="disabled")
        except Exception as err:
            err=str(err)
            if(err=="unmatched ')' (<string>, line 1)") or err=="invalid syntax (<string>, line 1)":
                err=str(err)[:-18]         #cut "(<string>, line 1)"
            print("Expression not valid: " + err)
            infu.text_stringDebug.configure(state="normal")
            infu.text_stringDebug.delete("1.0", "end")
            infu.text_stringDebug.insert("end", err)
            infu.text_stringDebug.configure(state="disabled")
            infu.funcWindow.deiconify()
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
