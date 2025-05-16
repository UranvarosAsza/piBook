import time
import board
import digitalio

OnboardLed = digitalio.DigitalInOut(board.LED)
Led1 = digitalio.DigitalInOut(board.IO12)
Led2 = digitalio.DigitalInOut(board.IO1)
Led3 =  digitalio.DigitalInOut(board.IO10)
#leds = LED(led_pin=[board.IO12, board.IO1,board.IO10, ])   
OnboardLed.switch_to_output()
Led1.switch_to_output()
Led2.switch_to_output()
Led3.switch_to_output()
##print(dir(board))

while True:
    OnboardLed.value = True
    print("Onboard LED Blinks")
    time.sleep(1)
    OnboardLed.value = False
    time.sleep(2)

    Led1.value = True
    print("Led 1 LED Blinks") #Középső
    time.sleep(1)
    Led1.value = False
    time.sleep(2)

    Led2.value = True
    print("Led 2 LED Blinks") #caps
    time.sleep(1)
    Led2.value = False
    time.sleep(2)
