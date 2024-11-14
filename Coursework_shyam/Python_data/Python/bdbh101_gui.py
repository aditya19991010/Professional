import tkinter as tk

# Tcl (Tool Command Language) is a very powerful but easy to learn dynamic programming language,
# suitable for a very wide range of uses, including web and desktop applications, networking, administration,
# testing and many more. Open source and business-friendly, Tcl is a mature yet evolving language that is truly
# cross platform, easily deployed and highly extensible.
#
# Tk is a graphical user interface toolkit that takes developing desktop applications to a higher level than
# conventional approaches. Tk is the standard GUI not only for Tcl, but for many other dynamic languages, and can
# produce rich, native applications that run unchanged across Windows, Mac OS X, Linux and more.

def main():

    # ### Adding a Widget
    # window = tk.Tk()
    # greeting = tk.Label(text="Hello, Tkinter")
    #
    # # There are several ways to add widgets to a window. Right now, you can use the Label widget’s .pack() method
    # greeting.pack()
    #
    # # There are numerous valid color names, including:
    # # "red"
    # # "orange"
    # # "yellow"
    # # "green"
    # # "blue"
    # # "purple"
    # # https://www.tcl.tk/man/tcl/TkCmd/colors.html
    # # https://en.wikipedia.org/wiki/Web_colors#Hex_triplet
    # label = tk.Label(text="Hello, Tkinter",fg="white",bg="blue",width=10,height=10)
    # label = tk.Label(text="Hello, Tkinter", background="#34A2FE")
    # label.pack()
    #
    # # Displaying Clickable Buttons With Button Widgets
    # button = tk.Button(text="Click me!", width=25, height=5, bg="blue",fg="yellow" )
    # button.pack()
    # window.mainloop()

    # ### Getting Multiline User Input With Text Widgets
    # window = tk.Tk()
    # text_box = tk.Text()
    # text_box.pack()
    # window.mainloop()


    # ### Assigning Widgets to Frames With Frame Widgets
    # window = tk.Tk()
    #
    # frame_a = tk.Frame()
    # frame_b = tk.Frame()
    #
    # label_a = tk.Label(master=frame_a, text="I'm in Frame A")
    # label_a.pack()
    #
    # label_b = tk.Label(master=frame_b, text="I'm in Frame B")
    # label_b.pack()
    #
    # frame_a.pack()
    # frame_b.pack()
    #
    # window.mainloop()

    # ### Adjusting Frame Appearance With Reliefs
    # border_effects = {
    #     "flat": tk.FLAT,
    #     "sunken": tk.SUNKEN,
    #     "raised": tk.RAISED,
    #     "groove": tk.GROOVE,
    #     "ridge": tk.RIDGE,
    # }
    #
    # window = tk.Tk()
    #
    # for relief_name, relief in border_effects.items():
    #     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    #     frame.pack(side=tk.LEFT)
    #     label = tk.Label(master=frame, text=relief_name)
    #     label.pack()
    #
    # window.mainloop()


    # ### Controlling Layout With Geometry Managers
    # window = tk.Tk()
    #
    # frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
    # frame1.pack()
    #
    # frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
    # frame2.pack()
    #
    # frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
    # frame3.pack()
    #
    # window.mainloop()

    # # tk.X
    # window = tk.Tk()
    #
    # frame1 = tk.Frame(master=window, height=100, bg="red")
    # frame1.pack(fill=tk.X)
    #
    # frame2 = tk.Frame(master=window, height=50, bg="yellow")
    # frame2.pack(fill=tk.X)
    #
    # frame3 = tk.Frame(master=window, height=25, bg="blue")
    # frame3.pack(fill=tk.X)
    #
    # window.mainloop()

    # # tk.LEFT
    # window = tk.Tk()
    #
    # frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    # frame1.pack(fill=tk.Y, side=tk.LEFT)
    #
    # frame2 = tk.Frame(master=window, width=100, bg="yellow")
    # frame2.pack(fill=tk.Y, side=tk.LEFT)
    #
    # frame3 = tk.Frame(master=window, width=50, bg="blue")
    # frame3.pack(fill=tk.Y, side=tk.LEFT)
    #
    # window.mainloop()


    ## tk.BOTH
    # window = tk.Tk()
    #
    # frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    # frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    #
    # frame2 = tk.Frame(master=window, width=100, bg="yellow")
    # frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    #
    # frame3 = tk.Frame(master=window, width=50, bg="blue")
    # frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    #
    # window.mainloop()

    # # The .place() Geometry Manager
    # window = tk.Tk()
    #
    # frame = tk.Frame(master=window, width=150, height=150)
    # frame.pack()
    #
    # label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
    # label1.place(x=0, y=0)
    #
    # label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
    # label2.place(x=75, y=75)
    #
    # window.mainloop()

    # # The .grid() Geometry Manager
    # window = tk.Tk()
    #
    # for i in range(3):
    #     for j in range(3):
    #         frame = tk.Frame(
    #             master=window,
    #             relief=tk.RAISED,
    #             borderwidth=1
    #         )
    #         frame.grid(row=i, column=j)
    #         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
    #         label.pack()
    #
    # window.mainloop()

    # ## grid - padding
    # import tkinter as tk
    #
    # window = tk.Tk()
    #
    # for i in range(3):
    #     for j in range(3):
    #         frame = tk.Frame(
    #             master=window,
    #             relief=tk.RAISED,
    #             borderwidth=1
    #         )
    #         frame.grid(row=i, column=j, padx=5, pady=5)
    #         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
    #         label.pack()
    #
    # window.mainloop()

    # ## label - padding
    # import tkinter as tk
    #
    # window = tk.Tk()
    #
    # for i in range(3):
    #     for j in range(3):
    #         frame = tk.Frame(
    #             master=window,
    #             relief=tk.RAISED,
    #             borderwidth=1
    #         )
    #         frame.grid(row=i, column=j, padx=5, pady=5)
    #         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
    #         label.pack(padx=5, pady=5)
    #
    # window.mainloop()


    # ## make grid responsive - i.e. with resizing window, grid should also get resized
    # window = tk.Tk()
    #
    # for i in range(3):
    #     window.columnconfigure(i, weight=1, minsize=75)
    #     window.rowconfigure(i, weight=1, minsize=50)
    #
    #     for j in range(0, 3):
    #         frame = tk.Frame(
    #             master=window,
    #             relief=tk.RAISED,
    #             borderwidth=1
    #         )
    #         frame.grid(row=i, column=j, padx=5, pady=5)
    #         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
    #         label.pack(padx=5, pady=5)
    #
    # window.mainloop()





    ### Making Your Applications Interactive
    # window = tk.Tk()
    #
    # def handle_keypress(event):
    #     """Print the character associated to the key pressed"""
    #     print(event.char)
    #
    # # Bind keypress event to handle_keypress()
    # window.bind("<Key>", handle_keypress)
    #
    # window.mainloop()

    # window = tk.Tk()
    # def handle_click(event):
    #     print("The button was clicked!")
    #
    # button = tk.Button(text="Click me!")
    # button.pack()
    #
    # button.bind("<Button-1>", handle_click)
    # window.mainloop()



    # ### inc and dec
    # window = tk.Tk()
    #
    # def increase():
    #     value = int(lbl_value["text"])
    #     lbl_value["text"] = f"{value + 1}"
    #
    # def decrease():
    #     value = int(lbl_value["text"])
    #     lbl_value["text"] = f"{value - 1}"
    #
    # btn_decrease = tk.Button(master=window, text="-", command=decrease)
    # btn_decrease.grid(row=0, column=0, sticky="nsew")
    #
    # lbl_value = tk.Label(master=window, text="0")
    # lbl_value.grid(row=0, column=1)
    #
    # btn_increase = tk.Button(master=window, text="+", command=increase)
    # btn_increase.grid(row=0, column=2, sticky="nsew")
    #
    # window.mainloop()



    # ### Getting User Input With Entry Widgets
    # root = tk.Tk()
    #
    # # setting the windows size
    # root.geometry("600x400")
    #
    # # declaring string variable
    # # for storing name and password
    # name_var = tk.StringVar()
    # passw_var = tk.StringVar()
    #
    # # defining a function that will
    # # get the name and password and
    # # print them on the screen
    # def submit():
    #     name = name_var.get()
    #     password = passw_var.get()
    #
    #     print("The name is : " + name)
    #     print("The password is : " + password)
    #
    #     name_var.set("")
    #     passw_var.set("")
    #
    # # creating a label for
    # # name using widget Label
    # name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
    #
    # # creating a entry for input
    # # name using widget Entry
    # name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
    #
    # # creating a label for password
    # passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
    #
    # # creating a entry for password
    # passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
    #
    # # creating a button using the widget
    # # Button that will call the submit function
    # sub_btn = tk.Button(root, text='Submit', command=submit)
    #
    # # placing the label and entry in
    # # the required position using grid
    # # method
    # name_label.grid(row=0, column=0)
    # name_entry.grid(row=0, column=1)
    # passw_label.grid(row=1, column=0)
    # passw_entry.grid(row=1, column=1)
    # sub_btn.grid(row=2, column=1)
    #
    # # performing an infinite loop
    # # for the window to display
    # # window.mainloop() tells Python to run the Tkinter event loop. This method listens for events,
    # # such as button clicks or keypresses, and blocks any code that comes after it from running until you close
    # # the window where you called the method.
    # root.mainloop()












    print('End')

# Construct to not include whole program in other includes
if __name__ == "__main__":
   main()