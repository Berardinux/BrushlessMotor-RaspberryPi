from gpiozero import PWMOutputDevice
import time

# Pin definitions
PIN = 26  # GPIO 26 corresponds to physical pin 37

# Initialize PWM device with 50Hz frequency
motor = PWMOutputDevice(PIN, frequency=50)

def set_motor_speed(duty_cycle):
    """Sets the motor speed with the given duty cycle (0.0 to 1.0)."""
    motor.value = duty_cycle / 1000  # Convert percentage to a value between 0 and 1
    print(f"Set motor speed to {duty_cycle}%")

try:
    for i in range(100, 60, -1):
        set_motor_speed(i)
        time.sleep(.5)

    for i in range (60, 100, +1):
        set_motor_speed(i)
        time.sleep(.5)
    
    set_motor_speed(100)
    time.sleep(5)

except KeyboardInterrupt:
    pass
finally:
    motor.value = 0  # Stop PWM
    print("GPIO cleaned up.")

