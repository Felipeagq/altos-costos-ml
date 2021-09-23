__1 = None
__2 = None
__3 = None
__4 = None
__5 = None
__6 = None
__7 = None
__8 = None
__9 = None
__10 = None
__11 = None
__12 = '6'
__13 = None
__14 = None
__15 = None
__16 = '1800-01-01' # PREDETERMINADA
__17 = None
__18 = None
__19 = ' '
__20 = ' '
__21 = ' '
__22 = ' ' # PREDETERMINADA
__23 = " "
__24 = " "
__25 = ' ' # 80010054401
__26 = " "
__27 = " "
__28 = " "
__29 = ' '
__30 = ' '
# MAMA
__31 = '98'
__32 = '1845-01-01'
__33 = '98'
__34 = '98'
__35 = '1845-01-01'
__36 = '98'
__37 = '98'
__38 = '98'
__39 = '1845-01-01'
__40 = '1'
__41 = '3'
__42 = '2'
__43 = '1845-01-01'
__44 = '99'
__45 = '98'
__46 = '98'
__47 = '97'
__48 = '97'
__49 = '97'
__50 = '97'
__51 = '97'
__52 = '97'
__53 = '97'
__54 = '97'
__55 = '98'
__56 = ' '
__57 = '1845-01-01'
__58 = '98'
__59 = '98'
__60 = '98'
__61 = '98'
__62 = '98'
__63 = '98'
__64 = '98'
__65 = '98'
__66 = '98'
__67 = '98'
__68 = '98'
__69 = '98'
__70 = '98'
__71 = '98'
__72 = '98'
__73 = '98'
__74 = '98'
__75 = '1845-01-01'
__76 = '98'
__77 = '98'
#__78 = '98'
__78 = " "
__79 = '1845-01-01'
__80 = '98'
__81 = '98'
__82 = '98'
__83 = '98'
__84 = '98'
__85 = '98'
__86 = '98'
__87 = '98'
__88 = '98'
__89 = '98'
__90 = '98'
__91 = '98'
__92 = '98'
__93 = '98'
__94 = '98'
__95 = '98'
__96 = '98'
__97 = '1845-01-01'
__98 = '98'
__99 = '98'
__100 = "98"
__101 = '98'
__102 = '1845-01-01'
__103 = '98'
__104 = '98'
__105 = '98'
#__105 = " "
__106 = '1845-01-01'
__107 = '98'
__108 = '98'
__109 = '98'
__110 = ' '
__111 = '98'
__112 = '98'
__113 = '98'
__114 = '1845-01-01'
__115 = ' '
__116 = '98'
__117 = '98'
__118 = '98'
__119 = '98'
__120 = '1845-01-01'
__121 = '98'
__122 = '98'
__123 = '1845-01-01'
__124 = ' '
__125 = '98'
__126 = '98'
__127 = '98'
__128 = '98'
__129 = '1845-01-01'
__130 = '98'
__131 = '98'
__132 = '98'    # PREDETERMINADA
__133 = '98'    # PREDETERMINADA
__134 = '98'    # PREDETERMINADA
__135 = '1845-01-01'    # PREDETERMINADA
__136 = '98'    # PREDETERMINADA
__137 = '98'    # PREDETERMINADA
__138 = '1845-01-01'    # PREDETERMINADA
__139 = '98'    # PREDETERMINADA
__140 = '2'
__141 = '2'
__142 = '2'
__143 = '2'
__144 = '2'
__145 = '2'
__146 = ' '
__147 = '1845-01-01'
__148 = '98'
__149 = '98'    # PREDETERMINADA
__150 = '1845-01-01'    # PREDETERMINADA
__151 = '98'    # PREDETERMINADA
__152 = '98'
__153 = '1845-01-01'
__154 = '98'
__155 = '4'
__156 = '98' # PREDETERMINADA
__157 = '9'
__158 = '5'
__159 = '1'
__160 = '0'
__161 = '1'
__162 = '1845-01-01'    # PREDETERMINADA
__163 = '1845-01-01'
__164 = '98'
__165= '98' # PREDETERMINADA
__166 = '2021-01-01'

