from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images/mainbackground.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

img0 = PhotoImage(file = f"images/btclogo.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 216, y = 255,
    width = 218,
    height = 201)

img1 = PhotoImage(file = f"images/ethlogo.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 568, y = 255,
    width = 218,
    height = 201)

window.resizable(False, False)
window.mainloop()
