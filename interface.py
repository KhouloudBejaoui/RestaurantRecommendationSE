import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

from experta import Fact

import rules


def findRestaurant():
    expertSystem = rules.Restaurant()
    expertSystem.reset()
    expertSystem.declare(Fact(action='restaurant'))
    expertSystem.declare(Fact(gouvernorat=rules.g))
    expertSystem.declare(Fact(budget=int(rules.b)))
    expertSystem.declare(Fact(espace=str(espace.get())))
    expertSystem.declare(Fact(parking=str(parking.get())))
    expertSystem.declare(Fact(vegan=str(vegan.get())))
    expertSystem.declare(Fact(sucre_sale=str(sucre_sale.get())))
    expertSystem.declare(Fact(cuisine=str(cuisine.get())))
    expertSystem.declare(Fact(plat=str(plat.get())))
    expertSystem.run()
    return expertSystem.name, expertSystem.photo


def openNewWindow():
    newWindow = tk.Toplevel()
    newWindow.title("Where To Eat")
    newWindow.config(bg="#ffffff")
    # sets the geometry of toplevel
    newWindow.geometry("1100x800")
    rules.g = gouvernorat.get()
    rules.b = budget.get()
    name, photo = findRestaurant()
    # when no restaurant matches the user inputs
    if name == photo == '':
        photo = r'.\RestaurantSE\Images\notFound.png'

    img = ImageTk.PhotoImage(Image.open(photo).resize((680, 600)))
    canvas = tk.Canvas(newWindow, width=900, height=700)
    canvas.configure(bg='white')
    canvas.configure(highlightthickness=0)
    canvas.pack()
    canvas.create_image(400, 350, anchor=tk.CENTER, image=img)
    canvas.img = img

    # label to display name restaurant
    name_restaurant = tk.Label(newWindow)
    ft = tkFont.Font(family='Helvetica', size=25)
    name_restaurant["font"] = ft
    name_restaurant["fg"] = "#00aa6c"
    name_restaurant["bg"] = "#ffffff"
    name_restaurant["justify"] = "center"
    name_restaurant["text"] = str(name)
    name_restaurant.place(x=450, y=0.5)


source = tk.Tk()
source.title("Where To Eat ")
source.config(bg="#ffffff")
source.resizable(True, True)
#source.geometry("1100x1100")
width = source.winfo_screenwidth()
height = source.winfo_screenheight()
source.geometry("%dx%d" % (width, height))
# Variables for choosing the selected fields
gouvernorat = tk.Entry()
budget = tk.Entry()
espace = tk.IntVar()
parking = tk.IntVar()
vegan = tk.IntVar()
sucre_sale = tk.IntVar()
cuisine = tk.IntVar()
plat = tk.IntVar()

# interface du programme
fontStyle = tkFont.Font(family="Helvetica", size=20, weight="bold")
l1 = tk.Label(source, text="Where To Eat", width=40,
              fg='#00aa6c', bg="#ffffff", font=fontStyle, justify="center", padx=340)
l1.place(x=3, y=3)

fontTipo = tkFont.Font(family="Helvetica", size=12)

# Q1:gouvernorat
tk.Label(source, text="Quel est votre gouvernorat ? ",
         width=45, bg="#ffffff", font=fontTipo).grid(row=3, column=0, pady=45)

gouvernorat.grid(row=4, column=0)
t = gouvernorat.get()
print(t)
# Q2: Budget
tk.Label(source, text="Quel est votre budget ? ",
         width=45, bg="#ffffff", font=fontTipo, pady=20).grid(row=5, column=0)
budget.grid(row=6, column=0)

# Q3:espace
tk.Label(source, text="Voulez-vous un restaurant couvert ou en plein air ?",
         width=40, bg="#ffffff", font=fontTipo, pady=20).grid(row=7, column=0)

c5 = tk.Checkbutton(source, text="Couvert", variable=espace,
                    onvalue=1, bg="#ffffff")
c5.grid(row=8, column=0)

