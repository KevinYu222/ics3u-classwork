from random import randint
import time

score = 0
reward = [25, 25, 25, 25]
cable_color = ["BLUE", "YELLOW", "GREEN", "BLACK"]
cable_number = []
def play_entry():
    print("[1] Play")
    print("[2] Quit")

while score < 100:
    run = False
    print(f"Completion Score: {score}/100")
    print("Main Menu")
    print("---------")
    print("[1] Reset the Power")
    print("[2] Feed the Raptors")
    print("[3] Fix the Wiring")
    print("[4] Upload Log Files")
    while run == False:
        game = int(input("Choice: "))
        if game > 0 and game < 5:
            run = True
        else:
            print("Invalid Answer.")
        print()
    
    if game == 1:
        green_button = False
        pump = 0
        print("Reset the Power: The object of this mini-game is to reset the power of the space-station. The player must prime the power-grid three times before pressing the green button. If they prime it more/less than three times, the panel explodes and the mini-game fails. If they prime three times, then press the green button, they complete the mini-game.")
        play_entry()
        choice = int(input("Choice: "))
        print()

        if choice == 1:
            while green_button == False:
                print("[1] Pump the primer handle")
                print("[2] Press the green button")
                choice = int(input("Choice: "))
                print()
                
                if choice == 1:
                    print("You pumped the primer.")
                    pump += 1
                    print()
                elif choice == 2:
                    if pump != 3:
                        print("Mission Failed! You die!")
                        break
                    elif pump == 3:
                        if reward[game - 1] != 0:
                            print("Congratulations! You have completed this game!")
                            print("+ 25")
                            score += reward[game - 1]
                            reward[game - 1] = 0
                        else:
                            print("You played this game before.")
                        green_button = True
                print()
        elif choice == 2:
            print()

    if game == 2:
        loaded_gurney = False
        feeded_raptor = False
        print("There are Velociraptors on board the space-station (obviously). In this mini-game, you must feed them. First, you must load a cow onto the gurney, which is attached to a crane which will be lowered into the raptor's pen.")
        play_entry()
        choice = int(input("Choice: "))
        print()

        if choice == 1:
            while feeded_raptor == False:
                print("[1] Load Cow onto Gurney")
                print("[2] Lower the Gurney into the Pen")
                choice = int(input("Choice: "))
                print()
                if choice == 1:
                    if loaded_gurney == False:
                        print("You loaded a cow onto a gurney.")
                        loaded_gurney = True
                    else:
                        print("You cannot load twice.")
                    print()
                elif choice == 2:
                    if loaded_gurney == True:
                        if reward[game - 1] != 0:
                            print("Congratulations! you completed the challenge!")
                            print("+ 25")
                            score += reward[game - 1]
                            reward[game - 1] = 0
                        else:
                            print("You have completed this game before.")
                        feeded_raptor = True
                    else:
                        print("No cow on the gurney! Mission Fail! You die!")
                        break
                    print()
        
        elif choice == 2:
            print()
    
    if game == 3:
        restore_control = False
        cable = 0
        print("The main orbital control console on the space station is behaving erratically. There are four usb cables that have been removed from their ports BLUE, YELLOW, GREEN, and BLACK. You need to plug the USB cables back into their proper ports with the following map:")
        print("Cable colour      Port number")
        print(" BLUE              1")
        print(" YELLOW            2")
        print(" GREEN             3")
        print(" BLACK             4")
        print()
        play_entry()
        choice = int(input("Choice: "))
        print()

        if choice == 1:
            while restore_control == False:
                while cable <= 3:
                    choice = int(input(f"What number port you need to plug the {cable_color[cable]} cable into? "))
                    if choice not in cable_number and choice > 0 and choice < 5:
                        cable_number.append(choice)
                        cable += 1
                    else:
                        if choice in cable_number:
                            print("This number port is already taken.")
                        else:
                            print("Invalid input.")
                    print()
                
                print("Checking for accuracy...")
                if cable_number[0] == 1 and cable_number[1] == 2 and cable_number[2] == 3 and cable_number[3] == 4:
                    if reward[game - 1] != 0:
                        print("Congratulations! You have completed the challenge!")
                        print("+ 25")
                        score += reward[game - 1]
                        reward[game - 1] = 0
                    else:
                        print("You have completed the challenge before.")
                    restore_control = True
                else:
                    print("Ohno, you have wrong input is wrong, You fail!")
                    break
                print()

                cable_number = []
        elif choice == 2:
            print()
    
    if game == 4:
        upload = False
        password = randint(1000, 9999)
        print("Your log files need to be uploaded to the space station's main server. Enter the daily password and then upload the log files")
        play_entry()
        choice = int(input("Choice: "))
        print()
        
        if choice == 1:
            while upload == False:
                print("[1] Check sticky note with password on it")
                print("[2] Enter Password")
                choice = int(input("Choice: "))
                print()

                if choice == 1:
                    print(f"Your Password: {password}")
                    input("Enter to go back ")
                    print()
                elif choice == 2:
                    choice = int(input("Please enter your password: "))
                    if choice == password:
                        print("Correct Password.")
                        print()

                        while True:
                            print("[1] Upload log files")
                            print("[2] Exit")
                            choice = int(input("Choice: "))
                            print()

                            if choice == 1:
                                print("Uploading log file")
                                print("██████")
                                time.sleep(3)
                                print("DONE!")
                                upload = True
                            elif choice == 2:
                                if upload == True:
                                    if reward[game - 1] != 0:
                                        print("Congratulations! You completed the challenge!")
                                        print("+ 25")
                                        score += 25
                                        reward[game - 1] = 0
                                    else:
                                        print("You have already completed the challenge before.")
                                    break
                                else:
                                    print("You have not upload the log file yet.")
                        print()

print(f"Completion Score: {score}/100")
print("WOW! You have completed all the mini games, GREAT JOB!")
