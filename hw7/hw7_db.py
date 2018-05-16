import paho.mqtt.db as mqtt

def onConnect(db, data, flags, rc):
    print('Connected with result code {}'.format(rc))
    db.subscribe('request')
def onMessage(db, data, msg):
    print(msg.topic, msg.payload)
    if msg.payload == b'request':
        db.publish('goods', '雞包紙包雞 $80')

def mqttSetup():
    global db
    db = mqtt.Client()
    db.on_connect = onConnect
    db.on_message = onMessage
    db.connect('localhost', 1883, 60)
def mqttLoop():
    global db
    db.loop_forever()

if __name__ == '__main__':
    mqttSetup()
    mqttLoop()
