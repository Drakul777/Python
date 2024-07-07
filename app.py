from tkinter import *
import webbrowser


def open_graven_channel():
    webbrowser.open_new("http://youtube.com/gravenilvectuto")


#créer une premiere fenetre
window = Tk()

#personnaliser la fenetre
window.title("My application")
window.geometry('720x480')
window.minsize(480, 360)
window.iconbitmap("Logo.ico")
window.config(background='#0066CE')

#créer la boite
frame = Frame(window, bg='#0066CE', bd=0, relief=SUNKEN)

#ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur l'application", font=("Arial", 40), bg="#0066CE", fg='white')
label_title.pack()

#ajouter un second texte
label_subtitle = Label(frame, text="Hey salut à tous c'est Graven", font=("Arial", 25), bg="#0066CE", fg='white')
label_subtitle.pack()

#ajouter un nouveau bouton
yt_button = Button(frame, text="Ouvrir Youtube", font=("Arial", 25), bg="white", fg="#0066CE", command=open_graven_channel)
yt_button.pack(pady=50, fill=X)

#ajouter
frame.pack(expand=YES)

#afficher
window.mainloop()
