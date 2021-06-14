import numpy as np
import pandas as pd
import json

'''
# 2 CREACION DEL DICCIONARIO DE PALABRAS DE BD
Segundo paso de Altos Costos:
- Cargamos el dataset.
- Volvemos el dataset un DataFrame nombrando cada columna.
- Normalizamos la data: minuscula y sin acento.
- Generamos un diccionario de toda la data adquirida.
'''
def main():
    # Cargamos la base de datos que se encuentra en BD.npy
    db = np.load("BD.npy",allow_pickle=True) 

    # Volvemos el np.array un DataFrame
    df = pd.DataFrame(db)
    df.drop([0,1,2],axis=0,inplace=True)
    df.reset_index(inplace=True,drop=True)

    # Le damos nombres a las columnas
    columnas = ['id','created_at','update_at','dalete_at','tipo','folio','area','subarea','texto','valor','document_id']
    df.columns = columnas

    # FUNCIONES 

    # Creamos función para transformar todas las letras en minuscula
    def to_lower(texto):
        texto = texto.lower()
        return texto 

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


    # Aplicamos la función para transformar el DataFrame en numerico
    for columna in df.columns:
        try:
            df[columna] = df[columna].apply(lambda x : to_lower(x))
            df[columna] = df[columna].apply(lambda x : normalize(x))
        except:
            continue



    tipos = {}
    for tipo in df['tipo'].unique():
        valores = df[df['tipo']==tipo][['texto','valor']].values
        tipos[str(tipo)] = {}
        for i in range(len(valores)):
            key = valores[i][0]
            value = valores[i][1]
            tipos[str(tipo)][key] = value


    with open("dic_1.json","w") as f:
        json.dump(tipos,f)


if __name__ == '__main__':
    main()
    print("Se corrio como programa principal")