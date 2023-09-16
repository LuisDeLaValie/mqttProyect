# Fill in your Adafruit IO Authentication and Feed MQTT Topic details
from lib.umqtt.simple import MQTTClient

class ServerMQTT:

    def __init__(self):
        self.mqtt_client = MQTTClient( 
            client_id="",
            server = "mqtt.thingsboard.cloud",
            user = "1Icqq9M1e7HEDzt7g8ip",
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

