import sys, os
from PIL import Image
#############################################################################################
def png_jpg(png):
    try:
        img = Image.open(png)
        rgb_img = img.convert("RGB")
        save_path = os.path.join(r"C:\Users\{}\Images".format(os.getlogin()), "convertido.jpeg")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        rgb_img.save(save_path, format="JPEG")
        print(save_path)
    except Exception as e:
        print(f"ERROR: ", e)

def jpg_png(jpg):
    try:
        img = Image.open(jpg)
        save_path = os.path.join(r"C:\Users\{}\Images".format(os.getlogin()), "convertido.png")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        img.save(save_path, format="PNG")
        print(save_path)
    except Exception as e:
        print(f"ERROR: ", e)

def jpg_bmp(jpg):
    try:
        img = Image.open(jpg)
        save_path = os.path.join(r"C:\Users\{}\Images".format(os.getlogin()), "convertido.bmp")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        img.save(save_path, format="BMP")
        print(save_path)
    except Exception as e:
        print(f"ERROR: ", e)

def png_tiff(png):
    try:
        img = Image.open(png)
        save_path = os.path.join(r"C:\Users\{}\Images".format(os.getlogin()), "convertido.tiff")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        img.save(save_path, format="TIFF")
        print(save_path)
    except Exception as e:
        print(f"ERROR: ", e)
#############################################################################################
if str(sys.argv[1]) == "func1":
    png_jpg(str(sys.argv[2]))
if str(sys.argv[1]) == "func2":
    jpg_png(str(sys.argv[2]))
if str(sys.argv[1]) == "func3":
    jpg_bmp(str(sys.argv[2]))
if str(sys.argv[1]) == "func4":
    png_tiff(str(sys.argv[2]))