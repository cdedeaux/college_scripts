import pyautogui
import time
import threading
from tkinter import *
from tkinter import ttk
from pynput import keyboard


clicking = False

def start_clicking():
    global clicking
    while clicking:
        delay = .000001
        pyautogui.click() # Default is left click
    
def on_start():
    global clicking
    if clicking:
        return
    clicking = True
    t = threading.Thread(target=start_clicking)
    t.daemon = True
    t.start()
def on_stop(event=None):
    global clicking
    clicking = False
    

def start_hotkeys():
    with keyboard.GlobalHotKeys({
        '<ctrl>+h': on_start,
        '<ctrl>+i': on_stop
    }) as h:
        h.join()

hotkey_thread = threading.Thread(target=start_hotkeys)
hotkey_thread.daemon = True
hotkey_thread.start()



root = Tk()
root.title("Auto Clicker")
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
ttk.Label(mainframe, text="Cool Auto Clicker").grid(column=1, row=1, columnspan=3)


ttk.Button(mainframe, text="Start (Ctrl + H)", command=on_start).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Stop (Ctrl + I)", command=on_stop).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Quit", command=root.quit).grid(column=3, row=3, sticky=N)
ttk.Combobox(mainframe, values=["Left Click", "Right Click", "Middle Click"]).grid(column=1, row=5, columnspan=3, sticky=(W, E))

root.mainloop()

