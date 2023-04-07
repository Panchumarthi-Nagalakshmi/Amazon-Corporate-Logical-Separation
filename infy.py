import paho.mqtt.client as mqtt

infy_server='172.31.23.99'
infy_port=1884
client=mqtt.Client()
client.connect(infy_server,infy_port)

client.subscribe('infy/data')

def publishMessage(k):
    client.publish('B7/data',k)

def notification(client,userdata,msg):
    t=msg.payload
    t=t.decode('utf-8')
    print(t)
    publishMessage('INFOSYS')

client.on_message=notification
client.loop_forever()
