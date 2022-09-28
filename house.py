import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.title("Fluffy's House")
window.geometry("533x300")
window.configure(background='#0000ff')
path = "bun.png"
image = Image.open(path)
resize_image = image.resize((533,300))
img = ImageTk.PhotoImage(resize_image)
panel = tk.Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
window.resizable(width=False, height=False)
window.mainloop()