import time 
from pdf_to_txt1 import pdf_to_txt
import glob
import os
import requests
import json
import pandas as pd
from openpyxl import Workbook
import re
from openpyxl import load_workbook
#import nltk
#import cac_data_4
def main(Paciente,row,Fcorte,Eps):
    #Convertimos el pdf en texto
    #pdf_to_txt_3.pdf_to_csv('CC 40925684 - HC')

    # Cargamos el diccionario
    file = open("dic_1.json",)
    dic = json.load(file)

    ####################################
    ### DECLARAMOS ALGUNAS FUNCIONES ###
    ####################################

    # Funcion para quitar los acentos 
    def mayusculas_sec_clave(s):
        ''' Funcion para volver mayusculas las secciones clave'''
        replacements =(
            ('motivo de consulta','MOTIVO DE CONSULTA'),
            ('enfermedad actual','ENFERMEDAD ACTUAL'),
            ('examen fisico','EXAMEN FÍSICO'),
            ('analisis','ANÁLISIS'),
            ('evolucion medico','EVOLUCION MEDICO'),
            ('antecedentes','ANTECEDENTES'),
            ('plan y manejo','PLAN Y MANEJO'),
            ('diagnostico','DIAGNÓSTICO'),
            ('diagnóstico','DIAGNÓSTICO'),
            ('ordenes','ORDENES'),
            ('órdenes','ÓRDENES'),
            ('interconsultas','INTERCONSULTAS'),
            ('notas enfermeria','NOTAS ENFERMERIA'),
            ('formula médica','FORMULA MÉDICA'),
            ('formatos','FORMATOS'),
            ('evolucion medico','EVOLUCION MEDICO'),
            ('recomendaciones','RECOMENDACIONES'),
            ('descripcion cirugia',"DESCRIPCIÓN CIRUGÍA"),
            ('nota de ingreso','NOTA DE INGRESO'),
            ('observaciones','OBSERVACIONES')
            )
        for a, b in replacements:
            s = s.replace(a, b)
        return s

    def lower(text):
        return text.lower()

    def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ó", "o"),
            ("ú", "u"),
            ('\xa0','')
        )
        for a, b in replacements:
            s = s.replace(a, b)
        return s

    def aux(text,search,helper=False):
        start = text.find(search)
        aux = text[start:]
        end = aux.find('\n')
        fragmento = aux[:end]
        if helper==True:
            fragmento = fragmento[fragmento.find(':')+2:]
            return fragmento.replace('\n','')
        return fragmento.replace('\n','')


    def search_text_in_text(texto,dic,tipo):
        success = 0
        for item in dic[tipo].keys():
            if item in texto:
                success = 1
            if texto.count(item) != 0:
                print(f'{item} --> {dic[tipo][item][0]} ')
        if success == 0:
            print(dic[tipo]['na'])

    def aux_2(text,search):
        try:
            start = text.find(search)
            aux = text[start+3:]
            end = aux.find('$ $')
            fragmento = aux[:end]
            return fragmento
        except:
            fragmento = None
            return fragmento


    def aux_reg(text,search):
        try:
            start = text.find(search)
            aux = text[start:]
            end = aux.find('sede')
            if 'sede' not in aux:
                end = aux.find('75.0 *hosvital*')
            fragmento = aux[:end]
            return fragmento
        except:
            fragmento = None
            return fragmento

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



    ###########################################
    ### EMPEZAMOS EL PROCESAMIENTO GENTERAL ###
    ###########################################
    secciones = []

    with open(Paciente,'rb') as file:
        paciente = file.read().decode()
        paciente = paciente.lower().replace('\n\n',' \n\n ') # quitamos los "\n"
        paciente = mayusculas_sec_clave(paciente) # agregamos las mayusculas de las secciones
        paciente = normalize(paciente) # quitamos los acentos de la data
        #paciente = remove_punctuation(paciente)
        folios = paciente.split('==>') # separamos por secciones 
            


    #with open("HISTORIA CLÍNICA No.CC 84046881 -- WARNER CHISTIAN MONTENEGRO BARROS.txt",'r') as file:
    #    paciente = file.read()
    #paciente = paciente.lower()
    #paciente = mayusculas_sec_clave(paciente)
    #paciente = normalize(paciente)



    # Sacamos la informacion del encabezado
    def info_Encabezado(texto):
        '''
        Esta función extrae la información de los items
        1 --> 16
        los cuales aparecen en el encabezado del historial clinico
        -----------
        Parametros:
        -----------
        - texto (string)    :el historial clinico convertido en texto
                            y normalizado.

        '''
        def lower(text):
            return text.lower()

        def normalize(s):
            replacements = (
                ("á", "a"),
                ("é", "e"),
                ("í", "i"),
                ("ó", "o"),
                ("ó", "o"),
                ("ú", "u"),
            )
            for a, b in replacements:
                s = s.replace(a, b)
            return s
        
        
        import re
        head = aux(texto,'historia clinica')

        # identificacion
        head2 = head[head.find('.')+1:head.find('.')+3]
        name = head[head.find('- ')+2:].split()
        __5 = head2.upper()
        __6 = re.findall('[0-9]+', head)[0]

        # nombres
        try:
            header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
            res = requests.get(f"http://190.131.222.108:8088/api/v1/macna/patient/{__6}/type/{__5}/information",headers=header)
            persona = json.loads(res.text)
            __1 = persona["data"][0]["fName"]          
            __2 = persona["data"][0]["sName"]            
            __3 = persona["data"][0]["fLastname"]
            __4 = persona["data"][0]["sLastname"]
        # nombres
        except:
            __1 = name[0].upper()            
            __2 = name[1].upper()            
            __3 = name[2].upper()            
            __4 = name[3].upper()

        # fecha nacimiento
        fecha = aux(texto,'fecha nacimiento:',True)
        fecha = fecha.split('/')
        fecha = fecha[::-1]
        __7 = '-'.join(fecha)

        # sexo
        __8 = aux(texto,'sexo:',True)
        if 'masculino' in __8:
            __8 = 'M'
        else:
            __8 = 'F'

        edad = aux(texto,'edad actual',True)
        edad = int(edad[:2])

        if edad < 60:
            __9 = '9622'
        elif __8 == 'F' and edad > 60:
            __9 = '9111'
        else:
            __9 = '9629'
        # ocupación
        #__9 = aux(texto,'ocupacion:',True)

        # afiliado
        #__10 = aux(texto,'afiliado:',True) # si es contributivo o subsidiado.

        # codigo eps
        eps = aux(texto,'empresa:',True) #COMFAGUAJIRA PGP ONCOLOGIA y SUBSIDIADO son diferentes?
        __11 = None

        if 'subsidiado' in eps:
            __10 = 'S'
        else:
            __10 = 'C'
        # mirar el df[df['tipo']==11]['texto'].unique()
        #grupo2
        etnia = aux(texto,'etnia:',True)
        # PERTENENCIA ETNICA
        if etnia == 'indigena':
            __12 = '1'
        elif  etnia == 'ROM':
            __12 = '2'
        elif  etnia == 'Raizal':
            __12 = '3'
        elif etnia == 'palenquero':
            __12 = '4'
        elif  etnia == 'negro':
            __12 = '5'
        else:
            __12 = '6'

        #__13 = aux(texto,'grupo poblacional: ',True)
        if edad > 60:
            __13 = '31'
        else:
            __13 = '5'

        # residencia
        data = pd.read_csv('municipios.csv',sep=',')
        # poner en minuscula , codigo y hacer
        municipio = aux(texto,'municipio: ',True)
        municipio = municipio.replace('\r','').lstrip().rstrip()

        data['municipio'] = data['municipio'].apply(lambda x: lower(x))
        data['municipio'] = data['municipio'].apply(lambda x: normalize(x))
        codigo = data[data['municipio']==municipio]['codigo'].values[0]
        codigo = int(codigo)
        codigo = str(codigo)
        if len(codigo) == 4:
            codigo = '0' + codigo
        __14 = codigo

        __15 = aux(texto,'ono: 3',True) # acento
        __15 = re.findall('[0-9]+',__15)
        if __15 == '':
            __15 = '0'

        __16 = "" # en todos los casos a sido na


        return __1,__2,__3,__4,__5,__6,__7,__8,__9,__10,__11,__12,__13,__14,__15,__16
    try:
        __1,__2,__3,__4,__5,__6,__7,__8,__9,__10,__11,__12,__13,__14,__15,__16 = info_Encabezado(paciente)
    except:
        pass

    print(__5,__6)
    ###################
    ### VARIABLE 17 ###
    ###################
    def _17(folios,dic,__6,__5):
        import statistics
        from statistics import mode
        try:
            header = {"X-Authorization":"OcUacy2Q3REsQX4KPA2x7LnMYrNo0HthgAIFt6YKYvuQNOSimUgzPGMcFyN376jJ"}
            res = requests.get(f"http://190.131.222.108:8088/api/v1/macna/patient/{__6}/type/{__5}/information",headers=header)
            persona = json.loads(res.text)
            diag = []
            for i in range(len(persona["data"])):
                diag.append(persona["data"][i]["diagnostics_cod"])
            diag =  [x for x in diag if x is not None]
            print(diag)
            diagx = statistics.mode(diag)
            print(diagx)
            print("llega aca")
            if "C" in diagx:
                print("entra al if")
                return diagx
            print("entrando al for")
            for c in diag:
                print(c)
                if "C" in c:
                    return c
            print("termino el try")             
        except:
            print("entrando en except")
            here = []
            diagnosticos = []
            for folio in range(len(folios)):
                if '$$DIAGNÓSTICO' in folios[folio]:
                    here.append(folio)
            try:
                # preguntar si es el primer diagnostico
                # el ultimo diagnostico
                # o el más frecuente
                for i in here:
                    to_back = folios[i].find("$$DIAGNÓSTICO")
                    diagnostic = folios[i][to_back-5:to_back]
                    diagnostic = diagnostic.replace("\n","")
                    if not diagnostic.isalnum():
                        continue
                    if "c" in diagnostic:
                        diagnosticos.append(diagnostic)
                print("Diagnostico encontrado")
                print(diagnosticos)
                diag = mode(diagnosticos)
                print(diag)
                __17 = diag
                return __17.replace("\n","").replace("c","C")
                
            except:
                return 'No hubo diagnostico'
    try:
        __17 = _17(folios,dic,__6,__5)
    except:
        print("fallo __17")




    """    ###################
    ### VARIABLE 18 ###
    ###################
    lista_eliminar = ['patologia', 'enfermedad actual','de patologia','fecha','biopsia','patologia.','cancer de vejiga','desde abril 2009 ','-mamografia bilateral','na','hace , 10 años','cuadrantectomia','ap','cancer cervical hace 13 años','desde hace , mas de 5 años','linfoma']
    [dic['18'].pop(key,None) for key in lista_eliminar]
    lista_agregar = ['desde hace']
    [dic['18'].update({key:None}) for key in lista_agregar]
    def _18(folios,dic):
        import re
        for folio in range(len(folios)):
            for valor in dic['18'].keys():
                if valor in folios[folio]:
                    n = folios[folio].find(valor)

                    text = folios[folio][n-70:n+70]

                    x = re.search('[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]',text)
                    if x:

                        #return '-'.join(x[0].split('-')[::-1])
                        return " "

                else:
                    variable = None

        if variable:
            #return variable
            return " "
        variable = "1800-01-01"
        #return variable
        return " "
    try:
        __18 = _18(folios,dic)
    except:
        print("fallo _18")"""




    """###################
    ### VARIABLE 21 ###
    ###################
    lista_eliminar = ['na','n','ap','linfoma ','linfoma no hodgkin','linfoma no hodgkin','linfoma','caso','patologia','reporte','biopsia']
    [dic['21'].pop(key,None) for key in lista_eliminar]
    lista_agregar = []
    [dic['21'].update({key:None}) for key in lista_agregar]
    agregar  = {
        "Inmunohistoquímica":'5',
        "Citometría de flujo":'6',
        "Clínica exclusivamente":'7',
        "Otro":'8',
        "Genética":'9',
        "Patología básica":'10',
        "Desconocido":'99',
        "Persona con aseguramiento":'55'
    }
    dic['21'].update(agregar)
    def __21_(folios,dic):
        for folio in folios:
            for llave in dic['21'].keys():
                if llave in folio:
                    return dic['21'][llave]
        return '99'
    try:
        __21 = __21_(folios,dic)
    except:
        print("fallo __21_")"""

    


    """###################
    ### VARIABLE 27 ###
    ###################
    lista_eliminar = ['na','n','ap','linfoma ','el reporte biopsia de mama derecha','fecha','biopsia','patologia','patologia','cirugia','carcinoma','carcinoma ','ca de mama','tumor']
    [dic['27'].pop(key,None) for key in lista_eliminar]
    lista_agregar = ['el reporte biopsia', 'dx en','años de evolucion']
    [dic['27'].update({key:None}) for key in lista_agregar]
    t_27 = { # enfermedad actual
        "adenocarcinoma":1,
        "carcinoma escamocelular":2,
        "carcinoma de células basales":3,
        "carcinoma diferente":4,
        "oligodendroglioma":5,
        "astrocitoma":6,
        "ependimoma":7,
        "neuroblastoma":8,
        "meduloblastoma":9,
        "hepatoblastoma":10,
        "rabdomiosarcoma":11,
        "leiomiosarcoma":12,
        "osteosarcoma":13,
        "fibrosarcoma":14,
        "angiosarcoma":15,
        "condrosarcoma":16,
        "otros sarcomas":17,
        "pancreatoblastoma":18,
        "blastoma pleuropulmonar":19,
        "otros tipos histológicos no mencionados":20,
        "melanoma":21,
        "carcinoma papilar de tiroides":24,
        "persona con aseguramiento":25,
        "no se realizó estudio histopatológico":98
    }
    dic['27'].update(t_27)
    # una lista y marcar la moda como el return 
    def _27(folios,dic):
        variable = None
        for folio in folios:
            folio = folio.replace('adenocarginoma','adenocarcinoma')
            for llave in dic['27'].keys():
                if llave in folio:
                    variable = llave
                    return dic['27'][llave]
        if variable == None:
            return dic["Otros tipos histológicos no mencionados"]
    try:
        __27 = _27(folios,dic)
    except:
        print("fallo _27")"""




    ###################
    ### VARIABLE 28 ###
    ###################
    import time
    lista_eliminar = ['na',]
    [dic['28'].pop(key,None) for key in lista_eliminar]
    lista_agregar = ['el reporte biopsia', 'dx en','años de evolucion']
    dic_aux_28 = {'moderadamente diferenciado':2}
    dic['28'].update(dic_aux_28)
    [dic['28'].update({key:None}) for key in lista_agregar]
    def _28(folios,dic):
        from scipy import stats
        resultado = []
        variable = None
        for folio in folios:
            folio_aux = folio.replace('\n',' ')
            if 'MODERADAMENTE DIFERENCIADO'.lower () in folio_aux:
                return '2'
            if 'MOD DIFERENCIADO'.lower () in folio_aux:
                return '2'
            for llave in dic['28'].keys():
                if llave in folio:
                    variable = llave
                    resultado.append(dic['28'][llave])
        
        if variable == None:
            return '94'

        return stats.mode(resultado)[0][0]
    try:
        __28 = _28(folios,dic)
    except:
        print("falló _28")




    """###################
    ### VARIABLE 30 ###
    ###################
    lista_eliminar = []
    for llave in dic['30'].keys():
        if 'fecha' in llave:
            lista_eliminar.append(llave)
    lista_eliminar.append('na')
    [dic['30'].pop(key,None) for key in lista_eliminar]
    def _30(folios,dic):
        n = len(folios)
        folio = folios[n-1]
        for llave in dic['30'].keys():
            if llave in folio:
                return ' '
                #return dic['30'][llave]
        start = folio.find('fecha') + 6
        end = start + 10
        fecha = folio[start:end]
        fecha = fecha.split('/')
        fecha = fecha[::-1]
        return ' ' # RESPUESTA ES ANTERIOR AL PERIODO DE ANALISIS DE LA HC
        #return '-'.join(fecha)
    try:
        __30 = _30(folios,dic)
    except:
        print("falló _30")
"""

