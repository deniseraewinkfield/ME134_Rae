import sys
sys.path.insert(0, '/home/rae/PyLX-16A-master')
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    print("Motors connected!")
except ServoTimeoutError as e:
    print(f"Motor not responding: {e}")
    exit()

def move_motor(servo_id, servo, angle):
    """Move a single motor to a given angle"""
    try:
        servo.move(angle)
        time.sleep(0.5)
        print(f"Motor {servo_id} moved to {servo.get_physical_angle():.1f} degrees")
    except ServoTimeoutError:
        print(f"Motor {servo_id} disconnected!")
    except ServoArgumentError:
        print(f"Invalid angle! Must be between 0 and 240 degrees.")

print("\nType 'quit' to exit")
print("Valid angles: 0 to 240 degrees\n")

while True:
    motor = input("Which motor? (2, 3, or 'both'): ").strip()
    if motor == 'quit':
        break

    angle_input = input("Enter angle (0-240): ").strip()
    if angle_input == 'quit':
        break

    try:
        angle = float(angle_input)
        if motor == '2':
            move_motor(2, servo2, angle)
        elif motor == '3':
            move_motor(3, servo3, angle)
        elif motor == 'both':
            move_motor(2, servo2, angle)
            move_motor(3, servo3, angle)
        else:
            print("Invalid motor! Enter 2, 3, or 'both'")
    except ValueError:
        print("Invalid angle! Please enter a number.")

# Return to center on exit
servo2.move(120)
servo3.move(120)
print("Returned to center. Goodbye!")