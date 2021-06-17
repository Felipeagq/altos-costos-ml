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
__19 = '1800-01-01'
__20 = '1800-01-01'
__21 = '10'
__22 = '98' # PREDETERMINADA
__23 = None
__24 = None
__25 = '99' # 80010054401
__26 = None
__27 = None
__28 = None
__29 = '99'
__30 = '1800-01-01'
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
__56 = '98'
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
__100 = '2'
__101 = '98'
__102 = '1845-01-01'
__103 = '98'
__104 = '98'
__105 = '98'
__106 = '1845-01-01'
__107 = '98'
__108 = '98'
__109 = '98'
__110 = '98'
__111 = '98'
__112 = '98'
__113 = '98'
__114 = '1845-01-01'
__115 = '98'
__116 = '98'
__117 = '98'
__118 = '98'
__119 = '98'
__120 = '1845-01-01'
__121 = '98'
__122 = '98'
__123 = '1845-01-01'
__124 = '98'
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
__146 = '2'
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

p4 = "40925684"
p2 = "84046881"
p3 = "1192943668"
p1 = p4

from pdf_to_txt_3 import pdf_to_csv
#import connect_db_1
#import bd_to_dic_2
#import pdf_to_txt_3
import json
import datetime
import glob
import pandas as pd
import os
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import nltk
#import cac_data_4
def main(Paciente,row):
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
        __5 = head[head.find('.')+1:head.find('.')+3]
        __6 = re.findall('[0-9]+', head)
        name = head[head.find('-- ')+3:].split()

        # nombres
        try:
            __1 = name[0]
            __2 = name[1]
            __3 = name[2]
            __4 = name[3]
            print(__1)
            print(__2)
            print(__3)
            print(__4)
            print(__5)
            print(__6[0])
        except:
            print('error')
        # fecha nacimiento
        fecha = aux(texto,'fecha nacimiento:',True)
        fecha = fecha.split('/')
        fecha = fecha[::-1]
        __7 = '-'.join(fecha)
        print(__7)
        # sexo
        __8 = aux(texto,'sexo:',True)
        if 'masculino' in __8:
            __8 = 'M'
        else:
            __8 = 'F'
        print(__8)
        edad = aux(texto,'edad actual',True)
        edad = int(edad[:2])
        print(f'edad{edad}')
        if edad < 60:
            __9 = '9622'
        elif __8 == 'F' and edad > 60:
            __9 = '9111'
        else:
            __9 = '9629'
        # ocupación
        #__9 = aux(texto,'ocupacion:',True)
        #print(__9)
        # afiliado
        #__10 = aux(texto,'afiliado:',True) # si es contributivo o subsidiado.
        #print(__10)
        # codigo eps
        __11 = aux(texto,'empresa:',True) #COMFAGUAJIRA PGP ONCOLOGIA y SUBSIDIADO son diferentes?
        print(__11)
        if 'subsidiado' in __11:
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
        print(__12)
        #__13 = aux(texto,'grupo poblacional: ',True)
        if edad > 60:
            __13 = '31'
        else:
            __13 = '5'
        print(__13)
        # residencia
        data = pd.read_csv('municipios.csv',sep=',')
        # poner en minuscula , codigo y hacer
        municipio = aux(texto,'municipio: ',True)
        municipio = municipio.replace('\r','').lstrip().rstrip()
        print(f'----{municipio}----')
        data['municipio'] = data['municipio'].apply(lambda x: lower(x))
        data['municipio'] = data['municipio'].apply(lambda x: normalize(x))
        codigo = data[data['municipio']==municipio]['codigo'].values[0]
        __14 = str(codigo)
        print(f'==>14: {__14}')
        __15 = aux(texto,'ono: 3',True) # acento
        print(__15)
        __16 = "1800-01-01" # en todos los casos a sido na
        print(__16)

        return __1,__2,__3,__4,__5,__6[0],__7,__8,__9,__10,__11,__12,__13,__14,__15,__16

    __1,__2,__3,__4,__5,__6,__7,__8,__9,__10,__11,__12,__13,__14,__15,__16 = info_Encabezado(paciente)


    ###################
    ### VARIABLE 17 ###
    ###################
    def _17(folios,dic):
        here = []
        for folio in range(len(folios)):
            if '$$DIAGNÓSTICO' in folios[folio]:
                here.append(folio)
        try:
            ultimo = max(here)
            fragmento = aux(folios[ultimo],"$$DIAGNÓSTICO")
            for valor in dic['17'].values():
                if valor in fragmento:
                    variable = valor
                    return variable
                else:
                    variable = 'c'+fragmento[15:18] # preguntar por esto
                return variable
        except:
            return 'No hubo diagnostico'
    __17 = _17(folios,dic)
    print(f'==> 17: {__17}')



    ###################
    ### VARIABLE 18 ###
    ###################
    lista_eliminar = ['patologia', 'enfermedad actual','de patologia','fecha','biopsia','patologia.','cancer de vejiga','desde abril 2009 ','-mamografia bilateral','na','hace , 10 años','cuadrantectomia','ap','cancer cervical hace 13 años','desde hace , mas de 5 años','linfoma']
    [dic['18'].pop(key,None) for key in lista_eliminar]
    lista_agregar = ['desde hace']
    [dic['18'].update({key:None}) for key in lista_agregar]
    def _18(folios,dic):
        for folio in range(len(folios)):
            for valor in dic['18'].keys():
                if valor in folios[folio]:
                    variable = valor
                else:
                    variable = None
            #print('Ninguna coincidencia encontrada')
        if variable:
            return variable
        variable = "1800-01-01"
        return variable
    __18 = _18(folios,dic)
    print(f'==> 18 {__18}')



    ###################
    ### VARIABLE 26 ###
    ###################
    def _26(folios):
        for folio in folios:
            frag = aux_reg(folio,'reg. ')
            if 'oncologia' in frag:
                start = folio.find('fecha') + 6
                end = start + 10
                fecha = folio[start:end]
                fecha = fecha.split('/')
                fecha = fecha[::-1]
                return '-'.join(fecha)
            else:
                return "1800-01-01"
    __26 = _26(folios)
    print(f'==>26 : {__26}')
    print(' ')




    ###################
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
                return dic['30'][llave]
        start = folio.find('fecha') + 6
        end = start + 10
        fecha = folio[start:end]
        fecha = fecha.split('/')
        fecha = fecha[::-1]
        return '-'.join(fecha)
    __30 = _30(folios,dic)
    print(f'==> 30: {__30}')



    ###################################
    ### DOLOR Y CUIDADOS PALIATIVOS ###
    ###################################
    def _140__148(folios):
        _140 = None
        for folio in folios:
            here = []
            for i in range(len(folio)-5):
                sub = folio[i:i+4] # n-grams de caracteres
                if sub == 'reg.':
                    here.append(i)

            for ii in here:
                frag = folio[ii:ii+30]
                if 'dolor y cuidados' in frag:
                    start = folio.find('fecha') + 6
                    end = start + 10
                    _140 =  "1"
                    _141 = "1"
                    _146 = "1"
                    fecha = folio[start:end]
                    fecha = fecha.split('/')
                    fecha = fecha[::-1]
                    _147 = '-'.join(fecha)
                    if _147.replace(' ','').isalpha():
                        _147 = '1845-01-01'
                    break
            if _140 =="1":
                break
        if _140 == None:
            _140 = "2"
            _141 = "2"
            _146 = "2"
            _147 =  "1845-01-01"
        _142,_143,_144,_145 = ("2","2","2","2")
        _148 = "98" # "80010054401"
        return _140,_141,_142,_143,_144,_145,_146,_147,_148
    __140,__141,__142,__143,__144,__145,__146,__147,__148 = _140__148(folios)
    print('dolor ')
    print(f'==>140: {__140}')
    print(f'==>141: {__141}')
    print(f'==>142: {__142}')
    print(f'==>143: {__143}')
    print(f'==>144: {__144}')
    print(f'==>145: {__145}')
    print(f'==>146: {__146}')
    print(f'==>147: {__147}')
    print(f'==>148: {__148}')
    print(' ')




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

    ###################
    ### NUTRICION ###
    ###################
    def _152__156(folios):
        _152 = None
        for folio in folios:
            here = []
            for i in range(len(folio)-5):
                sub = folio[i:i+4] # n-grams de caracteres
                if sub == 'reg.':
                    here.append(i)

            for ii in here:
                frag = folio[ii:ii+30]
                print(frag)
                print('---')
                if 'nutricion' in frag:
                    start = folio.find('fecha') + 6
                    end = start + 10
                    _152 =  "1"
                    fecha = folio[start:end]
                    fecha = fecha.split('/')
                    fecha = fecha[::-1]
                    _153 =  '-'.join(fecha)
                    print(f'-->{_153}--')
                    if 'hora' in _153:
                        fecha = folio[end+11:end+21]
                        fecha = fecha.split('/')
                        fecha = fecha[::-1]
                        _153 =  '-'.join(fecha)
                        print('aqui entro')
                    _155 = "1"
                    break
            if _152 =="1":
                break
        if _152 == None:
            _152 = "2"
            _155 = "2"
            _153 = "1845-01-01"
        _156 = "98"
        _154 = "98" # "80010054401"
        return _152,_153,_154,_155,_156
    __152,__153,__154,__155,__156 = _152__156(folios)
    print('Nutricion')
    print(f'==>152: {__152}')
    print(f'==>153: {__153}')
    print(f'==>154: {__154}')
    print(f'==>155: {__155}')
    print(f'==>156: {__156}')
    print(' ')


