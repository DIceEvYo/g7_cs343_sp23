from tkinter import *
from tkinter import ttk


def rentalPayment():
  # Créer la fenêtre principale
  newWindow = Tk()
  newWindow.geometry('640x360')
  newWindow.title('Rental Payment')
  newWindow['bg'] = 'white'
  newWindow.config(bg='white')
  font = ("Arial", 12)
  title_font = ("Arial bold", 18)

  # Lire les informations des locataires à partir du fichier tenant.txt
  with open('tenants.txt', 'r') as file:
    rentalInfo = [line.strip().split(',') for line in file]

  # Créer un widget Frame pour afficher la liste des locataires
  frame = Frame(newWindow, bd=2, relief=SOLID, bg='white')
  frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

  # Ajouter un label pour afficher le titre de la page
  Label(frame,
        text="Rental Payment",
        font=title_font,
        padx=20,
        pady=20,
        bg='white').pack(expand=True, fill=BOTH)

  # Créer un widget Treeview pour afficher les informations des locataires sous forme de tableau
  tree = ttk.Treeview(frame,
                      columns=('firstname', 'lastname', 'roomnumber'),
                      show='headings')

  # Ajouter des en-têtes de colonnes
  tree.heading('firstname', text='First Name')
  tree.heading('lastname', text='Last Name')
  tree.heading('roomnumber', text='Room Number')

  # Ajouter chaque dépense à la liste
  for rentalInfo in rentalInfo:
    firstname = rentalInfo[1]
    lastname = rentalInfo[2]
    roomnumber = rentalInfo[3]
    tree.insert('', 'end', values=(firstname, lastname, roomnumber))

  # Afficher la liste des dépenses dans la fenêtre avec une scrollbar
  scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
  tree.configure(yscroll=scrollbar.set)
  tree.pack(side=LEFT, fill=BOTH, padx=20, pady=20, expand=True)
  scrollbar.pack(side=RIGHT, fill=Y)

  # Ajouter un bouton pour retourner à la page d'accueil
  Button(newWindow, text="Homepage", font=font,
         command=newWindow.destroy).pack(fill=X,
                                         expand=True,
                                         side=BOTTOM,
                                         padx=20,
                                         pady=20)

  # Lancer la boucle principale
  newWindow.mainloop()
