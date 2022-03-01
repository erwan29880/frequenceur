import frequence
import record

def main():

    enr = record.Record().rec()
    fr = frequence.Frequence(enr).freq()
  

    print(fr)

main()

