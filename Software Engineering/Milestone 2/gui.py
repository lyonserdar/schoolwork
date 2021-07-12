import tkinter as tk

# To create exe file: pyinstaller --onefile main.py


class Application(tk.Frame):
    """
    TODO
    """

    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.master.title("UVSim")  # Window Title
        self.master.geometry("1080x720")  # Window Size

    def create_widgets(self):
        self.code_text = tk.StringVar()
        self.code_label = tk.Label(
            self, text="Input your code here", font=("bold", 14), pady=20
        )
        self.code_label.pack()
        # self.code_label.grid(row=0, column=1, sticky=tk.W)

        # self.hi_there = tk.Button(self, command=self.say_hi)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # self.quit.pack(side="bottom")

    # def say_hi(self):
    #     print("hi there, everyone!")

