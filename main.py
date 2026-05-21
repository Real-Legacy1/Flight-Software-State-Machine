from enum import Enum
import random
import time

class SystemState(Enum):
    BOOT = "BOOT"
    IDLE = "IDLE"
    ACTIVE = "ACTIVE"
    SAFE_MODE = "SAFE_MODE"

class FlightSystem:
    def __init__(self):
        self.current_state = SystemState.BOOT
        self.temperature = 22.0
        self.battery = 100.0
        self.fault = False


    def boot(self):
        print("Booting...")
        time.sleep(1)
        self.current_state = SystemState.IDLE
        print("System is now IDLE.")

    def generate_telemetry(self):
        print("Generating telemetry...")
        time.sleep(1)
        print("State: " + self.current_state.value +  " | Temperature: " + str(self.temperature) + " | Battery: " + str(self.battery) + " | Fault: " + str(self.fault))