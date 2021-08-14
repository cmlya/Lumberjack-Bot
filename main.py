import pyautogui
from colors import Colors
import keyboard
import time

button_y = 1500
left_button_x = 1200
right_button_x = 1500
start_button_x = (left_button_x + right_button_x) / 2
branch_y = 935
right_branch_x = 1500
left_branch_x = 1245
side = ""


def start():
    pyautogui.click(x=start_button_x, y=button_y)
    print(Colors.SKY + Colors.UNDERLINE + "Game started" + Colors.RESET)


def lumberjack_side():
    color = (207, 70, 59)
    s = pyautogui.screenshot()
    middle_x = int(s.width / 2)
    middle_y = int(s.height / 2)
    for x in range(1000, middle_x):
        for y in range(middle_y, 1250):
            if s.getpixel((x, y)) == color:
                return "left"
    return "right"


def click_left():
    pyautogui.click(x=left_button_x, y=button_y, clicks=2, interval=0.07)
    global side
    side = "left"
    # print(Colors.GRASS + "Moved left" + Colors.RESET)


def click_right():
    pyautogui.click(x=right_button_x, y=button_y, clicks=2, interval=0.07)
    global side
    side = "right"
    # print(Colors.GRASS + "Moved right" + Colors.RESET)


def check_branch():
    time1 = time.time()
    # s = pyautogui.screenshot('scrn.png', region=(800, 500, 1600, 900))
    s = pyautogui.screenshot()
    print(Colors.PINK + "time elapsed: " + str(time.time() - time1) + Colors.RESET)
    global side
    if side == "left":
        if s.getpixel((left_branch_x, branch_y)) == (161, 116, 56):
            click_right()
        else:
            click_left()
    else:
        if s.getpixel((right_branch_x, branch_y)) == (161, 116, 56):
            click_left()
        else:
            click_right()

    pyautogui.sleep(0.05)


def main():
    pyautogui.sleep(2)
    start()
    global side
    side = lumberjack_side()
    while True:
        check_branch()
        if keyboard.is_pressed('q'):
            break


if __name__ == "__main__":
    main()
