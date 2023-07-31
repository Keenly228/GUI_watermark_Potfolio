from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import filedialog, ttk
from change_size_dialog import ChangeSizeDialog

ALPHA = 100
BLUE = "#00BFFF"

def open_image():
    file_path = filedialog.askopenfilename()
    im = PIL.Image.open(file_path)
    image_tk = ImageTk.PhotoImage(im)
    label.configure(image=image_tk)
    label.image = image_tk

def add_watermark():
    watermark_path = filedialog.askopenfilename()
    watermark_im = PIL.Image.open(watermark_path).convert("RGBA")
    watermark_im.thumbnail((100, 100))
    image_tk = label.image
    if image_tk:
        image = ImageTk.getimage(image_tk)
        image_resized = image.resize((image.width // 2, image.height // 2))
        image_with_watermark = image_resized.copy()
        position = (image_resized.width - watermark_im.width, image_resized.height - watermark_im.height)
        alpha_mask = watermark_im.split()[3].point(lambda i: i * ALPHA / 255)
        image_with_watermark.paste(watermark_im, position, mask=alpha_mask)
        image_tk_with_watermark = ImageTk.PhotoImage(image_with_watermark)
        label.configure(image=image_tk_with_watermark)
        label.image = image_tk_with_watermark

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    image_tk = label.image
    if image_tk:
        image = ImageTk.getimage(image_tk)
        image.save(file_path)

def change_size():
    image_tk = label.image
    if image_tk:
        image = ImageTk.getimage(image_tk)
        dialog = ChangeSizeDialog(image.width, image.height)
        window.wait_window(dialog.top)  # Wait for the dialog window to close
        if dialog.width is not None and dialog.height is not None and dialog.width > 0 and dialog.height > 0:
            resized_image = image.resize((dialog.width, dialog.height))
            image_tk_resized = ImageTk.PhotoImage(resized_image)
            label.configure(image=image_tk_resized)
            label.image = image_tk_resized

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My first watermark GUI program.")
window.minsize(width=800, height=600)
window.config(pady=150, bg=BLUE)

style = ttk.Style()
style.configure("TButton", foreground="white", background="#333", padding=10, font=("Arial", 12))
style.configure("TLabel", foreground="white", background=BLUE, font=("Arial", 14))

button_frame = Frame(window, bg=BLUE)
button_frame.grid(column=0, row=1, rowspan=3, padx=20)

button_open = Button(button_frame, text="Open image", command=open_image, highlightthickness=0)
button_open.grid(column=0, row=0, pady=10)

button_save = Button(button_frame, text="Save image", command=save_image, highlightthickness=0)
button_save.grid(column=0, row=1, pady=10)

button_watermark = Button(button_frame, text="Apply a watermark", command=add_watermark, highlightthickness=0)
button_watermark.grid(column=0, row=2, pady=10)

button_change_size = Button(button_frame, text="Change Size", command=change_size, highlightthickness=0)
button_change_size.grid(column=0, row=3, pady=10)

label = Label(window, text="Your Photo", background=BLUE)
label.grid(column=1, row=0, columnspan=2, padx=10, rowspan=4)



window.mainloop()
