import paho.mqtt.client as mqtt
import zion.jabber.myJabber as myJabber
import sys, xmpp
import zion.setting as set

client = mqtt.Client()



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe(set.mqtt_topic)
    client.subscribe(set.mqtt_Gateway)



# При получении сообщений по Mqtt
def on_message(client, userdata, msg):
    print(msg.topic+" "+(msg.payload.decode()))
    # if(msg.payload == b'Kirill'):
    #     print("yes")
    if (msg.topic == set.mqtt_Gateway):
        myJabber.send_msg(set.Jab_name, msg.payload)

    # if(msg.payload != b''):
    #     myJabber.send_msg(set.Jab_name,msg.payload)




def publish(topic,msg):
   client.publish(topic, msg)
   #client.publish(set.mqtt_Gateway, msg)




def mqtt_start(): #Запуск mqtt
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(set.mqtt_host, set.mqtt_port)
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

