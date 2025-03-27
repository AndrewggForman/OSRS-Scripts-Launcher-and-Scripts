# This program is a series of clicks and waits to fish karambwans,, bank them, and repeat, including travel between.
# It does not use any sort of checking and relies on a specific screen size

# (I could change in the future to work more generally by checking large sections of the screen for the points to click on
# and find where to click using images or ratios depending on window size (although, the latter would make assumptions on OSRS style chosen) )

# Modules
import pyautogui 
import pyscreeze
import random
import time

# Clicker Functions 

def click_bwan_spot():
    pyautogui.click( (random.randint(1360, 1370), random.randint(395, 400)), duration=0.5 )

def click_karamja_fairy_ring():
    pyautogui.click( (random.randint(1430, 1470), random.randint(810, 840)), duration=0.5 ) 

def click_bank_chest_minimap():
    pyautogui.click( (1848, 173), duration=0.5 )

def click_bank_chest_object():
    pyautogui.click( (random.randint(1415, 1430), random.randint(550, 560)), duration=0.5 ) 

def click_deposit_icon():
    pyautogui.click( (random.randint(1440, 1460), random.randint(830, 845)), duration=0.5 ) 

def click_to_empty_barrel():
    pyautogui.click( (random.randint(1625, 1645), random.randint(725, 740)), duration=0.5 )

def click_chasm_fairy_ring_minimap():
    pyautogui.click( (1690, 110), duration=0.5 )

def click_chasm_fairy_ring():
    pyautogui.click( (random.randint(1410, 1420), random.randint(555, 565)), duration=0.5 )

def click_DKP():
    pyautogui.click( (random.randint(1640, 1750), random.randint(880, 885)), duration=0.5 )

def click_DJR():
    pyautogui.click( (random.randint(1640, 1750), random.randint(770, 780)), duration=0.5 )

def click_confirm_teleport():
    pyautogui.click( (random.randint(1150, 1300), random.randint(580, 600)), duration=0.5 )


# Pathing Functions

def bank_to_fishing():
    click_chasm_fairy_ring_minimap()
    time.sleep(12)
    click_chasm_fairy_ring()
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    click_DKP()
    time.sleep(2)
    click_confirm_teleport()
    time.sleep(4)
    click_bwan_spot()
    pyautogui.click()
    

def fishing_to_bank_and_deposit():
    click_karamja_fairy_ring()
    time.sleep(4)
    click_DJR()
    time.sleep(2)
    click_confirm_teleport()
    time.sleep(4)
    click_bank_chest_minimap()
    time.sleep(12)
    click_bank_chest_object()
    pyautogui.click()
    time.sleep(2)
    click_deposit_icon()
    time.sleep(0.3)
    click_to_empty_barrel()


# initial setup, setting up some leeway time at start of program, then the pause interval between clicks, then the timer to end script
time.sleep(5)
pyautogui.PAUSE = 0.5

timer_expired = False
start = time.time()
logout_timer = random.randint(20000, 21300)


# main loop, oscillating between fishing and banking unless we pass the timer
while timer_expired == False:
    # we need to start the bank, the loops begins from bank to fishing, goes from fishing to bank, and then start back at bank, 
    # intervals of 4 minutes between function and each function probably takes 20-40 seconds 

    bank_to_fishing()
    time.sleep(240)
    fishing_to_bank_and_deposit()
    time.sleep(1)
    time_elapsed = time.time() - start
    if time_elapsed > logout_timer:
        timer_expired = True

        print("!!!!\n")
        print(f"start time: {start} and end time {time.time()} and the total time elapsed: {time.time() - start} seconds")
        print("Program is over!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
