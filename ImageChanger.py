from tkinter import *
from PIL import Image
from tkinter.filedialog import *
from tkinter import messagebox

c0 = "#000000" #black
c1 = "#59656f" #red
c2 = "#ffffff" #white
c3 = "#0074eb" #blue
c4 = "#59b456" #green

window = Tk()
window.geometry("405x250")
window.title("Image Changer")
window.configure(background=c2)

frame = Frame(window, width=405, height=250, bg=c2, relief="flat")
frame.grid(row=0, column=0,sticky=NSEW)

app_name = Label(frame, text="Image Changer", width=24, height=1, anchor=CENTER,
                 pady =7, padx=10, relief="flat", font=("Courier 20 bold"), bg=c2,fg=c0)
app_name.grid(row=0, column=0,columnspan=2,sticky=NSEW,pady=1)



def newArch():
    file = askopenfilename()
    img = Image.open(file)

    img_height, img_width = img.size

    def convert():

        height = int(enter_height.get())
        width = int(enter_width.get())
        print(height, width)

        new_value = (height, width)
        new_img = img.resize(new_value)

        img_save = asksaveasfilename()
        new_img.save(img_save+".jpg")

        messagebox.showinfo("Compressed with success")

        real_size.destroy()
        new_height.destroy()
        new_width.destroy()
        enter_height.destroy()
        enter_width.destroy()
        button_convert.destroy()
    
    
    
    real_size = Label(frame, text="Height and width " + str(img_height) +"x"+ str(img_width), width=24,
                      pady=7, padx=10, relief="flat", font=("Courier 12 bold"), bg=c2, fg=c3)
    real_size.grid(row=2, column=0, columnspan=2, sticky=NSEW, pady=1)


    new_height = Label(frame, text="Text new height", width=10, height=1,anchor=CENTER,
                       pady=7, padx=10, relief="flat", font=("Courier 10 bold"), bg=c2, fg=c0)
    new_height.grid(row=3, column=0, sticky=NSEW, pady=5)

    new_width = Label(frame, text="Text new width", width=10, height=1,anchor=CENTER,
                      pady=7, padx=10, relief="flat", font=("Courier 10 bold"), bg=c2, fg=c0)
    new_width.grid(row=3, column=1, sticky=NSEW, pady=5)

    enter_height = Entry(frame, width=9, justify="center")
    enter_height.grid(row=4, column=0, sticky=NSEW, pady=5)

    enter_width = Entry(frame, width=9, justify="center")
    enter_width.grid(row=4, column=1, sticky=NSEW, pady=5)    

    button_convert = Button(frame, text="Convert", width=10, height=1,font="5", anchor=CENTER,
                            relief="raised", bg=c4,fg=c2, command=convert)
    button_convert.grid(row=5, column=0,columnspan=2,sticky=NSEW,pady=5)       




button_new = Button(frame, text="Select new image +", width=10, height=1,font="5", anchor=CENTER,
                    relief="raised", bg=c3,fg=c2, command = newArch)

button_new.grid(row=1, column=0,columnspan=2,sticky=NSEW,pady=1)


window.mainloop()