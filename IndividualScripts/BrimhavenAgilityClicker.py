import pyautogui 
import random
import time


# Create a timer to that hasn't expired and get the start time, also create a random time to logout between 5 and 6 hours
timer_expired = False
start = time.time()
logout_timer = random.randint(20000, 21300)
print(logout_timer)

# until the timer expires continue running:
while timer_expired == False:
    # setup a failsafe to exit by dragging mouse to topleft corner of primary monitor/screen, implement a random pause between clicks
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = random.randint(1,10) * 0.1

    # get x and y mouse positions, randomize positions slightly every time while remaining inside correct tiles
    x_position = 1199 + random.randint(1, 88)
    y_position = 470 + random.randint(1,33)

    # move mouse to correct x,y positions, not immediately over interval then click
    pyautogui.moveTo(x_position, y_position, 0.5)
    pyautogui.click(clicks = 1)

    # get time elapsed by removing start time from current time, returns seconds elapsed, if its been more than the logout timer, end the program
    time_elapsed = time.time() - start
    if time_elapsed > logout_timer:
        timer_expired = True
        print()
        print()
        print()
        print()
        print()
        print("!!!!\n")
        print(f"start time: {start} and end time {time.time()} and the total time elapsed: {time.time() - start} seconds")
        print("Program is over!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Program is over!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Program is over!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Program is over!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Program is over!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#locateOnScreen()