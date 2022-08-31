import threading
import time

from db.database import Database
from dataset.Sensores import dataset as sensores


sensores = Database(database="bancoiot", collection="sensores", dataset=sensores)
sensores.resetDatabase()

def setTemperature(temperature, intervalo, nameSensor):
    #SETA O SENSOR PARA FALSO NO INICIO
    response = sensores.collection.find_one_and_update({"nomeSensor": nameSensor},
       {"$set": {
           "sensorAlarmado": False
       }}, upsert=True)

    while temperature <= 38:
        temperature = temperature + 8
        response = sensores.collection.find_one_and_update({"nomeSensor": nameSensor},
        {"$set": {
            "valorSensor": temperature
        }},        upsert= True)

        print("Temperatura atual no sensor", nameSensor,":",temperature)
        time.sleep(intervalo)
    else:
        print("Atenção! Temperatura muito alta! Verificar Sensor", nameSensor)
        response = sensores.collection.find_one_and_update({"nomeSensor": nameSensor},
           {"$set": {
               "sensorAlarmado": True
           }}, upsert=True)

sensorA = threading.Thread(target=setTemperature, args=(30, 10, 'SensorA'))
sensorA.start()

sensorB = threading.Thread(target=setTemperature, args=(25, 10, 'SensorB'))
sensorB.start()

sensorC = threading.Thread(target=setTemperature, args=(23, 10, 'SensorC'))
sensorC.start()