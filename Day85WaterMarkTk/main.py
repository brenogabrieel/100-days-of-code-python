from tkinter import *
from tkinter import filedialog as fd
import tkinter.messagebox
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os


# --------- Variables for Watermark and Image -----------------
img_main = ""
file_main = ""
font_size_main = 60
height_main = 0
width_main = 0
rotation_main = 0
color_main = (255, 255, 255)
font_main = "arial"
original_height = 0
original_width = 0


# ---------- Creating Main Functions ------------------------

def select_file():
    global file_main
    try:
        filename = fd.askopenfilename(filetypes=[("jpeg", ".jpg .jpeg"),
                                                 ("png", ".png"),
                                                 ("bitmap", "bmp"),
                                                 ("gif", ".gif")])
        show_image(filename)
        file_main = filename
    except AttributeError:
        pass


def show_image(filename):
    global height_main, width_main, original_height, original_width
    img = (Image.open(filename))
    width, height = img.size[0], img.size[1]
    r_img = resize(img)
    panel.configure(image=r_img)
    panel.image = r_img
    height_main = height / 2
    width_main = width / 2
    original_height = height
    original_width = width


def resize(img):
    size = img.size
    f_size = (700, 600)
    factor = min(float(f_size[1]) / size[1], float(f_size[0]) / size[0])
    width = int(size[0] * factor)
    height = int(size[1] * factor)
    r_img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(r_img)


def watermark():
    global img_main, file_main, font_size_main
    try:
        with Image.open(file_main).convert("RGBA") as base:
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            # get a font
            fnt = ImageFont.truetype(font_main, font_size_main)
            # get a drawing context
            d = ImageDraw.Draw(txt)
            # draw text
            fill = color_main
            d.text((width_main, height_main), f"{wmark_entry.get()}", font=fnt, fill=fill)
            rotated_txt = txt.rotate(rotation_main)
            out = Image.alpha_composite(base, rotated_txt)

            marked_img = out.convert("RGBA")
            w_img = resize(marked_img)
            panel.configure(image=w_img)
            panel.image = w_img

            img_main = marked_img
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error", "No such file.")
    except PIL.UnidentifiedImageError:
        tkinter.messagebox.showerror("Error", "Wrong file extension.")
    except AttributeError:
        pass


def save(marked_img):
    path = fd.asksaveasfilename(confirmoverwrite=True, defaultextension="png", filetypes=[("jpeg", ".jpg"),
                                                                                          ("png", ".png"),
                                                                                          ("bitmap", "bmp"),
                                                                                          ("gif", ".gif")])
    if path is not None:
        if os.path.splitext(path)[1] == ".jpg":
            image = marked_img.convert("RGB")
            image.save(path)
            tkinter.messagebox.showinfo("Success", "Image got watermarked and saved.")

# ----------- Creating a GUI -------------------
window = Tk()
window.title("Watermarking")
window.minsize(height=100, width=500)
window.config(padx=20, pady=20, bg="#404040")

# ----------- Blank Photo ----------------------
blank_photo = Image.new(mode="RGBA", size=(700, 600), color="#242424")
image1 = ImageTk.PhotoImage(blank_photo)
panel = Label(window, image=image1)
panel.image = image1  # keep a reference
panel.grid(column=0, rowspan=15)

# ----------- Image Size Label -----------------
image_size = Label(text=f"Image size {height_main}/{width_main} (height/width)", bg="#000000", fg="#fafafa",
                   font=("Arial", 8))
image_size.grid(column=0, row=16)

# ----------- Watermark Text -------------------
wmark = Label(text="Watermark:", width=15, bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"))
wmark.grid(column=3, row=2, sticky=W)
wmark_entry = Entry(width=50, bg="#242424", fg="#fafafa")
wmark_entry.grid(column=4, row=2, columnspan=4)
wmark_entry.get()



# -------------- Show Watermark Button -------------
show_wm = Button(text="Show", bg="#000000", fg="#fafafa", command=watermark)
show_wm.grid(column=8, row=2)

# -------------- Save Watermarked Image Button ----------------
save_img = Button(text="Save", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold"), command=lambda: save(img_main), width=14, height=2)
save_img.grid(column=6, row=3)


# --------------- Select Image File --------------------
select = Button(text="Select file", font=("Arial", 12), bg="#000000", fg="#fafafa", command=select_file)
select.grid(column=0, row=17)

# -------------- Application Loop -----------------
window.mainloop()