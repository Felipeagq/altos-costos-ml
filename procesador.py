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

import time 
from pdf_to_txt_3 import pdf_to_csv
import glob
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
        __5 = head2.upper()
        __6 = re.findall('[0-9]+', head)
        name = head[head.find('- ')+2:].split()

        # nombres
        try:
            __1 = name[0].upper()            
            __2 = name[1].upper()            
            __3 = name[2].upper()            
            __4 = name[3].upper()

        except:
            print('error en el nombre')
            __4 = 'NONE'
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
        if __15 == '':
            __15 = '0'

        __16 = "" # en todos los casos a sido na


        return __1,__2,__3,__4,__5,__6[0],__7,__8,__9,__10,__11,__12,__13,__14,__15,__16
    try:
        __1,__2,__3,__4,__5,__6,__7,__8,__9,__10,__11,__12,__13,__14,__15,__16 = info_Encabezado(paciente)
    except:
        pass


    ###################
    ### VARIABLE 17 ###
    ###################
    def _17(folios,dic):
        here = []
        for folio in range(len(folios)):
            if '$$DIAGNÓSTICO' in folios[folio]:
                here.append(folio)
        try:
            # preguntar si es el primer diagnostico
            # el ultimo diagnostico
            # o el más frecuente
            ultimo = max(here)
            fragmento = aux(folios[ultimo],"$$DIAGNÓSTICO")
            fragmento = aux(folios[here[0]],"$$DIAGNÓSTICO")
            for valor in dic['17'].values():
                if valor in fragmento:
                    variable = valor
                    return variable
                else:
                    variable = 'C'+fragmento[15:18] # preguntar por esto
                return variable.replace("t",'1')
            
        except:
            return 'No hubo diagnostico'
    __17 = _17(folios,dic)




    ###################
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
    __18 = _18(folios,dic)




    ###################
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
    __21 = __21_(folios,dic)

    

    ###################
    ### VARIABLE 26 ###
    ###################
    def __26_(folios):
        for folio in folios:
            n = folio.find('reg. ')
            frag = folio[n:]
            if 'oncologia' in frag:
                start = folio.find('fecha') + 6
                end = start + 10
                fecha = folio[start:end]
                fecha = fecha.split('/')
                fecha = fecha[::-1]
                return '-'.join(fecha)
        return " "
    __26 = __26_(folios)



    ###################
    ### VARIABLE 25 ###
    ###################
    def _25_():
        __25, __26 = ' ',' '
        return __25, __26
    __25, __26 = _25_()


    ###################
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
    __27 = _27(folios,dic)




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
    __28 = _28(folios,dic)




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
                return ' '
                #return dic['30'][llave]
        start = folio.find('fecha') + 6
        end = start + 10
        fecha = folio[start:end]
        fecha = fecha.split('/')
        fecha = fecha[::-1]
        return ' ' # RESPUESTA ES ANTERIOR AL PERIODO DE ANALISIS DE LA HC
        #return '-'.join(fecha)
    __30 = _30(folios,dic)


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
            _32 = ' '
            _33 = '98'
            return _31,_32,_33

    __31,__32,__33 = _31__33(folios,dic)


    #####################
    ### ColoRectal 34 ###
    #####################
    def _34_(__17):
        colorectal = ['c180','c181','c182','c183','c184','c185','c186','c187','c188','c189','c19x','c20x','c210','c211','c212','c218','d010','d011','d012','d013']
        if __17 in colorectal:
            __34 = '99'
        else:
            __34 = '98'
        return __34
    __34 = _34_(__17)

    


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
        except:
            pass
        if encontrado_hodg == 0:
            codigo = '98'
        return codigo
    __36 = _36_(folios,dic)






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
    __37 = _37_(folios,dic)





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
    __38,__39 = _38__39_(folios,__17)






    ####################
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
            return "2"
        if variable == None:
            return '99'
        return stats.mode(resultado)[0][0]
    __40 = _40(folios,dic,__29)


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
    __41 = _41(folios,dic)




    ############################
    ### QUIMIOTERAPIA 45 -77 ###
    ############################
    def _45__77_(folios,diag):
        # identifico todos los folios donde sale la palabra clave 
        quimios = []
        CIE = ['C835', 'C910', 'C920', 'C924','C925']
        leucemias = ['C910', 'C920', 'C924', 'C925', 'C930','C940', 'C942', 'C918', 'C926', 'C928', 'C933']
        if diag in leucemias:
            leucemia = True
        else:
            leucemia = False        
        if diag in CIE:
            for i in range(len(folios)):
                if ('se inicia protocolo de quimioterapia' in folios[i]) or ('se administra segun protocolo de quimioterapia' in folios[i]) or ('aplica protocolo de quimioterapia' in folios[i]) or ('aplica quimioterapia segun protocolo' in folios[i]) or ('realizar protocolo quimioterapia' in folios[i]) or (' DA INICIO A PROTOCOLO DE QUIMIOTERAPIA'.lower() in folios[i]) or ('ADMINISTRA QUIMIOTERAPIA'.lower() in folios[i]) or ('ADMINISTRA PROTOGOLO DE QUIMIOTERAPIA'.lower() in folios[i]):
                    quimios.append(i)

            if len(quimios)>1 :
                print(f'cantidad de quimios es {len(quimios)}')
                __45 = '1'
                #__46 = str(len(quimios))
                __46 = '98'
                __47 = '97' 
                __48 = '97'
                __49 = '97'
                __50 = '97'
                __51 = '97'
                __52 = '97'
                __53 = '97'
                __54 = '97'
                __55 = str(len(quimios))
                __56 = ''
                start = folios[quimios[0]].find('fecha') + 6
                end = start + 10
                fecha = folios[quimios[0]][start:end]
                fecha = fecha.split('/')
                fecha = fecha[::-1]
                __57 = '-'.join(fecha)
                __58 = '80010054401'
                __59 = '80010054401'
                __60 = '98'
                ## medicamentos ##
                encontrados = []
                data = pd.read_csv('atc_medicamentos.csv')
                data['descripcion_atc'] = data['descripcion_atc'].apply(lambda x: lower(x))
                data['descripcion_atc'] = data['descripcion_atc'].apply(lambda x: normalize(x))
                medicamentos = list(data['descripcion_atc'].unique())
                for i in quimios:
                    for medicamento in medicamentos:
                        if medicamento in folios[i]:
                            if leucemia == False:
                                if medicamento == 'dexametasona':
                                    continue                                 
                            encontrados.append(medicamento)
                __61 = str(len(encontrados))
                if 'intratecal' in folios[quimios[0]]:
                    __74 = '1'
                else :
                    __74 = '2'
                if  'termina infusion de quimioterapia sin complicaciones' in folios[quimios[0]]:
                    start = folios[quimios[-1]].find('fecha') + 6
                    end = start + 10
                    fecha = folios[quimios[-1]][start:end]
                    fecha = fecha.split('/')
                    fecha = fecha[::-1]
                    __75 = '-'.join(fecha)                     
                    __76 = '1'
                else : 
                    __76 = '1'
                    # aqui se puede colocar si el paciente murio o si abandono

        else:
            for i in range(len(folios)):
                if ('se inicia protocolo de quimioterapia' in folios[i]) or ('se administra segun protocolo de quimioterapia' in folios[i]) or ('aplica protocolo de quimioterapia' in folios[i]) or ('aplica quimioterapia segun protocolo' in folios[i]) or ('realizar protocolo quimioterapia' in folios[i]) or (' DA INICIO A PROTOCOLO DE QUIMIOTERAPIA'.lower() in folios[i]) or ('ADMINISTRA QUIMIOTERAPIA'.lower() in folios[i]) or ('ADMINISTRA PROTOGOLO DE QUIMIOTERAPIA'.lower() in folios[i]):
                    quimios.append(i)
            if len(quimios)>0 :
                __45 = '1'
                #__46 = str(len(quimios))
                __46 = '98'
                __55 = str(len(quimios))
            else:
                __45 = '98'
                __46 = '98'
                __55 = '98'
            __47 = '97' 
            __48 = '97'
            __49 = '97'
            __50 = '97'
            __51 = '97'
            __52 = '97'
            __53 = '97'
            __54 = '97'
            #__55 = '98'
            __56 = ''
            if len(quimios)>0 :
                start = folios[quimios[0]].find('fecha') + 6
                end = start + 10
                fecha = folios[quimios[0]][start:end]
                fecha = fecha.split('/')
                fecha = fecha[::-1]
                __57 = '-'.join(fecha)
                __58 = '1'
                __59 = '80010054401'
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
                __61 = str(len(encontrados))
                for i in range(12):
                    encontrados.append('97')
                __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73 = encontrados[0],encontrados[1],encontrados[2],encontrados[3],encontrados[4],encontrados[5],encontrados[6],encontrados[7],encontrados[8],encontrados[9],encontrados[10],encontrados[11]
                __74 = "2"
                __75 = "22"
                if 'intratecal' in folios[quimios[0]]:
                    __74 = '1'
                else :
                    __74 = '2'
                if  'termina infusion de quimioterapia sin complicaciones' in folios[quimios[0]]:
                    __76 = '1'
                    start = folios[quimios[0]].find('fecha') + 6
                    end = start + 10
                    fecha = folios[quimios[0]][start:end]
                    fecha = fecha.split('/')
                    fecha = fecha[::-1]
                    __75 = '-'.join(fecha)                
                else : 
                    __76 = 'N/A'
                    __75 = ' '          
            else:
                __57 = '1845-01-01'
                __56 = '98'
                __58 = '98'
                __59 = '98'
                __61 = '98'
                __62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73,__74,__75,__76 = '98','98','98','98','98','98','98','98','98','98','98','98','98','98','98'
                
            __60 = '98'

        if __45 == '98':
            __59 = '98'
        elif __45 == '1':
            __59 = '80010054401'
        else:
            __59 = ' '
            
        if int(__45) == 1 and leucemia == False:
            start = folios[quimios[0]].find('fecha') + 6
            end = start + 10
            fecha = folios[quimios[0]][start:end]
            fecha = fecha.split('/')
            fecha = fecha[::-1]
            __75 = '-'.join(fecha)  
        # ESPERANDO
        
        if int(__45) == 98:
            encontrados2 = []
            folios2 = []
            data_aplica = pd.read_csv('aplica_atc_medicamentos.csv')
            data_aplica['descripcion_atc'] = data_aplica['descripcion_atc'].apply(lambda x: lower(x))
            data_aplica['descripcion_atc'] = data_aplica['descripcion_atc'].apply(lambda x: normalize(x))
            medicamentos2 = list(data_aplica['descripcion_atc'].unique())
            for folio in folios:
                for medicamento2 in medicamentos2:
                    if medicamento2 in folio:
                        encontrados2.append(medicamento2)
                        folios2.append(folio)
            """start = folios2[0].find('fecha') + 6
            end = start + 10
            fecha = folios2[0][start:end]
            fecha = fecha.split('/')
            fecha = fecha[::-1]
            __75 = '-'.join(fecha)"""            
            try:
                __61 = '1'
                __62 = data_aplica[data_aplica['descripcion_atc']==encontrados2[0]]['codigo_atc'].values[0]
                __74 = '2'
            except:
                __61 = '98'
            if len(encontrados2) > 0:
                __45 = '1'
            #__73 = '98'
        return __45,__46,__47,__48,__49,__50,__51,__52,__53,__54,__55,__56,__57,__58,__59,__60,__61,__62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73,__74,__75,__76
    __45,__46,__47,__48,__49,__50,__51,__52,__53,__54,__55,__56,__57,__58,__59,__60,__61,__62,__63,__64,__65,__66,__67,__68,__69,__70,__71,__72,__73,__74,__75,__76 = _45__77_(folios,__17)

    print("-- -- -- -- -- -- -- -- -- -- -- --")





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
        return __78,__55,__80,__81,__82,__83,__84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95,__96,__97,__98,__99
    __78,__55,__80,__81,__82,__83,__84,__85,__86,__87,__88,__89,__90,__91,__92,__93,__94,__95,__96,__97,__98,__99 = _78__99_(folios,__17,__55)







    
    ###############
    ### CIRUGIA ###
    ###############
    dic['159'].clear()
    lista_agregar = ["muerto", "muerte", "fallecio","fallecimiento","fallecido",'pcte fallecio','se declara muerte clinica','paciente fallecido','se declara fallecido','se entrega acta de defuncion','se declara paciente fallecida','fallecida','muerta','declara fallecido','declara fallecida']
    [dic['159'].update({key:'2'}) for key in lista_agregar]
    def _100__111(folios,dic):
        import re
        here = []
        for folio in range(len(folios)):
            if 'descripcon cirugia' in folios[folio]:
                here.append(folio)
        if len(here)!=0:
            __100 = '1'
            __101 = str(len(here))
            folio_1 = here[0]

            start = folios[folio_1].find('fecha') + 6
            end = start + 10
            fecha = folios[folio_1][start:end]
            fecha = fecha.split('/')
            fecha = fecha[::-1]
            __102 = '-'.join(fecha)
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
            __110 = '98'
            __111 = '1'
            
            if len(here)>1:
                folio_2 = here[-1]
                start = folios[folio_2].find('fecha') + 6
                end = start + 10
                fecha = folios[folio_2][start:end]
                fecha = fecha.split('/')
                fecha = fecha[::-1]
                __106 = '-'.join(fecha)
                __107 = '1' # PENDIENTEEE
                __108 = '80010054401'
                n2 = folios[folio_2].find('codigo')
                aux2 = folios[folio_2][n2:]
                start1 = aux2.find('\n')
                codigo_aux2 = aux2[start1+2:start1+13]
                codigo2 = re.findall('[0-9]',codigo_aux2)
                __109 = ''.join(codigo2) 
                __110 = '1' # PENDIENTEEE
                __111 = '1'
                for llave in dic['159'].keys():
                    if llave in folio_2:
                        __111 = '2'
                
                
        else:
            __100 = '2'
            __101 = '98'
            __102 = '1845-01-01'
            __103 = '98'
            __104 = "98"
            __105 = '98'
            #__105 = " "
            __106 = '1845-01-01'
            __107 = '98'
            __108 = '98'
            __109 = '98'
            __110 = '98'
            __111 = '98'
        
        return __100,__101,__102,__103,__104,__105,__106,__107,__108,__109,__110,__111
    __100,__101,__102,__103,__104,__105,__106,__107,__108,__109,__110,__111 = _100__111(folios,dic)




    
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
        braqui = []
        braquiterapia = False
        radio = False 
        folios_r = []
        for folio in folios:
            if'tratamiento de radioterapia' in folio:
                folios_r.append(folio)
        
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
            patron_1 = "[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"
            patron_2 = "[0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
            patron_3 = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
            patron_4 = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9]"
            patrones = (patron_1,patron_2,patron_3,patron_4)  
            match = []          
            for folio in folios_r:
                start = folio.find("inicio tratamiento")
                for patron in patrones:
                    match = re.findall(patron,folio[start:])

            sesiones = re.findall(r"[-+]?\d*\.\d+|\d+ gy",folios_r[0])
            for i in range(len(sesiones)):
                sesiones[i] = sesiones[i].replace("gy","").replace(" ","")
            print( "No de sesiones: ", sesiones )
            
            
            print(match[:])
            try:
                __123,__129 = "20"+"-".join(match[0].split("/")[::-1]),"20"+"-".join(match[1].split("/")[::-1]) #114 # 120
            except:
                __123,__129 = "N/A","N/A" #114 # 120
            print(f"El numero de folios con braqui: {len(braqui)}")
            if braquiterapia:
                print("ESTE PACIENTE TUVO BRAQUITERAPIA")
                for folio in braqui:
                    if "1/4" in folio:
                        fecha_inicio_braqui = re.findall(patron_3,folio)
                        print(fecha_inicio_braqui[0])
                        if "/" in fecha_inicio_braqui[0]:
                            __123 = "-".join(fecha_inicio_braqui[0].split("/")[::-1]) #114
                        else:
                            __123 = "-".join(fecha_inicio_braqui[0].split("-")[::-1]) #114
                        break
                for folio in braqui:
                    if "4/4" in folio:
                        fecha_fin_braqui = re.findall(patron_3,folio)
                        print(fecha_fin_braqui[0])
                        if "/" in fecha_inicio_braqui[0]:
                            __129 = "-".join(fecha_fin_braqui[0].split("/")[::-1]) # 120
                        else:
                            __129 = "-".join(fecha_fin_braqui[0].split("-")[::-1]) # 120
                        break
                
        else:
            __117 = "98"
            __118 = "98"
            __121 = "98"
            __122 = "98"
            __116 = "98"
            __123 = "98" #114
            __129 = "98" # 120
            
            
        print("resultado radioterapia".upper())
        print("__112:", __112)
        print("__116:",__116)

        return __112,__116,__117,__118,__121,__122,__123,__129
    __112,__116,__117,__118,__121,__122,__123,__129 = _112__131(folios,dic)


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
                    fecha = folio[start:end]
                    fecha = fecha.split('/')
                    fecha = fecha[::-1]
                    _147 = '-'.join(fecha)
                    _140 =  "1"
                    _141 = "1"
                    _146 = "1"
                    _148 = "80010054401"

                    
                    break
            if _140 =="1":
                break
        if _140 == None:
            _140 = "2"
            _141 = "2"
            _146 = "2"
            _147 =  "1845-01-01"
            _148 = "98" # "80010054401"
        _142,_143,_144,_145 = ("2","2","2","2")
        
        return _140,_141,_142,_143,_144,_145,_146,_147,_148
    __140,__141,__142,__143,__144,__145,__146,__147,__148 = _140__148(folios)


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
                if 'nutricion' in frag:
                    start = folio.find('fecha') + 6
                    end = start + 10
                    #_152 =  "1"
                    if 'enteral' in folio:
                        _152 = '1'
                    elif 'parenteral' in folio:
                        _152 = '2'
                    elif ('enteral' in folio) and ('parenteral' in folio):
                        _152 = '3'
                    else :
                        _152 = '4' 
                    fecha = folio[start:end]
                    fecha = fecha.split('/')
                    fecha = fecha[::-1]
                    _153 =  '-'.join(fecha)
                    if 'hora' in _153:
                        fecha = folio[end+11:end+21]
                        fecha = fecha.split('/')
                        fecha = fecha[::-1]
                        _153 =  '-'.join(fecha)

                    _155 = "1"
                    _154 = "80010054401"
                    break
            if _152 =="1":
                break
        if _152 == None:
            _152 = "98"
            _155 = "4"
            _153 = "1845-01-01"
        _156 = "98"
        _154 = "98" # "80010054401"
        return _152,_153,_154,_155,_156
    __152,__153,__154,__155,__156 = _152__156(folios)




    print('llegó hasta aqui')