c6 = tk.Checkbutton(source, text="Plein air", variable=espace,
                    onvalue=2, bg="#ffffff")
c6.grid(row=9, column=0)

# Q4:parking
tk.Label(source, text="Voulez-vous un parking ? ",
         width=50, bg="#ffffff", font=fontTipo, pady=20).grid(row=10, column=0)

c7 = tk.Checkbutton(source, text="Yes", variable=parking,
                    onvalue=1,
                    bg="#ffffff")
c7.grid(row=11, column=0)

c8 = tk.Checkbutton(source, text="No", variable=parking,
                    onvalue=2,
                    bg="#ffffff")
c8.grid(row=12, column=0)



# Q5:vegan
tk.Label(source, text="Êtes-vous vegan ? ",
         width=50, bg="#ffffff", font=fontTipo).grid(row=3, column=1)

c9 = tk.Checkbutton(source, text="Yes", variable=vegan,
                    onvalue=1,
                    bg="#ffffff")
c9.grid(row=4, column=1)

c10 = tk.Checkbutton(source, text="No", variable=vegan,
                     onvalue=2,
                     bg="#ffffff")
c10.grid(row=5, column=1)

# Q7:sucre_sale
tk.Label(source, text="Vous préférez du salé ou sucré ?",
         width=50, bg="#ffffff", font=fontTipo, pady=20).grid(row=6, column=1)

c13 = tk.Checkbutton(source, text="Sucré", variable=sucre_sale,
                     onvalue=1,
                     bg="#ffffff")
c13.grid(row=7, column=1)

c14 = tk.Checkbutton(source, text="Salé", variable=sucre_sale,
                     onvalue=2,
                     bg="#ffffff")
c14.grid(row=8, column=1)

# Q8:cuisine
tk.Label(source, text="Quelle est votre cuisine préférée ?",
         width=40, bg="#ffffff", font=fontTipo).grid(row=9, column=1)

c15 = tk.Checkbutton(source, text="Tunisienne", variable=cuisine,
                     onvalue=1,
                     bg="#ffffff")
c15.grid(row=10, column=1)
c16 = tk.Checkbutton(source, text="Américaine", variable=cuisine,
                     onvalue=2,
                     bg="#ffffff")
c16.grid(row=11, column=1)
c17 = tk.Checkbutton(source, text="Europeienne", variable=cuisine,
                     onvalue=3,
                     bg="#ffffff")
c17.grid(row=12, column=1)
c18 = tk.Checkbutton(source, text="Asiatique", variable=cuisine,
                     onvalue=4,
                     bg="#ffffff")
c18.grid(row=13, column=1)
c19 = tk.Checkbutton(source, text="Italienne", variable=cuisine,
                     onvalue=5,
                     bg="#ffffff")
c19.grid(row=14, column=1)

# Q9:plat
tk.Label(source, text="Qu'est ce que vous voulez manger ?",
         width=40, bg="#ffffff", font=fontTipo).grid(row=3, column=2)

c20 = tk.Checkbutton(source, text="Pasta", variable=plat,
                     onvalue=1,
                     bg="#ffffff")
c20.grid(row=4, column=2)

c20 = tk.Checkbutton(source, text="Pizza", variable=plat,
                     onvalue=2,
                     bg="#ffffff")
c20.grid(row=5, column=2)
c21 = tk.Checkbutton(source, text="Burger", variable=plat,
                     onvalue=3,
                     bg="#ffffff")
c21.grid(row=6, column=2)

c22 = tk.Checkbutton(source, text="Poisson", variable=plat,
                     onvalue=4,
                     bg="#ffffff")
c22.grid(row=7, column=2)

c23 = tk.Checkbutton(source, text="Suchi", variable=plat,
                     onvalue=5,
                     bg="#ffffff")
c23.grid(row=8, column=2)

c24 = tk.Checkbutton(source, text="Viande", variable=plat,
                     onvalue=6,
                     bg="#ffffff")
c24.grid(row=9, column=2)

c25 = tk.Checkbutton(source, text="Glace", variable=plat,
                     onvalue=7,
                     bg="#ffffff")
