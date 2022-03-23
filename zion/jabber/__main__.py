import zion.jabber.mqtt as mqtt
import zion.jabber.myJabber as myJabber
from threading import *



def _mqtt():
    mqtt.mqtt_start()

def _jabber():
    myJabber.start()





t1 = Thread(target=_mqtt, args=())
t2 = Thread(target=_jabber, args=())

t1.start()
t2.start()