###################################### 
### RESULTADO FINAL DE LA ATENCIÓN ###
######################################

    def _157__166(folios,dic,__45,__100,__112):
        dic['159'].clear()
        lista_agregar = ["muerto", "muerte", "fallecio","fallecimiento","fallecido",'pcte fallecio','se declara muerte clinica','paciente fallecido','se declara fallecido','se entrega acta de defuncion','se declara paciente fallecida','fallecida','muerta','declara fallecido','declara fallecida']
        [dic['159'].update({key:'2'}) for key in lista_agregar]
        
        for key in dic['159'].keys():
            here = findKeyWord(folios[-1],key,5)

            if key in folios[-1]:
                __159 = '2'
                break
            elif key in folios[-2]:
                __159 = '2'
                break
            else:
                __159 = '1'
        

        if __159 == "2": # paciente fallecido    

            __157 = '98'
            __158 = '99'
            __160 = '4'
            __161 = '12' 
            folio = folios[-1]                
            start = folio.find('fecha') + 6
            end = start + 10
            fecha = folio[start:end]
            fecha = fecha.split('/')
            fecha = fecha[::-1]
            __163 = '-'.join(fecha)
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
    __157,__158,__159,__160,__161,__162,__163,__164,__165,__166,__41 = _157__166(folios,dic,__45,__100,__112)










    
    
    __11 = Eps
    __166 = Fcorte

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
        pdf_to_csv(hc[:-4])

        continue
    
    pacientes = glob.glob('HISTORIA*.txt')

    print(' ')
    row = 7
    
    
    f = '2021-01-01'
    eps = 'cura_tu vida'
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
    
    #main("HISTORIA CLÍNICA No.CC 32657114 -- NIDIAN ZENIT POLO ESCORCIA.txt",row,f,eps)




# U --> w
# mv /home/felipeagq/lya/bnndn/altos-costos-backend/backend_2/prueba2.xlsx /mnt/c/Users/'Felipe Gonzalez'/Desktop/pdf/
#
# w -> U
# mv /mnt/c/Users/'Felipe Gonzalez'/Desktop/pdf/prueba2.xlsx /home/felipeagq/lya/bnndn/altos-costos-backend/backend_2/