# Fill in your Adafruit IO Authentication and Feed MQTT Topic details
from lib.umqtt.simple import MQTTClient

class ServerMQTT:

    def __init__(self):
        self.mqtt_client = MQTTClient( 
            client_id="b85ad470-0ef9-11ee-b46c-d528757047e3",
            server = "mqtt.thingsboard.cloud",
            user = "43hDdUt1v13Q4y2EQ4Ly",
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

    def subscribe(self,topic):
        self.mqtt_client.subscribe(topic)
    
    def listen(self,callback):
        self.mqtt_client.set_callback(callback)



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