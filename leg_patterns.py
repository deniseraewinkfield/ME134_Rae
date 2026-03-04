import sys
sys.path.insert(0, '/home/rae/PyLX-16A-master')
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:
    servo2 = LX16A(2)
    servo3 = LX16A(3)
except ServoTimeoutError as e:
    print(f"Motor not responding: {e}")
    exit()

def walking_gait(cycles=3):
    """Alternating leg movement to simulate walking"""
    print("--- Pattern 1: Walking Gait ---")
    try:
        for i in range(cycles):
            servo2.move(60)
            servo3.move(180)
            time.sleep(0.5)
            servo2.move(120)
            servo3.move(60)
            time.sleep(0.5)
        print("Walking gait complete!")
    except ServoTimeoutError:
        print("Motor disconnected during walking gait!")

def kick(cycles=3, speed=0.05):
    """Simulate a kicking/swing motion"""
    print("--- Pattern 3: Kick/Swing ---")
    try:
        for i in range(cycles):
            # Wind up
            for angle in range(120, 60, -5):
                servo2.move(angle)
                servo3.move(angle)
                time.sleep(speed)
            # Kick forward fast
            servo2.move(200)
            servo3.move(200)
            time.sleep(0.3)
            # Return to center
            for angle in range(200, 120, -5):
                servo2.move(angle)
                servo3.move(angle)
                time.sleep(speed)
            time.sleep(0.5)
        print("Kick complete!")
    except ServoTimeoutError:
        print("Motor disconnected during kick!")

def slow_crouch():
    """Slowly lower and raise the leg"""
    print("--- Pattern 2: Slow Crouch ---")
    try:
        for angle in range(120, 60, -5):
            servo2.move(angle)
            servo3.move(angle)
            time.sleep(0.05)
        time.sleep(1)
        for angle in range(60, 120, 5):
            servo2.move(angle)
            servo3.move(angle)
            time.sleep(0.05)
        print("Slow crouch complete!")
    except ServoTimeoutError:
        print("Motor disconnected during slow crouch!")

# Run patterns
#time.sleep(5)
#walking_gait(cycles=3)
time.sleep(3)
kick(cycles=3, speed=0.05)

# Return to center
servo2.move(120)
servo3.move(120)
print("\nDone!")