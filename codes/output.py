# import serial
# import time

# serialInst = serial.Serial()
# com = '/dev/cu.usbmodem1101'
# serialInst.baudrate = 115200
# serialInst.port = com
# serialInst.open()

# try:
#     with open('log.txt', 'r') as log_file:
#         for line in log_file:
#             command = line.strip()  # Remove any leading/trailing whitespace
#             if command:  # Check if the line is not empty
#                 serialInst.write(command.encode('utf-8'))
#                 print(f"Sent command: {command}")
#                 time.sleep(1)  # Add a small delay if necessary to prevent overwhelming the Arduino
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     serialInst.close()
#     print("Serial connection closed.")
import socket
import time

host = '192.168.188.188'  # Replace with the actual IP address printed by the Arduino
port = 80

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open('log.txt', 'r') as log_file:
            for line in log_file:
                command = line.strip()  # Remove any leading/trailing whitespace
                # if command:  # Check if the line is not empty
                s.sendall(command.encode('utf-8') + b'\n')
                print(f"Sent command: {command}")
                time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")

