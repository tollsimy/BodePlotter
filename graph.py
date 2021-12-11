from tkinter.constants import Y
import demoFunct as dmf
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button

if __name__ == "__main__":
    print("This script is a module and can't run on it's own, start main.py instead!")

def roundRange(valueMin,valueMax,axis):

    if(axis=="modulus"):
        axMin=YMinMod
        axMax=YMaxMod
    elif(axis=="phase"):
        axMin=YMinPh
        axMax=YMaxPh
    elif(axis=="x"):
        axMin=XMin
        axMax=XMax
    else:
        raise Exception("axis can be 'modulus, 'phase' or 'x'!")

    if((valueMin-10)<axMin):
        valueMin=axMin
    else:
        valueMin-=10
        valueMin=round(valueMin)

    if((valueMax+10)>axMax):
        valueMax=axMax
    else:
        valueMax+=10
        valueMax=round(valueMax)
    
    return (valueMin,valueMax)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def set_labels(artists, labels):
    for artist, label in zip(artists, labels):
        artist.set_label(label)

#default values
XMin=0.001
XMax=10000000000
resolution=1000      #mnumber of points in the X array  
YMinMod=-5000
YMaxMod=5000
YMinPh = -180
YMaxPh = +180
defaultXaxisMin = "1"
defaultXaxisMax = "1000000"
defaultYaxisMinMod = "-50"
defaultYaxisMaxMod = "100"
defaultYaxisMinPh = "-180"
defaultYaxisMaxPh = "180"
maxStrLenghtX=10
maxStrLenghtYMod=5

x = x = np.logspace(np.log10(XMin),np.log10(XMax),num=resolution)       #X Axis space
modulus = dmf.mod                                                       #modulus space
phase = dmf.phase                                                       #phase space

fig, (axMod, axPh) = plt.subplots(2,1,figsize=(10,6))
axMod.set_ylabel("|H(jw)| dB")
axPh.set_ylabel("<H(jw) °")
axMod.set_xscale("log")
axPh.set_xscale("log")
axPh.set_yticks(range(int(defaultYaxisMinPh),int(defaultYaxisMaxPh),45))
plt.xlabel("frequency")
plt.grid(True, which="both")
plt.ion()
axMod.grid(which='minor', alpha=0.5)
axMod.grid(which='major', alpha=0.5)
axPh.grid(which='minor', alpha=0.5)
axPh.grid(which='major', alpha=0.5)
axMod.margins(0, 0)    #set 0% margin outside X values for autoscaling
fig.subplots_adjust(bottom=0.2)
fig.subplots_adjust(left=0.2)
fig.subplots_adjust(right=0.95)
fig.subplots_adjust(top=0.95)
axModP, = axMod.plot(x, modulus, linewidth=2.0)
axPhP, = axPh.plot(x, phase, linewidth=2.0)

#set x axis low limit
def setLowXLim(lowLim):
    (currLow,currHigh) = axMod.get_xlim()
    #min cannot be higher than max an viceversa
    if(float(lowLim)<currHigh):
        axMod.set_xlim(float(lowLim),currHigh)
        axPh.set_xlim(float(lowLim),currHigh)
    else:
        llx_text_box.set_val(currLow)
    plt.draw()

#set x axis high limit
def setHighXLim(highLim):
    (currLow,currHigh) = axMod.get_xlim()
    if(float(highLim)>currLow):
        axMod.set_xlim(currLow,float(highLim))
        axPh.set_xlim(currLow,float(highLim))
    else:
        hlx_text_box.set_val(currHigh)
    plt.draw()

#-------------Module---------------------------------

#set y Module axis low limit
def setLowYLimMod(lowLim):
    (currLow,currHigh) = axMod.get_ylim()
    if(float(lowLim)<currHigh):
        axMod.set_ylim(float(lowLim),currHigh)
    else:
        llyMod_text_box.set_val(currLow)
    plt.draw()

#set y Module axis high limit
def setHighYLimMod(highLim):
    (currLow,currHigh) = axMod.get_ylim()
    if(float(highLim)>currLow):
        axMod.set_ylim(currLow,float(highLim))
    else:
        hlyMod_text_box.set_val(currHigh)
    plt.draw()

#-----------------------------phase

