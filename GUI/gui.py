from tkinter import Tk, Label, Button
import os

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title('Accelo')

        self.label = Label(master, text='Welcome!!')
        self.label.pack(pady=8)

        root.geometry("500x500")

        self.greet_button = Button(master, text='Run the Program',command=self.greet, 
                                    height = 10, width = 20)
        self.greet_button.pack(pady=8)

        self.close_button = Button(master, text='Close Program', command=master.quit,
                                    height = 10, width = 20)
        self.close_button.pack(pady=8)

    def greet(self):
        os.system('python /home/aditya/MachineLearning/Accelo/Data_Collection/Images/save_images_from_multiple_cameras.py')
        print('Running the Program')

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()