import requests
import glob
import pandas as pd
import json 
import re


def main(C,CC,diag):
    def info(C,CC):
        """C : numero de documento 
            CC: tipo de documento"""
        header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
        link = f"http://190.131.222.108:8088/api/v1/macna/patient/{C}/type/{CC}/information"
        print(link)
        res = requests.get(url= link,headers=header,timeout=60)
        persona = json.loads(res.text)
        return persona
    leucemias = ['C910', 'C920', 'C924', 'C925', 'C930','C940', 'C942', 'C918', 'C926', 'C928', 'C933']
    if diag not in leucemias:
        try:
            Quimios = []
            persona = info(C,CC)
            data_med = pd.read_csv('atc_medicamentos.csv')
            medicamentos = list(data_med['codigo_atc'].unique())
            if persona["data"] != []:
                for data in persona["data"][0]["admissions"]:
                    Atencion = []
                    Medicamentos = []
                    if data["attentionType"] == "HOSPITAL_DIA":
                        inicio_fecha = data["admDate"][:10]
                        fin_fecha = data["outputDate"][:10]
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
                                            Medicamentos.append(codigo)
                        Medicamentos = list(set(Medicamentos))
                        if Medicamentos == []:
                            continue
                        Atencion.append(inicio_fecha)
                        Atencion.append(fin_fecha)  
                        Atencion.append(Medicamentos)
                        Quimios.append(Atencion)
            print(Quimios)
            cantidad_quimios = len(Quimios)
            if cantidad_quimios == 0:
                print("No tuvo quimios")
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
                __74 = "2"
                __75 = "1845-01-01"
                __76 = "1"
                __77 = "98"        
                __78 = "97"
                __79 = "1845-01-01" #hormo_fechas[-1]
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
                print("lectura de folios para ver si tuvo hormonoterapia")

            # SI TUVO PERO UNA SOLA QUIMIOTERAPIA
            if cantidad_quimios == 1:
                print("Solo tuvo 1 ciclo de quimios")
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
                __55 = cantidad_quimios
                __56 = " "
                __57 = Quimios[0][0]
                __58 = "1"
                __59 = "80010054401"
                __60 = "98"
                __61 = len(Quimios[0][-1])
                encontrados = list(Quimios[0][-1]).copy()
                for i in range(12):
                    encontrados.append('97')
                __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                __74 = "2"
                __75 = Quimios[0][1]
                __76 = "1"
                __77 = "98"        
                __78 = "97"
                __79 = "1845-01-01" #hormo_fechas[-1]
                __80 = '98' 
                __81 = '98'
                __82 = '98'
                __83 = '98'
                encontrados = []
                for i in range(12):
                    encontrados.append('97')
                __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                __96 = "98"
                __97 = "1845-01-01"
                __98 = "98"
                __99 = "98"

            # SI TUVO VARIAS QUIMIOS QUIMIOTERAPIA
            if cantidad_quimios > 1:
                print(f"Tuvo {cantidad_quimios} ciclos de quimios")
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
                __55 = cantidad_quimios
                __56 = " "
                __57 = Quimios[0][0]
                __58 = "1"
                __59 = "80010054401"
                __60 = "98"
                __61 = len(Quimios[0][-1])
                encontrados = list(Quimios[0][-1]).copy()
                for i in range(12):
                    encontrados.append('97')
                __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                __74 = "2"
                __75 = Quimios[0][1]
                __76 = "1"
                __77 = "98"        
                __78 = "97"
                __79 = Quimios[-1][0] #hormo_fechas[-1]
                __80 = '1' 
                __81 = '80010054401'
                __82 = '98'
                __83 = len(Quimios[-1][-1])
                encontrados = list(Quimios[-1][-1]).copy()
                for i in range(12):
                    encontrados.append('97')
                __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                __96 = " " #intratecal
                __97 = Quimios[-1][1]
                __98 = "1"
                __99 = "98"
            return __45,__46,__47,__48,__49,__50,__51,__52,__53,__54,__55,__56,__57,__58,__59,__60,__61,__62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73,__74,__75,__76,__77,__78,__79, __80, __81, __82, __83, __84, __85, __86, __87, __88, __89, __90, __91, __92, __93, __94, __95, __96, __97, __98, __99
        except Exception as e:
            print(e)
            print("No tuvo quimios")
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
            __78 = "97"
            __79 = "1845-01-01" #hormo_fechas[-1]
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
    else:
        print("El diagnostico es leucemia")
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
        __78 = "97"
        __79 = "1845-01-01" #hormo_fechas[-1]
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


        return __45,__46,__47,__48,__49,__50,__51,__52,__53,__54,__55,__56,__57,__58,__59,__60,__61,__62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73,__74,__75,__76,__77,__78,__79, __80, __81, __82, __83, __84, __85, __86, __87, __88, __89, __90, __91, __92, __93, __94, __95, __96, __97, __98, __99

    
if __name__ == '__main__':
    cedulas = ["8713010","28104919","30723970","72044663"]
    for c in cedulas:
        print("\n","--"*50)
        __45,__46,__47,__48,__49,__50,__51,__52,__53,__54,__55,__56,__57,__58,__59,__60,__61,__62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73,__74,__75,__76,__77,__78,__79, __80, __81, __82, __83, __84, __85, __86, __87, __88, __89, __90, __91, __92, __93, __94, __95, __96, __97, __98, __99 = main(c,"CC","C625")
        print(f""" 
PRIMER CICLO DE QUIMIOTERAPIA:
__45: {__45}
__46: {__46}
__47: {__47}
__48: {__48}
__49: {__49}
__50: {__50}
__51: {__51}
__52: {__52}
__53: {__53}
__54: {__54}
__55: {__55}
__56: {__56}
__57: {__57}
__58: {__58}
__59: {__59}
__60: {__60}
__61: {__61}
__62: {__62}
__63: {__63}
__64: {__64}
__65: {__65}
__66: {__66}
__67: {__67}
__68: {__68}
__69: {__69}
__70: {__70}
__71: {__71}
__72: {__72}
__73: {__73}
__74: {__74}
__75: {__75}
__76: {__76}
__77: {__77}
SEGUNDO CICLO DE QUIMIOTERAPIA:
__78: {__78}
__79: {__79}
 __80: {__80}
 __81: {__81}
 __82: {__82}
 __83: {__83}
 __84: {__84}
 __85: {__85}
 __86: {__86}
 __87: {__87}
 __88: {__88}
 __89: {__89}
 __90: {__90}
 __91: {__91}
 __92: {__92}
 __93: {__93}
 __94: {__94}
 __95: {__95}
 __96: {__96}
 __97: {__97}
 __98: {__98}
 __99: {__99}
        """)