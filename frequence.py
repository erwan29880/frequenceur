import scipy.io.wavfile as wav
import numpy as np
from numpy.fft import fft, fftfreq
import os
import time
import sounddevice as sd 
import matplotlib.pyplot as plt





class Frequence:
    """Calcul de la fréquence d'une note ; le format d'entrée est un tableau numpy"""


    def __init__(self, enregistrement):
        self.signal = enregistrement
        self.rate = 44100
       


    def format_tableau(self):
        """definit un tableau à une dimension ; les sons stéréos sont moyennés pour ne faire qu'un canal"""


        if len(self.signal.shape) == 2:
            
            array_prov = (self.signal[:,0] + self.signal[:,1])/2
            return np.ravel(array_prov)

        if len(self.signal.shape) == 1:
            
            return np.ravel(self.signal)
        
        

    def fourier(self):
        """définit la transformée de Fourier"""


        # avoir un seul canal
        sig = self.format_tableau()
        N = sig.shape[0]

        # transformée de fourier
        X = fft(sig)  
        # fréquences de la transformée de fourier
        freq = fftfreq(sig.shape[0], d=1/self.rate) 

        # On prend la valeur absolue de l'amplitude uniquement pour les fréquences positives et normalisation
        X_abs = np.abs(X[:N//2])*2.0/N
        # ne garder que les valeurs positives
        freq_pos = freq[:N//2]

        return X_abs, freq_pos



    def freq(self):
        """calcule la fréquence du son en hertz selon la transformée de Fourier"""


        X_abs, freq_pos = self.fourier()

        # trouver l'amplitude maximale
        val = np.max(X_abs)
        # trouver l'index de cette valeur
        val2 = np.where(X_abs == val)
        val2 = val2[0][0]
        # retourne la valeur de la fréquence à l'index val2
        return freq_pos[val2]
                
 
    def graphique_fourier(self):

        X_abs, freq_pos = self.fourier()

        plt.plot(freq_pos, X_abs, label="Amplitude absolue")
        plt.xlim(0, 6000)  # On réduit la plage des fréquences à la zone utile
        plt.grid()
        plt.xlabel(r"Fréquence (Hz)")
        plt.ylabel(r"Amplitude $|X(f)|$")
        plt.title("Transformée de Fourier")
        plt.show()


    def graphique_periodique(self,debut=0, fin=500):
        plt.figure()
        plt.grid()
        plt.plot(self.signal[debut:fin])
        plt.xlabel('temps fs')
        plt.ylabel('amplitude')
        plt.title("périodes de l'onde sonore")
        plt.show()





class FrequenceWave(Frequence):
    """Calcul de la fréquence d'une note ; le format d'entrée est un fichier wave"""


    def __init__(self, enregistrement):
        super().__init__(enregistrement)
        self.rate, self.signal = wav.read(enregistrement)
       




if __name__ == "__main__":

    nom_fichier = 'test.wav'
    # nom_fichier = '1_la3.wav'
    # nom_fichier = '4_do3.wav'
    nom_fichier = 'do3.wav'
    fichier = os.path.join(os.getcwd(),'Documents','frequenceur', 'sons',nom_fichier)
      
    
    fr = FrequenceWave(fichier)

   
    print(fr.freq())

    fr.graphique_periodique()