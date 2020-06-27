from tkinter import filedialog,Button,Frame,Tk
# from ocrtestone import
########################################################

class Textify:

    def __init__(self,master):
        self.master = master
        self.initializeOutlineFrame()

    def initializeOutlineFrame(self):
        self.convertImageButton = Button(self.master,text="Convert Image",command=self.browseIMG)
        self.convertImageButton.pack()
        self.convertPdfButton = Button(self.master,text="Convert pdf",command=self.browsePDF)
        self.convertPdfButton.pack()
        self.batchConvertButton = Button(self.master,text="Convert multiple files",command=self.browseAllFiles)
        self.batchConvertButton.pack()

    def browsePDF(self):
        filename = filedialog.askopenfilename(initialdir = "/",
        title = "Select a File",filetypes = (("pdf files","*.pdf*"),("all files", "*.*")))
        saveLocation = filedialog.asksaveasfilename(initialdir = "/",title="Save file as",filetypes=("text files","*.txt*"))
        print(filename)

    def browseIMG(self):
        filename = filedialog.askopenfilename(initialdir = "/",
        title = "Select a File",filetypes = (("jpg files","*.JPG*"),("png files","*.PNG*")))

    def browseAllFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
        title = "Select files",filetypes = (("jpg files","*.JPG*"),("png files","*.PNG*"),("pdf files","*.pdf*"),("all files", "*.*")))


window = Tk()
window.title("Textify")
window.geometry("300x300")
app = Textify(window)
window.mainloop()

# frame = tk.Frame(master=window,width = 350, height = 350)
# frame.pack()
# convertPdfButton = tk.Button(master=window,text = "Convert pdf",command = browsePDF)
# convertImageButton = tk.Button(master=window,text = "Convert image",command = browseIMG)
# convertPdfButton.place(x=150,y=175)
# convertImageButton.place(x= 150, y= 220)
########################################################

#######################################################
# test = PasswordGenerator()
# result = test.getTenCharacterPassword()
# print(result)

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#         self.setCanvas()
#
#     def setCanvas(self):
#         w = Canvas(self.master, width=200, height=100)
#         w.pack()
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()
#################################################

###################################################
# class App:
#     def __init__(self, master):
#         self.master = master
#
#
# # create the application
# root = Tk()
# myapp = App(root)
#
# #
# # here are method calls to the window manager class
# #
# myapp.master.title("My Do-Nothing Application")
# myapp.master.maxsize(1000, 400)
#
# # start the program
# root.mainloop()
##########################################################
