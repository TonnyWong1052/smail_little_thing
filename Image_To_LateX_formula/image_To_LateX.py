from PIL import Image
from tkinter import Tk, filedialog
import time
import sys
import pyperclip
from PIL import ImageGrab
from pix2tex.cli import LatexOCR
model = LatexOCR()

# remark: leaflet / https://www.latexlive.com/
def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if file_path:
        try:
            image = Image.open(file_path)
            return image
        except Exception as e:
            print("Error：", str(e))

    return None

selected_image = select_image()

if selected_image:
    return_text = '\\begin{align}'+str(model(selected_image))+ '\end{align}'
    pyperclip.copy(return_text)
    print(return_text)
else:
    print("Something get error")

sys.exit()