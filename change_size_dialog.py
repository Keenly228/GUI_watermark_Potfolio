from tkinter import Toplevel, Label, Entry, Button, END
from tkinter import messagebox

class ChangeSizeDialog:
    def __init__(self, initial_width, initial_height):
        self.top = Toplevel()
        self.top.title("Change Size")

        self.width_label = Label(self.top, text="Width:")
        self.width_label.grid(row=0, column=0, padx=5, pady=5)
        self.width_entry = Entry(self.top)
        self.width_entry.insert(END, str(initial_width))
        self.width_entry.grid(row=0, column=1, padx=5, pady=5)

        self.height_label = Label(self.top, text="Height:")
        self.height_label.grid(row=1, column=0, padx=5, pady=5)
        self.height_entry = Entry(self.top)
        self.height_entry.insert(END, str(initial_height))
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)

        self.ok_button = Button(self.top, text="OK", command=self.ok)
        self.ok_button.grid(row=2, column=0, padx=5, pady=5)
        self.cancel_button = Button(self.top, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=2, column=1, padx=5, pady=5)

    def ok(self):
        try:
            self.width = int(self.width_entry.get())
            self.height = int(self.height_entry.get())
            self.top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values for width and height.")

    def cancel(self):
        self.top.destroy()

