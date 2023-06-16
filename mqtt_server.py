# Fill in your Adafruit IO Authentication and Feed MQTT Topic details
from lib.umqtt.simple import MQTTClient

class ServerMQTT:
    mqtt_host = "mqtt.thingsboard.cloud"
    mqtt_username = "NzL2dxqmi3OJ3IQUmaZg"  # Your Adafruit IO username

    def __init__(self):
        self.mqtt_client = MQTTClient( 
            client_id="06d2c110-0bdc-11ee-af14-175a6432e834",
            server = self.mqtt_host,
            user = "NzL2dxqmi3OJ3IQUmaZg",
            password = "",
            port = 1883
        )
        self.mqtt_client.connect()

    def publicar(self,topic,data):
        msg = str(data)
        print(f"data:{msg}")
        self.mqtt_client.publish(topic,msg)

    def disconect(self):
        self.mqtt_client.disconnect()


""" 
# Enter a random ID for this MQTT Client
# It needs to be globally unique across all of Adafruit IO.
# mqtt_client_id = "somethingreallyrandomandunique123"
mqtt_client_id = ""

# Initialize our MQTTClient and connect to the MQTT server  
mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=mqtt_username,
        password=mqtt_password)

mqtt_client.connect()

#  mqtt pub -t 'v1/devices/me/telemetry' -h 'mqtt.thingsboard.cloud' -p '1883' -u 'hjUTU84ehdAOfvhzXsNJ' -m {"temperature":25} """