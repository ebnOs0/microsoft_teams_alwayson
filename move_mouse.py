from pynput.mouse import Controller
import time
from dateutil import parser
from datetime import datetime

mouse = Controller()


def mouse_move(mouse, ran_x, ran_y, *, sleep_time=10):
    """movement control

    Args:
        mouse (pynput.mouse.Controller): pynput.mouse.Controller
        ran_x (list): x axis limitation
        ran_y (list): y axis limitation
    """
    mouse.move(ran_x[n], ran_y[n])
    mouse.scroll(0, -2)
    print("Mouse Moving at {}".format(datetime.now()))
    time.sleep(sleep_time)  # save some energy


def time_gap(start_time, end_time):
    """set a time gap for freezing mouse

    Args:
        start_time (str): xx:xx time
        end_time (str): xx:xx time

    Returns:
        Boolean: True for gap time, False for work time
    """
    if datetime.now() >= parser.parse(start_time) and datetime.now() <= parser.parse(
        end_time
    ):
        return True
    else:
        return False


# Read pointer position
print("The current pointer position is {0}".format(mouse.position))
# range of mouse movement
ran_x = [0, 100, 0, -100]
ran_y = [100, 0, -100, 0]
n = 0
while True:
    if not time_gap("11:30", "12:50"):
        try:
            mouse_move(mouse, ran_x, ran_y, sleep_time=15)
            if n != 3:
                n = n + 1
            else:
                n = 0
        except KeyboardInterrupt:
            break
    else:
        print("Have a rest, dude")
        time.sleep(100)
print("\nPLAY TO WIN!")
