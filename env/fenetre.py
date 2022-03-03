import tkinter as tk
import tkinter.font as tkFont
from frequence import Frequence, FrequenceWave
from record import Record
from frequence_note import Frequence_note
import os
import numpy
from tkinter import filedialog



class Fen:


    def __init__(self):

        
        # initialisation de la fenêtre
        self.root = tk.Tk()
        self.root["bg"] = "white"
       
        
        # définition de la taille des frames et canvas
        
        self.height = 300
        self.height_frame = 50
        self.y_note = 100
        hauteur_fenetre = self.height + 2*(self.height_frame)
        self.width = hauteur_fenetre
        self.root.minsize(self.width,hauteur_fenetre)
        
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


        # définition de la taille des polices
        self.size = 60
        self.size2 = 20

        # grande police puis petite police
        self.font1 = tkFont.Font( family = "Arial" , size = self.size )
        self.font2 = tkFont.Font( family = "Arial" , size = self.size2, weight='bold' )

        # création d'une variable de texte pour l'erreur en hertz
        self.textevar = tk.StringVar()
        self.textevar.set("")
        self.var = None

        self.note_var = tk.StringVar()
        self.note_var.set("")
        self.canvas_note = tk.Label(self.canvas, textvariable = self.note_var, font=self.font1)

        



    # analyse d'un son à partir d'un fichier wave
    def analyse_son(self):
    
        # ouvrir un fichier wave pour analyse
        song = filedialog.askopenfilename(initialdir='/home/erwan/Musique', title="choisissez un fichier", filetypes=[('wave Files', '*.wav')])

        # lit le fichier et retourne un tableau numpy
        fr = FrequenceWave(song).freq()

        # retourne la note
        texte = Frequence_note(fr).determiner_note


        # affichage de la note      
        taille = len(texte)*self.size
        x = (self.width/2) - (taille/2) 
        self.note_var.set(texte)
        self.canvas_note.place(x = x, y = self.y_note)

        # mise en forme de la différence de fréquence
        texteBrut = Frequence_note(fr).determiner_frequence_la_plus_proche[0]
        texteBrut = str(texteBrut)
        texte = texteBrut.replace('.', ',')
        if not texte.startswith('-'):
            texte = '+' + texte
        texte = texte + 'Hertz'

        # changement de texte pour la fréquence
        self.textevar.set(texte)
        
        




    def enregistrement(self):
        # lance l'enregistrement et retourne un tableau numpy
        enr = Record().rec()
        
        # retourne la fréquence en hertz de la note
        fr = Frequence(enr).freq()

        # affiche la note correspondante
        texte = Frequence_note(fr).determiner_note

        # changement de texte pour la note
        # affichage de la note      
        taille = len(texte)*self.size
        x = (self.width/2) - (taille/2) 
        self.note_var.set(texte)
        self.canvas_note.place(x = x, y = self.y_note)

        
        # affichage de la différence d'accordage en hertz : mise en feorme du texte et affichage
        texteBrut = Frequence_note(fr).determiner_frequence_la_plus_proche[0]
        texteBrut = str(texteBrut)
        texte = texteBrut.replace('.', ',')
        if not texte.startswith('-'):
            texte = '+' + texte
        texte = texte + 'Hertz'

        self.textevar.set(texte)






    # placement des éléments dans la fenêtre
    def fen_princ(self):

        self.canvas.pack()
        self.frame1.pack()
        self.frame2.pack()

        # mise en forme du graphisme cercle
        x1 = 55
        y1 = 20
        x2 = self.width - x1
        y2 = self.height - y1 

        padding = 10

        self.canvas.create_oval(x1, y1, x2, y2, width=2,outline="black")
        self.canvas.create_oval(x1+padding, y1+padding, x2-padding, y2-padding, width=2,outline="black")
        

        # pré-placement de la différence en hertz 
        self.var = tk.Label(self.frame1, textvariable=self.textevar, font=self.font2)
        self.var.pack()

        button = tk.Button(self.frame2, text='lancer', command = self.analyse_son)
        button.grid(column=0, row=0)
        button = tk.Button(self.frame2, text='rec', command = self.enregistrement)
        button.grid(column=1, row=0)



    def rafraichir(self) :
        self.canvas.update_idletasks()


    # lancement de l'affichage
    def afficher(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    fen = Fen()
    fen.fen_princ()
    
    fen.afficher()