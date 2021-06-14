# PROCESO EN GENERAL 
1. Nos conectamos  a la base de datos.
2. A partir del dataset creamos un diccionario de {"texto":\["area","valor"]}
3. Convertimos el historial clinico de .pdf a .txt, dando indicaciones de separación por area y por folio.


# DOCUMENTOS EN GENERAL
1. hist_clinicas.ipynb veo el data set de historias clinicas
2. NNtrain.ipynb  recojo el texto de todas las historias clinicas en texto y creo el index_word, el reverse_index_word y la lista de palabras por cada seccion tanto en letras como en numeros. Prepocesar la data para entrenar la red neuronal.
3. masked_pdf.ipynb ya empiezo a sacar los datos del pdf


