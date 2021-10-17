from tkinter import *
from AddFrame import *

addFrameCreated = False


# functions:

def onAddComponent(*args):
	print("Add Component button pressed.")
	global addFrameCreated
	if not addFrameCreated:
		createFrameAdd()
		addFrameCreated = True
	else:
		print("Add Component window already open.")

def onExit():
	print("Exit button pressed.")
	frame_main.quit()



# create frames:
frame_main = Tk()
frame_main.title("Main Frame")
# frame_main.bind('<Return>',onSubmit)

# create widgets:
# Add component button
btnAddComp = Button(frame_main, text="Add Component", command=onAddComponent)
btnAddComp.grid(row=0, column=0)

# Exit button
btnExit = Button(frame_main, text="Exit", command=onExit)
btnExit.grid(row=1, column=1)

# mount frames:
frame_main.mainloop()

