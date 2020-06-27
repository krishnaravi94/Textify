
# from tkinter import Tk, Label, Button

# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")
#
#         self.label = Label(master, text="This is our first GUI!")
#         self.label.pack()
#
#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()
#
#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#
#     def greet(self):
#         print("Greetings!")
#
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()
list1 = [1,2,4,6,7,10,11,13,15,16]
celsiusToFarenheitList = list(map(lambda x: float((9/5)*x) +32,list1))
print(celsiusToFarenheitList)
# evenList = list(filter(lambda result: result%2 == 0,list1))
# print(evenList)
# evenSquaredList = map(lambda squaredNumber: squaredNumber ** 2,evenList)
# print(evenSquaredList)
# evenSquaredList = map(result())
