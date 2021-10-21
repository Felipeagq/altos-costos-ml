####################
### RADIOTERAPIA ###
####################
import re


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

    if __112 == "98":
        __115 = "98"
        __124 = "98"
    if __112 == "1":
        __115 = " "
        __124 = " "

    return __112,__113,__114,__115,__116,__117,__118,__120,__121,__122,__124