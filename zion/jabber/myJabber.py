import xmpp
from zion.jabber.jabber_bot import JabberBot
import zion.mqtt.mqtt as mqtt
import zion.setting as set


config = set.jab_config

bot = JabberBot(config['jid'], config['password'])

def message_handler(conn, mess):
    text = mess.getBody()
    user = mess.getFrom()
    reply = text
    conn.send(xmpp.Message(mess.getFrom(), reply))
    print(text)
    mqtt.publish('/jabber',str(text))


def start():
    bot.register_handler('message', message_handler)
    bot.start()


def send_msg(adr,text):
    bot.conn.send(xmpp.Message(adr, str(text.decode())))