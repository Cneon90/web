import zion.mqtt.mqtt as mqtt
import zion.jabber.myJabber as myJabber
import zion.telegramm.bot_telegramm as telegramm

from threading import *

def _mqtt():
    mqtt.mqtt_start()

def _jabber():
    myJabber.start()

def _telegramm():
    telegramm.start()


Tmqtt = Thread(target=_mqtt, args=())
Tjabber = Thread(target=_jabber, args=())
Ttelegramm = Thread(target=_telegramm, args=())

Tmqtt.start()
Tjabber.start()
Ttelegramm.start()
