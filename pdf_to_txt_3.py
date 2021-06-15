# Importamos la libreria
import fitz
import cv2
import os
import sys
import pandas as pd
import pytesseract

"""
# 3 GENERAR EL TEXTO A PARTIR DEL PDF
Tercer paso de Altos Costos:
- Tomamos el historial clinico en PDF y generamos un archivo de texto
colocando "==>" en cada FOLIO y colocando "$$" en cada seccion 
""" 


def normalize(s):
    de = ['MOTIVO DE CONSULTA',
        'ENFERMEDAD ACTUAL',
        'EXAMEN',
        'ANÁLISIS',
        'PLAN Y MANEJO',
        'DIAGNÓSTICO',
        'ORDENES',
        'ÓRDENES',
        'INTERCONSULTAS',
        'NOTAS ENFERMERIA',
        'FORMULA MÉDICA',
        'FORMATOS',
        'RECOMENDACIONES',
        'NOTA DE INGRESO',
        'OBSERVACIONES']
    a = ['$$MOTIVO DE CONSULTA',
        '$$ENFERMEDAD ACTUAL',
        '$$EXAMEN',
        '$$ANÁLISIS',
        '$$PLAN Y MANEJO',
        '$$DIAGNÓSTICO',
        '$$ORDENES',
        '$$ÓRDENES',
        '$$INTERCONSULTAS',
        '$$NOTAS ENFERMERIA',
        '$$FORMULA MÉDICA',
        '$$FORMATOS',
        '$$RECOMENDACIONES',
        '$$NOTA DE INGRESO',
        '$$OBSERVACIONES']
    replacements = (zip(de,a) )
    for a, b in replacements:
        s = s.replace(a, b)
    return s



def pdf_to_csv(documento):
    # Ruta del documento de pdf
    pdf_documento = '{}.pdf'.format(documento)

    # Creamos el objeto del documento de pdf abierto
    documento = fitz.open(pdf_documento)

    # Guardamos la pagina 0 como imagen 
    page = documento[0]
    pix = page.get_pixmap()
    pix.writeImage("page-{}.png".format(page.number))

    imagen = cv2.imread('page-{}.png'.format(page.number))
    (x,y,w,h,x2,y2) = 0,0, imagen.shape[1], 230, imagen.shape[1], imagen.shape[0]
    superior = imagen[y:y+h,x:x+w]
    cv2.imwrite('superior.png',superior)

    imagen = cv2.imread('superior.png')
    imagen = cv2.resize(imagen,(1268,460)) 
    text = pytesseract.image_to_string(imagen,lang='spa')

    paciente = text[text.index('HISTORIA CLÍNICA No.'):text.index('HISTORIA CLÍNICA No.') + text[text.index('HISTORIA CLÍNICA No.'):].index('\n')]
    print(paciente)

    texto = text
    #texto = texto.lower()
    texto = texto.replace("Afiliado","\nAfiliado")
    texto = texto.replace("Edad actual","\nEdad actual")
    texto = texto.replace("Sexo","\nSexo")
    texto = texto.replace("Grupo Sanguíneo","\nGrupo Sanguíneo")
    texto = texto.replace("Estado Civil","\nestado civil")
    texto = texto.replace("Dirección","\nDirección")
    texto = texto.replace("Departamento","\nDepartamento")
    texto = texto.replace("Ocupacion","\nOcupacion")
    texto = texto.replace("Grupo Etnico","\nGrupo Etnico")
    texto = texto.replace("Atención Especial","\nAtención Especial")
    texto = texto.replace("\n\nDiscapacidad","\nDiscapacidad")
    texto = texto.replace("Grupo Poblacional","\nGrupo Poblacional")
    print(texto)
    file = open(f"{paciente}.txt","w")
    file.write(texto)
    file.close()

    texto = []
    documento = fitz.open(pdf_documento)
    paginas = len(documento)
    for pagina in range(0,paginas):
        page = documento[pagina]
        pix = page.get_pixmap()
        pix.writeImage("page-{}.png".format(page.number))
        imagen = cv2.imread('page-{}.png'.format(page.number))
        (x,y,w,h,x2,y2) = 0,0, imagen.shape[1], 230, imagen.shape[1], imagen.shape[0]
        inferior = imagen[y+h:y2,x:x+w]
        cv2.imwrite('inferior.png',inferior)
        imagen = cv2.imread('inferior.png')
        imagen = cv2.resize(imagen,(2377,2190)) 
        text = pytesseract.image_to_string(imagen,lang='spa')
        texto.append(text)
        if os.path.exists("page-{}.png".format(page.number)):
            os.remove("page-{}.png".format(page.number))

    if os.path.exists("inferior.png"):
        os.remove("inferior.png")
    if os.path.exists("superior.png"):
        os.remove("superior.png")

    file = open(f"{paciente}.txt","a")
    for text in texto:
        text = normalize(text)
        file.write(text.replace('FOLIO','==> FOLIO'))
    file.close()


if __name__=='__main__':
    pdf_to_csv('CC 929904 HC')

    