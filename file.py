from microbit import *

count = 0
was_pressed = False

def pwas_pressed():
    global was_pressed
    if pin0.read_digital():
        was_pressed = True
        return False
    else:
        if was_pressed:
            was_pressed = False
            return True
        else:
            return False

lock = True
while True:
    display.scroll(str(pin2.read_digital()), wait = False)
    # if pwas_pressed():
    #     # display.set_pixel(count % 5, int(count / 5), 9)
    #     # count += 1
    #     lock = not lock
    # if pin1.read_digital():
    #     if not lock:
    #         display.show(Image.GIRAFFE, wait = False)
    # else:
    #     display.clear()
    
    # if pin2.read_digital():
    #     display.show(Image.GIRAFFE, wait = False)
    # else:
    #     display.clear()
