from gpiozero import PWMOutputDevice
import time

# Pin definitions
PIN = 26  # GPIO 26 corresponds to physical pin 37

# Initialize PWM device with 50Hz frequency
motor = PWMOutputDevice(PIN, frequency=50)

print("Full throttle")
motor.value = .1
time.sleep(2)

print("Half Speed")
motor.value = .09
time.sleep(4)

print("Low Speed")
motor.value = .08
time.sleep(4)

motor.value = 0  # Stop PWM
print("GPIO cleaned up.")