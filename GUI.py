# GUI application for 3d-printing error detection
import tkinter as tk
import cv2

LARGE_FONT = ("Verdana", 12)


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        # self.parent = parent
        # self.vid = cv2.VideoCapture(0)
        # if not self.vid.isOpened():
        #     raise ValueError("Unable to open video source")
        # # Get video source width and height
        # self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # def __del__(self):
    #     if self.vid.isOpened():
    #         self.vid.release()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button


def run():
    # root = tk.Tk()
    # root.title("GUI")
    app = MainApplication()
    app.mainloop()
