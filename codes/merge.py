import serial
import matplotlib.pyplot as plt
import time

ser = serial.Serial('/dev/cu.usbmodem1201', 115200)

# Initialize variables for previous coordinates
prev_x, prev_y = 3, 3

# Hard-coded square coordinates
square_coords = [(3, 3), (3, 10), (10, 10), (10, 3), (3, 3)]

def send_command(command, cali=False):
    command_str = f"{command}_cali" if cali else command
    try:
        with open('log.txt', 'a') as log_file:
            log_file.write(f"{command_str}\n")
        print(f"Sending command: {command_str}")
    except Exception as e:
        print(f"Failed to send command: {command_str}. Error: {e}")

def check_and_send_command(x, y):
    if y == 3 and (x >= 3 and x < 10):
        command = "EAST_TIP"
    elif x == 10 and (y >= 3 and y < 10):
        command = "NORTH_TIP"
    elif y == 10 and (x > 3 and x <= 10):
        command = "WEST_TIP"
    elif x == 3 and (y > 3 and y <= 10):
        command = "SOUTH_TIP"
    else:
        command = "UNKNOWN_TIP_OFF"

    send_command(command)

def correct_path(x, y):
    if (1<=x < 3) or (8<=x<10) and (3<=y<=10):
        send_command("EAST_TIP_OFF")
        time.sleep(0.5)
        verify_movement("EAST_TIP_OFF", x, y)
    elif (12>=x > 10) or (5>=x>3) and (3<=y<=10):
        send_command("WEST_TIP_OFF")
        time.sleep(0.5)
        verify_movement("WEST_TIP_OFF", x, y)
    elif (1<=y < 3) or (8<=y<10) and  (3<=x<=10):
        send_command("NORTH_TIP_OFF")
        time.sleep(0.5)
        verify_movement("NORTH_TIP_OFF", x, y)
    elif (12>= y > 10) or (5>=y>3) and (3<=x<=10):
        send_command("SOUTH_TIP_OFF")
        time.sleep(0.5)
        verify_movement("SOUTH_TIP_OFF", x, y)

def verify_movement(command, initial_x, initial_y):
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            coords = line.split(',')
            if len(coords) == 2:
                y, x = int(coords[0]), int(coords[1])
                if command == "EAST_TIP_OFF" and x > initial_x:
                    break
                elif command == "WEST_TIP_OFF" and x < initial_x:
                    break
                elif command == "NORTH_TIP_OFF" and y < initial_y:
                    break
                elif command == "SOUTH_TIP_OFF" and y > initial_y:
                    break
                elif x != initial_x or y != initial_y:
                    break
                print("Movement not detected, repeating command")
                send_command(command, cali=True)
                time.sleep(0.5)

def calibrate():
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            coords = line.split(',')
            if len(coords) == 2:
                y, x = int(coords[0]), int(coords[1])  # Swap x and y for plotting
                print(f"Current coordinates during calibration: {x}, {y}")
                if x == 3 and y == 3:
                    print("Calibration complete. Reached (3, 3)")
                    break
                initial_x, initial_y = x, y
                if x > 3:
                    send_command("WEST", cali=True)
                elif x < 3:
                    send_command("EAST", cali=True)
                elif y > 3:
                    send_command("SOUTH", cali=True)
                elif y < 3:
                    send_command("NORTH", cali=True)
                time.sleep(0.5)  # Simulate a delay for movement
                
                # Read the coordinates again to ensure movement
                line = ser.readline().decode('utf-8').strip()
                if line:
                    coords = line.split(',')
                    if len(coords) == 2:
                        y, x = int(coords[0]), int(coords[1])
                        if x == initial_x and y == initial_y:
                            print("Movement not detected, repeating command")
                            continue  # Repeat the command

if __name__ == "__main__":
    try:
        plt.figure()
        plt.title('Coordinates Graph with Arrows and Square')
        plt.xlabel('X')
        plt.ylabel('Y')
        
        # Plot the hard-coded square
        square_x, square_y = zip(*square_coords)
        plt.plot(square_x, square_y, 'r-', label='Hard-coded Square')
        
        calibrated = False
        
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                coords = line.split(',')
                if len(coords) == 3:
                    y, x, butt = int(coords[0]), int(coords[1]), int(coords[2])   # Swap x and y for plotting
                    print(f"Current coordinates: {x}, {y}")
                    if not calibrated and input("Press 'c' to calibrate: ").lower() == 'c':
                        calibrate()
                        calibrated = True  # Set the flag to indicate calibration is done
                    elif calibrated:
                        check_and_send_command(x, y)
                        if x != 0 or y != 0:  # Skip (0, 0) coordinates
                            if prev_x is not None and prev_y is not None:
                                if x != prev_x or y != prev_y:
                                    plt.annotate('', xy=(x, y), xytext=(prev_x, prev_y),
                                                 arrowprops=dict(arrowstyle='->', color='b', lw=2),
                                                 annotation_clip=False)
                                if x < 3 or x > 10 or y < 3 or y > 10:
                                    correct_path(x, y)
                        
                            prev_x, prev_y = x, y
                        
                            plt.plot(x, y, 'bo')  # Plot current point
                            plt.pause(0.1)  # Pause to allow plot to update
                    
        plt.legend()
        plt.show()

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()
        with open('log.txt', 'w') as log_file:
            log_file.write("") 
