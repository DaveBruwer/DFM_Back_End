from tkinter import *

labelText = ""

# functions:

def buttonPress():
	labelText = myinput.get()
	print(labelText)
	global myLabel
	# myLabel.grid()
	myLabel.grid_forget()
	myLabel = Label(frame1, text=labelText)
	# myLabel.grid(row=2, column=0)
	if labelText:
	# 	myLabel.grid_forget()
		myLabel.grid(row=2, column=0)

def clearLabel():
	global myLabel
	myLabel.grid_forget()



# create frames:
frame1 = Tk()
frame1.title("Frame 1")
# frame2 = Tk()
# frame2.title("Frame 2")

# create widgets:
myinput = Entry(frame1, width=25)
myinput.grid(row=0, column=0)

myButton = Button(frame1, width = 10, text="Enter", command=buttonPress)
myButton.grid(row=1, column=0)
# myButton2 = Button(frame1, text="Clear", command=clearLabel)
# myButton2.grid(row=1, column=1)

myLabel = Label(frame1, text=labelText)



# mount frames:
frame1.mainloop()

