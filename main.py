import connect_db_1
import bd_to_dic_2
import pdf_to_txt_3
import json
import glob
import nltk
#import cac_data_4

#Convertimos el pdf en texto
#pdf_to_txt_3.pdf_to_csv('CC 1192943668 - HC')

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
        ('examen físico','EXAMEN FÍSICO'),
        ('análisis','ANÁLISIS'),
        ('plan y manejo','PLAN Y MANEJO'),
        ('diagnóstico','DIAGNÓSTICO'),
        ('ordenes','ORDENES'),
        ('órdenes','ÓRDENES'),
        ('interconsultas','INTERCONSULTAS'),
        ('notas enfermeria','NOTAS ENFERMERIA'),
        ('formula médica','FORMULA MÉDICA'),
        ('formatos','FORMATOS'),
        ('recomendaciones','RECOMENDACIONES'),
        ('nota de ingreso','NOTA DE INGRESO'),
        ('observaciones','OBSERVACIONES')
        )
    for a, b in replacements:
        s = s.replace(a, b)
    return s

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
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
    



# Empezamos el procesamiento general
secciones = []
textos = glob.glob('*1192943668*.txt')
for texto in textos:
    with open(texto,'r') as file:
        paciente = file.read()
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
    helper = aux(texto,'fecha nacimiento:',True)
    __7 = helper[helper.find(':')]
    print(__7)
    # sexo
    __8 = aux(texto,'sexo:',True)
    if 'masculino' in __8:
        __8 = 'M'
    else:
        __8 = 'F'
    print(__8)
    # ocupación
    __9 = aux(texto,'ocupacion:',True)
    print(__9)
    # afiliado
    __10 = aux(texto,'afiliado:',True)
    print(__10)
    # codigo eps
    __11 = aux(texto,'empresa:',True) #COMFAGUAJIRA PGP ONCOLOGIA y SUBSIDIADO son diferentes?
    print(__11)
    # mirar el df[df['tipo']==11]['texto'].unique()
    #grupo2
    __12 = aux(texto,'etnia:',True)
    print(__12)
    __13 = aux(texto,'grupo poblacional: ',True)
    print(__13)
    # residencia 
    __14 = aux(texto,'municipio: ',True)
    print(__14)
    __15 = aux(texto,'telefono:',True) # acento
    print(__15)
    __16 = "1800-01-0" # en todos los casos a sido na
    print(__16)

    return __1,__2,__3,__4,__5,__6,__7,__8,__9,__10,__11,__12,__13,__14,__15,__16

__1,__2,__3,__4,__5,__6,__7,__8,__9,__10,__11,__12,__13,__14,__15,__16 = info_Encabezado(paciente)


###################
### VARIABLE 17 ###
###################
def _17(folios,dic):
    here = []
    for folio in range(len(folios)):
        if '$$DIAGNÓSTICO' in folios[folio]:
            here.append(folio)
    ultimo = max(here)
    fragmento = aux(folios[ultimo],"$$DIAGNÓSTICO")
    for valor in dic['17'].values():
        if valor in fragmento:
            variable = valor
            return variable
        else:
            variable = 'c'+fragmento[15:18]
        return variable
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
    return folio[start:end]
__30 = _30(folios,dic)
print(f'==> 30: {__30}')



###################################
### DOLOR Y CUIDADOS PALIATIVOS ###
###################################
def _140__148(folios):
    _140 = None
    for folio in folios:
        frag = aux_reg(folio,'reg. ')
        if 'dolor y cuidados' in frag:
            start = folio.find('fecha') + 6
            end = start + 10
            _140 =  "1"
            _141 = "1"
            _146 = "1"
            _147 = folio[start:end]
        else:
            pass
    if _140 == None:
        _140 = "2"
        _141 = "2" 
    _142,_143,_144,_145 = ("2","2","2","2")
    _148 = "98" # "80010054401"
    return _140,_141,_142,_143,_144,_145,_146,_147,_148
__140,__141,__142,__143,__144,__145,__146,__147,__148 = _140__148(folios)
print('Dolor')
print(f'==>140: {__140}')
print(f'==>141: {__141}')
print(f'==>142: {__142}')
print(f'==>143: {__143}')
print(f'==>144: {__144}')
print(f'==>145: {__145}')
print(f'==>146: {__146}')
print(f'==>147: {__147}')
print(f'==>148: {__148}')



###################
### PSIQUIATRIA ###
###################
def _149__151(folios):
    _149 = None
    for folio in folios:
        here = []
        for i in range(len(folio)-5):
            sub = folio[i:i+4]
            if sub == 'reg.':
                here.append(i)

        for ii in here:
            frag = folio[ii:ii+30]
            if 'psicologia' in frag:
                start = folio.find('fecha') + 6
                end = start + 10
                fecha = folio[start:end]
                _149 =  "1"
                _150 = fecha
                break
        if _149 == "1":
            break
    if _149 == None:
        _149 = "2"
        _150 = "1845-01-01"
    _151 = "98" # "80010054401"
    return _149,_150,_151
__149,__150,__151 = _149__151(folios)
print('psicologia')
print(f'==>149: {__149}')
print(f'==>150: {__150}')
print(f'==>151: {__151}')
print(' ')


###################
### NUTRICION ###
###################
def _152__155(folios):
    _152 = None
    for folio in folios:
        frag = aux_reg(folio,'reg. ')
        if 'nutricion' in frag:
            start = folio.find('fecha') + 6
            end = start + 10
            _152 =  "1"
            _153 = folio[start:end]
            _155 = "1"
        else:
            pass
    if _152 == None:
        _152 = "2"
        _155 = "2"
        _153 = "1845-01-01"
    _154 = "98" # "80010054401"
    return _152,_153,_154,_155
__152,__153,__154,__155 = _152__155(folios)
print('Nutricion')
print(f'==>152: {__152}')
print(f'==>153: {__153}')
print(f'==>154: {__154}')
print(f'==>155: {__155}')