###################
### CANCER MAMA ###
###################
    def _31__33(folios,dic):
        lista_eliminar = ['na','0','trastuzumab','pendiente inmunohsitoquimica ','para inicio de protocolo de quimioterapia','viene a protocolo de quimioterapia','vengo a protocolo de quimioterapia','no trajo ihq','inmunohistoquimica pendiente ','receptores de estrogeno 10%, progesterona negativo, her 2 negativo','inmunohistoquimica pendiente','recetores de estrogenos positivos progestagenos negativos her 2 neu negativo','inmunohistoquimica 23-02-2017 re y rp 100% y her 2 +1','se solicita nuevamente el estudio de inmunohistoquimicapara el her 2','receptores de estrogenos y progesterona positivos, her 2 negativo','receptores hormonales + y her 2 negativo','ca de mama izq triple negativo','receptores hormonales positivos, her 2 negativo,','vengo a protocolo de quimioterapia','desde hace']
        [dic['33'].pop(key,None) for key in lista_eliminar]
        from scipy import stats
        resultado = []
        try:
            for i in range(len(folios)):

                for llave in dic['33'].keys():
                    if llave in folios[i]:
                        centro = folios[i].find(llave)
                        frag = folios[i][centro-5:centro+30]
                        if 'positivo' in frag:
                            resultado.append(int(1))
                        elif 'negativo' in frag:
                            resultado.append(int(3))
            _33 = stats.mode(resultado)[0][0]
            _32 = ' '
            _31 = '1'
            return _31,_32,_33
        except:
            _31 = '98'
            _32 = '1845-01-01'
            _33 = '98'
            return _31,_32,_33
    try:
        __31,__32,__33 = _31__33(folios,dic)
    except:
        print("falló _31__33")


    #####################
    ### ColoRectal 34 ###
    #####################
    def _34_(__17):
        print("__17",__17)
        colorectal = ['C180','C181','C182','C183','C184','C185','C186','C187','C188','C189','C19x','C20x','C210','C211','C212','C218','D010','D011','D012','D013']
        if __17 in colorectal:
            __34 = '99'
        else:
            __34 = '98'
        return __34
    try:
        __34 = _34_(__17)
    except:
        print("Falló _34_")

    


