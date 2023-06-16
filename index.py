import random
import time
from conect import connect
from mqtt_server import ServerMQTT


try:
    con = connect()
    mqtt = ServerMQTT()

    while True:
        temp = random.randint(20, 100)
        mqtt.publicar(
            "v1/devices/me/telemetry",
            """{
                "temperature": {temp}
            }"""
        )
        time.sleep(3)
except Exception as e:
    print(f'Failed to publish message: {e}')
finally:
    mqtt.disconect()