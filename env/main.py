from frequence import Frequence, FrequenceWave
from record import Record
from frequence_note import Frequence_note
import os


def enregistrement():

    # lance l'enregistrement et retourne un tableau numpy
    enr = Record().rec()
    
    # retourne la fréquence en hertz de la note
    fr = Frequence(enr).freq()

    # affiche la note correspondante
    print(Frequence_note(fr).determiner_note)
       
    
    

def analyse_son():

    # fichier wave à analyser :
    nom_fichier = 'la3.wav'
    fichier = os.path.join(os.getcwd(),'env','sons',nom_fichier)

    # lit le fichier et retourne un tableau numpy
    fr = FrequenceWave(fichier).freq()

    print(Frequence_note(fr).determiner_note)



analyse_son()
