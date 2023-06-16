import network
from time import sleep

def connect():
        #Connect to WLAN
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect("emiliomac", "Emilio23")
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)        
        ip = wlan.ifconfig()[0]
        print(f'Connected on {ip}')
        return ip
