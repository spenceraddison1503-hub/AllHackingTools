#!/usr/bin/python3
#Copyright 2021 AllHackingTools
#Written by : Misha Korzhik
#Github     : http://github.com/mishakorzik

import os
import subprocess
import time

REPO_ROOT = os.path.abspath(os.path.dirname(__file__))


def run_command(command):
    subprocess.run(command, cwd=REPO_ROOT, check=False)


def run_menu_action(*command):
    run_command(["bash", "src/Inf.sh"])
    run_command(list(command))


os.system("clear")
os.chdir(REPO_ROOT)
os.system("bash Logo.sh")
os.system("bash src/MenuOps.sh")

op = str(input("Options: "))

if op == "1":
    run_menu_action("python2", "Files/IpMenu.py")
elif op == "2":
    run_menu_action("python2", "Files/RouterMenu.py")
elif op == "3":
    run_menu_action("python2", "Files/MailMenu.py")
elif op == "4":
    run_menu_action("python2", "Files/WebMenu.py")
elif op == "5":
    run_menu_action("python2", "Files/CamHackMenu.py")
elif op == "6":
    run_menu_action("python2", "Files/AndroidMenu.py")
elif op == "7":
    run_menu_action("python2", "Files/SQLinjectionMenu.py")
elif op == "8":
    run_menu_action("python2", "Files/SocialMenu.py")
elif op == "9":
    run_menu_action("python2", "Files/SpamMenu.py")
elif op == "10":
    run_menu_action("python2", "Files/AnalistickMenu.py")
elif op == "11":
    run_menu_action("python2", "Files/DarkSearchMenu.py")
elif op == "12":
    run_menu_action("python2", "Files/PhishingMenu.py")
elif op == "13":
    run_menu_action("python2", "Files/PassworldMenu.py")
elif op == "14":
    run_menu_action("python2", "Files/WordlistGeneratorMenu.py")
elif op == "15":
    run_menu_action("python2", "Files/XSSAttackMenu.py")
elif op == "16":
    run_menu_action("python2", "Files/discordMenu.py")
elif op == "17":
    run_menu_action("python2", "Files/telegramMenu.py")
elif op == "18":
    run_menu_action("python2", "Files/Other.py")
elif op == "19":
    run_menu_action("python2", "Files/TermuxS.py")
elif op == "20":
    run_menu_action("python2", ".settings/settingsMenu.py")
elif op == "21":
    run_menu_action("bash", ".settings/LICENSE.sh")
    run_menu_action("python3", "src/Timer2.py")
    run_command(["python2", "MainMenu.py"])
elif op == "22":
    run_menu_action("bash", "src/UpdateTool.sh")
    time.sleep(1)
    run_command(["bash", "-lc", "cd $HOME && git clone https://github.com/mishakorzik/AutoUpdateMyTools && cd AutoUpdateMyTools && bash AllHackingToolupdate.sh"])
elif op == "23":
    run_menu_action("bash", "src/About.sh")
elif op == "13324715":
    print("[DEBUG] Developer mode successfully enabled!")
    time.sleep(0.8)
    run_command(["bash", "-lc", "cd .settings && mv DesingLogo.py /data/data/com.termux/files/home/AllHackingTools/.temp/ && mv DesingMenu.py /data/data/com.termux/files/home/AllHackingTools/.temp/"])
    print("[DEBUG] Please restart AllHackingTools!")
    run_command(["bash", "-lc", "mv MainMenu.py /data/data/com.termux/files/home/AllHackingTools/.temp/temp && cd .settings && cd debug && cp MainMenu.py /data/data/com.termux/files/home/AllHackingTools/"])
    print("[DEBUG] Warning! Customization has been disabled.")
elif op == "24":
    run_command(["bash", "-lc", "clear && bash Logo.sh"])
    print("\033[1;31;40mExiting System...")
    time.sleep(0.7)
else:
    print("\033[1;31;40mInvalid input. Reloading Tools")
    time.sleep(1.6)
    run_command(["python2", "MainMenu.py"])
