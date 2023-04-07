import paho.mqtt.client as mqtt

tcs_server='172.31.31.169'
tcs_port=1883
client=mqtt.Client()
client.connect(tcs_server,tcs_port)

client.subscribe('tcs/data')

def publishMessage(k):
    client.publish('B7/data',k)

def notification(client,userdata,msg):
    t=msg.payload
    t=t.decode('utf-8')
    print(t)
    publishMessage('TCS')

client.on_message=notification
client.loop_forever()
