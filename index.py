import random
import time
from conect import connect
from mqtt_server import ServerMQTT


def subscription(topic, message):
    print (f'Topic {topic} received message {message}') 
     # Debug print out of what was received over MQTT
    """  if message == b'on':
        print("LED ON")
        led.value(1)
    elif message == b'off':
        print("LED OFF")
        led.value(0) """


con = connect()
mqtt = ServerMQTT()

# mqtt.listen(subscription)
# mqtt.subscribe("v1/devices/me/rpc/request/+")

try:
    while True:
        temp = random.randint(20, 100)
        data = {
            "temperature": temp
        }

        """data = {
            "ts": time.time()*1000,
            "values":{
                "temperature": temp
            }
        }"""
        
        mqtt.publicar( "v1/devices/me/telemetry", data )
        time.sleep(10)
        
except Exception as e:
    print(f'Failed to publish message: {e}')
finally:
    mqtt.disconect()