##################
### HODGKIN 36 ###
##################
    def _36_(folios,dic):
        lista_eliminar = ['na','n',]
        [dic['36'].pop(key,None) for key in lista_eliminar]

        t_36 = {
            " estadio i":"1",
            " estadio ii":"2",
            " ii":"2",
            " estadio iii":"3",
            " iii":"3",
            " estadio iv":"4",
            " iv":"4",
            " estadio ia":"5",
            " ia":"5",
            " estadio ib":"6",
            " ib":"6",
            " estadio iia":"7",
            " iia":"7",
            " estadio iib":"8",
            " iib":"8",
            " estadio iiia":"9",
            " iiia":"9",
            " estadio iiib":"10",
            " iiib":"10",
            " estadio iva":"11",
            " iva":"11",
            " estadio ivb":"12",
            " ivb":"12",
        }
        dic['36'].update(t_36)
        from scipy import stats
        count = 0
        resultado = []
        encontrado_hodg = 0
        for folio in folios:
            if 'hodgkin' in folio:
                for llave in dic['36'].keys():
                    if llave in folio:
                        encontrado_hodg = encontrado_hodg +1
                        resultado.append(dic['36'][llave])
        try:                        
            codigo = stats.mode(resultado)[0][0]
            codigo = " "
        except:
            pass
        if encontrado_hodg == 0:
            codigo = '98'
        return codigo
    try:
        __36 = _36_(folios,dic)
    except:
        print("Fallo _36_")






