import random
import time
from conect import connect
from mqtt_server import ServerMQTT


con = connect()
mqtt = ServerMQTT()

try:

    while True:
        temp = random.randint(20, 100)
        data = {
                "temperature": temp
            }
        mqtt.publicar( "v1/devices/me/telemetry", data )
        time.sleep(5)
except Exception as e:
    print(f'Failed to publish message: {e}')
finally:
    mqtt.disconect()