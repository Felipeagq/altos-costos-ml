###################################### 
### RESULTADO FINAL DE LA ATENCIÓN ###
######################################
import requests
import json
import re

def findKeyWord(text,keyWord,n):
    wordlist = text.split()
    here = []
    for i in range(len(wordlist)):
        if wordlist[i] == keyWord:
            if i > n:
                nGram = wordlist[i-n:i+n+1]
            elif i+n > len(wordlist):
                nGram = wordlist[i-n:]
            elif ((2*n)+1)>len(wordlist):
                nGram = wordlist[:]
            else:
                nGram = wordlist[:i+n]
            here.append(nGram)
    return here


def _157__166(folios,dic,__45,__100,__112,__6,__5,__59,__72,__95,__104):
    abandono = False
    print("entrando a resultado final")
    __157 = "98"
    print(__157)
    header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
    res = requests.get(f"http://190.131.222.108:8088/api/v1/macna/patient/{__6}/type/{__5}/information",headers=header)
    persona = json.loads(res.text)

    paciente = persona["data"][0]

    if paciente["deathState"] == 1:
        print("persona encontrada muerta")
        __159 = "2"
        __163 = paciente["deathDate"][:10]
        print("variables",__159,__163)
    else:
        print("entro al else")
        __159 = "1"
        __163 = "1845-01-01"

    # Datos hasta el momento
    print("__159",__159)
    print("__45",__45)
    print("__100",__100)
    print("__112",__112)
    print(__157)

    if __159 == "2": # paciente fallecido    
        print("paciente fallecido")
        __157 = '98'
        __158 = '99'
        __160 = '4'
        __161 = '12' 
        __164 = '1' 
    else: # si se encuentra vivo

        __158 = '5' # A EVALUAR
        if "paciente abandon" in folios[-1]:
            abandono = True
            __158 = '6'
            __160 = '9' 
            __161 = '8'
        else:
            __160 = '0' 
            __161 = '1' 
        __163 = '1845-01-01' 
        __164 = '98'        
        
    # if "paciente abandon" in folios[-1]: # ALTA VOLUNTRIA
    #     abandono = True
    #     __158 = '6'
    #     __160 = '7'
    #     __161 = '9'
    __165 = '98'
    __162 = '1845-01-01'
    __166 = '2021-01-01' # encontrar alguna forma de cambiar la fecha de corte ¿cada cuanto es la fecha de corte? 

    # Comienzo a examinar la variable 157
    if  (int(__45)==1) and (int(__100)!=1) and (int(__112)!=1):
        __157 = '2'
        __41 = '2'
        __161 = "1"

    elif (int(__45)!=1) and (int(__100)==1) and (int(__112)!=1):
        __157 = '3'
        __41 = '2'
        __161 = "1"

    elif (int(__45)!=1) and (int(__100)!=1) and (int(__112)==1):
        __157 = '1'
        __41 = '2'
        __161 = "1"    

    elif (int(__45)==1) and (int(__100)==1) and (int(__112)!=1):
        __157 = '6' # aqui iba 5
        __41 = '2'
        __161 = "1"

    elif (int(__45)==1) and (int(__100)!=1) and (int(__112)==1):
        __157 = '4'
        __41 = '2'
        __161 = "1"

    elif (int(__45)!=1) and (int(__100)==1) and (int(__112)==1):
        __157 = '5'
        __41 = '2'
        __161 = "1"
    
    elif (int(__45)==1) and (int(__100)==1) and (int(__112)==1):
        __157 = '10'
        __41 = '2'
        __161 = "1"

    else:
        __157 = '9'
        __161 = '3'
        __41 = '3'

    if __159 == "2": # paciente fallecido
        __157 = '98'
    
    if __160 == "9":
        __161 = "8"
    
    if __160 == "7":
        __161 = "9"

    if __157 == "9":
        __161 = "3"

    if __159 == "1":
        if abandono == False:
            manejos_oncologicos = (__59,__72,__95,__104)
            print(list(set(manejos_oncologicos)))
            if "2" in manejos_oncologicos:
                __158 = "97"
            else:
                __158 = "5"

            if "3" in manejos_oncologicos:
                __158 = "97"
            else:
                __158 = "5"
            if list(set(manejos_oncologicos))[0]=='98' and len(list(set(manejos_oncologicos))[0])==1:
                print(set(manejos_oncologicos))
                __158 = "7"
        else:
            __158 ="6"

    
    return __157,__158,__159,__160,__161,__162,__163,__164,__165,__166,__41