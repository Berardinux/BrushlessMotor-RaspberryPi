import RPi.GPIO as GPIO
import time

# Motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
pinMotor_pwm = GPIO.PWM(8, 50)
pinMotor_pwm.start(0)

try:
    while True:  # Add the while loop to continuously run the motor
        # Set motor speed
        pinMotor_pwm.ChangeDutyCycle(40)
except KeyboardInterrupt:
    pass
finally:
    pinMotor_pwm.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO
