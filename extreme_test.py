import sys
sys.path.insert(0, '/home/rae/PyLX-16A-master')
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

def test_motor(servo_id):
    try:
        servo = LX16A(servo_id)
        
        print(f"\nTesting Motor {servo_id}...")

        print(f"Motor {servo_id}: Moving to 0 degrees (minimum)")
        servo.move(0)
        time.sleep(2)
        print(f"Motor {servo_id} position: {servo.get_physical_angle():.1f} deg")

        print(f"Motor {servo_id}: Moving to 240 degrees (maximum)")
        servo.move(240)
        time.sleep(2)
        print(f"Motor {servo_id} position: {servo.get_physical_angle():.1f} deg")

        print(f"Motor {servo_id}: Moving to center (120 degrees)")
        servo.move(120)
        time.sleep(2)
        print(f"Motor {servo_id} position: {servo.get_physical_angle():.1f} deg")

    except ServoTimeoutError:
        print(f"Motor {servo_id}: disconnected or not responding!")
    except ServoChecksumError:
        print(f"Motor {servo_id}: communication error - check wiring!")
    except ServoArgumentError as e:
        print(f"Motor {servo_id}: invalid command - {e}")
    except Exception as e:
        print(f"Motor {servo_id}: unexpected error - {e}")

test_motor(2)
test_motor(3)

print("\nDone!")