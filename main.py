import time
from config import LOW_WATER_THRESHOLD, HIGH_WATER_THRESHOLD, CHECK_INTERVAL
from alerts import send_alert
from logger import log_status


pump_status = False

def read_water_level():
 
    import random
    return random.randint(0, 100)

def control_pump(water_level):
    global pump_status
    if water_level < LOW_WATER_THRESHOLD and not pump_status:
        pump_status = True
        log_status(f"Pump turned ON. Water level: {water_level}%")
        send_alert("Water level low! Pump turned ON.")
    elif water_level > HIGH_WATER_THRESHOLD and pump_status:
        pump_status = False
        log_status(f"Pump turned OFF. Water level: {water_level}%")
        send_alert("Water tank full! Pump turned OFF.")
    else:
        log_status(f"Pump status unchanged. Water level: {water_level}%")

def main():
    while True:
        water_level = read_water_level()
        print(f"Current water level: {water_level}%")
        control_pump(water_level)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
