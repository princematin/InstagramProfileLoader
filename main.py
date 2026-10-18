# imports
from tkinter import *
import instaloader
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

# commands
def prof_loader():
    loader = instaloader.Instaloader()

    prof = instaloader.Profile.from_username(loader.context, f"{input_id.get()}")
    a = urlopen(prof.get_profile_pic_url())
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    image_label.config(image=pic)
    image_label.image = pic
    image_label.place(x=20, y=220)

    text1.delete("1.0", "end")
    text2.delete("1.0", "end")
    text3.delete("1.0", "end")
    text4.delete("1.0", "end")

    text1.insert("1.0", f"username : {prof.username}")
    text2.insert("1.0", f"biography : {prof.biography}")
    text3.insert("1.0", f"followers : {prof.followers}")
    text4.insert("1.0", f"following : {prof.followees}")

# window

window = Tk()
window.geometry("700x500")
window.maxsize(800, 800)
window.minsize(300, 300)
window.title("InstagramProfileLoader")
window.configure(bg="lightblue")


# labels
text = Label(window,
    text="Enter Profile ID", 
    bg="light blue"
    )

text.place(x= 200, y=20)

image_label = Label(window)

# buttom
button = Button(
    window,
    text="Click to show",
    fg="blue",
    background="gray"
    )
button.config(command=prof_loader)
button.place(x=200, y=80)

# inputs
input_id = Entry(window, width=20)
input_id.place(x=200, y= 50)

# text
text1 = Text(window, bg="gray", height=1, width=40)
text1.place(x=20, y=120)

text2 = Text(window, bg="gray", height=1, width=100)
text2.place(x=20, y=140)

text3 = Text(window, bg="gray", height=1, width=20)
text3.place(x=20, y=160)

text4 = Text(window, bg="gray", height=1, width=20)
text4.place(x=20, y=180)

# loop
window.mainloop()
