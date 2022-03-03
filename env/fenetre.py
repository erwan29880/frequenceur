import tkinter as tk
import tkinter.font as tkFont
from frequence import Frequence, FrequenceWave
from record import Record
from frequence_note import Frequence_note
import os
import numpy



class Fen:


    def __init__(self, size):

        # initialisation de la fenêtre
        self.root = tk.Tk()
        self.root.minsize(1050,600)
        self.root["bg"] = "white"

        # définition de la taille des polices
        self.size = 60
        self.size2 = 20
        
        # définition de la taille des frames et canvas
        self.width = 300
        self.height = 300
        self.height_frame = 50
        self.y_note = 100
        
        # initialisation des frames et canvas
        self.frame1 = tk.Frame(self.root)
        self.frame1["bg"] = "white"
        self.frame1.config(width=self.width, height=self.height_frame)

        self.frame2 = tk.Frame(self.root)
        self.frame2["bg"] = "white"
        self.frame2.config(width=self.width, height=self.height_frame)

        self.canvas = tk.Canvas(self.root)
        self.canvas.config(width=self.width, height=self.height)
        self.canvas["bg"] = "grey"

        # création d'une variable de texte pour l'erreur en hertz
        self.textevar = tk.StringVar()
        self.textevar.set("")
        self.var = None
        
        # grande police puis petite police
        self.font1 = tkFont.Font ( family = "Arial" , size = self.size )
        self.font2 = tkFont.Font ( family = "Arial" , size = self.size2, weight='bold' )


    # analyse d'un son à partir d'un fichier wave
    def analyse_son(self):
    
        # fichier wave à analyser :
        nom_fichier = 'sol3.wav'
        fichier = os.path.join(os.getcwd(),'env','sons',nom_fichier)

        # lit le fichier et retourne un tableau numpy
        fr = FrequenceWave(fichier).freq()

        texte = Frequence_note(fr).determiner_note



        taille = len(texte)*self.size
        x = (self.width/2) - (taille/2) 
        y = (self.height/2) - taille
        tk.Label(self.canvas, text = texte, font=self.font1).place(x = x, y = self.y_note)


        texteBrut = Frequence_note(fr).determiner_frequence_la_plus_proche[0]
        texteBrut = str(texteBrut)
        texte = texteBrut.replace('.', ',')
        if not texte.startswith('-'):
            texte = '+' + texte
        texte = texte + 'Hertz'

        self.textevar.set(texte)




    def enregistrement(self):
        # lance l'enregistrement et retourne un tableau numpy
        enr = Record().rec()
        
        # retourne la fréquence en hertz de la note
        fr = Frequence(enr).freq()

        # affiche la note correspondante
        texte = Frequence_note(fr).determiner_note

        # déterminer l'abscisse de la note
        taille = len(texte)*self.size
        x = (self.width/2) - (taille/2) 
        # affichage de la note
        tk.Label(self.canvas, text = texte, font=self.font1).place(x = x, y = self.y_note)

        # affichage de la différence d'accordage en hertz
        texteBrut = Frequence_note(fr).determiner_frequence_la_plus_proche[0]
        texteBrut = str(texteBrut)
        texte = texteBrut.replace('.', ',')
        if not texte.startswith('-'):
            texte = '+' + texte
        texte = texte + 'Hertz'

        self.textevar.set(texte)






    # placement des éléments dans la fenêtre
    def fen_princ(self):

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Quitter", command=self.root.quit)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
        self.canvas.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.canvas.create_oval(20,20,280,280, width=2,outline="black")
        self.canvas.create_oval(30,30,270,270,width=2,outline="black")

        self.var = tk.Label(self.frame1, textvariable=self.textevar, font=self.font2)
        self.var.pack()

        button = tk.Button(self.frame2, text='lancer', command = self.analyse_son)
        button.grid(column=0, row=0)
        button = tk.Button(self.frame2, text='rec', command = self.enregistrement)
        button.grid(column=1, row=0)

    


    # lancement de l'affichage
    def afficher(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    fen = Fen(10)
    fen.fen_princ()
    
    fen.afficher()