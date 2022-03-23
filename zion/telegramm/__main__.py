import zion.telegramm.mqtt as mqtt
import zion.telegramm.bot_telegramm as telega
from threading import *

def _mqtt():
    mqtt.mqtt_start()

def _telegramm():
    print('start')
    telega.start()


t1 = Thread(target=_mqtt, args=())
t2 = Thread(target=_telegramm, args=())

t1.start()
t2.start()


