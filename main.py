import pyautogui
from colors import Colors
import keyboard
import time
import statistics as stat

button_y = 1500
left_button_x = 1200
right_button_x = 1500
start_button_x = (left_button_x + right_button_x) / 2
abs_branch_y = 935
abs_right_branch_x = 1500
abs_left_branch_x = 1245

top_x = 1150
top_y = 800
bottom_x = 450
width = 700
height = 400

branch_search_area = (
    top_x,
    top_y,
    width,
    height
)
side = ""
durations = []


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
    # s = pyautogui.screenshot('scrn.png', region=branch_search_area)
    s = pyautogui.screenshot()
    global side
    if side == "left":
        # if s.getpixel((abs_left_branch_x - top_x, abs_branch_y - top_y)) == (161, 116, 56):
        if s.getpixel((abs_left_branch_x, abs_branch_y)) == (161, 116, 56):
            click_right()
        else:
            click_left()
    else:
        # if s.getpixel((abs_right_branch_x - top_x, abs_branch_y - top_y)) == (161, 116, 56):
        if s.getpixel((abs_right_branch_x, abs_branch_y)) == (161, 116, 56):
            click_left()
        else:
            click_right()
    durations.append(time.time() - time1)
    # print(Colors.PINK + "time elapsed: " + str(time.time() - time1) + Colors.RESET)
    print(Colors.SKY + "avg dur: " + str(stat.mean(durations)) + Colors.RESET)
    pyautogui.sleep(0.04)


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
