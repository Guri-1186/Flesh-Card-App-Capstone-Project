from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title=("Flashy")
window.config(padx = 50, pady = 50,bg = BACKGROUND_COLOR)

canvas = Canvas(height=526, width = 800)
card_front_img = PhotoImage(file = "images/card_front.png")
canvas.create_image(400,263,image = card_front_img)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row = 0, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400,263, text = "Word", font = ("Arile", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknow_button = Button(image=cross_image, highlightthickness=0)
unknow_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(column=1, row=1)















window.mainloop()




