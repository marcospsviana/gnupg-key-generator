from tkinter import ttk
from tkinter import Tk, PhotoImage

class MainWindow(ttk.Widget):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.create_widgets()
        self.main_frame = ttk.Frame(self.master)
        self.main_frame.pack()
        self.master.title("Main Window")
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.master.configure(bg="white")
        self.create_widgets()
        self.logo = PhotoImage(file="logo.png")
        self.master.iconphoto(False, self.logo)
        self.logo.grid(row=0, column=0)
        self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = root.mainloop()
    MainWindow(root)
    
