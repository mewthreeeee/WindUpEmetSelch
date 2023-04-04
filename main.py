import json
import tkinter as tk
from PIL import Image, ImageTk

f = open('config.json')
settings = json.load(f)

window = tk.Tk()
window.geometry(f"{settings['size']}x{settings['size']}")
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

image = ImageTk.PhotoImage(Image.open("assets/solus1.png").resize((settings['size'],settings['size']), Image.LANCZOS))
solus = tk.Label(window, image=image, bd=0, bg='black')
solus.pack()

rightClickMenu = tk.Menu(window, tearoff=0)
rightClickMenu.add_command(label="Defeat", command=window.destroy)

def showRightClickMenu(event):
    try:
        rightClickMenu.tk_popup(event.x_root, event.y_root)
    finally:
        rightClickMenu.grab_release()

solus.bind("<Button-3>", showRightClickMenu)

x,y = 0,0
def drag(event):
    global x, y
    offsetX, offsetY = event.x - x, event.y - y
    newX, newY = window.winfo_x() + offsetX, window.winfo_y() + offsetY
    newGeo = f"+{newX}+{newY}"
    window.geometry(newGeo)

window.bind("<B1-Motion>", drag)

window.mainloop() 