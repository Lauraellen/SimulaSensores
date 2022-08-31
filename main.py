import threading
import time

from db.database import Database
from dataset.Sensores import dataset as sensores


sensores = Database(database="bancoiot", collection="sensores", dataset=sensores)
sensores.resetDatabase()



# def sayHello(nome, intervalo):
#     while True:
#         print(nome, "Say hello")
#         time.sleep(intervalo)
#
#
# x = threading.Thread(target=sayHello, args=('Thread 1', 2))
# x.start()
