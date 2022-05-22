# current version: 2.1.2 (gambling update)
# changes: typing q by accident no longer crashes the game!!
import time
import random

# declares variables----------------------------------------------------------------------------------------------------
# misc----------------------------------------------------------
risk = 0
loss = 0
# upgrade amounts-----------------------------------------------
with open(r'C:\Users\birtw\Downloads\clicker-main\clicker-main\save.txt') as file:
    savestate = file.readlines()
    unit1 = int(savestate[13])
    unit2 = int(savestate[14])
    unit3 = int(savestate[15])
    unit4 = int(savestate[16])
    unit5 = int(savestate[17])
    unit6 = int(savestate[18])
    unit7 = int(savestate[19])
    unit8 = int(savestate[20])
    unit9 = int(savestate[21])
    unit10 = int(savestate[22])
    unitc1 = int(savestate[23])
    unitc2 = int(savestate[24])
    unitc3 = int(savestate[25])
    unitc4 = int(savestate[26])
    unitc5 = int(savestate[27])
    # amount given per click and per tick---------------------------
    per_tick_result = int(savestate[10])
    per_click_result = int(savestate[11])
    # stats---------------------------------------------------------
    points = int(savestate[1])
    ticks = int(savestate[2])
    clicks = int(savestate[3])
    # yes/no variables----------------------------------------------
    not_enough_points = 0
    # achievements--------------------------------------------------
    ac = int(savestate[5])  # up to 5
    at = int(savestate[6])  # up to 6
    appt = int(savestate[7])  # up to 8
    appc = int(savestate[8])  # up to 8
