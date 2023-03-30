import serial
import time
import keyboard

# Set up serial communication
print("Program starting...")
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Delay for the Arduino to initialize
time.sleep(2)
print("Connection established!")
# Run continuously
while True:
    if keyboard.is_pressed('w'):
        ser.write(bytes([0x01]))  # Send byte 0x01 to move forward
    elif keyboard.is_pressed('s'):
        ser.write(bytes([0x02]))  # Send byte 0x02 to move backward
    elif keyboard.is_pressed('a'):
        ser.write(bytes([0x03]))  # Send byte 0x03 to strafe left
    elif keyboard.is_pressed('d'):
        ser.write(bytes([0x04]))  # Send byte 0x04 to strafe right
    elif keyboard.is_pressed('q'):
        ser.write(bytes([0x05]))  # Send byte 0x05 to rotate left (counter-clockwise)
    elif keyboard.is_pressed('e'):
        ser.write(bytes([0x06]))  # Send byte 0x06 to rotate right (clockwise)
    else:
        ser.write(bytes([0x00]))  # Send byte 0x00 to stop movement

    # Delay for arduino to respond
    time.sleep(0.1)
