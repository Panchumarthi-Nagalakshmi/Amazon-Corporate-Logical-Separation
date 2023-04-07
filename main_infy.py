import paho.mqtt.client as mqtt

infy_server='54.74.237.95'
infy_port=1884
client=mqtt.Client()
client.connect(infy_server,infy_port)
client.publish('infy/data','hi')

client.subscribe('B7/data')

def notification(client,userdata,msg):
    t=msg.payload
    t=t.decode('utf-8')
    print(t)

client.on_message=notification
client.loop_forever()
