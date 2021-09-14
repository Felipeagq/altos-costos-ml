import requests
import glob
import json 
import re

def info(C,CC):
    """C : numero de documento 
        CC: tipo de documento"""
    header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
    link = f"http://190.131.222.108:8088/api/v1/macna/patient/{C}/type/{CC}/information"
    print(link)
    res = requests.get(url= link,headers=header,timeout=10
    )
    persona = json.loads(res.text)
    return persona

personas = glob.glob("*CC *.txt")

personas2 = [re.findall(r'\d+',i)[0] for i in personas]

for persona in personas2:
    try:
        print(" ")
        sujeto = info(persona,"CC")
        for admisiones in sujeto["data"][0]["admissions"]:
            for ad in admisiones["folios"]:
                for prod in ad["procedures"]:
                        print(prod)
    except Exception as e:
        print(e,"PRI PRA EXPLOTOOOO")