while 0 == 0:  # action menu -------------------------------------------------------------------------------------------
    points += (per_tick_result * (1 + (appt / 10)))
    print(unit1)
    # achievement check ----------------------------------------
    if ac == 0 and clicks > 100:
        ac = 1
    if ac == 1 and clicks > 200:
        ac = 2
    if ac == 2 and clicks > 500:
        ac = 3
    if ac == 3 and clicks > 1000:
        ac = 4
    if ac == 4 and clicks > 5000:
        ac = 5
    if at == 0 and ticks > 100:
        at = 1
    if at == 1 and ticks > 200:
        at = 2
    if at == 2 and ticks > 500:
        at = 3
    if at == 3 and ticks > 1000:
        at = 4
    if at == 4 and ticks > 5000:
        at = 5
    if at == 5 and ticks > 20000:
        at = 6
    if appt == 0 and per_tick_result > 10:
        appt = 1
    if appt == 1 and per_tick_result > 50:
        appt = 2
    if appt == 2 and per_tick_result > 100:
        appt = 3
    if appt == 3 and per_tick_result > 250:
        appt = 4
    if appt == 4 and per_tick_result > 500:
        appt = 5
    if appt == 5 and per_tick_result > 1000:
        appt = 6
    if appt == 6 and per_tick_result > 5000:
        appt = 7
    if appt == 7 and per_tick_result > 10000:
        appt = 8
    if appc == 0 and per_click_result > 10:
        appc = 1
    if appc == 1 and per_click_result > 50:
        appc = 2
    if appc == 2 and per_click_result > 100:
        appc = 3
    if appc == 3 and per_click_result > 250:
        appc = 4
    if appc == 4 and per_click_result > 500:
        appc = 5
    if appc == 5 and per_click_result > 1000:
        appc = 6
    if appc == 6 and per_click_result > 5000:
        appc = 7
    if appc == 7 and per_click_result > 10000:
        appc = 8
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # separation
    print("Points per tick =", per_tick_result)
    print("Points per click =", per_click_result)
    print("Points =", round(points))
    option = input(
        "Enter input:\nc: click\ns: shop\nq: leave\na: achievements\ng: rng machine (100,000 points)\nanything else: does nothing\n")
    time.sleep(0.1 - (at / 100))
    ticks += 1
    if option == "c":  # adds the value per click to point amount
        points += per_click_result * (1 + (ac / 10) + (appc / 20))
        clicks += 1
    if option == "q":  # closes the game
        with open(r'C:\Users\birtw\Downloads\clicker-main\clicker-main\save.txt', 'r') as file:
            savestate = file.readlines()
            savestate[1] = str(round(points))
            savestate[3] = str(ticks)
            savestate[5] = str(clicks)
            savestate[7] = "achievements:"
            savestate[9] = str(ac)
            savestate[11] = str(at)
            savestate[13] = str(appc)
            savestate[15] = str(appt)
            savestate[17] = "given:"
            savestate[19] = str(per_tick_result)
            savestate[21] = str(per_click_result)
            savestate[23] = "upgrades"
            savestate[25] = str(unit1)
            savestate[27] = str(unit2)
            savestate[29] = str(unit3)
            savestate[31] = str(unit4)
            savestate[33] = str(unit5)
            savestate[35] = str(unit6)
            savestate[37] = str(unit7)
            savestate[39] = str(unit8)
            savestate[41] = str(unit9)
            savestate[43] = str(unit10)
            savestate[45] = str(unitc1)
            savestate[47] = str(unitc2)
            savestate[49] = str(unitc3)
            savestate[51] = str(unitc4)
            savestate[53] = str(unitc5)
            savestate[54] = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            x = 2
            while x < 52:
                savestate[x] = "\n"
                x += 2
        with open(r'C:\Users\birtw\Downloads\clicker-main\clicker-main\save.txt', 'w') as file:
            file.writelines(savestate)
        quit("game closed by q key.")
    if option == "s":  # opens the shop
        while not option == "q":
            print(
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            option = input("a to show autoclickers, c to show click upgrades, q to go back.\n")
            # auto types -----------------------------------------------------------------------------------------------------------
            if option == "a":
                while not option == "q":
                    print(
                        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # separation
                    print("\nAUTOCLICKERS")
                    print("\ntype 1 (1 point per clicker):")
                    print("amount:", unit1)
                    print("cost:", round((10 * 1.3 * unit1)) + 10)
                    print("\ntype 2 (5 points per clicker):")
                    print("amount:", unit2)
                    print("cost:", 50 * 2 * (unit2 + 1))
                    print("\ntype 3 (20 points per clicker):")
                    print("amount:", unit3)
                    print("cost:", round(1000 * 2.4 * (unit3 + 1)))
                    print("\ntype 4 (100 points per clicker):")
                    print("amount:", unit4)
                    print("cost:", 25000 * 4 * (unit4 + 1))
                    print("\ntype 5 (300 points per clicker):")
                    print("amount:", unit5)
                    print("cost:", round(500000 * 6.5 * (unit5 + 1)))
                    print("\ntype 6 (1000 points per clicker):")
                    print("amount:", unit6)
                    print("cost:", 10000000 * 8 * (unit6 + 1))
                    print("\ntype 7 (10000 points per clicker):")
                    print("amount:", unit7)
                    print("cost:", 600000000 * 14 * (unit7 + 1))
                    print("\ntype 8 (200000 points per clicker):")
                    print("amount:", unit8)
                    print("cost:", 100000000000 * 16 * (unit8 + 1))
                    print("\ntype 9 (4000000 points per clicker):")
                    print("amount:", unit9)
                    print("cost:", 100000000000000 * 25 * (unit9 + 1))
                    print("\ntype 10 (160000000 points per clicker):")
                    print("amount:", unit10)
                    print("cost:", 10000000000000000000 * 32 * (unit10 + 1), "\n")
                    if not_enough_points == 1:
                        print("not enough points!")
                    print("points:", points)
                    option = input("enter type number to buy an autoclicker (1). type q to go back.\n")
                    not_enough_points = 0
                    if option == "1":
                        if points >= round((10 * 1.3 * unit1)) + 10:
                            per_tick_result += 1
                            points -= round((10 * 1.3 * unit1)) + 10
                            unit1 += 1
                        else:
                            not_enough_points = 1
                    if option == "2":
                        if points >= (50 * 2 * (unit2 + 1)):
                            per_tick_result += 5
                            points -= (50 * 2 * (unit2 + 1))
                            unit2 += 1
                        else:
                            not_enough_points = 1
                    if option == "3":
                        if points >= round(1000 * 2.4 * (unit3 + 1)):
                            per_tick_result += 20
                            points -= round(1000 * 2.4 * (unit3 + 1))
                            unit3 += 1
                        else:
                            not_enough_points = 1
                    if option == "4":
                        if points >= (25000 * 4 * (unit4 + 1)):
                            per_tick_result += 100
                            points -= (25000 * 4 * (unit4 + 1))
                            unit4 += 1
                        else:
                            not_enough_points = 1
                    if option == "5":
                        if points >= round(500000 * 6.5 * (unit5 + 1)):
                            per_tick_result += 300
                            points -= (500000 * 6.5 * (unit5 + 1))
                            unit5 += 1
                        else:
                            not_enough_points = 1
                    if option == "6":
                        if points >= (10000000 * 8 * (unit6 + 1)):
                            per_tick_result += 1000
                            points -= (10000000 * 8 * (unit6 + 1))
                            unit6 += 1
                        else:
                            not_enough_points = 1
                    if option == "7":
                        if points >= (600000000 * 14 * (unit7 + 1)):
                            per_tick_result += 10000
                            points -= (600000000 * 14 * (unit7 + 1))
                            unit7 += 1
                        else:
                            not_enough_points = 1
                    if option == "8":
                        if points >= (100000000000 * 16 * (unit8 + 1)):
                            per_tick_result += 200000
                            points -= (100000000000 * 16 * (unit8 + 1))
                            unit8 += 1
                        else:
                            not_enough_points = 1
                    if option == "9":
                        if points >= (100000000000000 * 25 * (unit9 + 1)):
                            per_tick_result += 4000000
                            points -= (100000000000000 * 25 * (unit9 + 1))
                            unit9 += 1
                        else:
                            not_enough_points = 1
                    if option == "10":
                        if points >= (10000000000000000000 * 32 * (unit10 + 1)):
                            per_tick_result += 160000000
                            points -= (10000000000000000000 * 32 * (unit10 + 1))
                            unit10 += 1
                        else:
                            not_enough_points = 1
            # click types ----------------------------------------------------------------------------------------------------------
            if option == "c":
                while not option == "q":
                    print(
                        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\nCLICK UPGRADES")
                    print("\nlevel 1 (1 point per upgrade):")
                    print("amount:", unitc1)
                    print("cost:", 100 * 3 * (unitc1 + 1))
                    print("\nlevel 2 (5 points per upgrade):")
                    print("amount:", unitc2)
                    print("cost:", 500 * 4 * (unitc2 + 1))
                    print("\nlevel 3 (20 points per upgrade):")
                    print("amount:", unitc3)
                    print("cost:", 2500 * 5 * (unitc3 + 1))
                    print("\nlevel 4 (100 points per upgrade):")
                    print("amount:", unitc4)
                    print("cost:", 10000 * 7 * (unitc4 + 1))
                    print("\nlevel 5 (DOUBLES points per upgrade):")
                    print("amount:", unitc5)
                    print("cost:", round(100000 * pow(2.2, (unitc5 + 1))), "\n")
                    if not_enough_points == 1:
                        print("not enough points!")
                    print("points:", points)
                    option = input("type the upgrade number click upgrade (2).\ntype q to go back.\n")
                    not_enough_points = 0
                    if option == "1":
                        if points >= 100 * 3 * (unitc1 + 1):
                            per_click_result += 1
                            points -= 100 * 3 * (unitc1 + 1)
                            unitc1 += 1
                        else:
                            not_enough_points = 1
                    if option == "2":
                        if points >= (500 * 4 * (unitc2 + 1)):
                            per_click_result += 5
                            points -= (500 * 4 * (unitc2 + 1))
                            unitc2 += 1
                        else:
                            not_enough_points = 1
                    if option == "3":
                        if points >= 2500 * 5 * (unitc3 + 1):
                            per_click_result += 20
                            points -= 2500 * 5 * (unitc3 + 1)
                            unitc3 += 1
                        else:
                            not_enough_points = 1
                    if option == "4":
                        if points >= (10000 * 7 * (unitc4 + 1)):
                            per_click_result += 100
                            points -= (10000 * 7 * (unitc4 + 1))
                            unitc4 += 1
                        else:
                            not_enough_points = 1
                    if option == "5":
                        if points >= round(100000 * pow(2.2, (unitc5 + 1))):
                            per_click_result *= 2
                            points -= round(100000 * pow(2.2, (unitc5 + 1)))
                            unitc5 += 1
                        else:
                            not_enough_points = 1
    if option == "a":  # shows achievements
        while not option == "q":
            print(
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # separation
            print("achievements + stats\n\n")
            print("clicks")
            print("amount:", clicks)
            print("progress:", ac, "/ 5", "(+", ac * 10, "% to points per click)\n\n")
            print("ticks")
            print("amount:", ticks)
            print("progress:", at, "/ 6", "(+", at * 10, "% to tick cooldown)\n\n\n")
            print("points per tick")
            print("progress:", appt, "/ 8", "(+", appt * 10, "% to points per tick)\n\n")
            print("points per click")
            print("progress:", appc, "/ 8", "(+", appc * 5, "% to points per click)\n\n")
            print("q to close\n")
            option = input()
    if option == "g" and points > 100000:  # the rng machine
        while risk < 11:
            print(
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if loss == 1:
                print("success! gained", round(points / (11 - risk)), "points.")
                points += round(points / (11 - risk))
            if loss == 2:
                print("failure... lost", round(points / (11 - risk)), "points.")
                points -= round(points / (11 - risk))
            loss = 0
            risk = 0
            try:
                risk = int(input("enter risk to take, enter 11 to go back (up to 10: risk up, cost up, reward up, and chance down)\n"))
                if 11 > risk > 0:
                    chance = round(50 - risk * 4)
                    print("cost:", round(points / (11 - risk)))
                    print("reward:", round((points / (11 - risk)) * 2))
                    print("chance:", round(50 - risk * 4), "%")
                    option = input("are you sure you want to continue? enter b to go back, enter anything else to continue")
                    if option == "b":
                        print("this line of text is here to fill space")
                    elif chance > random.randint(1, 100):
                        loss = 1
                    else:
                        loss = 2
                else:
                    print("this line of text is here to fill space")
            except:
                ()