######################################
### RESULTADO FINAL DE LA ATENCIÓN ###
######################################
    def _157__166(folios,dic):
        dic['159'].clear()
        lista_agregar = ["muerto", "muerte", "fallecio","fallecimiento","fallecido",'pcte fallecio','se declara muerte clinica','paciente fallecido','se declara fallecido','se entrega acta de defuncion','se declara paciente fallecida','fallecida','muerta','declara fallecido','declara fallecida']
        [dic['159'].update({key:'2'}) for key in lista_agregar]
        for key in dic['159'].keys():
            here = findKeyWord(folios[-1],key,5)
            print('var 149 ngram :',here)
            if key in folios[-1]:
                __159 = '2'
                break
            else:
                __159 = '1'
        if __159 == "2": # paciente fallecido    
            print('Muerto')
            __157 = '98'
            __158 = '99'
            __160 = '4'
            __161 = '12'                                      
            __163 = '' # fechad del folio                    
            __164 = '' # buscar en el texto y pregunta si hay area especifica. KWIC                                   
        else: # si se encuentra vivo       
            print('Vivo')                  
            __158 = '' # A EVALUAR    
            __157 = '' # A EVALUAR  
            __160 = '' # inferir                     
            __161 = '' #inferir
            __163 = '1845-01-01' # ¿como evaluar persona con aseguramiento?     
            __164 = '98'        
            
            
        __165 = '98'
        __162 = '1845-01-01'
        __166 = '2021-01-01' # encontrar alguna forma de cambiar la fecha de corte ¿cada cuanto es la fecha de corte? 
        return __157,__158,__159,__160,__161,__162,__163,__164,__165,__166
    __157,__158,__159,__160,__161,__162,__163,__164,__165,__166 = _157__166(folios,dic)
    print(f'==>157: {__157}')
    print(f'==>158: {__158}')
    print(f'==>159: {__159}')
    print(f'==>160: {__160}')
    print(f'==>161: {__161}')
    print(f'==>162: {__162}')
    print(f'==>163: {__163}')
    print(f'==>164: {__164}')
    print(f'==>165: {__165}')
    print(f'==>166: {__166}')
    

    try:
        variables_final = (__1 ,__2 ,__3 ,__4 ,__5 ,__6 ,__7 ,__8 ,__9 ,__10 ,__11 ,__12 ,__13 ,__14 ,__15 ,__16 ,__17 ,__18 ,__19 ,__20 ,__21 ,__22 ,__23 ,__24 ,__25 ,__26 ,__27 ,__28 ,__29 ,__30 ,__31 ,__32 ,__33 ,__34 ,__35 ,__36 ,__37 ,__38 ,__39 ,__40 ,__41 ,__42 ,__43 ,__44 ,__45 ,__46 ,__47 ,__48 ,__49 ,__50 ,__51 ,__52 ,__53 ,__54 ,__55 ,__56 ,__57 ,__58 ,__59 ,__60 ,__61 ,__62 ,__63 ,__64 ,__65 ,__66 ,__67 ,__68 ,__69 ,__70 ,__71 ,__72 ,__73 ,__74 ,__75 ,__76 ,__77 ,__78 ,__79 ,__80 ,__81 ,__82 ,__83 ,__84 ,__85 ,__86 ,__87 ,__88 ,__89 ,__90 ,__91 ,__92 ,__93 ,__94 ,__95 ,__96 ,__97 ,__98 ,__99 ,__100 ,__101 ,__102 ,__103 ,__104 ,__105 ,__106 ,__107 ,__108 ,__109 ,__110 ,__111 ,__112 ,__113 ,__114 ,__115 ,__116 ,__117 ,__118 ,__119 ,__120 ,__121 ,__122 ,__123 ,__124 ,__125 ,__126 ,__127 ,__128 ,__129 ,__130 ,__131 ,__132 ,__133 ,__134 ,__135 ,__136 ,__137 ,__138 ,__139 ,__140 ,__141 ,__142 ,__143 ,__144 ,__145 ,__146 ,__147 ,__148 ,__149 ,__150 ,__151 ,__152 ,__153 ,__154 ,__155 ,__156 ,__157 ,__158 ,__159 ,__160 ,__161 ,__162 ,__163 ,__164 ,__165 ,__166) 
    except:
        pass

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
            continue

    wb.save("prueba2.xlsx")

if __name__ == '__main__':
    hcs = glob.glob('*.pdf')
    for hc in hcs:
        #pdf_to_csv(hc[:-4])
        print(hc[:-4])
    pacientes = glob.glob('HISTORIA*.txt')
    print(pacientes)
    row = 7
    for paciente in pacientes:
        try:
            main(paciente,row)
        except Exception as e:
            print(e)
            continue
        row = row + 1
        print('-- -- -- -- -- -- -- -- -- -- -- -- -- -- ')
    print('-- -- -- -- Proceso terminado -- -- -- -- ')
    
    
    
    
    
    
    
    
