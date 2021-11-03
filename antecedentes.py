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
        
        res = requests.get(url= link,headers=header,timeout=60)
        persona = json.loads(res.text)
        return persona
    persona = info(C,CC,folio)

    if persona["msg"] == "Ok":
        persona = persona["data"][0]

        ## ESTADIFICACION ##
        __18 = persona["FECHA_INFORME"]
        if __18 == None:
            __18 = "1800-01-01"

        __19 = persona["FECHA_REMISION"]
        if __19 == None:
            __19 = "1800-01-01"

        __20 = persona["FECHA_INGRESO"]
        if __20 == None:
            __20 = "1800-01-01"

        # NO entregadas
        __21 = "10"
        __22 = " "

        __23 = persona["FECHA_RECOLECCION_MUESTRA"]
        if __23 == None:
            __23 = "1800-01-01"

        __24 = persona["FECHA_INFORME"]
        if __24 == None:
            __24 = "1800-01-01"

        if __20 != None:
            __25 = "80010054401"
        else:
            __25 = "99"
    
        # No entregado
        __26 = " "
        __27 = " "


        __28 = persona["GRADO_DIFERENCIACION"]
        try:
            __28 = re.findall("[0-9]+",__28)[0]
        except:
            print(__28)
            __28 = "99"
        #if __28 == None:
           


        estadificacion = {
        'ec 0 (tumor in situ)' : "0",
        'ec IIA o 2a' : "11",
        'ec IIB': "14",
        'ec IIIA o 3a': "17",
        'ec IIIB o 3b': "18",
        'ec IIIC o 3c': "19",
        'ec IV o 4': "20",
        'ec III o 3': "16",
        'ec IIC o 2c': "15",
        'ec IVA o 4a': "21",
        'ec IVB o 4b': "22",
        'ec IA1': "3",
        'ec IA2': " 4",
        'ec IAB': "26",
        'ec IIID o 3d': "29",
        'ec I o 1': "1",
        'ec II o 2': "10",
        'ec IA1': "3",
        'ec IA2': "4",
        'ec IB1': "6",
        'ec IB2': "7",
        'ec IIA1': "12",
        'ec IIA2': "13",
        'ec IVA o 4a': "21",
        'ec IVB o 4b': "22",
        'ec IIIC1 o 3c1': "27",
        'ec IIIC2 o 3c2': "28",
        'ec IB3': "30",
        'ec IC1': "31",
        'ec IC2': "32",
        'ec IC3': "33",
        'ec IC o 1c': "8",
        'ec IS o 1s': "9",
        'ec IVC o 4c': "23",
        'ec 4S(para neuroblastoma)': "24",
        'ec V o 5': "25",
        'No Aplica' : "98"
        }
        estadio = persona["ESTADIFICACION"]
        estadio_code = estadificacion.get(estadio,"98")
        __29 = estadio_code

        __30 = persona["FECHA_PRUEBA"]
        if __30 == None:
            __30 = " "


        ## CANCER MAMA ##
        her_2 = {
            'Positivo' : "1",
            'Negativo': "3",
            'Equivoco o indeterminado': "2",
            'Cero o negativo': "4",
        }
        her = persona["RESULTADO_HER_2"]
        codigo_her = her_2.get(her,"98")
        if codigo_her == "98":
            __33 = "98"
            __31 = "1"
            __32 = " "
        else:
            __33 = "98"
            __32 = "1845-01-01"
            __31 = "98"

        ## CANCER COLORECTAL ##
        estadios_dukes = {
            "A":"1",
            "B":"2",
            "C":"3",
            "D":"4"
        }
        estadio_d = persona["ESTADIO_DUKES"]
        __34 = estadios_dukes.get(estadio_d,"98")
        if __34 == "98":
            __35 = "1845-01-01"
        else:
            __35 = persona["FECHA_PRUEBA"]




        ## HODGKIN ##
        estadios_hodgkin = {
        'Estadio I': "1", 
        'Estadio II': "2",
        'Estadio III': "3",
        'Estadio IV': "4",
        'Estadio IA': "5",
        'Estadio IB': "6",
        'Estadio IIA': "7",
        'Estadio IIB': "8",
        'Estadio IIIA': "9",
        'Estadio IIIB': "10",
        'Estadio IVA' : "11",
        'Estadio IVB' : "12",
        'Extranodal cualquier estadio': "13",
        'Primario SNC' : "14",
        'Primario Mediastinal': "15",
        'Primario de otros organos': "16", 
        }
        estadio_h = persona["ESTADIO_LINFOMA"]
        __36 = estadios_hodgkin.get(estadio_h,"98")

        ## LINFOMA ##
        gleason = persona["ESCALA_GLEASON"]
        print(gleason)
        if gleason != None:
            estadio_gleason = re.findall(r"[0-9]+",gleason)
            if estadio_gleason == []:
                __37 = "98"
            else:
                codigo_gleason = estadio_gleason[0]
                if codigo_gleason == '6':
                    __37 = "11"
                if "3+4" in codigo_gleason:
                    __37 = "12"
                if "4+3" in codigo_gleason:
                    __37 = "13"
                if codigo_gleason == '8':
                    __37 = "14"
                if codigo_gleason == '9':
                    __37 = "15"
                else:
                    __37 = "98"
        else:
            __37 = "98"


        riesgos_leucemia = {
            'Bajo riesgo':"1",
            'Riesgo intemedio bajo':"1",
            'Intermedio':"3",
            'Riesgo intemedio alto':"5",
            'Riesgo alto':"5",
        }
        riesgo = persona["RIESGO_LEUCEMIA"]
        ## LEUCEMIA - LINFOMA ##
        __38 = persona.get(riesgo,"98")
        __39 = persona["FECHA_CLASIFICACION_RIESGO"]
        if __39 == None:
            __39 = "1845-01-01"

        ## ANTECEDENTES ##
        __40 = " "
        __41 = " "
        __42 = "2"
        __43 = "1845-01-01"
        __44 = "99"


    else:
        __18 = " "
        __19 = " "
        __20 = " "
        __21 = " "
        __22 = " "
        __23 = " "
        __24 = " "
        __25 = " "
        __26 = " "
        __27 = " "
        __28 = " "
        __29 = " "
        __30 = " "
        __31 = " "
        __32 = " "
        __33 = " "
        __34 = " "
        __35 = " "
        __36 = " "
        __37 = " "
        __38 = " "
        __39 = " "
        __40 = " "
        __41 = " "
        __42 = " "
        __43 = " "
        __44 = " "


    return __18,__19,__20,__21,__22,__23,__24,__25,__26,__27,__28,__29,__30,__31,__32,__33,__34,__35,__36,__37,__38,__39,__40,__41,__42,__43,__44


if __name__ == "__main__":
    C = "1049532810"
    C = "1048277134"
    CC = "CC"
    folio = 16
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

    