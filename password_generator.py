import string
from tkinter import *
from random import randint, choice
def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#créer la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("Logo.ico")
window.config(bg="#0066CE")

#créer la frame principale
frame = Frame(window, bg='#0066CE', )

#création d'image
width = 300
height = 300
image = PhotoImage(file="Protection.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#0066CE', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous boite
right_frame = Frame(frame, bg='#0066CE')

#créer un titre
label_title = Label(right_frame, text='Mot de passe', font=("Arial", 20), bg='#0066CE', fg='white')
label_title.pack()

#créer un champs/entrée/input
password_entry = Entry(right_frame, font=("Arial", 20), bg='#0066CE', fg='white')
password_entry.pack()

#créer un Bouton
generate_password_button = Button(right_frame, text='Générer', font=("Arial", 20), bg='#0066CE', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

#on place la sous boite a droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

#afficher la frame
frame.pack(expand=YES)

#on crée une barre de menu
menu_bar = Menu(window)
#creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichiers", menu=file_menu)

# configurer notre fenetre pour ajouter cette menu bar
window.config(menu=menu_bar)


#afficher la fenetre
window.mainloop()