c25.grid(row=10, column=2)

c26 = tk.Checkbutton(source, text="Crepe", variable=plat,
                     onvalue=8,
                     bg="#ffffff")
c26.grid(row=11, column=2)

# Submit button
ft = tkFont.Font(family='Times', size=12)
b1 = tk.Button(source, text="Chercher", command=openNewWindow, bg="#00aa6c", borderwidth="0px", font=ft,
               fg="#ffffff")
b1.place(x=600, y=540, width=200, height=38)
photo = r'.\RestaurantSE\Images\restaurant.png'
img = ImageTk.PhotoImage(Image.open(photo).resize((100, 100)))
canvas = tk.Canvas(source, width=100, height=100)
canvas.place(x=650, y=580)
canvas.create_image(1, 0, anchor=tk.NW, image=img)
canvas.img = img

photo1 = r'.\RestaurantSE\Images\vegetable.png'
img1 = ImageTk.PhotoImage(Image.open(photo1).resize((25, 25)))
canvas1 = tk.Canvas(source, width=25, height=25)
canvas1.place(x=580, y=40)
canvas1.create_image(1, 0, anchor=tk.NW, image=img1)
canvas1.img = img1

photo2 = r'.\RestaurantSE\Images\placeholder.png'
img2 = ImageTk.PhotoImage(Image.open(photo2).resize((25, 25)))
canvas2 = tk.Canvas(source, width=25, height=25)
canvas2.place(x=90, y=45)
canvas2.create_image(1, 0, anchor=tk.NW, image=img2)
canvas2.img = img2

photo3 = r'.\RestaurantSE\Images\dollar.png'
img3 = ImageTk.PhotoImage(Image.open(photo3).resize((25, 25)))
canvas3 = tk.Canvas(source, width=25, height=25)
canvas3.place(x=100, y=160)
canvas3.create_image(1, 0, anchor=tk.NW, image=img3)
canvas3.img = img3

photo4 = r'.\RestaurantSE\Images\vehicle.png'
img4 = ImageTk.PhotoImage(Image.open(photo4).resize((25, 25)))
canvas4 = tk.Canvas(source, width=25, height=25)
canvas4.place(x=100, y=390)
canvas4.create_image(1, 0, anchor=tk.NW, image=img4)
canvas4.img = img4

photo5 = r'.\RestaurantSE\Images\garden.png'
img5 = ImageTk.PhotoImage(Image.open(photo5).resize((25, 25)))
canvas5 = tk.Canvas(source, width=25, height=25)
canvas5.place(x=20, y=280)
canvas5.create_image(1, 0, anchor=tk.NW, image=img5)
canvas5.img = img5

photo6 = r'.\RestaurantSE\Images\donut.png'
img6 = ImageTk.PhotoImage(Image.open(photo6).resize((25, 25)))
canvas6 = tk.Canvas(source, width=25, height=25)
canvas6.place(x=530, y=220)
canvas6.create_image(1, 0, anchor=tk.NW, image=img6)
canvas6.img = img6

photo7 = r'.\RestaurantSE\Images\cutlery.png'
img7 = ImageTk.PhotoImage(Image.open(photo7).resize((25, 25)))
canvas7 = tk.Canvas(source, width=25, height=25)
canvas7.place(x=530, y=350)
canvas7.create_image(1, 0, anchor=tk.NW, image=img7)
canvas7.img = img7

photo8 = r'.\RestaurantSE\Images\plat.png'
img8 = ImageTk.PhotoImage(Image.open(photo8).resize((25, 25)))
canvas8 = tk.Canvas(source, width=25, height=25)
canvas8.place(x=940, y=40)
canvas8.create_image(1, 0, anchor=tk.NW, image=img8)
canvas8.img = img8

copyright = tk.Label(source, text="© Imen Dridi et Khouloud Bejaoui 2ING1", width=40,
              fg='#000000', bg="#ffffff", font=fontTipo, justify="center")
copyright.place(x=5, y=650)

source.mainloop()
