import requests
import json
import re

############################
### QUIMIOTERAPIA 45 -77 ###
############################
def _45__77_(folios,diag,C,CC):
    import numpy as np
    print("- - - - -Quimioterapia- - - - -")
    # identifico todos los folios donde sale la palabra clave 
    leucemias = ['C910', 'C920', 'C924', 'C925', 'C930','C940', 'C942', 'C918', 'C926', 'C928', 'C933']
    if diag not in leucemias:
        try:
            def info(C,CC):
                """C : numero de documento 
                    CC: tipo de documento"""
                header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
                link = f"http://190.131.222.108:8088/api/v1/macna/patient/{C}/type/{CC}/information"
                print(link)
                res = requests.get(url= link,headers=header,timeout=15)
                persona = json.loads(res.text)
                return persona
            c1 = '55312587'
            c2 = 'CC'
            persona = info(C,CC)
            import pandas as pd
            fechas = []
            data_med = pd.read_csv('atc_medicamentos.csv')
            #data['codigo_atc'] = data['codigo_atc'].apply(lambda x: x.lower())
            medicamentos = list(data_med['codigo_atc'].unique())
            med = []
            for data in persona["data"][0]["admissions"]:
                if data["attentionType"] == "HOSPITAL_DIA":
                    inicio = data["admDate"][:10]
                    fin = data["outputDate"][:10]
                    if int(fin[:4])>=2021:
                        print(fin[:4])
                        print("tuvo fin en el 2021")
                    #if True:
                        fechas.append([inicio,fin])
                        med2 = []
                        for order in data["folios"]:
                            #print(order["admConsecutive"])
                            if order["ordering"] != []:
                                for orden in order["ordering"]:
                                    #print(orden["sumDesc"])
                                    for medicamento in medicamentos:
                                        if medicamento in orden["sumACTCod"]:
                                            if medicamento == "H02AB02":
                                                continue
                                            codigo = medicamento
                                            med2.append(codigo)
                        med.append(list(set(med2)))
            med2 = []
            fechas2 = []
            for m in range(len(med)):
                if med[m] != []:
                    med2.append(med[m])
                    fechas2.append(fechas[m])
            print("med2",med2)
            print(" ")
            print("fechas2",fechas2)
            print(" ")
            if len(med2)>0: # si si tiene quimio
                print("entró al if de medicamentos")
                quimio = True
                __45 = "1"
                __46 = "98"
                __47 = '97' 
                __48 = '97'
                __49 = '97'
                __50 = '97'
                __51 = '97'
                __52 = '97'
                __53 = '97'
                __54 = '97'
                __55 = len(fechas)
                __56 = " "
                __57 = fechas[0][0]
                __58 = "1"
                __59 = "80010054401"
                __60 = "98"
                __61 = len(med[0])
                encontrados = list(med[0]).copy()
                for i in range(12):
                    encontrados.append('97')
                __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                __74 = "2"
                __75 = fechas[0][1]
                __76 = "1"
                __77 = "98"
                terminado = True
                print("termino si tuvo")
                if len(med2)>1:
                    print("tuvo más de una quimioterapia")
                    __79 = fechas[-1][0]
                    __80 = "1"
                    __81 = "80010054401"
                    __82 = "98"
                    __83 = len(med2[-1])
                    med_q2 = list(med2[-1]).copy()
                    for i in range(12):
                        med_q2.append('97')
                    __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                    __96 = "2"
                    __97 = fechas[-1][1]
                    __98 = "1"
                    __99 = "98"
                    print(f"fechas de la segunda quimio {__79} / {__97}")
                else:
                    __78 = " "
                    __79 = "97"
                    __80 = '97' 
                    __81 = '97'
                    __82 = '97'
                    __83 = '97'
                    encontrados = []
                    for i in range(12):
                        encontrados.append('97')
                    __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                    __96 = "98"
                    __97 = "1845-01-01"
                    __98 = "98"
                    __99 = "98"
            else: # si no tiene quimio por tratamiento especial
                print("entro a hormonoterapia")
                hormonoterapia = pd.read_csv("hormonoterapia.csv")
                hormo_fechas = []
                patron_fecha = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
                hormo_med = hormonoterapia["DESCRIPCIÓN_ATC"].values
                med_encontrados = []
                med_encontrados2 = []
                print("medicamentos hromonoterapia")
                for folio in folios:
                    folio_actual = folio.replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," ")
                    for med_hormo in hormo_med:
                        if med_hormo in folio:
                            a_agregar = hormonoterapia[hormonoterapia["DESCRIPCIÓN_ATC"]==med_hormo]["CODIGO_ATC"].values

                            med_encontrados.append(a_agregar[0])
                            fechas = re.findall(patron_fecha,folio_actual)
                            print("fechas:",fechas)
                            fecha = fechas[0]
                            print("fecha:",fecha)
                            fecha_as_list = fecha.split("/")[::-1]
                            print(fecha_as_list)
                            print('-'.join(fecha_as_list))
                            try:
                            #print("fecha de hormonoterapia",fecha)
                                hormo_fechas.append('-'.join(fecha_as_list))
                                print("agregado")
                            except:
                                continue
                            #print("fechas",hormo_fechas)
                print((med_encontrados))
                print(list(med_encontrados))
                aaa = np.array(med_encontrados)
                print(aaa)    
                print("LLEGÓ HASTA AQUI")
                med_encontrados2.append(list(set(med_encontrados)))
                print(med_encontrados2)
                print("hormo_fechas:",hormo_fechas)
                b = [i for i in hormo_fechas if i != []]
                c = [j for j in med_encontrados2 if j != []]
                print(hormo_fechas)
                print("hormo fechas en lista",list(hormo_fechas))
                print("b",b)
                if  len(c)>0:
                    print("El paciente tuvo hormonoterapia")
                    __45 = "1"
                    __46 = "98"
                    __47 = '97' 
                    __48 = '97'
                    __49 = '97'
                    __50 = '97'
                    __51 = '97'
                    __52 = '97'
                    __53 = '97'
                    __54 = '97'
                    __55 = "1"
                    __56 = " "
                    __57 = hormo_fechas[0]
                    __58 = "1"
                    __59 = "80010054401"
                    __60 = "98"
                    __61 = len(list(med_encontrados2[0]))
                    encontrados = list(med_encontrados2[0]).copy()
                    for i in range(12):
                        encontrados.append('97')
                    __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]                
                    __74 = "2"
                    __75 = "1800-01-01"
                    __76 = "3"
                    __77 = "98"
                    if len(hormo_fechas)>1:
                        __78 = "97"
                        __79 = "1845-01-01" #hormo_fechas[-1]
                        __80 = '98' 
                        __81 = '98'
                        __82 = '98'
                        __83 = '98'
                        encontrados = list(med_encontrados2[-1]).copy()
                        for i in range(12):
                            encontrados.append('97')
                        __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                        __96 = "98"
                        __97 = "1845-01-01"
                        __98 = "98"
                        __99 = "98"           
                        print("TUVO HORMONOTERAPIA")
                    else:
                        __78 = " "
                        __79 = "1845-01-01"
                        __80 = '98' 
                        __81 = '98'
                        __82 = '98'
                        __83 = '98'
                        encontrados = []
                        for i in range(12):
                            encontrados.append('98')
                        __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                        __96 = "98"
                        __97 = "1845-01-01"
                        __98 = "98"
                        __99 = "98"           
                        print("TUVO HORMONOTERAPIA")
                else:
                    __45 = "98"
                    __46 = "98"
                    __47 = '97' 
                    __48 = '97'
                    __49 = '97'
                    __50 = '97'
                    __51 = '97'
                    __52 = '97'
                    __53 = '97'
                    __54 = '97'
                    __55 = "98"
                    __56 = "98"
                    __57 = "1845-01-01"
                    __58 = "98"
                    __59 = "98"
                    __60 = "98"
                    __61 = "98"
                    encontrados = []
                    for i in range(12):
                        encontrados.append('98')
                    __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                    __74 = "98"
                    __75 = "1845-01-01"
                    __76 = "98"
                    __77 = "98" 
                    __78 = "98"
                    __79 = "1845-01-01"
                    __80 = '98' 
                    __81 = '98'
                    __82 = '98'
                    __83 = '98'
                    encontrados = []
                    for i in range(12):
                        encontrados.append('98')
                    __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                    __96 = "98"
                    __97 = "1845-01-01"
                    __98 = "98"
                    __99 = "98"                        
                    print("TERMINO PERO NO TUVO QUIMIOTERAPIA")
        except Exception as e:
            print(e)
            print("entro al except DE QUIMIOTERAPIA")
            __45 = "0"
            __46 = "N/A"
            __47 = 'N/A' 
            __48 = 'N/A'
            __49 = 'N/A'
            __50 = 'N/A'
            __51 = 'N/A'
            __52 = 'N/A'
            __53 = 'N/A'
            __54 = 'N/A'
            __55 = "N/A"
            __56 = "N/A"
            __57 = "N/A"
            __58 = "N/A"
            __59 = "N/A"
            __60 = "N/A"
            __61 = "N/A"
            encontrados = []
            for i in range(12):
                encontrados.append('98')
            __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
            __74 = "N/A"
            __75 = "N/A"
            __76 = "N/A"
            __77 = "N/A"
            __79 = "N/A"
            __80 = 'N/A' 
            __81 = 'N/A'
            __82 = 'N/A'
            __83 = 'N/A'
            encontrados = []
            for i in range(12):
                encontrados.append('98')
            __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
            __96 = "N/A"
            __97 = "1845-01-01"
            __98 = "N/A"
            __99 = "N/A"                
    else:
        __45 = "98"
        __46 = "98"
        __47 = '98' 
        __48 = '98'
        __49 = '98'
        __50 = '98'
        __51 = '98'
        __52 = '98'
        __53 = '98'
        __54 = '98'
        __55 = "98"
        __56 = " "
        __57 = "1845-01-01"
        __58 = "98"
        __59 = "98"
        __60 = "98"
        __61 = "98"
        encontrados = []
        for i in range(12):
            encontrados.append('98')
        __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
        __74 = "98"
        __75 = "1845-01-01"
        __76 = "98"
        __77 = "98"
        __78 = " "
        __79 = "1845-01-01"
        __80 = '98' 
        __81 = '98'
        __82 = '98'
        __83 = '98'
        encontrados = []
        for i in range(12):
            encontrados.append('98')
        __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
        __96 = "98"
        __97 = "1845-01-01"
        __98 = "98"
        __99 = "98"
    __56 = " "            
    return __45,__46,__47,__48,__49,__50,__51,__52,__53,__54,__55,__56,__57,__58,__59,__60,__61,__62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73,__74,__75,__76,__79, __80, __81, __82, __83, __84, __85, __86, __87, __88, __89, __90, __91, __92, __93, __94, __95, __96, __97, __98, __99



if __name__ == '__main__':
    print("ejecutandose como principal")