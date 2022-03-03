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

        self.df = super().enregistrement_csv
        self.valeurs = super().enregistrement_tableau


    @property
    def determiner_frequence_la_plus_proche(self):

        k = 0
        for i in range(len(self.valeurs)):
            if self.fr >= self.valeurs[i]:
                k += 1
            
            
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

        diff_hertz = self.fr - val
        diff_hertz = numpy.around(diff_hertz, decimals=3)

        return diff_hertz, val, position
           

    @property
    def determiner_note(self):
        diff_hertz = self.determiner_frequence_la_plus_proche[0]
        val = self.determiner_frequence_la_plus_proche[1]
        position = self.determiner_frequence_la_plus_proche[2]
        len_ligne_df = self.df.shape[1]

        pos_data_frame = position % len_ligne_df

        return self.df.columns[pos_data_frame]
        



if __name__ == "__main__":


    # fichier wave à analyser :
    # décocher une ligne dans __init__
    nom_fichier = 'mi3.wav'
    # nom_fichier = '12_lab3.wav'
    nom_fichier = 'SI.wav'
    fichier = os.path.join(os.getcwd(),'sons', nom_fichier)

    

    clf = Frequence_note(fichier, prod=False)
    print(clf.fr)
    print(clf.fr)
    print(clf.determiner_frequence_la_plus_proche)
    
    print(clf.determiner_note)
   