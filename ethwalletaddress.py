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

background_img = PhotoImage(file = f"images/ethbackground.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"images/textbar.png")
entry0_bg = canvas.create_image(
    526.0, 346.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    fg = "#000000",
    highlightthickness = 0)

entry0.place(
    x = 326.0, y = 322,
    width = 400.0,
    height = 46)

img0 = PhotoImage(file = f"images/submit.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 813, y = 329,
    width = 95,
    height = 34)

window.resizable(False, False)
window.mainloop()
