import pyautogui 
import pyscreeze
import random
import time

# setting up a logout timer using some random duration of time between 5 and 6 hours ish and 
timer_expired = False
start = time.time()
logout_timer = random.randint(20000, 21300)


# handles mining the three rocks
def mining_guild_triple_rock_clicker():
    pyautogui.click( (random.randint(1300, 1430), random.randint(850, 920)), duration=0.5 )
    pyautogui.click( (random.randint(1100, 1160), random.randint(600, 660)), duration=0.6 )
    pyautogui.click( (random.randint(1360, 1430), random.randint(350, 410)), duration=0.4 )


# handles going from the iron triple rock spot to the box and depositing and returning back to the mining guild
def deposit_to_deposit_box():
    pyautogui.click(deposit_box_coordinate, duration=0.5 )
    time.sleep(5)
    pyautogui.click( (random.randint(1350, 1425), random.randint(325, 425)), duration=0.5)
    time.sleep(2)
    pyautogui.click( (random.randint(1140, 1160), random.randint(600, 620)), duration=0.4 )
    pyautogui.click(triple_rock_coordinate, duration=0.5)
    time.sleep(5)

# coordinates for the deposite box minimap click and the triple rock spot minimap click
deposit_box_coordinate = (1684, 162)
triple_rock_coordinate = (1840, 134)

# delay before it begins so I have time to setup screen
time.sleep(3)

while timer_expired == False:
    # setup a failsafe to exit by dragging mouse to topleft corner of primary monitor/screen, implement a random pause between clicks
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = random.randint(4, 8) * 0.1

    # Check if the bottom right of my inventory contains iron ore
    try:
        pyautogui.locateOnScreen('mining_guild_images\iron_ore_in_inventory.PNG', confidence=0.5, grayscale=True, region=(1762, 969, 100, 80))
        print("inventory full of iron ore")

    # If the inventory isnt full, mine the three iron rocks, need to check last inventory slot for either a iron ore or a gem
    except:
        try:
            pyautogui.locateOnScreen("mining_guild_images\\ruby_in_inventory.PNG", confidence=0.5, grayscale=True, region=(1762, 969, 100, 80))
            print("inventory full with a ruby at the end")

        except:
            try:
                pyautogui.locateOnScreen("mining_guild_images\\sapphire_in_inventory.PNG", confidence=0.5, grayscale=True, region=(1762, 969, 100, 80))
                print("inventory full with a sapphire at the end")

            except: 

                try:
                    pyautogui.locateOnScreen("mining_guild_images\\emerald_in_inventory.PNG", confidence=0.5, grayscale=True, region=(1762, 969, 100, 80))
                    print("inventory full with a emerald at the end")

                except:

                    try: 
                        pyautogui.locateOnScreen("mining_guild_images\\diamond_in_inventory.PNG", confidence=0.5, grayscale=True, region=(1762, 969, 100, 80))
                        print("inventory full with a diamond at the end")
                    except:
                        mining_guild_triple_rock_clicker()

                    else:
                        deposit_to_deposit_box()
                
                else: 
                    deposit_to_deposit_box()
                
            else: 
                deposit_to_deposit_box()
        else:
            deposit_to_deposit_box()

    # else go to the deposit box, then open it, then deposit ore, then return back to triple rock
    else:
        deposit_to_deposit_box()

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