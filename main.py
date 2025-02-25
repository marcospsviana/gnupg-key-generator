from tkinter import ttk

class MainWindow(ttk.Widget):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()


if __name__ == "__main__":
    root = ttk.Tk()
    app = root.mainloop()
    MainWindow(root)
    
