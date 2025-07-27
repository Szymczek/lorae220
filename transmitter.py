import time
import serial

SERIAL_PORT = '/dev/serial0'
BAUD_RATE = 9600
SEND_INTERVAL = 5  
MESSAGE_TO_SEND = b"AUTO" 

try:
    lora = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE)

    while True:
        print(f"Sending message: {MESSAGE_TO_SEND.decode()}")
        lora.write(MESSAGE_TO_SEND)

        time.sleep(SEND_INTERVAL)

except KeyboardInterrupt:
    print("\nProgram stopped.")

finally:
    if 'lora' in locals() and lora.is_open:
        lora.close()
    print("Serial port closed.")