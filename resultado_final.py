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


def _157__166(folios,dic,__45,__100,__112,__6,__5,__140):
    print("entrando a resultado final")
    __157 = "98"
    print(__157)
    try:
        print("Entró en el try")
        header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
        res = requests.get(f"http://190.131.222.108:8088/api/v1/macna/patient/{__6}/type/{__5}/information",headers=header)
        persona = json.loads(res.text)
        if persona["data"] is not None:
            for n in persona["data"]:
                if n["deceased"] == 1:
                    print("persona encontrada muerta")
                    __159 = "2"
                    __163 = n["deathDate"][:10]
                    print("variables",__159,__163)
                    break
                else:
                    print("entro al else")
                    __159 = "1"
                    __163 = "1845-01-01"
        else:
            raise Exception
    except:
        print("Comenzóel except")
        dic['159'].clear()
        lista_agregar = ['pcte fallecio','se declara muerte clinica','paciente fallecido','declara fallecido','se entrega acta de defuncion','declara paciente fallecida','declara fallecido','declara fallecida', 'sin signos vitales','declarada paciente fallecida','declarado paciente fallecido', 'acta defuncion','sala de paz','sala de reposo','morgue','anuncian defuncion','anunciar muerte','certificado defuncion']
        [dic['159'].update({key:'2'}) for key in lista_agregar]
        patron_fecha = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
        print("Antes del for")
        for key in dic['159'].keys():
            folios[-1] = folios[-1].replace('\n',' ')
            here = findKeyWord(folios[-1],key,5)
            
            if key in folios[-1].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "):
                print("encontrado muerto -1")
                __159 = '2'
                fechas = re.findall(patron_fecha,folios[-1].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "))
                fecha = fechas[0]
                __163 = '-'.join(fecha.split("/")[::-1])
                break

            elif key in folios[-2].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "):
                print("encontrado muerto -2")
                __159 = '2'
                fechas = re.findall(patron_fecha,folios[-2].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "))
                fecha = fechas[0]
                __163 = '-'.join(fecha.split("/")[::-1])                
                break
            
            

            elif key in folios[-3].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "):
                print("encontrado muerto -3")
                __159 = '2'
                fechas = re.findall(patron_fecha,folios[-3].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "))
                fecha = fechas[0]
                __163 = '-'.join(fecha.split("/")[::-1])                
                break            
            else:
                __159 = '1'
    print("salio del try except")
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

        __164 = '1' # buscar en el texto y pregunta si hay area especifica. KWIC
    else: # si se encuentra vivo

        __158 = '5' # A EVALUAR
        if "paciente abandon" in folios[-1]:
            __158 = '6'
        #45  = quimio
        #100 = cirugia
        #112 = radio
        __160 = '9' # inferir
        __161 = '1' #inferir
        __163 = '1845-01-01' # ¿como evaluar persona con aseguramiento?     
        __164 = '98'        
        
    if "paciente abandon" in folios[-1]:
        __158 = '6'
        __161 = '8'
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
        __41 = '3'

    if __159 == "2": # paciente fallecido
        __157 = '98'
    
    if __160 == "9":
        __161 = "8"
    
    if __160 == "7":
        __161 = "9"

    if __157 == "9":
        __161 = "3"
                

    
    return __157,__158,__159,__160,__161,__162,__163,__164,__165,__166,__41