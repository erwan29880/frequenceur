import numpy
from notes import Note
import os
import frequence



class Frequence_note(Note):
    """retourne la fréquence/la note la plus proche de la note enregistrée/jouée"""



    def __init__(self, note_jouee, prod=True):
        super().__init__()
        
        #en production
        if prod==True:
            self.fr = note_jouee

        # en test    
        else:
            self.fr = frequence.FrequenceWave(fichier).freq()

        # un dataframe pandas pour un tableau des notes associées à leurs fréquences sur plusieurs octaves
        self.df = super().enregistrement_csv
        # un tableau numpy à une dimension pour effectuer la recherche de fréquence la plus proche
        self.valeurs = super().enregistrement_tableau


    @property
    def determiner_frequence_la_plus_proche(self):

        # trouver la position de la fréquence à tester la plus proche dans le tableau numpy 
        k = 0
        for i in range(len(self.valeurs)):
            if self.fr >= self.valeurs[i]:
                k += 1
            
        # déterminer si la fréquence est plus proche de la fréquence supérieure ou inférieure afin de déterminer le nom de la note
        note_superieure = self.valeurs[k]
        note_inferieure = self.valeurs[k-1]
        moyenne = (note_superieure + note_inferieure)/2

        # note plus proche de la note inférieure
        if self.fr <= moyenne:
            val = note_inferieure
            position = k-1
            
        # note plus proche de la note supérieure    
        else:
            val = note_superieure
            position = k

        # calculer la différence en hertz entre la note et la fréquence juste
        diff_hertz = self.fr - val
        diff_hertz = numpy.around(diff_hertz, decimals=3)

        # retourne l'erreur d'accord en hertz, la fréquence juste proche, la position dans le tableau numpy
        return diff_hertz, val, position
           

    @property
    def determiner_note(self):
        diff_hertz = self.determiner_frequence_la_plus_proche[0]
        val = self.determiner_frequence_la_plus_proche[1]
        position = self.determiner_frequence_la_plus_proche[2]

        # le dataframe a 12 colonnes pour chacune de notes
        len_ligne_df = self.df.shape[1]

        # le modulo retourne le numéro de colonne
        pos_data_frame = position % len_ligne_df

        # le nom de la colonne est une note de musique
        return self.df.columns[pos_data_frame]
        



if __name__ == "__main__":


    # fichier wave à analyser :
    # décocher une ligne dans __init__
    # nom_fichier = 'mi3.wav'
    # nom_fichier = '12_lab3.wav'
    nom_fichier = 'SI.wav'
    nom_fichier = 'sol3.wav'
    fichier = os.path.join(os.getcwd(),'env','sons', nom_fichier)

    

    clf = Frequence_note(fichier, prod=False)
    
    print(clf.fr)
    # print(clf.determiner_frequence_la_plus_proche[0])
    

    
    print(clf.determiner_note)
   