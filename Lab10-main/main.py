from tkinter import *

r = Tk()
r.title("Lab10")
r.geometry("500x500")


def readFile():
    file = open("/Users/ezgi/Desktop/Marvel.txt", "r")
    data = file.read()
    newText.insert(END, data)
    file.close()


def calculateFile():
    file = open("/Users/ezgi/Desktop/Marvel.txt", "r")
    ReadFile = file.read()
    ReadFile = ReadFile.split()
    calcList = []
    for x in ReadFile:
        if x not in calcList:
            calcList.append(x)

    for x in range(0, len(calcList)):
        data = (calcList[x], "=", ReadFile.count(calcList[x]))
        newText.insert(END, data)
        newText.insert(END, "\n")


newText = Text(r, width=60, height=20)
newText.pack()

readButton = Button(master=r, text="READ", width=25, command=readFile)
readButton.pack()
calculateButton = Button(master=r, text='CALCULATE', width=25, command=calculateFile)
calculateButton.pack()

r.mainloop()

