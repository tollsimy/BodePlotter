from tkinter import * 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from graph import fig as Hplot

if __name__ == "__main__":
    print("This script is a module and can't run on it's own, start main.py instead!")

# plot function is created for 
# plotting the graph in 
# tkinter window
global_fig = None

functStringNum ='''1'''
functStringDen ='''1+1j*f'''
functStringGStatic ='''10'''
num =""
den =""
gStatic=""
app=False
lastExpr=""

def _quitMain():
    window.quit()
    window.destroy()

def _quitFunc():
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
    if app: 
        app=False
        gStatic=str(text_boxGStatic.get('1.0', 'end'))
        gStatic=gStatic.split('\n', 1)[0]
        num=str(text_boxNum.get('1.0', 'end'))
        num=num.split('\n', 1)[0]
        den=str(text_boxDen.get('1.0', 'end'))
        den=den.split('\n', 1)[0]

def keybind (event):
        v = event.char
        try:
            v = int(v)
        except ValueError:
            if v!="\x08" and v!="" and v!="/" and v!="*" and v!="j" and v!="w" and v!="f" and v!="^" and v!="(" and v!=")" and v!="+" and v!="-" and v!="s" and v!=".":
                return "break"

def openFuncWindow():

    # Toplevel object which will
    # be treated as a new window
    global funcWindow

    funcWindow = Toplevel()
    gStaticFrame = Frame(funcWindow)
    gStaticFrame.pack(side="left",padx=10,anchor=NW, pady=0)
    functFrame = Frame(funcWindow)
    functFrame.pack(side="right",padx=40, anchor=N,pady=70)

    # sets the title of the
    # Toplevel widget
    funcWindow.title("Insert function")
 
    # sets the geometry of toplevel
    funcWindow.geometry("500x400")
 
    # A Label widget to show in toplevel
    Label(gStaticFrame, text ="Insert new function to plot:").pack(side="top",pady=30,padx=0)
    
    cancelFuncButt = Button( master=functFrame,
                     command = _quitFunc,
                     height = 1, 
                     width = 15,
                     text = "Cancel")
    cancelFuncButt.pack(side="bottom",pady=25, padx=0)
    
    applyFuncButt = Button( master=functFrame,
                     command = _applyFunc,
                     height = 1, 
                     width = 15,
                     text = "Apply")
    applyFuncButt.pack(side="bottom",pady=30, padx=0)
    
    #------create texbox and validate text insered in it-----------------------
    global text_boxNum
    global text_boxDen
    global text_boxGStatic
    
    text_boxGStatic = Text( master=gStaticFrame,
                     height=1,
                     width=10,
                     wrap='word'
                    )
    text_boxGStatic.insert('end', functStringGStatic)
    text_boxGStatic.pack(side="left",pady=0)
    text_boxGStatic.bind('<KeyPress>', keybind)
    
    text_boxNum = Text( master=functFrame,
                     height=1,
                     width=25,
                     wrap='word'
                    )
    text_boxNum.insert('end', functStringNum)
    text_boxNum.pack(side="top")
    text_boxNum.bind('<KeyPress>', keybind)

    text_boxDen = Text( master=functFrame,
                     height=1,
                     width=25,
                     wrap='word'
                    )
    text_boxDen.insert('end', functStringDen)
    text_boxDen.pack(side="bottom",pady=10)
    text_boxDen.bind('<KeyPress>', keybind)

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





