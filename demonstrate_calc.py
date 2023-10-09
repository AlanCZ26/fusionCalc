from tkinter import * #tkinter makes the windows work
from tkinter import ttk #ttk makes the buttons work
from math import * #math allows for more complex calculations

#create window
mainWindow = Tk()
#set the window size and name
mainWindow.geometry("250x200+0+0")
mainWindow.title("Main")

#create a grid for the buttons & labels to sit in
frame = ttk.Frame(mainWindow,padding=10)
frame.grid()

#define the kill button
def kill():
    mainWindow.destroy()

#prevent multiple auxillary windows from opening simultaneously
def killOtherWindows():
    print("first window opened") #so it doesn't throw an error on the first run

#pythagorean calculator
def pythagWindow():
    #kill other windows
    global killOtherWindows #so the function can be updated from other places
    killOtherWindows()
    #update killOtherWindows
    def killOtherWindows():
        secondWindow.destroy()

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

    #create labels and inputs
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
        #by replacing any points (".") with an empty string (""), we can make .isdigit read decimals
        #count how many of the three inputs are numbers by converting the booleans into ints and adding
        inputNum = int((pythagA.replace(".","")).isdigit()) + int((pythagB.replace(".","")).isdigit()) + int((pythagC.replace(".","")).isdigit())
        #make inputs numbers
        if ((pythagA.replace(".","")).isdigit()): numA = float(pythagA)
        if ((pythagB.replace(".","")).isdigit()): numB = float(pythagB)
        if ((pythagC.replace(".","")).isdigit()): numC = float(pythagC)
        #if exactly 2 of the 3 inputs are numbers, run
        if inputNum == 2:
            #if finding C from A and B:
            if ((pythagC.replace(".","")).isdigit()) == False: output = sqrt(numA*numA + numB*numB)
            #if finding A from B and C:
            elif ((pythagA.replace(".","")).isdigit()) == False: output = sqrt(numC*numC - numB*numB)
            #if finding B from C and A:
            elif ((pythagB.replace(".","")).isdigit()) == False: output = sqrt(numC*numC - numA*numA)
            else: #theoretically this should never happen but you never know
                print("error ??")
                output = "error"
            #print the output to the window
            output = round(output,5) #round to 5 digits
            Label(frame2, text=output,width="8",justify="left",).grid(column=3,row=5)
            Label(frame2, text="output:").grid(column=2,row=5)
        #if some amount other than 2 numbers is inputted, throw an error
        else:print("error")
    ttk.Button(frame2, text="calc",command=pythagCalc).grid(column=2,row=1)
ttk.Button(frame, text="Pythagorean Calc", command=pythagWindow).grid(column=2,row=1)

#radians/degrees converter
def angleConvWindow():
    #kill any other windows
    global killOtherWindows #so the function can be updated from other places
    killOtherWindows()
    #update killOtherWindows
    def killOtherWindows():
        thirdWindow.destroy()
    
    #function to create 3rd window
    thirdWindow = Tk()

    #update the kill function so that Quit button kills this window
    def kill():
        mainWindow.destroy()
        thirdWindow.destroy()
    #update the quit button on the main window
    ttk.Button(frame, text="Quit", command=kill).grid(column=0,row=0)

    #modify the name, size and location
    thirdWindow.geometry("300x200+700+300")
    thirdWindow.title("Deg-Rad Converter")
    #create grid for new window
    frame3 = ttk.Frame(thirdWindow,padding=10)
    frame3.grid()

    #create labels and inputs
    ttk.Label(frame3,text="input").grid(column=1,row=1)
    entryAngleConverter = Entry(frame3,width="8")
    entryAngleConverter.grid(column=2,row=1)

    def convRadToDeg():
        inputNum = (entryAngleConverter.get()) #get the input value
        if ((inputNum.replace(".","")).isdigit()): #this detects the negative symbol "-", to catch any cases where the input is negative
            num = float(inputNum) #converting the string (which is confirmed to be all numbers by the previous step) to a float
            #calculate the output
            output = degrees(num) * pi #assume it's by pi because who uses radians and doesn't have it in pi
            output = round(output,10) #round digits
            outputMod = output % 360 #mod 360, to provide more info
            #print output to window
            Label(frame3, text=output,width="13",justify="left").grid(column=3,row=3)
            Label(frame3, text="output:").grid(column=2,row=3)
            Label(frame3, text=outputMod,width="13",justify="left").grid(column=3,row=4)
            Label(frame3, text="output mod 360:").grid(column=2,row=4)
        else: print("Please input a positive number!")        
    ttk.Button(frame3,text="To Degrees", command=convRadToDeg).grid(column=1,row=2)

    def convDegtoRad():
        inputNum = (entryAngleConverter.get()) #get the input values
        if ((inputNum.replace(".","")).isdigit()): 
            num = float(inputNum)
            #calculate the output
            output = radians(num) / pi #div by pi to make it readable
            output = round(output,10) #round digits
            outputMod = output % 2 #2pi radians is 1 rotation
            output = (str(output) + "pi") #add pi back to make it claer
            outputMod = (str(outputMod) + "pi") 
            #print output to window
            Label(frame3, text=output,width="13",justify="left").grid(column=3,row=3)
            Label(frame3, text="output:").grid(column=2,row=3)
            Label(frame3, text=outputMod,width="13",justify="left").grid(column=3,row=4)
            Label(frame3, text="output mod 2:").grid(column=2,row=4)
        else: print("Please input a positive number!")        
    ttk.Button(frame3,text="To Radians", command=convDegtoRad).grid(column=1,row=3)
ttk.Button(frame, text="Deg-Rad Converter", command=angleConvWindow).grid(column=2,row=2)

#quit button
ttk.Button(frame, text="Quit", command=kill).grid(column=0,row=0)

#main loop so the windows don't instantly die
mainWindow.mainloop()
