import time
import sounddevice as sd 


class Record:
    """retoune un tableau numpy"""


    def __init__(self, duree=2, freq=44100):

        self.duration = 2
        self.freq = 44100

    def rec(self):

        time.sleep(1)
        recording = sd.rec(int(self.duration * self.freq), samplerate=self.freq, channels=2)
        sd.wait()  
        return recording
        

if __name__ == "__main__":

    enr = Record().rec()
    print(enr.shape)