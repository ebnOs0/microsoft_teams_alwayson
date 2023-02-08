from pynput.mouse import Button, Controller
import time
import random
from dateutil import parser
from datetime import datetime

mouse = Controller()

# Read pointer position
print("The current pointer position is {0}".format(mouse.position))

# # Set pointer position
# mouse.position = (10, 20)
# print('Now we have moved it to {0}'.format(
#     mouse.position))

# Move pointer relative to current position
# ran_x = random.randint(-100, 100)
# ran_y = random.randint(-100, 100)
ran_x = [0, 100, 0, -100]
ran_y = [100, 0, -100, 0]
n = 0
while True:
    # if (
    #     datetime.now() > parser.parse("9:00") and datetime.now() < parser.parse("11:30")
    # ) or (
    #     datetime.now() > parser.parse("11:30")
    #     and datetime.now() < parser.parse("18:00")
    # ):
    if (
        datetime.now() < parser.parse("11:30")
    ) or (
        datetime.now() > parser.parse("12:50")
    ):    
        print('OS Mode')
        try:
            # mouse.press(Button.left)
            # mouse.release(Button.left)
            mouse.move(ran_x[n], ran_y[n])
            mouse.scroll(0, -2)
            print("The current pointer position is {0}".format(mouse.position))
            # mouse.press(Button.right)
            # mouse.release(Button.right)
            time.sleep(10)
            if n != 3:
                n = n + 1
            else:
                n = 0
        except KeyboardInterrupt:
            break
    else:
        print('OoO Mode')
        time.sleep(100)
print("End")


# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)

# # Double click; this is different from pressing and releasing
# # twice on Mac OSX
# mouse.click(Button.left, 2)

# # Scroll two steps down
# mouse.scroll(0, 2)
