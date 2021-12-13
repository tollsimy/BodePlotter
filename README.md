# BodePlotter
Simple electrician's made Python Bode Plotter.
Don't judge my code, i'm not @notfilippo (FR-ATM).

## How to install BodePlotter
Tested on Python 3.8.10.<br/>
Simply move to the BodePlotter directory and lauch:

```
pip install -r requirements.txt
```

## How to start the plotter
Move to the BodePlotter directory and lauch:

```
python main.py
```
or if you are running Windows start BodePlotter.bat

## How to use the plotter
Click on the "Change H(jw)" button and insert the function that you want to plot.<br/>
<br/>
![screen](https://user-images.githubusercontent.com/94357442/145812793-ec1fff7f-9255-41c0-a8dd-4ee504f85514.png).<br/>
Insert Static Gain (left box), Numerator and Denominator (top right and bottom right boxes). <br/>
<br/>
Rules: <br/>
- Imaginary number must be written in the form *"aj"* **with *"j"* after the number and not multiplicated with asterisk *"&ast;"* and with *"a"* integer**. <br/>
You can always write "1j&ast;(1/2)" if you want float number. <br/>
- Variables are *"s"* (s=jw), *"w"* (w=2pif) and *"f"* and **apart from "s" (s=Jw) they must be multiplicated with asterisk "*"**. <br/>
(e.g. "2s*(f**2)", "1j&ast;2&ast;f")
- Allowed operations are sum "+", subtraction "-", multiplication "&ast;", division "/" and power "&ast;&ast;". Brackets "(", ")" are also allowed. 