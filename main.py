from tkinter import filedialog
import os
import random

openFile = filedialog.askdirectory()
num = random.randint(0, len(os.listdir(openFile)))
print(os.listdir(openFile)[num])
