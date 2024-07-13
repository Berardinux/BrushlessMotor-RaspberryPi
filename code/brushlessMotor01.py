from gpiozero import PWMOutputDevice
import time

# Pin definitions
PIN = 26  # GPIO 26 corresponds to physical pin 37

# Initialize PWM device with 50Hz frequency
motor = PWMOutputDevice(PIN, frequency=50)

def set_motor_speed(duty_cycle):
    """Sets the motor speed with the given duty cycle (0.0 to 1.0)."""
    motor.value = duty_cycle / 100  # Convert percentage to a value between 0 and 1
    print(f"Set motor speed to {duty_cycle}%")

try:
    # Initialization sequence for ESC
    print("Initializing ESC...")

    # Step 1: Send high signal to arm the ESC (full throttle)
    set_motor_speed(10)  # 10% duty cycle (full throttle)
    time.sleep(2)  # wait for 2 seconds
    print("Step 1 complete: Full throttle signal sent")

    # Step 2: Send low signal to arm the ESC (minimum throttle)
    set_motor_speed(5)  # 5% duty cycle (minimum throttle)
    time.sleep(2)  # wait for 2 seconds
    print("Step 2 complete: Minimum throttle signal sent")

    print("ESC armed and ready to control the motor.")

    # Now you can set the motor speed
    set_motor_speed(7.5)  # Adjust this value to control speed (7.5% is typically mid-point)
    time.sleep(4)  # Run for 4 seconds
    print("Motor running at 75% speed for 4 seconds")

except KeyboardInterrupt:
    pass
finally:
    motor.value = 0  # Stop PWM
    print("GPIO cleaned up.")

