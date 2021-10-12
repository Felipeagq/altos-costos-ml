import requests
import glob
import pandas as pd
import json 
import re


def main(C,CC):
    def info(C,CC):
        """C : numero de documento 
            CC: tipo de documento"""
        header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
        link = f"http://190.131.222.108:8088/api/v1/macna/patient/{C}/type/{CC}/information"
        print(link)
        res = requests.get(url= link,headers=header,timeout=60)
        persona = json.loads(res.text)
        return persona

    cirugias_codes = pd.read_csv("cirugia.csv")

    cirugia_1 = cirugias_codes[cirugias_codes["importancia"]==1]["codigo"].values
    cirugia_1 = list(cirugia_1)

    cirugia_2 = cirugias_codes[cirugias_codes["importancia"]==2]["codigo"].values
    cirugia_2 = list(cirugia_2)


    cirugia_3 = cirugias_codes[cirugias_codes["importancia"]==3]["codigo"].values
    cirugia_3 = list(cirugia_3)



    paciente = info(C,CC)
    admisiones = paciente["data"][0]["admissions"]

    cirugias_paciente = []

    for entrada in admisiones:
        for procedimientos in entrada["folios"]:
            for cirugias in procedimientos["procedures"]:
                fecha = cirugias["procDate"]
                if int(fecha[:4])>2020:
                #if True:
                    for cirugia in cirugias["surgeries"]:
                        print(cirugia)
                        codigo = int(cirugia["surgeryCode"])
                        if codigo in cirugia_1:
                            cirugias_paciente.append([fecha,codigo,1])
                            break

                        if codigo in cirugia_2:
                            cirugias_paciente.append([fecha,codigo,2])
                            break

                        if codigo in cirugia_3:
                            cirugias_paciente.append([fecha,codigo,3])
                            break                               

    print(cirugias_paciente)

    if len(cirugias_paciente)>0:
        __100 = "1"
        __101 = str(len(cirugias_paciente))
        __102 = str(cirugias_paciente[0][0])
        __103 = "80010054401"
        __104 = str(cirugias_paciente[0][1])
        __105 = "1"
        if len(cirugias_paciente)>1:
            __106 = str(cirugias_paciente[-1][0])
            __107 = "1"
            __108 = "80010054401"
            __109 = str(cirugias_paciente[-1][1])
            __110 = "98"
            __111 = "1"        
        else:
            __106 = "98"
            __107 = "98"
            __108 = "98"
            __109 = "98"
            __110 = "98"
            __111 = "1"
    else:
        __100 = "2"
        __101 = "98"
        __102 = "1845-01-01"
        __103 = "98"
        __104 = "98"
        __105 = "98"
        __106 = "1845-01-01"
        __107 = "98"
        __108 = "98"
        __109 = "98"
        __110 = "98"
        __111 = "98"      


    print(f"""
        __100 = {__100}
        __101 = {__101}
        __102 = {__102}
        __103 = {__103}
        __104 = {__104}
        __105 = {__105}
        __106 = {__106}
        __107 = {__107}
        __108 = {__108}
        __109 = {__109}
        __110 = {__110}
        __111 = {__111}      
    """)

    return __100,__101,__102,__103,__104,__105,__106,__107,__108,__109,__110,__111

if __name__ == '__main__':
    main("22898972","CC")