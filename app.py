#!/bin/python
import sys
sys.dont_write_bytecode = True
from botocore.retries import bucket
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import os
from dotenv import load_dotenv
# from werkzeug.utils import redirect, send_file
import boto3
import io
import requests
import time
import logging
import json
from botocore.exceptions import ClientError
import main
import paho.mqtt.client as mqtt
import pandas as pd
from flask_mqtt import Mqtt

# Cargamos variables del entorno
load_dotenv()

# Creamos la aplicación en flask
app = Flask(__name__)
CORS(app)

# Creamos el cliente s3
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")
s3_client = boto3.client("s3",
                         region_name="us-east-2",
                         aws_access_key_id=ACCESS_KEY_ID,
                         aws_secret_access_key=SECRET_ACCESS_KEY
                         )

# Guardamos el path actual
path = os.getcwd()


# Creamos función para descargar todos los archivos con un prefijo
def descargar_prefix(prefix, quantity):
    """
    Esta función obtiene todos un listado de todos los files 
    que contienen cierto prefijo, los descarga, 
    los extrae en una carpeta llamada "unpack"
    Y luego elimina los archivos.
    """
    bucket_nombre = "macna-data"
    # listado de los files con el prefijo:
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_nombre, Prefix=prefix)
    quantity = int(quantity)
    print(f"la cantidad es {quantity}")
    bandera = True
    print('pages main:', pages)
    vueltas = 1
    while bandera:
        print(f"voy por la vuelta {vueltas}")
        vueltas += 1
        time.sleep(2)
        count = 0
        for page in pages:
            print(page.keys())
            if 'Contents' in page.keys():
                for obj in page['Contents']:
                    if (obj.get("Key", None) != None):
                        count += 1
                        print(obj.get("Key", None))
                    if (count == quantity):
                        bandera = False
                        print(f"count: {count}, quantity: {quantity}")
            else:
                pages = paginator.paginate(Bucket=bucket_nombre, Prefix=prefix)

    for page in pages:
        print(page.keys())
        for obj in page['Contents']:
            name_file = obj.get("Key", None)
            nombre = os.path.join(path, name_file.split("/")[-1])
            s3_client.download_file(Bucket=bucket_nombre, Key=name_file, Filename=nombre)
            print(f"Archivo {name_file} descargado")


# pdf-upload/2021-07-22 13:06:10.913379
# pdf-upload/2021-07-22 13:04:51.213792
host = 'macna.clinicabonnadona.com'
user, pws = "processing_backend", "b0nn4d0n4"
app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = host
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = user
app.config['MQTT_PASSWORD'] = pws
app.config['MQTT_KEEPALIVE'] = 20
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt(app)


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print('conectado')


@mqtt.on_message()
def handle_messages(client, userdata, message):
    mensaje = message.payload.decode()
    print('el mensaje inicial es:', mensaje)
    time.sleep(2)
    # try:
    mensaje = json.loads(mensaje)
    try:
        fcorte = mensaje['datos']['fcorte']
        eps = mensaje['datos']['eps']
        ref = mensaje['datos']['ref']
        hash = mensaje['datos']['hash']
    except Exception as e:
        print('Entra a la excepcion debido a este error:', e)
        mensaje['datos'] = {}
        mensaje['datos']['fcorte'] = '2022-09-26'
        mensaje['datos']['eps'] = 'Testing'
        mensaje['datos']['ref'] = '045f9ced2e0761b38f4490e798f29a12'
        mensaje['datos']['hash'] = '045f9ced2e0761b38f4490e798f29a12'

    print("MENSAJE")
    print('========================================')
    print('El mnensaje que se muestra entre las barras es:', mensaje)
    print('========================================')

    fcorte = mensaje['datos']['fcorte']
    eps = mensaje['datos']['eps']
    ref = mensaje['datos']['ref']
    hash = '045f9ced2e0761b38f4490e798f29a12'
    mqtt_2 = Mqtt(app)
    mqtt_2._connect()
    while not mqtt_2.connected:
        print('Conectando')
        mqtt_2._connect()
        time.sleep(1)

    link = main.main(fcorte, eps, mqtt_2, hash)
    try:
        print("en el try")
        data = json.dumps({
            "hash": hash,
            "step": "finished",
            "percentage": "100%",
            "page": "done",
            "link": link
        })
        print("en el finally")
        print('hash de la app principal:', hash)
        print('data de la app principal:', data)
        mqtt_2.publish(hash, data)

    except Exception as e:
        print('')
        print("en el except")
        data = json.dumps({
            "hash": hash,
            "step": "failed",
            "percentage": 0,
            "link": " "
        })
        mqtt_2.publish(hash, data)
    # except:
    #     pass


# La primera ruta del backend_2, para verificar que este ok
@app.route("/")
def index():
    return "Hola mundo desde docker en el backend_2"


# Segunda ruta, la cual procesa los .pdf
@app.route("/procesar", methods=["POST"])
@cross_origin()
def procesar():
    print(" ")
    # Cargamos el json
    resp = request.get_json()
    if resp != " ":
        try:
            print('========================================')
            print(resp)
            print('========================================')
            fcorte = resp["fcorte"]
            print(fcorte)
            eps = resp['eps']
            print(eps)
            hash = resp['hash']
            print(hash)
            prefix = f"pdf-upload/{hash}"
            print("Aqui suenaaaa-----")
            print(prefix)
            hash = resp['hash']
            quantity = resp['quantity']
            print(quantity)
            mqtt.subscribe(hash)
            print("subscrito")
            time.sleep(2.1)
            data1 = json.dumps({
                "hash": hash,
                "step": "Downloading pdf",
                "percentage": " ",
                "link": " "
            })
            mqtt.publish(hash, data1)
            descargar_prefix(prefix, quantity)
            time.sleep(2.1)
            data3 = json.dumps({
                "hash": hash,
                "step": "pdf Downloadead",
                "percentage": " ",
                "link": " "
            })
            mqtt.publish(hash, data3)

            data2 = json.dumps({"datos": {
                "fcorte": fcorte,
                "eps": eps,
                "ref": hash,
                "hash": hash
            }})
            print("La petición llegó correctamente")
            mqtt.publish(hash, data2)
        except Exception as e:
            print("el error es: ")
            print(f"{e}")
            print(e.__class__, "400")
            return "400"
    else:
        print("400")
        return "400"
    return "200 si llego"


if __name__ == "__main__":
    app.run(debug=True,
            host="localhost",
            # host="0.0.0.0",
            port=6062)
    mqtt.init_app(app)
