from tkinter import *
from tkinter import ttk
from time import *
from threading import *
from math import *



#create window
mainWindow = Tk()
#secondWindow = Tk()

#set the window size and name
mainWindow.geometry("500x500+0+0")
mainWindow.title("Main")

#create a grid
frame = ttk.Frame(mainWindow,padding=10)
frame.grid()

#testing
def temp():
    num = int(testEntry.get())
    Label(frame, text=num).grid(column=1,row=1)

#kill
def kill():
    mainWindow.destroy()

#create labels
ttk.Label(frame, text="hello world").grid(column=1,row=1)


#text entry
testEntry = Entry(frame)
testEntry.grid(column=0,row=1)

#pythagorean calculator
def pythagWindow():
    #function that creates the second window
    secondWindow = Tk()

    #update the kill function so that Quit button kills this window
    def kill():
        mainWindow.destroy()
        secondWindow.destroy()
    #update the quit button on the main window
    ttk.Button(frame, text="Quit", command=kill).grid(column=0,row=0)
    
    #modify the name, size and location
    secondWindow.geometry("300x200+700+300")
    secondWindow.title("Pythagorean Calculator")

    #create grid for new window
    frame2 = ttk.Frame(secondWindow,padding=10)
    frame2.grid()

    #create labels and buttons
    ttk.Label(frame2,text="a").grid(column=1,row=2)
    entryPythagA = Entry(frame2,width="5")
    entryPythagA.grid(column=2,row=2)    #input a
    ttk.Label(frame2,text="b").grid(column=1,row=3)
    entryPythagB = Entry(frame2,width="5")
    entryPythagB.grid(column=2,row=3)    #input b
    ttk.Label(frame2,text="c").grid(column=1,row=4)
    entryPythagC = Entry(frame2,width="5")
    entryPythagC.grid(column=2,row=4)    #input c

    def pythagCalc():    #calc button
        #get the input values
        pythagA = (entryPythagA.get())
        pythagB = (entryPythagB.get())
        pythagC = (entryPythagC.get())
        
        #count how many of the three inputs are numbers by converting the booleans into ints and adding
        inputNum = int((pythagA.replace(".","")).isdigit()) + int((pythagB.replace(".","")).isdigit()) + int((pythagC.replace(".","")).isdigit())

        #make inputs numbers
        if ((pythagA.replace(".","")).isdigit()): numA = float(pythagA)
        if ((pythagB.replace(".","")).isdigit()): numB = float(pythagB)
        if ((pythagC.replace(".","")).isdigit()): numC = float(pythagC)

        #if exactly 2 of the 3 inputs are numbers, run
        if inputNum == 2:
            #if finding C from A and B:
            if ((pythagC.replace(".","")).isdigit()) == False:
                output = sqrt(numA*numA + numB*numB)
            #if finding A from B and C:
            elif ((pythagA.replace(".","")).isdigit()) == False:
                output = sqrt(numC*numC - numB*numB)
            #if finding B from C and A:
            elif ((pythagB.replace(".","")).isdigit()) == False:
                output = sqrt(numC*numC - numA*numA)
            else: #theoretically this should never happen but you never know
                print("error ??")
                output = "error"
            #print the output to the window
            output = round(output,5) #round to 5 digits
            frame2
            Label(frame2, text=output,width="8",justify="left",).grid(column=3,row=5)
            Label(frame2, text="output:").grid(column=2,row=5)
        #if some amount other than 2 numbers is inputted, throw an error
        else:print("error")

    ttk.Button(frame2, text="calc",command=pythagCalc).grid(column=2,row=1)
ttk.Button(frame, text="Pythag", command=pythagWindow).grid(column=2,row=2)



#buttons
ttk.Button(frame, text="Quit", command=kill).grid(column=0,row=0)

#main loop
mainWindow.mainloop()
