import requests
import json 

def info(C,CC):
    """C : numero de documento 
        CC: tipo de documento"""
    header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
    link = f"http://190.131.222.108:8088/api/v1/macna/patient/{C}/type/{CC}/information"
    print(link)
    res = requests.get(url= link,headers=header,timeout=10)
    persona = json.loads(res.text)
    return persona


c1 = '32840720'
c2 = 'CC'
persona = info(c1,c2)
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
        #if int(fin[:4])>=2021:
        if True:
            fechas.append([inicio,fin])
            med2 = []
            for order in data["folios"]:
                #print(order["admConsecutive"])
                if order["ordering"] != []:
                    for orden in order["ordering"]:
                        #print(orden["sumACTCod"])
                        for medicamento in medicamentos:
                            if medicamento in orden["sumACTCod"]:
                                if medicamento == "H02AB02":
                                    continue
                                codigo = data_med[data_med['codigo_atc']==medicamento]['codigo_atc'].values[0]
                                med2.append(codigo)
            med.append(set(med2))

                #print("se encontro orden")
            #print(order["ordering"])
print(fechas)
print(fechas[0][0])
print(med)
print(len(med[0]))