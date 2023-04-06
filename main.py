import json
import tkinter as tk
from PIL import Image, ImageTk
from screeninfo import get_monitors
import random
import math
import time
import bisect

class Minion:
    def __init__(self):
        self.settings = json.load(open('config.json'))
        self.settings['screenGeo'] = self.getScreenGeometry()
        
        self.state = {}

        self.master = tk.Tk()
        self.x, self.y = 0, 0
        self.initializeWindow()
        self.initializeSolus()

        self.initializeRightClickMenu()
        self.master.bind("<Button-3>", self.handlerRightClickMenu)
        self.master.bind("<B1-Motion>", self.handlerDrag)
        self.master.bind("<Button-1>", self.handlerLeftClick)

        self.master.geometry(f"+400+400")
        self.master.update()

        #mudar a imagem da label sem criar nova label:
        #label.configure(image=img)

    def run(self):
        self.master.after(100, self.update)
        self.master.mainloop()

    def update(self):
        print("in update")

        #Choosing random action based on the probabilities
        r = random.random()
        p = bisect.bisect_left(self.settings['probabilities'], r)
        action = self.settings['actions'][p]
        
        match action:
            case "idle":
                print("idle")
            case "moveRandomly":
                print("moveRandomly")
            case _:
                print(f"Action \"{action}\" not found!")

        self.master.after(500, self.update)

    def initializeWindow(self):
        self.master.attributes('-topmost', True)
        self.master.geometry(f"{self.settings['size']}x{self.settings['size']}")
        self.master.config(highlightbackground='black')
        self.master.overrideredirect(True)
        self.master.wm_attributes('-transparentcolor','black')

    def initializeSolus(self):
        self.image = ImageTk.PhotoImage(Image.open("assets/solus1.png").resize((self.settings['size'],self.settings['size']), Image.LANCZOS))
        self.solus = tk.Label(self.master, image=self.image, bd=0, bg='black')
        self.solus.pack()

    def initializeRightClickMenu(self):
        self.rightClickMenu = tk.Menu(self.master, tearoff=0)
        self.rightClickMenu.add_command(label="Move randomly", command=self.behaviorFly)
        self.rightClickMenu.add_command(label="Yeet", command=self.master.destroy)

    def handlerDrag(self, event):
        offsetX, offsetY = event.x - self.x, event.y - self.y
        newX, newY = self.master.winfo_x() + offsetX, self.master.winfo_y() + offsetY
        newGeo = f"+{newX}+{newY}"
        self.master.geometry(newGeo)
    
    def handlerLeftClick(self, event):
        self.x, self.y = event.x, event.y
        
    def handlerRightClickMenu(self, event):
        try:
            self.rightClickMenu.tk_popup(event.x_root, event.y_root)
        finally:
            self.rightClickMenu.grab_release()

    def behaviorFly(self):
        startingX, startingY = self.master.winfo_x(), self.master.winfo_y()
        goalX, goalY = random.randint(0, self.settings['screenGeo']['x']), random.randint(0, self.settings['screenGeo']['y'])

        steps = 10
        for i in range(steps):
            newX, newY = math.floor(((goalX - startingX)/steps) * (i+1)), math.floor(((goalY - startingY)/steps) * (i+1))
            self.master.geometry(f"+{startingX + newX}+{startingY + newY}")
            self.master.update()
            time.sleep(0.1)
    
    def placeholderDoNothing(self):
        return
    
    def getScreenGeometry(self):
        corner = {'x': 0, 'y': 0}
        maxX = -1
        maxY = -1
        for m in get_monitors():
            if m.x > maxX:
                maxX = m.x
                corner['x'] = maxX + m.width
            if m.y > maxY:
                maxY = m.y
                corner['y'] = maxY + m.height
        return corner

minion = Minion()
minion.run()