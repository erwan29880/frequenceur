import numpy as np
import pandas

class Note:

    def __init__(self):
    # initalise un dictionnaire avant de calculer les bonnes fréquences
        self.__notes = {
            1: ["A" ,0],
            2: ["A#",0],
            3: ["B" ,0],
            4: ["C" ,0],
            5: ["C#",0],
            6: ["D" ,0],
            7: ["D#",0],
            8: ["E" ,0],
            9: ["F" ,0],
            10:["F#",0],
            11:["G" ,0],
            12:["G#",0]
        }

    def __frequences(self):
        z = 0
        for i, j in zip(self.__notes.keys(), self.__notes.values()):
            liste = []

            # r est la valeur du demi-ton
            r = 2**(1/12)

            # valeur des notes incrémentées
            lis = round(440 * r**(z), 2)
            liste.append(j[0])
            liste.append(lis)
            z = z+1
            self.__notes[z] = liste
        
        return self.__notes


    def set_octave(self, octave = 4):
        lis = self.__frequences()
        liste = []
        for i in self.__notes.values():
            frequency = i[1] * 2 ** (((octave*12)-48) / 12) 
            liste.append(frequency)

        return liste

    @property
    def enregistrement_csv(self):
        # récupérer les notes du dictionnaire self.__notes
        enTete = ''
        qte = len(self.__notes.keys())
        
        # créer l'entete di fichier csv
        k = 0
        for i in self.__notes.values():
            k += 1
            if k < 12:
                enTete += i[0] +','
            elif k == 12:
                enTete += i[0] +'\n'
           
        # écrire dans le fichier csv
        with open('sons/notes.csv', 'w') as f:
            f.write(enTete)

        # ecrire les notes dans le fichier csv
        with open('sons/notes.csv', 'a') as f:
            for i in range(1,9):
                notes = self.set_octave(i)
                corps = ''
                for i in range(len(notes)):
                    if i < 11:
                        corps += str(notes[i]) +','
                    elif i == 11:
                        corps += str(notes[i]) +'\n'
                f.writelines(corps)
       
        return pandas.read_csv('sons/notes.csv')

    @property
    def enregistrement_tableau(self):
        liste = []
        for i in range(1,9):
            notes = self.set_octave(i)
            for j in range(len(notes)):
                liste.append(notes[j])
        return liste


if __name__ == "__main__":    

# vérification 

    notes = Note()
    # notes.set_octave(1)
    print(notes.enregistrement_csv)


    # print(notes)
