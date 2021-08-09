import glob
import os
import procesador
import zipfile
from openpyxl import Workbook
from openpyxl import load_workbook
import boto3
import json
import logging
from botocore.exceptions import ClientError
import time
from pdf_to_txt_3 import pdf_to_csv
from dotenv import load_dotenv
load_dotenv()

# Creamos el cliente s3
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")

# Función para crear el LINK de descarga del xlsx
def create_presigned_url(cliente, bucket_name, object_name, expiration=604800):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    # Creamos el link de descarga
    try:
        response = cliente.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    # The response contains the presigned URL
    return response


# Función principal
def main(fecha,eps,cliente_mqtt,hash):
    # Enumeramos todos los archivos .pdf
    hcs = glob.glob('*.pdf')
    n = (len(hcs))*2 +1
    print(f'El numero de total de procentajes{n}')
    actual = 1 
    data = json.dumps({
        "hash":hash,
        "step" : "processing",
        "percentage":'0%',
        "link": " "
    })
    cliente_mqtt.publish(hash,data)    
    for hc in hcs:
        # convertimos los .pdf en .txt
        pdf_to_csv(hc[:-4])
        procentaje = f'{((actual/n) *100)}%'
        data = json.dumps({
            "hash":hash,
            "step" : "processing",
            "percentage":procentaje,
            "link": " "
        })
        cliente_mqtt.publish(hash,data)
        print(hc[:-4])
        actual = actual + 1
    # Enumeramos todos los archivos 'HISTORIA*.txt'
    pacientes = glob.glob('HISTORIA*.txt')
    row = 7
    # Procesamos cada 'HISTORIA*.txt' y lo colocamos en el xlsx
    for paciente in pacientes:
        try:
            procesador.main(paciente,row,fecha,eps)
            print(row,paciente)
            procentaje = f'{((actual/n) *100)}%'
            data = json.dumps({
            "hash":hash,
            "step" : "processing",
            "percentage":procentaje,
            "link": " "
        })
            actual = actual + 1
            cliente_mqtt.publish(hash,data)
            # aqui va el MQTT
        except Exception as e:
            print('-- -- -- -- -- -- -- -- -- -- -- -- -- -- ')
            print(e)
            print(row ,paciente)
            print('-- -- -- -- -- -- -- -- -- -- -- -- -- -- ')
            actual = actual + 1
            continue
        row = row + 1
        
        print('-- -- -- -- -- -- -- -- -- -- -- -- -- -- ')

    # Eliminamos los .pdf del local
    for hc in hcs:
        try:
            os.remove(hc)
        except:
            continue
    
    # creamos el cliente s3
    s3_client = boto3.client("s3",
                        region_name="us-east-1",
                        aws_access_key_id=ACCESS_KEY_ID,
                        aws_secret_access_key=SECRET_ACCESS_KEY
                        )
    
    # Subimos el archivo .pdf al s3
    with open("prueba2.xlsx","rb") as archivo_file:
        data = archivo_file.read()
    # definimos los parametros de subida
    response = s3_client.put_object(
        Body= data,
        Bucket = "macna-data",
        Key= f"pdf-upload/,/MACNA-{eps}-{fecha}.xlsx"
    )
    print(response)
    archivo_file.close()
    # Generamos el link de descarga del xlsx
    print("generamos link")
    link =  create_presigned_url(s3_client,"macna-data",f"pdf-upload/,/MACNA-{eps}-{fecha}.xlsx")
    
    time.sleep(5)
    
    ##Borramos las modificaciones realizadas en el .xlsx
    row = 7
    wb = load_workbook(filename="prueba2.xlsx")
    ws = wb['CAC']
    for i in range(n):
        for i in range(1,167):
            try:
                # Borramos la celda.
                ws.cell(row=row,column=i,value=" ")
            except:
                continue
        row = row + 1
    # Guardamos los cambios realizados
    wb.save("prueba2.xlsx")
    
    ##Eliminamos los 'HISTORIA*.txt' generados
    for paciente in pacientes:
        try:
            os.remove(paciente)
        except:
            continue
    
    # Retornamos el link de descarga del .xlsx
    return link 
    
if __name__=='__main__':
    print("esta corriendo como __main__")