#set y Phase axis low limit
def setLowYLimPh(lowLim):
    if(lowLim<=defaultYaxisMinPh):
        (currLow,currHigh) = axPh.get_ylim()
        if(float(lowLim)<currHigh):
            axPh.set_ylim(float(lowLim),currHigh)
        else:
            llyPh_text_box.set_val(currLow)
        plt.draw()
    else:
        llyPh_text_box.set_val(defaultYaxisMinPh)
        plt.draw()

#set y Phase axis high limit
def setHighYLimPh(highLim):
    if(highLim<=defaultYaxisMaxPh):
        (currLow,currHigh) = axPh.get_ylim()
        if(float(highLim)>currLow):
            axPh.set_ylim(currLow,float(highLim))
        else:
            hlyPh_text_box.set_val(currHigh)
        plt.draw()
    else:
        hlyPh_text_box.set_val(defaultYaxisMaxPh)
        plt.draw()
#--------------------------------------

#autoscale axes
def autoScale(dummy):
    #autoscale x axis
    xAxMin=min(x)
    xAxMax=max(x)

    (xAxMin,xAxMax)=roundRange(xAxMin,xAxMax,"x")

    llx_text_box.set_val(xAxMin)
    hlx_text_box.set_val(xAxMax)

    #autoscale y axis

    modMin=min(modulus)
    modMax=max(modulus)
    phaseMin=min(phase)
    phaseMax=max(phase)

    (modMin,modMax)=roundRange(modMin,modMax,"modulus")
    (phaseMin,phaseMax)=roundRange(phaseMin,phaseMax,"phase")

    llyMod_text_box.set_val(modMin)
    hlyMod_text_box.set_val(modMax)
    llyPh_text_box.set_val(phaseMin)
    hlyPh_text_box.set_val(phaseMax)
    plt.draw()

#validate input
isEmptyXL=0
def validateInputXL(text):
    global isEmptyXL
    if(is_number(text) and isEmptyXL!=1):
        isEmptyXL=0
        llx_text_box.text_disp.set_color('black')
        if(len(text)>maxStrLenghtX):
            text=text[:-1]  #cut last number, the one exceeding
            llx_text_box.set_val(text)
    else:
        if(len(text)!=0):
            llx_text_box.set_val("NaN") #set a non number so it returns to this point unless you write a number
            llx_text_box.text_disp.set_color('red')
            isEmptyXL=0
        else:
            llx_text_box.set_val(str(XMin))
            isEmptyXL=1

isEmptyModYL=0
def validateInputModYL(text):
    global isEmptyModYL
    if(is_number(text) and isEmptyModYL!=1):
        isEmptyModYL=0
        llyMod_text_box.text_disp.set_color('black')
        if(len(text)>maxStrLenghtYMod+1):
            text=text[:-1]  #cut last number, the one exceeding
            llyMod_text_box.set_val(text)
    else:
        if(len(text)!=0):
            llyMod_text_box.set_val("NaN") #set a non number so it returns to this point unless you write a number
            llyMod_text_box.text_disp.set_color('red')
            isEmptyModYL=0
        else:
            llyMod_text_box.set_val(str(YMinMod))
            isEmptyModYL=1

isEmptyXH=0
def validateInputXH(text):
    global isEmptyXH
    if(is_number(text) and isEmptyXH!=1):
        isEmptyXH=0
        hlx_text_box.text_disp.set_color('black')
        if(len(text)>maxStrLenghtX):
            text=text[:-1]  #cut last number, the one exceeding
            hlx_text_box.set_val(text)
    else:
        if(len(text)!=0):
            hlx_text_box.set_val("NaN") #set a non number so it returns to this point unless you write a number
            hlx_text_box.text_disp.set_color('red')
            isEmptyXH=0
        else:
            hlx_text_box.set_val(str(XMax))
            isEmptyXH=1

isEmptyModYH=0
def validateInputModYH(text):
    global isEmptyModYH
    if(is_number(text) and isEmptyModYH!=1):
        isEmptyModYH=0
        hlyMod_text_box.text_disp.set_color('black')
        if(len(text)>maxStrLenghtYMod):
            text=text[:-1]  #cut last number, the one exceeding
            hlyMod_text_box.set_val(text)
    else:
        if(len(text)!=0):
            hlyMod_text_box.set_val("NaN") #set a non number so it returns to this point unless you write a number
            hlyMod_text_box.text_disp.set_color('red')
            isEmptyModYH=0
        else:
            hlyMod_text_box.set_val(str(YMaxMod))
            isEmptyModYH=1

