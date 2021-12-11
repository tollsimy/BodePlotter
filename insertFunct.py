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

functString ='''1/(1+1j*f)'''
expression =""
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


def enterKey(event):
    _applyFunc()

def extract_data():
    global expression
    global app
    if app: 
        app=False
        expression=str(text_box.get('1.0', 'end'))
        expression=expression.split('\n', 1)[0]

def keybind (event):
        v = event.char
        try:
            v = int(v)
        except ValueError:
            if v!="\x08" and v!="" and v!="/" and v!="*" and v!="j" and v!="w" and v!="f" and v!="^" and v!="(" and v!=")" and v!="+" and v!="-":
                return "break"

def openFuncWindow():

    # Toplevel object which will
    # be treated as a new window
    global funcWindow

    funcWindow = Toplevel()
 
    # sets the title of the
    # Toplevel widget
    funcWindow.title("Insert function")
 
    # sets the geometry of toplevel
    funcWindow.geometry("500x400")
 
    # A Label widget to show in toplevel
    Label(funcWindow, text ="Insert new function to plot:").pack()
    
    cancelFuncButt = Button( master=funcWindow,
                     command = _quitFunc,
                     height = 1, 
                     width = 15,
                     text = "Cancel")
    cancelFuncButt.pack(side="bottom",pady=25, padx=200)
    
    applyFuncButt = Button( master=funcWindow,
                     command = _applyFunc,
                     height = 1, 
                     width = 15,
                     text = "Apply")
    applyFuncButt.pack(side="bottom",pady=0, padx=100)
    
    #------create texbox and validate text insered in it-----------------------
    global text_box
    text_box = Text( master=funcWindow,
                     height=1,
                     width=40,
                     wrap='word'
                    )
    text_box.insert('end', functString)
    text_box.pack(side="top",pady=20, padx=100)
    text_box.bind('<Return>', enterKey)
    text_box.bind('<KeyPress>', keybind)

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





