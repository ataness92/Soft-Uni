import tkinter as tk

def render_image():
    pass

window = tk.Tk()
window.title("AI Image Generator")
window.geometry("500x350")

input_field = tk.Entry(window, width=14)
input_field.place(x=165, y=20)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)
generate_button.place(x=300, y=16)

window.mainloop()
