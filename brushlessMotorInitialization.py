import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
pinMotor_pwm = GPIO.PWM(37, 50)  # 50Hz PWM frequency
pinMotor_pwm.start(0)

def set_motor_speed(duty_cycle):
    pinMotor_pwm.ChangeDutyCycle(duty_cycle)

try:
    # Initialization sequence for ESC
    print("Initializing ESC...")

    # Step 1: Send high signal to arm the ESC (full throttle)
    set_motor_speed(10)  # 10% duty cycle (full throttle)
    time.sleep(2)  # wait for 2 seconds

    # Step 2: Send low signal to arm the ESC (minimum throttle)
    set_motor_speed(5)  # 5% duty cycle (minimum throttle)
    time.sleep(2)  # wait for 2 seconds

    print("ESC armed and ready to control the motor.")

    # Now you can set the motor speed
    set_motor_speed(7.5)  # Adjust this value to control speed (7.5% is typically mid-point)
    time.sleep(4)  # Run for 4 seconds

except KeyboardInterrupt:
    pass
finally:
    pinMotor_pwm.stop()
    GPIO.cleanup()
    print("GPIO cleaned up.")
