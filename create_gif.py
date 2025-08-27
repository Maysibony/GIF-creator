import imageio.v3 as iio
from PIL import Image
import numpy
import os, webbrowser
from tkinter import Tk, filedialog

choice = input ("Press 1 if you want to choose the pictures, 2 for the excellent GIF: ")
if choice == "1":
    #let the user choose 2 pictures for the GIF
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(
        title="---Please choose 2 pictures or more---",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    # validate files
    if not files:
        print("files not found")
        exit()
else:
    files = ["first_pic.png", "second_pic.png"];

images = [ ] # containing the image data

#resize pictures
w, h = Image.open(files[0]).size
for filename in files:
    im = Image.open(filename).convert('RGBA').resize((w, h), Image.LANCZOS)
    images.append(numpy.array(im))

# turning into a GIF
iio.imwrite('excellent.gif', images, duration = 500, loop=0)

# show the GIF
out_path = os.path.abspath("excellent.gif")
print("Saved to:", out_path)
try:
    os.startfile(out_path)
except Exception:
    webbrowser.open("file://" + out_path)