isEmptyPhYH=0
def validateInputPhYH(text):
    global isEmptyPhYH
    if(is_number(text) and isEmptyPhYH!=1):
        isEmptyPhYH=0
        hlyPh_text_box.text_disp.set_color('black')
        if(len(text)>maxStrLenghtYMod):
            text=text[:-1]  #cut last number, the one exceeding
            hlyPh_text_box.set_val(text)
    else:
        if(len(text)!=0):
            hlyPh_text_box.set_val("NaN") #set a non number so it returns to this point unless you write a number
            hlyPh_text_box.text_disp.set_color('red')
            isEmptyPhYH=0
        else:
            hlyPh_text_box.set_val(str(YMaxPh))
            isEmptyPhYH=1

isEmptyPhYL=0
def validateInputPhYL(text):
    global isEmptyPhYL
    if(is_number(text) and isEmptyPhYL!=1):
        isEmptyPhYL=0
        llyPh_text_box.text_disp.set_color('black')
        if(len(text)>maxStrLenghtYMod+1):
            text=text[:-1]  #cut last number, the one exceeding
            llyPh_text_box.set_val(text)
    else:
        if(len(text)!=0):
            llyPh_text_box.set_val("NaN") #set a non number so it returns to this point unless you write a number
            llyPh_text_box.text_disp.set_color('red')
            isEmptyPhYL=0
        else:
            llyPh_text_box.set_val(str(YMinPh))
            isEmptyPhYL=1

#low x limit TextBox
axbox = fig.add_axes([0.25, 0.05, 0.15, 0.05])
llx_text_box = TextBox(axbox, "Min ", textalignment="center")
llx_text_box.on_submit(setLowXLim)
llx_text_box.set_val(defaultXaxisMin)  # Trigger `submit` with the initial string.

#high x limit TextBox
axbox = fig.add_axes([0.75, 0.05, 0.15, 0.05])
hlx_text_box = TextBox(axbox, "Max ", textalignment="center")
hlx_text_box.on_submit(setHighXLim)
hlx_text_box.set_val(defaultXaxisMax)  # Trigger `submit` with the initial string.

#autoscale limit Button
axbox = fig.add_axes([0.525, 0.05, 0.1, 0.05])
as_button = Button(axbox, "AutoScale")
as_button.on_clicked(autoScale)

#low y Module limit TextBox
axbox = fig.add_axes([0.05, 0.6, 0.1, 0.05])
llyMod_text_box = TextBox(axbox, "Min ", textalignment="center")
llyMod_text_box.on_submit(setLowYLimMod)
llyMod_text_box.set_val(defaultYaxisMinMod)  # Trigger `submit` with the initial string.

#high y Module limit TextBox
axbox = fig.add_axes([0.05, 0.90, 0.1, 0.05])
hlyMod_text_box = TextBox(axbox, "Max ", textalignment="center")
hlyMod_text_box.on_submit(setHighYLimMod)
hlyMod_text_box.set_val(defaultYaxisMaxMod)  # Trigger `submit` with the initial string.

#--------------------phase------

#low y Phase limit TextBox
axbox = fig.add_axes([0.05, 0.2, 0.1, 0.05])
llyPh_text_box = TextBox(axbox, "Min ", textalignment="center")
llyPh_text_box.on_submit(setLowYLimPh)
llyPh_text_box.set_val(defaultYaxisMinPh)  # Trigger `submit` with the initial string.

#high y Phase limit TextBox
axbox = fig.add_axes([0.05, 0.5, 0.1, 0.05])
hlyPh_text_box = TextBox(axbox, "Max ", textalignment="center")
hlyPh_text_box.on_submit(setHighYLimPh)
hlyPh_text_box.set_val(defaultYaxisMaxPh)  # Trigger `submit` with the initial string.

#---------------------------------

llx_text_box.on_text_change(validateInputXL)
hlx_text_box.on_text_change(validateInputXH)
llyMod_text_box.on_text_change(validateInputModYL)
hlyMod_text_box.on_text_change(validateInputModYH)
llyPh_text_box.on_text_change(validateInputPhYL)
hlyPh_text_box.on_text_change(validateInputPhYH)

#plt.show()