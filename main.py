import json
import tkinter as tk
from PIL import Image,ImageTk

f = open('settings.json')
settings = json.load(f)
for i in settings:
    print(i)

window = tk.Tk()
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

image = ImageTk.PhotoImage(Image.open("assets/clockwork_solus_transparent.png"))
tk.Label(window, image=image, bd=0, bg='black').pack()

window.mainloop()