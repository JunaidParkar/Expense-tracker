import tkinter as tk

class CustomFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        # create a frame for the input fields
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(side="top", fill="x")

        # create a checkbox
        self.checkbox = tk.Checkbutton(self.input_frame, text="Checkbox")
        self.checkbox.grid(row=0, column=0, padx=10, pady=10)

        # create a date entry
        self.date = tk.Entry(self.input_frame)
        self.date.grid(row=0, column=1, padx=10, pady=10)

        # create an amount entry
        self.amount = tk.Entry(self.input_frame)
        self.amount.grid(row=0, column=2, padx=10, pady=10)

        # create a category entry
        self.category = tk.Entry(self.input_frame)
        self.category.grid(row=0, column=3, padx=10, pady=10)

        # create a description text widget
        self.description = tk.Text(self.input_frame, height=5, width=50, wrap='word')
        self.description.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

root = tk.Tk()
frame = CustomFrame(root)
frame.pack(side="top", fill="both", expand=True)
root.mainloop()