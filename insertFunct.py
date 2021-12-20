from tkinter import *
from tkinter.font import Font 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from graph import fig as Hplot
from tkinter.ttk import Separator
from tkinter.ttk import Style
import PIL as PIL
from os import path
from platform import system

if __name__ == "__main__":
    print("This script is a module and can't run on it's own, start main.py instead!")

def rcpath(rel_path):
    iconPath=path.dirname(path.realpath(__file__))+"\\" + rel_path
    if system == "Windows":                #if OS=Windows replace slashes
        iconPath=iconPath.replace("\\","/")
    return iconPath

# plot function is created for 
# plotting the graph in 
# tkinter window
global_fig = None

functStringNum ='''1'''
functStringDen ='''1+1j*f'''
functStringGStatic ='''1'''
num =""
den =""
gStatic=""
oldNum=functStringNum
oldDen=functStringDen
oldGStatic=functStringGStatic
app=False
lastExpr=""


def _quitMain():
    window.quit()
    if funcWindow is not None:
        funcWindow.destroy()
    window.destroy()

def _quitFunc():
    global app
    global oldNum
    global oldDen
    global oldGStatic
    global text_boxNum
    global text_boxDen
    global text_boxGStatic
    if (app!=True):
        #rewrite previous text in TextBoxes
        text_boxNum.delete(1.0, END)
        text_boxNum.insert(END,oldNum)
        text_boxDen.delete(1.0, END)
        text_boxDen.insert(END,oldDen)
        text_boxGStatic.delete(1.0, END)
        text_boxGStatic.insert(END,oldGStatic)
    funcWindow.withdraw()

def _applyFunc():
    global app
    app=True
    _quitFunc()

def extract_data():
    global num
    global gStatic
    global den
    global app
    global oldNum
    global oldDen
    global oldGStatic
    if app: 
        app=False
        gStatic=str(text_boxGStatic.get('1.0', 'end'))
        gStatic=gStatic.split('\n', 1)[0]
        num=str(text_boxNum.get('1.0', 'end'))
        num=num.split('\n', 1)[0]
        den=str(text_boxDen.get('1.0', 'end'))
        den=den.split('\n', 1)[0]
        #save previous values for eventual restoring
        oldGStatic=gStatic
        oldNum=num
        oldDen=den

def keybind (event):
        v = event.char
        try:
            v = int(v)
        except ValueError:      #allow ascii char for ctrl+c, ctrl+v, ctrl+x, operands and variables
            if v!="\x08" and v!="\x03" and v!="\x16" and v!="\x18" and v!="" and v!="/" and v!="*" and v!="j" and v!="w" and v!="f" and v!="(" and v!=")" and v!="+" and v!="-" and v!="s" and v!=".":
                return "break"

funcWindow=None
def openFuncWindow():

    global funcWindow
    if(funcWindow==None):
        funcWindow = Toplevel()

        funcWindow.title("Insert function")

        funcWindow.geometry("500x400")
        funcWindow.iconbitmap(rcpath('/images/icon.ico'))
    
        # two Frames, bottom for buttons and top for TextBoxes
        topFrame = Frame(funcWindow)
        topFrame.pack(side="top",padx=10, pady=0)
        bottomFrame = Frame(funcWindow)
        bottomFrame.pack(side="bottom",padx=0, anchor=N,pady=20)

        label=Label(topFrame, height=1, text="Insert new function to plot:")
        label.pack(side="top",pady=25)
        font = Font(size=16, weight="bold")
        label.configure(font=font)
        
        cancelFuncButt = Button( master=bottomFrame,
                        command = _quitFunc,
                        height = 1, 
                        width = 15,
                        text = "Cancel")
        cancelFuncButt.pack(side="bottom",pady=20)
        
        applyFuncButt = Button( master=bottomFrame,
                        command = _applyFunc,
                        height = 1, 
                        width = 15,
                        text = "Apply")
        applyFuncButt.pack(side="bottom")
        
        #------create texbox and validate text insered in it-----------------------
        global text_boxNum
        global text_boxDen
        global text_boxGStatic
        global text_stringDebug
        
        text_boxGStatic = Text( master=topFrame,
                        height=1,
                        width=10,
                        wrap='word'
                        )
        text_boxGStatic.insert('end', functStringGStatic)
        text_boxGStatic.pack(side="left",pady=30, padx=10)
        text_boxGStatic.bind('<KeyPress>', keybind)
        
        img = PIL.Image.open(rcpath("/images/cross.png"))
        imgTk = PIL.ImageTk.PhotoImage(img.resize((30,30)),master=topFrame)
        panel = Label(topFrame, image = imgTk)
        panel.image = imgTk       #needed to keep a reference for garbage collector
        panel.pack(side = "left",fill = "both", expand = "yes")

        text_boxNum = Text( master=topFrame,
                        height=1,
                        width=25,
                        wrap='word'
                        )
        text_boxNum.insert('end', functStringNum)
        text_boxNum.pack(side="top",pady=10,padx=10)
        text_boxNum.bind('<KeyPress>', keybind)

        line_style = Style()
        line_style.configure("Line.TSeparator", background="#000000")
        separator=Separator(topFrame,style="Line.TSeparator").pack(side="top",ipadx=130)

        text_boxDen = Text( master=topFrame,
                        height=1,
                        width=25,
                        wrap='word'
                        )
        text_boxDen.insert('end', functStringDen)
        text_boxDen.pack(side="bottom",pady=10)
        text_boxDen.bind('<KeyPress>', keybind)

        text_stringDebug = Text( master=bottomFrame,
                        height=1,
                        width=30,
                        wrap='word'
                        )
        text_stringDebug.insert('end',"Valid expression")
        text_stringDebug.pack(side="top",pady=20)
        text_stringDebug.configure(state="disabled")

        funcWindow.protocol("WM_DELETE_WINDOW", _quitFunc)
    else:
        funcWindow.deiconify()
    #------------------------------------------------------------


def changeFunc():
    openFuncWindow()

def plot():
    # the figure that will contain the plot
    global_fig = Hplot
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvasd = FigureCanvasTkAgg(global_fig,
                               master = window) 
    canvasd.draw()

    # placing the canvas on the Tkinter window
    canvasd.get_tk_widget().pack(fill= "both", expand = "True")
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvasd,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvasd.get_tk_widget().pack() 
  
# the main Tkinter window
window = Tk()

window.protocol("WM_DELETE_WINDOW", _quitMain)

# setting the title 
window.title('Bode Plotter')
  
# dimensions of the main window
window.geometry("1000x800")

topToolbar= Frame(window)
topToolbar.pack(side="top",anchor=NW)

changeFunc_button = Button(topToolbar, 
                     command = changeFunc,
                     height = 1, 
                     width = 15,
                     text = "Change H(jw)")

exit_button = Button(topToolbar, 
                     command = _quitMain,
                     height = 1, 
                     width = 15,
                     text = "Exit")
  
# place the button 
# in main window
changeFunc_button.pack(side="left",anchor=N)
exit_button.pack(side="left",anchor=NE)





