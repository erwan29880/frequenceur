import tkinter as tk
import tkinter.font as tkFont
from frequence import Frequence, FrequenceWave
from record import Record
from frequence_note import Frequence_note
import os



class Fen:


    def __init__(self, size):
        self.root = tk.Tk()
        self.size=int(size)
        self.root.minsize(1050,600)
        self.root["bg"] = "white"

        self.frameGauche = tk.Frame(self.root)
        self.frameGauche["bg"] = "white"
        self.frameGauche.config(width=300, height=300)

        self.canvas = tk.Canvas(self.root)
        self.canvas.config(width=300, height=300)
        self.canvas["bg"] = "grey"

        self.frameDroite = tk.Frame(self.root)
        self.frameDroite["bg"] = "white"
        self.frameDroite.config(width=300, height=300)


        self.font1 = tkFont.Font ( family = "Arial" , size = 100 )
        self.font2 = tkFont.Font ( family = "Arial" , size = self.size, weight='bold' )



    def analyse_son(self):
    
        # fichier wave à analyser :
        nom_fichier = 'SI.wav'
        fichier = os.path.join(os.getcwd(),'sons',nom_fichier)

        # lit le fichier et retourne un tableau numpy
        fr = FrequenceWave(fichier).freq()

        texte = Frequence_note(fr).determiner_note
        tk.Label(self.canvas, text = texte, font=self.font1).place(x = 100, y = 80)

        texte = Frequence_note(fr).determiner_frequence_la_plus_proche[0]
        tk.Label(self.frameDroite, text = texte, font=self.font1).place(x = 100, y = 120)
        



    def fen_princ(self):

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Quitter", command=self.root.quit)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
        self.frameGauche.grid(column = 0, row = 0)
        self.canvas.grid(column = 1, row = 0)
        self.frameDroite.grid(column = 2, row = 0)

        button = tk.Button(self.frameGauche, text='lancer', command = self.analyse_son)
        button.pack(anchor="w")
        

    
    # def ajout_composant(self, texte):
    #     label = tk.Label(self.frame, text=texte, font=self.font1)
    #     label['bg'] = "white" 
    #     label.pack(anchor="w")

    # def titre(self, texte):

    #     enpage = f'\n{texte}\n'
    #     label = tk.Label(self.frame, text=enpage, font=self.font2) 
    #     label['bg'] = "white" 
    #     label.pack(anchor="w")

    def button_lancement_analyse(self):

        button = tk.Button(self.frameGauche, text='lancer', command = self.analyse_son)
        button.place(x = 100, y = 100)


    def afficher(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    fen = Fen(10)
    fen.fen_princ()
    
    fen.afficher()