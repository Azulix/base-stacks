import webbrowser
import re
import sys
import os
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from pathlib import Path
import base64
from tkinter import *

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

ASSETS_PATH = Path(__file__).resolve().parent / "assets"

path = getattr(sys, '_MEIPASS', os.getcwd())



def btn_clicked():
    result=token_entry.get(1.0, tk.END+"-1c")
    print(result)
    message_bytes = result.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    tk.messagebox.showinfo("Encode", base64_message)    


    
os.chdir(path)

output_path = ""
window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "logo.png")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Base Stack's")

window.geometry("862x450")
window.configure(bg="#303030")
canvas = tk.Canvas(
    window, bg="#000000", height=519, width=862,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#303030", outline="")
canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#303030", outline="")

text_box_bg = tk.PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
token_entry_img = canvas.create_image(650.5, 167.5, image=text_box_bg)


def getTextInput():
    result=token_entry.get(1.0, tk.END+"-1c")
    print(result)
    
token_entry = tk.Text(bd=0, bg="#F6F7F9", highlightthickness=0)
token_entry.place(x=490.0, y=137+25, width=321.0, height=35)
token_entry.focus()


    
canvas.create_text(
    490.0, 156.0, text="Entre une valeur à encoder en base64", fill="#303030",
    font=("Arial-BoldMT", int(13.0)), anchor="w")
    

    



title = tk.Label(
    text="Base Stack's", bg="#0F056B",
    fg="white", font=("Arial-BoldMT", int(20.0)))
title.place(x=27.0, y=120.0)

info_text = tk.Label(
    text="Base Stack's is a very simple program. \n Its purpose is to encode in base64, \n that's all. \n Developed by \n VCH/Azulix/azulixnet.adkynet.eu\n",
    bg="#000000", fg="white", justify="left",
    font=("Georgia", int(16.0)))

info_text.place(x=27.0, y=200.0)



generate_btn_img2 = tk.PhotoImage(file=ASSETS_PATH / "start.png")
generate_btn2 = tk.Button(
    image=generate_btn_img2, borderwidth=0, highlightthickness=0,
    command=btn_clicked, relief="flat")
generate_btn2.place(x=557, y=301, width=180, height=55)

window.resizable(False, False)


window.mainloop()