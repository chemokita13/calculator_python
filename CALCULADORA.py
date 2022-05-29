from tkinter import *
from pynput import *
colorBotones = "#E52626"
colorAns = "#FF5733"
colorSignos = "#ECFF04"
colorIgual = "#35B216"
colorResultado = "#FFFFFF"
colorMarco = "#97BBDE"
result = None
nA = None
nB = None
nC = None
nD = None
signo = None
signo2= None
nfA = None
nfB = None
cam = False
ans = None
def resetV(): # reestablece las variables
    global nA,nB,nC,nD,nfA,nfB, signo, signo2, cam
    nA = None
    nB = None
    nC = None
    nD = None
    signo = None
    signo2= None
    nfA = None
    nfB = None
    cam = False
def f (): # crea nfB y opera
    global signo, signo2, nC,nD, nfA, nfB, result, win, l, ans, nA, nC
    if nfA == None:
        if nA == None:
            nfA=0
        else:
            if nB == None:
                nfA = nA
            else:
                nfA = nA*10 + nB 
    if nD != None:
        nfB = nC*10 + nD
    else:
        if nC==None:
            nC = 0
            nfB = 0
        else:
            nfB = nC
    if signo2=="+" or signo2==None:
        result= nfA + nfB
    if signo2 == "-":
        result = nfA - nfB
    if signo2 == "*":
        result = nfA*nfB
    ans = result
    l.config(text=result)
   
    resetV()
    win.update()
def o (signo): #crea nfA y guarda el signo
    global nA, nB, nfA, nfB, cam, signo2
    if cam == False:
        if nB != None:
            nfA = nA*10 + nB
        else: 
            nfA = nA
        if signo == "+":
            signo2 = "+"
        if signo == "-":
            signo2 = "-"
        if signo == "*":
            signo2 = "*"
        cam = True
    else: 
        if nD != None:
            nfB = nC*10 + nD
        else: 
            nfA = nC
    #print(f"nfA: {nfA}, nfB: {nfB}, cam: {cam}")
    win.update()
def num (n): #recoje n y nX
    global nA, nB, nC, nD, cam
    if cam == False:
        if nA == None:
            nA = n
        else:
            nB = n
        cam == True
    else:
        if nC == None:
            nC = n
        else:
            nD = n

win = Tk()
win.title("Calculator")
win.resizable(1,1)
win.geometry("200x350")
fr = LabelFrame(win, text="CALCULADORA")
fr.pack(expand=True, fill='both')
fr.config(bg=colorMarco, font=("kidsco", 15))
l = Label(fr, text=result, borderwidth=1, relief="solid")
l.grid(column=0, columnspan=3, row=0, sticky='nsew', ipadx=90, ipady=20)
l.config(bg=colorResultado, font=("kidsco", 15))
b1=Button(fr, text="1", command= lambda: num(1))
b2=Button(fr, text="2", command= lambda: num(2))
b3=Button(fr, text="3", command= lambda: num(3))
b4=Button(fr, text="4", command= lambda: num(4))
b5=Button(fr, text="5", command= lambda: num(5))
b6=Button(fr, text="6", command= lambda: num(6))
b7=Button(fr, text="7", command= lambda: num(7))
b8=Button(fr, text="8", command= lambda: num(8))
b9=Button(fr, text="9", command= lambda: num(9))
b0=Button(fr, text="0", command= lambda: num(0))
bAns=Button(fr, text="Ans", command= lambda: num(ans))
br=Button(fr, text="-", command= lambda: o("-"))
bm=Button(fr, text="x", command= lambda: o("*"))
bs=Button(fr, text="+", command= lambda: o("+"))
bi=Button(fr, text="=", command= lambda: f())
b1.grid(row=1, column=0, ipadx=5, pady=3, ipady=5, sticky='ew')
b2.grid(row=1, column=1, ipadx=5, pady=3, ipady=5, sticky='ew')
b3.grid(row=1, column=2, ipadx=5, pady=3, ipady=5, sticky='ew')
b4.grid(row=2, column=0, ipadx=5, pady=3, ipady=5, sticky='ew')
b5.grid(row=2, column=1, ipadx=5, pady=3, ipady=5, sticky='ew')
b6.grid(row=2, column=2, ipadx=5, pady=3, ipady=5, sticky='ew')
b7.grid(row=3, column=0, ipadx=5, pady=3, ipady=5, sticky='ew')
b8.grid(row=3, column=1, ipadx=5, pady=3, ipady=5, sticky='ew')
b9.grid(row=3, column=2, ipadx=5, pady=3, ipady=5, sticky='ew')
b0.grid(row=4,column=0, ipadx=5, pady=3, ipady=5, sticky='ew')
b1.config(bg=colorBotones)
b2.config(bg=colorBotones)
b3.config(bg=colorBotones)
b4.config(bg=colorBotones)
b5.config(bg=colorBotones)
b6.config(bg=colorBotones)
b7.config(bg=colorBotones)
b8.config(bg=colorBotones)
b9.config(bg=colorBotones)
b0.config(bg=colorBotones)
bAns.grid(row=4,column=1,columnspan=2, ipadx=5, pady=5, ipady=5, sticky='ew')
bAns.config(bg=colorAns)
bs.grid(row=5, column=0, ipadx=5, pady=5, ipady=5, sticky='ew')
br.grid(row=5, column=1, ipadx=5, pady=5, ipady=5, sticky='ew')
bm.grid(row=5, column=2, ipadx=5, pady=5, ipady=5, sticky='ew')
bs.config(bg=colorSignos)
br.config(bg=colorSignos)
bm.config(bg=colorSignos)
bi.grid(row=6, column=0, columnspan=3, sticky='nsew', ipadx=5, pady=5, ipady=5)
bi.config(bg=colorIgual) 
win.mainloop()
