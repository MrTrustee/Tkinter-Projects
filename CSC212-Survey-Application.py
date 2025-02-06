#I just feel like playing around with it
#    Author: Isaiah Ayomide Fakorede
#    A Student at the University of Lagos
#    Computer Science Department




import tkinter as tk
root = tk.Tk()
root.title("CSC212-Survey-Application")
root.geometry("640*480+300+300")
root.resizable(False, False)

#Adding Widgets to the Survey

title = tk.Label(
        root, 
        text = "Please take the Survey",
        font = ("Arial 16 bold"),
        bg = "brown",
        fg = "#FF0"
        )

name_label = tk.Label(root, text = "Please enter your name")
name_inp = tk.Entry(root)
student_attempt = tk.Checkbutton(
        root,
        text = "Check this button if you took CSC212"
        )
course_unit = tk.Label(
        root, 
        text = "How many units is the course?"
        )
course_unit_inp = tk.Spinbox(root, from_ = 0, to = 10, increment =1)

