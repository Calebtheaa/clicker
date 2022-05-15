# current version: 1.1 (achievement update > shop optimization)
# changes: moved menus to take less time to bulk buy
import time
# declares variables----------------------------------------------------------------------------------------------------
# upgrade amounts and prices------------------------------------
unit1 = 0
unit2 = 0
unit3 = 0
unit4 = 0
unit5 = 0
unit6 = 0
unit7 = 0
unit8 = 0
unit9 = 0
unit10 = 0
unitc1 = 0
unitc2 = 0
unitc3 = 0
unitc4 = 0
unitc5 = 0
# amount given per click and per tick---------------------------
per_tick_result = 0
per_click_result = 1
# stats---------------------------------------------------------
clicks = 0
ticks = 0
points = 0
# yes/no variables----------------------------------------------
not_enough_points = 0
# achievements--------------------------------------------------
ac = 0  # up to 5
at = 0  # up to 6
appt = 0  # up to 8
appc = 0  # up to 8
while 0 == 0:  # action menu -------------------------------------------------------------------------------------------
    points += (per_tick_result * (1 + (appt / 10)))
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
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # separation
    print("Points per tick =", per_tick_result)
    print("Points per click =", per_click_result)
    print("Points =", points)
    option = input("Enter input:\nc: click\ns: shop\nq: leave\na: achievements\nanything else: does nothing\n")
    time.sleep(0.1-(at / 100))
    ticks += 1
    if option == "c":  # adds the value per click to point amount
        points += per_click_result * (1 + (ac / 10) + (appc / 20))
        clicks += 1
    if option == "q":  # closes the game
        quit("game closed by q key.")
    if option == "s":  # opens the shop
        while not option == "q":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            option = input("a to show autoclickers, c to show click upgrades, q to go back.\n")
# auto types -----------------------------------------------------------------------------------------------------------
            if option == "a":
                while not option == "q":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # separation
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
                    option = input("enter type number after a t (t2) to buy an autoclicker.\ntype the upgrade number after a c for a click upgrade (c2).\ntype q to go back.\n")
                    not_enough_points = 0
                    if option == "t1":
                        if points >= round((10 * 1.3 * unit1)) + 10:
                            per_tick_result += 1
                            points -= round((10 * 1.3 * unit1)) + 10
                            unit1 += 1
                        else:
                            not_enough_points = 1
                    if option == "t2":
                        if points >= (50 * 2 * (unit2 + 1)):
                            per_tick_result += 5
                            points -= (50 * 2 * (unit2 + 1))
                            unit2 += 1
                        else:
                            not_enough_points = 1
                    if option == "t3":
                        if points >= round(1000 * 2.4 * (unit3 + 1)):
                            per_tick_result += 20
                            points -= round(1000 * 2.4 * (unit3 + 1))
                            unit3 += 1
                        else:
                            not_enough_points = 1
                    if option == "t4":
                        if points >= (25000 * 4 * (unit4 + 1)):
                            per_tick_result += 100
                            points -= (25000 * 4 * (unit4 + 1))
                            unit4 += 1
                        else:
                            not_enough_points = 1
                    if option == "t5":
                        if points >= round(500000 * 6.5 * (unit5 + 1)):
                            per_tick_result += 300
                            points -= (500000 * 6.5 * (unit5 + 1))
                            unit5 += 1
                        else:
                            not_enough_points = 1
                    if option == "t6":
                        if points >= (10000000 * 8 * (unit6 + 1)):
                            per_tick_result += 1000
                            points -= (10000000 * 8 * (unit6 + 1))
                            unit6 += 1
                        else:
                            not_enough_points = 1
                    if option == "t7":
                        if points >= (600000000 * 14 * (unit7 + 1)):
                            per_tick_result += 10000
                            points -= (600000000 * 14 * (unit7 + 1))
                            unit7 += 1
                        else:
                            not_enough_points = 1
                    if option == "t8":
                        if points >= (100000000000 * 16 * (unit8 + 1)):
                            per_tick_result += 200000
                            points -= (100000000000 * 16 * (unit8 + 1))
                            unit8 += 1
                        else:
                            not_enough_points = 1
                    if option == "t9":
                        if points >= (100000000000000 * 25 * (unit9 + 1)):
                            per_tick_result += 4000000
                            points -= (100000000000000 * 25 * (unit9 + 1))
                            unit9 += 1
                        else:
                            not_enough_points = 1
                    if option == "t10":
                        if points >= (10000000000000000000 * 32 * (unit10 + 1)):
                            per_tick_result += 160000000
                            points -= (10000000000000000000 * 32 * (unit10 + 1))
                            unit10 += 1
                        else:
                            not_enough_points = 1
# click types ----------------------------------------------------------------------------------------------------------
            if option == "c":
                while not option == "q":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
                    option = input("enter type number after a t (t2) to buy an autoclicker.\ntype the upgrade number after a c for a click upgrade (c2).\ntype q to go back.\n")
                    not_enough_points = 0
                    if option == "c1":
                        if points >= 100 * 3 * (unitc1 + 1):
                            per_click_result += 1
                            points -= 100 * 3 * (unitc1 + 1)
                            unitc1 += 1
                        else:
                            not_enough_points = 1
                    if option == "c2":
                        if points >= (500 * 4 * (unitc2 + 1)):
                            per_click_result += 5
                            points -= (500 * 4 * (unitc2 + 1))
                            unitc2 += 1
                        else:
                            not_enough_points = 1
                    if option == "c3":
                        if points >= 2500 * 5 * (unitc3 + 1):
                            per_click_result += 20
                            points -= 2500 * 5 * (unitc3 + 1)
                            unitc3 += 1
                        else:
                            not_enough_points = 1
                    if option == "c4":
                        if points >= (10000 * 7 * (unitc4 + 1)):
                            per_click_result += 100
                            points -= (10000 * 7 * (unitc4 + 1))
                            unitc4 += 1
                        else:
                            not_enough_points = 1
                    if option == "c5":
                        if points >= round(100000 * pow(2.2, (unitc5 + 1))):
                            per_click_result *= 2
                            points -= round(100000 * pow(2.2, (unitc5 + 1)))
                            unitc5 += 1
                        else:
                            not_enough_points = 1
    if option == "a":  # shows achievements
        while not option == "q":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # separation
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