###################
### PROSTATA 37 ###
###################
    def _37_(folios,dic):
        from scipy import stats 
        lista_eliminar = ['na','0','gleason','gleasson','score']
        [dic['37'].pop(key,None) for key in lista_eliminar]

        lista_agregar = [('gleason 3+5','14'),('gleason 5+3','14'),('gleason score 8','14'),('gleason grado 8','14'),('gleason 8','14'),('gleason 4+5','15'),('gleason 5+4','15'),('gleason 5+5','15'),('gleason grado 10','15'),('gleason score 10','15'),('gleason grado 9','15'),('gleason score 9','15')]
        [dic['37'].update({key:value}) for key,value in lista_agregar]
        resultado = []
        encontrado = 0
        try:
            for folio in folios:
                for llave in dic['37'].keys():
                    if llave in folio:
                        gleason = dic['37'][llave]
                        resultado.append(dic['37'][llave])
                        encontrado = encontrado + 1

            grado = stats.mode(resultado)[0][0]
        except:
            if encontrado == 0:
                grado = '98'
        return grado 
    try:
        __37 = _37_(folios,dic)
    except:
        print("fallo _37_")





    ################
    ### LEUCEMIA ###
    ################
    def _38__39_(folios,diag):
        for folio in folios:
            if 'leucemia' in folio:
                __38 = '3'
                start = folio.find('fecha') + 6
                end = start + 10
                fecha = folio[start:end]
                fecha = fecha.split('/')
                fecha = fecha[::-1]
                __39 = '-'.join(fecha)
                return __38,' '
        #return '98','1845-01-01'
        leucemias = ['C910', 'C920', 'C924', 'C925', 'C930','C940', 'C942', 'C918', 'C926', 'C928', 'C933']
        if diag in leucemias:
            leucemia = True
        else:
            leucemia = False
            
        linfomas = ['C810','C811','C812','C813','C817','C819','C820','C821','C822','C827','C829','C830','C831','C832','C833','C834','C835','C836','C837','C838','C839','C840','C841','C842','C843','C844','C845','C850','C851','C857','C859','C960','C961','C962','C963','C967','C969','C814','C823','C824','C825','C826','C846','C847','C848','C849','C852','C860','C861','C862','C863','C864','C865','C866','C884'] # colocar aquí los diag de linfoma
        if diag in linfomas:
            linfoma = True
        else:
            linfoma = False
            
        if not (leucemia and linfoma):     
            return '98','1845-01-01'
    try:
        __38,__39 = _38__39_(folios,__17)
    except:
        print("falló _38__39_")






    """####################
    ### VARIABLE 40 ####
    ####################
    lista_eliminar = ['na','ia']
    [dic['40'].pop(key,None) for key in lista_eliminar]
    lista_agregar = ['el reporte biopsia', 'dx en','años de evolucion']
    [dic['40'].update({key:None}) for key in lista_agregar]
    def _40(folios,dic,__29):
        from scipy import stats
        resultado = []
        variable = None
        for folio in folios:
            for llave in dic['40'].keys():
                if llave in folio:
                    variable = llave
                    resultado.append(dic['40'][llave])
        if __29 == '20':
            return " " # 2
        if variable == None:
            return ' ' # 99
        # return stats.mode(resultado)[0][0]
        return " "
    try:
        __40 = _40(folios,dic,__29)
    except:
        print("falló __40")"""


    ####################
    ### VARIABLE 41 ####
    ####################
    lista_eliminar = ['na','ia']
    [dic['41'].pop(key,None) for key in lista_eliminar]
    lista_agregar = ['el reporte biopsia', 'dx en','años de evolucion']
    [dic['41'].update({key:None}) for key in lista_agregar]
    def _41(folios,dic):
        from scipy import stats
        resultado = []
        variable = None
        for folio in folios:
            for llave in dic['41'].keys():
                if llave in folio:
                    variable = llave
                    resultado.append(dic['41'][llave])
        if variable == None:
            return '99'
        return stats.mode(resultado)[0][0]
    try:
        __41 = _41(folios,dic)
    except:
        print("falló __41")




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
                        __57 = hormo_fechas[0]
                        __58 = "1"
                        __59 = "80010054401"
                        __60 = "98"
                        __61 = len(list(med_encontrados2[0]))
                        encontrados = list(med_encontrados2[0]).copy()
                        for i in range(12):
                            encontrados.append('98')
                        __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]                
                        __74 = "98"
                        __75 = "1800-01-01"
                        __76 = "1"
                        __77 = "98"
                        if len(hormo_fechas)>1:
                            __78 = " "
                            __79 = hormo_fechas[-1]
                            __80 = '97' 
                            __81 = '97'
                            __82 = '97'
                            __83 = '97'
                            encontrados = list(med_encontrados2[-1]).copy()
                            for i in range(12):
                                encontrados.append('97')
                            __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                            __96 = "98"
                            __97 = "1800-01-01"
                            __98 = "98"
                            __99 = "98"           
                            print("TUVO HORMONOTERAPIA")
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
                    encontrados.append('N/A')
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
    try:
        __45,__46,__47,__48,__49,__50,__51,__52,__53,__54,__55,__56,__57,__58,__59,__60,__61,__62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73,__74,__75,__76,__79, __80, __81, __82, __83, __84, __85, __86, __87, __88, __89, __90, __91, __92, __93, __94, __95, __96, __97, __98, __99 = _45__77_(folios,__17,__6,__5)
    except Exception as e:
        print(e)
        print("falló _45__77_")

    print("-- -- -- -- -- -- -- -- -- -- -- --")





    """
    ############################
    ### QUIMIOTERAPIA 78 -77 ###
    ############################
    def _78__99_(folios,diag,__55):
        # identifico todos los folios donde sale la palabra clave 
        quimios = []
        leucemias = ['C910', 'C920', 'C924', 'C925', 'C930','C940', 'C942', 'C918', 'C926', 'C928', 'C933']
        if diag in leucemias:
            leucemia = True
        else:
            leucemia = False            
        for i in range(len(folios)):
            if ('se inicia protocolo de quimioterapia' in folios[i]) or ('se administra segun protocolo de quimioterapia' in folios[i]) or ('aplica protocolo de quimioterapia' in folios[i]) or ('aplica quimioterapia segun protocolo' in folios[i]) or (' DA INICIO A PROTOCOLO DE QUIMIOTERAPIA'.lower() in folios[i]) or ('ADMINISTRA QUIMIOTERAPIA'.lower() in folios[i]) or ('ADMINISTRA PROTOGOLO DE QUIMIOTERAPIA'.lower() in folios[i]):
                quimios.append(i)
                
        if len(quimios)>1 :
            #__78 = '2' # revisar
            __78 = " "
            start = folios[quimios[-1]].find('fecha') + 6
            end = start + 10
            fecha = folios[quimios[-1]][start:end]
            fecha = fecha.split('/')
            fecha = fecha[::-1]

            __79 = '-'.join(fecha)
            __80 = '1'
            __81 = '80010054401'
            __82 = '98'
            ## medicamentos ##
            encontrados = []
            data = pd.read_csv('atc_medicamentos.csv')
            data['descripcion_atc'] = data['descripcion_atc'].apply(lambda x: lower(x))
            data['descripcion_atc'] = data['descripcion_atc'].apply(lambda x: normalize(x))
            medicamentos = list(data['descripcion_atc'].unique())

            for medicamento in medicamentos:
                if medicamento in folios[quimios[0]]:
                    if leucemia == False:
                        if medicamento == 'dexametasona':
                            continue                        
                    values = data[data['descripcion_atc']==medicamento]['codigo_atc'].values[0]
                    encontrados.append(values)
            encontrados = set(encontrados)
            encontrados = list(encontrados)
            cuantos = str(len(encontrados))
            for i in range(12):
                encontrados.append('97')
            __83 = cuantos
            __84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
            if 'intratecal' in folios[quimios[-1]]:
                __96 = '1'
            else:
                __96 = '2'
            if  'termina infusion de quimioterapia sin complicaciones' in folios[quimios[0]]:
                __98 = '1'
            else : 
                __98 = 'N/A'                 
            __97 = "1800-01-01"
            __99 = '98'
        else:
            __78 = '98'
            __79 = '1845-01-01'
            __80 = '98'
            __81 = '98'
            __82 = '98'
            __83 = '98'
            __84 = '98'
            __85 = '98'
            __86 = '98'
            __87 = '98'
            __88 = '98'
            __89 = '98'
            __90 = '98'
            __91 = '98'
            __92 = '98'
            __93 = '98'
            __94 = '98'
            __95 = '98'
            __96 = '98'
            __97 = '1845-01-01'
            __98 = '98'
            __99 = '98'
            #__73 = '986
            if __55 == 1:
                __78 = '97'
                #__78 = " "
        __79 = " "
        __97 = " "
        return __78,__79,__55,__80,__81,__82,__83,__84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95,__96,__97,__98,__99
    try:
        __78,__79,__55,__80,__81,__82,__83,__84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95,__96,__97,__98,__99 = _78__99_(folios,__17,__55)
    except:
        print("falló _78__99_")
    """ 




    
    ###############
    ### CIRUGIA ###
    ###############
    dic['159'].clear()
    lista_agregar = ["muerto", "muerte", "fallecio","fallecimiento","fallecido",'pcte fallecio','se declara muerte clinica','paciente fallecido','se declara fallecido','se entrega acta de defuncion','se declara paciente fallecida','fallecida','muerta','declara fallecido','declara fallecida']
    [dic['159'].update({key:'2'}) for key in lista_agregar]
    def _100__111(folios,dic):
        print("Entrando a cirugia")
        __100 = "2"
        patron_fecha = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
        __100 = '98'
        print("__print: ",__100)
        import re
        here = []
        for folio in range(len(folios)):
            if 'descripcon cirugia' in folios[folio]:
                here.append(folio)

        if len(here)!=0:
            __100 = '1'
            print(__100)
            __101 = str(len(here))
            folio_1 = here[0]


            fechas = re.findall(patron_fecha,folios[folio_1].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "))
            fecha = fechas[0]
            __102 = '-'.join(fecha.split("/")[::-1])            
            __103 = "80010054401"
            n = folios[folio_1].find('codigo')
            aux = folios[folio_1][n:]
            start = aux.find('\n')
            codigo_aux = aux[start+2:start+13]
            codigo = re.findall('[0-9]',codigo_aux)
            __104 = ''.join(codigo) 
            #__105 = '1'
            __105 = " "
            __106 = '1845-01-01'
            __107 = '98'
            __108 = '98'
            __109 = '98'
            __110 = ' '
            __111 = '1'
            start = folios[folio_1].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," ").find("grupo quirurgico")
            folio_ciru = folios[folio_1][start+16:]
            codigo = re.findall('[0-9]+', folio_ciru)[0]
            __104 = codigo 
            __105 = "1"
            
            
            if len(here)>1:
                __100 = '1'
                print(__100)
                folio_2 = here[-1]
                fechas = re.findall(patron_fecha,folios[folio_2].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "))
                fecha = fechas[0]
                __106 = '-'.join(fecha.split("/")[::-1])   
                __107 = '1' # PENDIENTEEE
                __108 = '80010054401'
                n2 = folios[folio_2].find('codigo')
                aux2 = folios[folio_2][n2:]
                start1 = aux2.find('\n')
                codigo_aux2 = aux2[start1+2:start1+13]
                codigo2 = re.findall('[0-9]',codigo_aux2)
                start = folios[folio_1].replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," ").find("grupo quirurgico")
                folio_ciru = folios[folio_1][start+16:]
                codigo2 = re.findall('[0-9]+', folio_ciru)[0]                
                __109 = codigo2
                __110 = ' ' # 1
                __111 = '1'
                for llave in dic['159'].keys():
                    if llave in folios[folio_2]:
                        __111 = '2'  
        else:
            __100 = '2'
            print(__100)
            __101 = '98'
            __102 = '1845-01-01'
            __103 = '98'
            __104 = "98"
            __105 = '98'
            __106 = '1845-01-01'
            __107 = '98'
            __108 = '98'
            __109 = '98'
            __110 = ' '
            __111 = '98'
        print(__100)        
        return __100,__101,__102,__103,__104,__105,__106,__107,__108,__109,__110,__111
    try:
        __100,__101,__102,__103,__104,__105,__106,__107,__108,__109,__110,__111 = _100__111(folios,dic)
    except Exception as e:
        print(e)
        print("falló _100__111")

    print("100 : ",__100)



    print("-- -- --RADIOTERAPIA-- -- -- ")
    ####################
    ### RADIOTERAPIA ###
    ####################
    lista_eliminar = ['na',' na']
    [dic['116'].pop(key,None) for key in lista_eliminar]
    dic_16 ={
        'conformal':"922443",
        'conformal 3d':"922443",
    }
    dic['116'].update(dic_16) 
    
    
    def _112__131(folios,dic):
        encontrados_2 = []
        __116 = "N/A"
        __112 = "N/A"        
        __114 = "1845-01-01"
        __120 = "1845-01-01"
        
        braqui = []
        braquiterapia = False
        radio = False 
        folios_r = []
        for folio in folios:
            if'tratamiento de radioterapia' in folio:
                folios_r.append(folio.replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "))
        
        for folio in folios:
            if "BRAQUITERAPIA".lower() in folio:
                braquiterapia = True
                __116 = "922607"
                braqui.append(folio)
        print(f"la cantidad de folio es: {len(folios_r)}")
        
        if len(folios_r)>0:
            radio = True
            __112 = '1'
        else: 
            __112 = '98'
        
        tipos_r = {'braquiterapia':"922607"
            ,'convencional':"922442",
            'conformacional':"922443",
            'conformal':"922443",
            "Contormacional":"922443",
            "cordormacional":"922443" }
        
        if radio: #! cambio, coloqué el if
            for llave in tipos_r.keys():
                if llave in folios_r[0]:
                    __116 = tipos_r[llave]
                    radio = True
                    break
                else:
                    radio = True
                    __116 = "922442"
                
        if __116 == "922442":
            for folio in folios:
                if "radioterapia conformacional" in folio:
                    __116 = "922443"
                    radio = True
                    break
                if "radioterapia contormacional" in folio:
                    __116 = "922443"
                    radio = True
                    break
        
        
        radio_fin = ["abandono tratamiento"]
        
        
        if radio or braquiterapia:
            __117 = "1"
            __118 = "80010054401"
            __121 = "1"
            __122 = "98"
            for folio in folios:
                if 'INFORME DE RADIOTERAPIA'.lower() in folio:
                    if 'ABANDONO TRATAMIENTO'.lower() in folio:
                        __121 = "2"
                        __122 = "5"
                        print("PACIENTE ABANDONÓ TRATAMIENTO")
            patron_1 = "[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"
            patron_2 = "[0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
            patron_3 = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
            patron_4 = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9]"
            patrones = (patron_1,patron_2,patron_3,patron_4)  
            match = []     
            print("----")     
            for folio in folios_r:
                start = folio.find("inicio tratamiento")
                if start != -1:
                    aux = folio[start:]
                    end = aux.find("$$")
                    print(aux[:end])
                    for patron in patrones:
                        match.append(re.findall(patron,aux[:end]))
                if start == -1:
                    start = folio.find("completo tratamiento")
                    aux = folio[start:]
                    end = aux.find("$$")
                    print(aux[:end])
                    for patron in patrones:
                        match.append(re.findall(patron,aux[:end]))                    

            # Busco gy en folios_r
            try:
                encontrados = re.findall(r"[-+]?\d*\.\d+|\d+",folios_r[0])
                sesiones = []
                for encontrado in encontrados:
                    if encontrado != "0":
                        gy_encontrado = re.findall(f"{encontrado} gy",folios_r[0])
                        if len(gy_encontrado) > 0:
                            sesiones.append( gy_encontrado[0] )                            
                for i in range(len(sesiones)):
                    sesiones[i] = sesiones[i].replace("gy","").replace(" ","")
                print( "No de sesiones: ",sesiones )
                sessiones_aux = float(sesiones[0]),float(sesiones[1])
                print( max(sessiones_aux),min(sessiones_aux) )
                __113 = max(sessiones_aux)//min(sessiones_aux)
                print( f"Numero de presuntas sesiones { __113 }" )
            except:
                print("No se pudo calcular los gy")
                __113 = 0
                
            # si __113 == 0 busco gy en todos los folios
            if __113 == 0:
                print("Entrando a la seccion auxiliar")
                folios2_gy = []
                for folio in folios:
                    if "gy" in folio:
                        folios2_gy.append(folio)
                for folio in folios2_gy:
                    encontrados_2 = re.findall(r"[-+]?\d*\.\d+|\d+",folio)
                sesiones_2 = []
                for encontrado2 in encontrados_2:
                    if encontrado2 != "0":
                        gy_encontrado2 = re.findall(f"{encontrado2} gy",folios2_gy[0])
                        if len(gy_encontrado2) > 0:
                            sesiones_2.append( gy_encontrado2[0] )
                for i in range(len(sesiones_2)):
                    sesiones_2[i] = sesiones_2[i].replace("gy","").replace(" ","")
                print( "No de sesiones_2: ",sesiones_2 )
                try:
                    sessiones_aux_2 = float(sesiones_2[0]),float(sesiones_2[1])
                    print( max(sessiones_aux_2),min(sessiones_aux_2) )
                    __113 = max(sessiones_aux_2)//min(sessiones_aux_2)
                    print( f"Numero de presuntas sesiones { __113 }" )
                except Exception as e:
                    print(e)
            
            print('match:',match)
            match = [x for x in match if x]
            print("\n",match)
            if len(match)>1:
                if len(match[0]) ==1:
                    print("\nle quitamos el primero")
                    match = match[1:]
            print("la longitud de match es :",len(match))
            if len(match) !=0:
                try:
                    if "/" in match[0][0]:
                        __114 = "-".join(match[0][0].split("/")[::-1])
                        print("114",__114)
                        print(match[0][0])
                    if "/" in match[0][1]:
                        __120 = "-".join(match[0][1].split("/")[::-1]) #114 # 120
                        print("120",__120)
                        print(match[0][1])

                    if "-" in match[0][0]:
                        __114 = "-".join(match[0][0].split("-")[::-1])
                        print("114",__114)
                        print(match[0][0])
                    if "-" in match[0][1]:
                        __120 = "-".join(match[0][1].split("-")[::-1]) #114 # 120
                        print("120",__120)
                        print(match[0][1])
                    print(__114,"  /  ",__120)
                except:
                    __114,__120 = "N/A","N/A" #114 # 120
                print(__114,__120)
            print(f"El numero de folios con braqui: {len(braqui)}")
            if braquiterapia:
                print("ESTE PACIENTE TUVO BRAQUITERAPIA")
                for folio in braqui:
                    if "1/4" in folio:
                        fecha_inicio_braqui = re.findall(patron_3,folio)
                        print(fecha_inicio_braqui[0])
                        if "/" in fecha_inicio_braqui[0]:
                            __114 = "-".join(fecha_inicio_braqui[0].split("/")[::-1]) #114
                        else:
                            __114 = "-".join(fecha_inicio_braqui[0].split("-")[::-1]) #114
                        break
                for folio in braqui:
                    if "4/4" in folio:
                        fecha_fin_braqui = re.findall(patron_3,folio)
                        print(fecha_fin_braqui[0])
                        if "/" in fecha_inicio_braqui[0]:
                            __120 = "-".join(fecha_fin_braqui[0].split("/")[::-1]) # 120
                        else:
                            __120 = "-".join(fecha_fin_braqui[0].split("-")[::-1]) # 120
                        break
                __113 = __113 + 4
                print( f"la cantidad de sesiones de radio son {__113}" )
                
        else:
            __117 = "98"
            __116 = "98"
            __118 = "98"
            __121 = "98"
            __122 = "98"
            __116 = "98"
            __114 = "1845-01-01" #114
            __120 = "1845-01-01" # 120
            __113 = "98"
            

            
        print("resultado radioterapia".upper())
        print("__112:", __112)
        print("__116:",__116)

        return __112,__113,__114,__116,__117,__118,__120,__121,__122
    try:
        __112,__113,__114,__116,__117,__118,__120,__121,__122 = _112__131(folios,dic)
    except Exception as e:
        print(e)
        print("falló _112__131")
        pass
    print("Salio de radio")


    ###################################
    ### DOLOR Y CUIDADOS PALIATIVOS ###
    ###################################
    def _140__148(folios):
        _140 = None
        _146 = None
        patron_fecha = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
        for folio in folios:
            folio = folio.replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," ")
            start = folio.find("reg.")
            frag = folio[start:start+60]

            if 'dolor y cuidados' in frag:
                fechas = re.findall(patron_fecha,folio.replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "))
                fecha = fechas[0]
                _147 = '-'.join(fecha.split("/")[::-1])
                _140 =  "1"
                _141 = "1"
                _148 = "80010054401"
                break
        if _140 == "1":
            for folio in folios:
                folio = folio.replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," ")
                start = folio.find("reg.")
                frag = folio[start:start+60]
                if 'psicologia' in frag:
                    _146 = " " # 1


        if _140 == None:
            _140 = "2"
            _141 = "2"
            _146 = " " # 2
            _147 =  "1845-01-01"
            _148 = "98" # "80010054401"
        _142,_143,_144,_145 = ("2","2","2","2")
  
        return _140,_141,_142,_143,_144,_145,_146,_147,_148
    try:
        __140,__141,__142,__143,__144,__145,__146,__147,__148 = _140__148(folios)
    except:
        print("falló _140__148")


    """
    ###################
    ### PSICOLOGIA ###
    ###################
    def _146__148(folios,anterior):
        _146 = None
        for folio in folios:
            here = []
            for i in range(len(folio)-5):
                sub = folio[i:i+4] # n-grams de caracteres
                if sub == 'reg.':
                    here.append(i)

            for ii in here:
                frag = folio[ii:ii+30]
                if 'psicologia' in frag:
                    start = folio.find('fecha') + 6
                    end = start + 10
                    try:
                        fecha = folio[start:end]
                        fecha = fecha.split('/')
                        fecha = fecha[::-1]
                        _147 = '-'.join(fecha)
                        if _147.replace(' ','').isalpha():
                            _147 = '1845-01-01'
                    except:
                        _147 = 'problema'
                    _146 =  "1"
                    
                    break
            if _146 == "1":
                break
        if _146 == None:
            _146 = "2"
            _147 = "1845-01-01"
        _148 = "98" # "80010054401"
        return _146,_147,_148
    __146,__147,__148 = _146__148(folios)
    print('psicologia')
    print(f'==>146: {__146}')
    print(f'==>147: {__147}')
    print(f'==>148: {__148}')
    print(' ')
    """
    print("entrando a nutricion")
    ###################
    ### NUTRICION ###
    ###################
    def _152__156(folios):
        _152 = "98"
        patron_fecha = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
        for folio in folios:
            folio = folio.replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," ")
            start = folio.find("reg.")
            frag = folio[start:start+60]
            if 'nutricion' in frag:
                start = folio.find('fecha') + 6
                end = start + 10
                _152 = "1"
                fechas = re.findall(patron_fecha,folio.replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," "))
                fecha = fechas[0]
                _153 = '-'.join(fecha.split("/")[::-1])
                _155 = "1"
                _154 = "80010054401"
                break
        if _152 == "1":
            here = []
            for folio in folios:
                folio = folio.replace("\n"," ").replace("  "," ").replace("   "," ").replace("  "," ")
                start = folio.find("reg.")
                frag = folio[start:start+60]
                if 'nutricion' in frag:
                    here.append(folio)
            enteral = False 
            parenteral = False
            for aqui in here[::-1]:
                if 'parenteral' in aqui:
                    parenteral = True
                    _155 = '2'
                    break
                elif ' enteral' in aqui:
                    enteral = True
                    _155 = '1'
                    break
                else :
                    _155 = '4'

            for aqui in here[::-1]:
                if 'parenteral' in aqui:
                    parenteral = True
                if ' enteral' in aqui:
                    enteral = True
                if parenteral and enteral:
                    _155 = '3'
                    break
                else:
                    parenteral = False
                    enteral = False
            print(_155)           
        if _152 == "98":
            _152 = "98"
            _155 = "4"
            _154 = "98"
            _153 = "1845-01-01"
        _156 = "98"
        return _152,_153,_154,_155,_156
    try:
        __152,__153,__154,__155,__156 = _152__156(folios)
    except Exception as e:
        print("falló _152__156")
        print(e)

