from tkinter import *
from component import component

components = {}
lbl_components = {}

# functions:

def onSubmit(*args):

	number = inp_number.get()
	description = inp_descr.get()

	if number not in components:

		inp_number.delete(0, 'end')
		inp_descr.delete(0, 'end')

		inp_number.focus()

		components[number] = component(number, description)

		i = 3

		for key in components:
			print(components[key].number + " - " + components[key].description)
			if key in lbl_components:
				lbl_components[key].grid_forget()
			else:
				lbl_components[key] = Label(frame_add, text = components[key].number + " - " + components[key].description)
			lbl_components[key].grid(row=i, column=0, columnspan=2)
			i += 1
	else:
		print("Error: Part Number Already Exists!")



def createFrameAdd(*args):

	# create frames:
	frame_add = Tk()
	frame_add.title("Add Frame")
	frame_add.bind('<Return>',onSubmit)

	# create widgets:

	# Number input field
	lbl_number = Label(frame_add, text="Number:")
	lbl_number.grid(row=0, column=0)
	inp_number = Entry(frame_add, width=25)
	inp_number.grid(row=0, column=1)
	inp_number.focus()

	# Description input field
	lbl_descr = Label(frame_add, text="Description:")
	lbl_descr.grid(row=1, column=0)
	inp_descr = Entry(frame_add, width=25)
	inp_descr.grid(row=1, column=1)

	myButton = Button(frame_add, width = 10, text="Submit", command=onSubmit)
	myButton.grid(row=2, column=0)

print("test1")


# mount frames:
# frame_add.mainloop()

