import requests
import json 

def info(C,CC):
    """C : numero de documento 
        CC: tipo de documento"""
    header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
    link = f"http://190.131.222.108:8088/api/v1/macna/patient/{C}/type/{CC}/information"
    print(link)
    print("_______________________________-")
    res = requests.get(url= link,headers=header,timeout=5)
    persona = json.loads(res.text)
    return persona


c1 = '32836987'
c2 = 'CC'
info(c1,c2)