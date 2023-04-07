import paho.mqtt.client as mqtt

tcs_server='54.74.220.214'
tcs_port=1883
client=mqtt.Client()
client.connect(tcs_server,tcs_port)
client.publish('tcs/data','hi')

client.subscribe('B7/data')

def notification(client,userdata,msg):
    t=msg.payload
    t=t.decode('utf-8')
    print(t)

client.on_message=notification
client.loop_forever()
