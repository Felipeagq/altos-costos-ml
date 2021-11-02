import requests
import glob
import pandas as pd
import json 
import re
import peticion
from typing import Optional


def main(C:str, CC:str, folio:str) -> dict:
    def info(C,CC,folio):
        """C : numero de documento 
            CC: tipo de documento"""
        header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
        link = f"http://190.131.222.108:8088/api/v1/macna/get/patient/alto-cost-format/{C}/type/{CC}/folio/{folio}"
        print(link)
        res = requests.get(url= link,headers=header,timeout=60)
        persona = json.loads(res.text)
        return persona
    persona = info(C,CC,folio)

    if persona["msg"] == "Ok":
        persona = persona["data"][0]

        __18 = persona["FECHA_DX_CANCER"]
        __19 = persona["FECHA_REMISION"]
        __20 = persona["FECHA_INGRESO"]
        __21 = "N/A"
        __22 = "N/A"
        __23 = persona["FECHA_RECOLECCION_MUESTRA"]
        __24 = persona["FECHA_INFORME"]
        __25 = "Bonnadona"
        __26 = "PRIMERA_CONSULTA_MEDICO"
        __27 = "HISTOLOGIA_TUMOR"
        __28 = persona["GRADO_DIFERENCIACION"]
        __28 = re.findall("[0-9]+",__28)[0]
        __29 = persona["ESTADIFICACION"]
        __29 = re.findall("[0-9]+",__29)[0]
        __30 = persona["FECHA_PRUEBA"]
        __31 = "True / False"
        __32 = "FEHCA_HER2"
        __33 = persona["RESULTADO_HER_2"]
        __34 = persona["ESTADIO_DUKES"]
        __35 = "FECHA_DUKES"
        __36 = persona["ESTADIO_LINFOMA"]
        __37 = persona["ESCALA_GLEASON"]
        __38 = persona.get("RIESGO_LEUCEMIA","N/A")
        __39 = persona["FECHA_CLASIFICACION_RIESGO"]
        __40 = "N/A"
        __41 = "N/A"
        __42 = "N/A"
        __43 = "N/A"
        __44 = "N/A"

        print(persona)
    else:
        __18 = "N/A"
        __19 = "N/A"
        __20 = "N/A"
        __21 = "N/A"
        __22 = "N/A"
        __23 = "N/A"
        __24 = "N/A"
        __25 = "N/A"
        __26 = "N/A"
        __27 = "N/A"
        __28 = "N/A"
        __29 = "N/A"
        __30 = "N/A"
        __31 = "N/A"
        __32 = "N/A"
        __33 = "N/A"
        __34 = "N/A"
        __35 = "N/A"
        __36 = "N/A"
        __37 = "N/A"
        __38 = "N/A"
        __39 = "N/A"
        __40 = "N/A"
        __41 = "N/A"
        __42 = "N/A"
        __43 = "N/A"
        __44 = "N/A"


    return __18,__19,__20,__21,__22,__23,__24,__25,__26,__27,__28,__29,__30,__31,__32,__33,__34,__35,__36,__37,__38,__39,__40,__41,__42,__43,__44


if __name__ == "__main__":
    C = "1049532810"
    CC = "CC"
    folio = 1
    __18,__19,__20,__21,__22,__23,__24,__25,__26,__27,__28,__29,__30,__31,__32,__33,__34,__35,__36,__37,__38,__39,__40,__41,__42,__43,__44 = main(C,CC,folio)
    print(f"""
    __18 = {__18}
    __19 = {__19}
    __20 = {__20}
    __21 = {__21}
    __22 = {__22}
    __23 = {__23}
    __24 = {__24}
    __25 = {__25}
    __26 = {__26}
    __27 = {__27}
    __28 = {__28}
    __29 = {__29}
    __30 = {__30}
    __31 = {__31}
    __32 = {__32}
    __33 = {__33}
    __34 = {__34}
    __35 = {__35}
    __36 = {__36}
    __37 = {__37}
    __38 = {__38}
    __39 = {__39}
    __40 = {__40}
    __41 = {__41}
    __42 = {__42}
    __43 = {__43}
    __44 = {__44}
    """)

    