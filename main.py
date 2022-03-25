from tkinter import Tk, filedialog
import os
import random

root = Tk()
root.withdraw()
root.attributes('-topmost', True)

openFile = filedialog.askdirectory()
num = random.randint(0, len(os.listdir(openFile)))
print(os.listdir(openFile)[num])