###################################### 
### RESULTADO FINAL DE LA ATENCIÓN ###
######################################
    print("\n\nresultado final")
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
            
            
            __160 = '0' # inferir
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
            
            

        elif (int(__45)!=1) and (int(__100)==1) and (int(__112)!=1):
            __157 = '3'
            __41 = '2'
            
            

        elif (int(__45)!=1) and (int(__100)!=1) and (int(__112)==1):
            __157 = '1'
            __41 = '2'
            

        elif (int(__45)==1) and (int(__100)==1) and (int(__112)!=1):
            __157 = '5'
            __41 = '2'
            

        elif (int(__45)==1) and (int(__100)!=1) and (int(__112)==1):
            __157 = '4'
            __41 = '2'
            

        elif (int(__45)!=1) and (int(__100)==1) and (int(__112)==1):
            __157 = '6'
            __41 = '2'
            
        
        elif (int(__45)==1) and (int(__100)==1) and (int(__112)==1):
            __157 = '10'
            __41 = '2'
            

        else:
            __157 = '9'
            __41 = '3'

        if __159 == "2": # paciente fallecido
            __157 = '98'
        
        
        return __157,__158,__159,__160,__161,__162,__163,__164,__165,__166,__41
    try:
        __157,__158,__159,__160,__161,__162,__163,__164,__165,__166,__41 = _157__166(folios,dic,__45,__100,__112,__6,__5,__140)
    except Exception as e:
        print(e)
        print("falló _157__166")
        

    __11 = Eps
    __166 = Fcorte
    __16 = "1800-01-01"
    variables_final = (__1 ,__2 ,__3 ,__4 ,__5 ,__6 ,__7 ,__8 ,__9 ,__10 ,__11 ,__12 ,__13 ,__14 ,__15 ,__16 ,__17 ,__18 ,__19 ,__20 ,__21 ,__22 ,__23 ,__24 ,__25 ,__26 ,__27 ,__28 ,__29 ,__30 ,__31 ,__32 ,__33 ,__34 ,__35 ,__36 ,__37 ,__38 ,__39 ,__40 ,__41 ,__42 ,__43 ,__44 ,__45 ,__46 ,__47 ,__48 ,__49 ,__50 ,__51 ,__52 ,__53 ,__54 ,__55 ,__56 ,__57 ,__58 ,__59 ,__60 ,__61 ,__62 ,__63 ,__64 ,__65 ,__66 ,__67 ,__68 ,__69 ,__70 ,__71 ,__72 ,__73 ,__74 ,__75 ,__76 ,__77 ,__78 ,__79 ,__80 ,__81 ,__82 ,__83 ,__84 ,__85 ,__86 ,__87 ,__88 ,__89 ,__90 ,__91 ,__92 ,__93 ,__94 ,__95 ,__96 ,__97 ,__98 ,__99 ,__100 ,__101 ,__102 ,__103 ,__104 ,__105 ,__106 ,__107 ,__108 ,__109 ,__110 ,__111 ,__112 ,__113 ,__114 ,__115 ,__116 ,__117 ,__118 ,__119 ,__120 ,__121 ,__122 ,__123 ,__124 ,__125 ,__126 ,__127 ,__128 ,__129 ,__130 ,__131 ,__132 ,__133 ,__134 ,__135 ,__136 ,__137 ,__138 ,__139 ,__140 ,__141 ,__142 ,__143 ,__144 ,__145 ,__146 ,__147 ,__148 ,__149 ,__150 ,__151 ,__152 ,__153 ,__154 ,__155 ,__156 ,__157 ,__158 ,__159 ,__160 ,__161 ,__162 ,__163 ,__164 ,__165 ,__166) 

    #########################################
    ### TRABAJANDO CON WORKBOOK DE EXCELL ###
    #########################################
    #wb = Workbook() # creamos objeto de Excel
    #wb.save('prueba2.xlsx') 

    wb = load_workbook(filename="prueba2.xlsx")
    #wb.create_sheet('CAC',0)
    ws = wb['CAC']
    for i in range(1,167):
        try:
            ws.cell(row=row,column=i,value=variables_final[i-1])
        except:
            ws.cell(row=row,column=i,value="N/A")

    wb.save("prueba2.xlsx")

if __name__ == '__main__':
    hcs = glob.glob('*.pdf')
    for hc in hcs:
        pdf_to_txt(hc[:-4])

        continue
    
    pacientes = glob.glob('*7205297*.txt')
    pacientes = glob.glob('HISTORIA*.txt')
    print(f"La cantidad de pacientes es {len(pacientes)}")

    print(' ')
    row = 7
    
    
    f = '2021-05-18'
    eps = 'prueba'
    for paciente in pacientes:
        try:
            print(f'== == == == == {paciente} / {row} == == == == ==')
            main(paciente,row,f,eps)
        except Exception as e:
            print(e)
            continue
        row = row + 1
        for i in range(3):
            print(' ')
            
    print('-- -- -- -- PROCESO TERMINADO -- -- -- -- ')
    print("desde bnndn5") 
    