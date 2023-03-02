import serial
import TurtleToGPIO as turtle

# Set up the serial connection to the Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# Define a function to convert Raspberry Pi commands to Arduino commands
def convert_command(command):
    if command == "LED_ON":
        return "L1"
    elif command == "LED_OFF":
        return "L0"
    elif command == "MOTOR_FORWARD":
        return "M1"
    elif command == "MOTOR_BACKWARD":
        return "M0"
    else:
        return ""

# Wait for a command from the Raspberry Pi and send it to the Arduino
while True:
    command = input("Enter a command: ")
    arduino_command = convert_command(command)
    if arduino_command != "":
        ser.write(arduino_command.encode())

    # Read a response from the Arduino
    response = ser.readline()
    print(response)
