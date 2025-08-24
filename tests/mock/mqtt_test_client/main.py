import paho.mqtt.client as mqtt
from tests.mock.api_test_server.main import TEST_MAC_ADDR_1, TEST_MAC_ADDR_2
import time
import threading
import json

BROKER = "localhost"
PORT = 1883
USERNAME = "firmware-server-dev"
PASSWORD = "test123"

class FlashingSimulator:
    def __init__(self, client, mac_addr):
        self.client = client
        self.mac_addr = mac_addr
        self.status_topic = f"{mac_addr}/flashing/status"
        self.is_running = False
    
    def start_flashing_simulation(self):
        if self.is_running:
            print(f"Flashing simulation already running for {self.mac_addr}")
            return
        
        self.is_running = True
        thread = threading.Thread(target=self._simulate_flashing, daemon=True)
        thread.start()
    
    def _simulate_flashing(self):
        try:
            print(f"Starting flashing simulation for {self.mac_addr}")
            start_time = time.time()
            
            # Initial status
            self.client.publish(self.status_topic, "flashing")
            time.sleep(2)
            
            # Intermediate status
            self.client.publish(self.status_topic, "idle")
            time.sleep(3)
            
            # Final status (50/50 chance of success/failure)
            elapsed = time.time() - start_time
            final_status = "done" if int(elapsed) % 2 == 0 else "failed"
            self.client.publish(self.status_topic, final_status)
            
            print(f"Flashing simulation completed for {self.mac_addr}: {final_status}")
        finally:
            self.is_running = False

# Global simulators
simulators = {}

def on_message(client, userdata, msg):
    print(f"Received message on topic: {msg.topic}")
    
    topic_parts = msg.topic.split('/')
    if len(topic_parts) < 2:
        print(f"Invalid topic format: {msg.topic}")
        return
        
    mac_addr = topic_parts[0]
    command = topic_parts[1]
    
    if mac_addr not in [TEST_MAC_ADDR_1, TEST_MAC_ADDR_2]:
        print(f"Unknown MAC address: {mac_addr}")
        return
    
    if command == "firmware":
        # Initialize simulator if not exists
        if mac_addr not in simulators:
            simulators[mac_addr] = FlashingSimulator(client, mac_addr)
        
        # Start flashing simulation (non-blocking)
        simulators[mac_addr].start_flashing_simulation()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully")
        client.subscribe(f"{TEST_MAC_ADDR_1}/firmware")
        client.subscribe(f"{TEST_MAC_ADDR_2}/firmware")
        print(f"Subscribed to firmware topics for {TEST_MAC_ADDR_1} and {TEST_MAC_ADDR_2}")
    else:
        print(f"Failed to connect to MQTT broker, return code {rc}")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection from MQTT broker")

def __main__():
    print("Starting MQTT test client...")
    
    client = mqtt.Client(client_id="mqtt_test_client")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.username_pw_set(username=USERNAME, password=PASSWORD)
    
    try:
        client.connect(BROKER, PORT, 60)
        client.loop_start()
        
        print("MQTT client started. Publishing keepalive messages...")
        
        # Publish keepalive messages every 5 seconds
        while True:
            client.publish(f"{TEST_MAC_ADDR_1}/keepalive", "ping")
            client.publish(f"{TEST_MAC_ADDR_2}/keepalive", "ping")
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nReceived interrupt signal, shutting down...")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        print("Cleaning up...")
        client.loop_stop()
        client.disconnect()
        print("MQTT test client stopped")

if __name__ == "__main__":
    __main__()