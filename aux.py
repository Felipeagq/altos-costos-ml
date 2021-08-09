import re 
texto_1 = "inicio de radioterapia entre el 03-05-1999 y el 07-12-1999"
texto_2 = "inicio de radioterapia entre el 11-11-1111 y el 22-22-2222"
texto_3 = "inicio de radioterapia entre el 11/11/1111 y el 22/22/2222"
textos = (texto_1,texto_2,texto_3)
patron_1 = "[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"
patron_2 = "[0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
patron_3 = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
patron_4 = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9]"
patrones = (patron_1,patron_2,patron_3,patron_4)
match = []
"""for texto in textos:
    for patron in patrones:
        match.append(re.findall(patron,texto))
    match.append("/")

print(match)
print(len(match))"""

print("------------------------------------------------")

texto_4 = "el dia 99 del año el 2.0 Gy dia hasta 44.00 Gy + boost en region 23 anal dosis de 58 Gy  como 6 gy como d".lower()


encontrados = re.findall(r"[-+]?\d*\.\d+|\d+",texto_4)
print( re.findall(r"[-+]?\d*\.\d+|\d+",texto_4) )
gy = []
for encontrado in encontrados:
    print(encontrado)
    gy_encontrado = re.findall(f"{encontrado} gy",texto_4)
    if len(gy_encontrado) > 0:
        gy.append( gy_encontrado[0] )

print(gy)
