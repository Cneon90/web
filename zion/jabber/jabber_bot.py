import sys, xmpp

class JabberBot: #создаём класс нашего бота
    def __init__(self, jid, password):
        jid = xmpp.JID(jid)
        self.user, self.server, self.password = jid.getNode(), jid.getDomain(), password
        self.connect()
        self.auth()

    def connect(self): #функция подключения к серверу
        self.conn = xmpp.Client(self.server,debug = []) #
        conn_result =  self.conn.connect() #  self.conn.connect(('192.168.10.118',6000),)
        if not conn_result:
            print("Can't connect to server!\n")
            sys.exit(1)

    def auth(self): #аутентификация
        print(self.user)
        print(self.password)
        print(self.server)
        auth_result = self.conn.auth(self.user, self.password,sasl=1)
        if not auth_result:
            print("Can't to authorize!\n")
            sys.exit(1)

    def register_handler(self, name, handler): #привязка функций к событиям
        self.conn.RegisterHandler(name, handler)

    def step_on(self):
        try:
            self.conn.Process(1)
        except KeyboardInterrupt: return 0
        return 1

    def start(self):
        self.conn.sendInitPresence()

        while self.step_on(): pass