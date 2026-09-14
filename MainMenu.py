#!/usr/bin/python3
#Copyright 2021 AllHackingTools
#Written by : Misha Korzhik
#Github     : http://github.com/mishakorzik                                                                           
import os
import subprocess
import time
import sys

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))


def run_command(*command):
 subprocess.run(command, cwd=REPO_ROOT, check=False)


def run_python2(script):
 run_command("python2", script)


run_command("clear")
run_command("bash", "Logo.sh")
run_command("bash", "src/MenuOps.sh")

MENU_SCRIPTS = {
 "1": "Files/IpMenu.py",
 "2": "Files/RouterMenu.py",
 "3": "Files/MailMenu.py",
 "4": "Files/WebMenu.py",
 "5": "Files/CamHackMenu.py",
 "6": "Files/AndroidMenu.py",
 "7": "Files/SQLinjectionMenu.py",
 "8": "Files/SocialMenu.py",
 "9": "Files/SpamMenu.py",
 "10": "Files/AnalistickMenu.py",
 "11": "Files/DarkSearchMenu.py",
 "12": "Files/PhishingMenu.py",
 "13": "Files/PassworldMenu.py",
 "14": "Files/WordlistGeneratorMenu.py",
 "15": "Files/XSSAttackMenu.py",
 "16": "Files/discordMenu.py",
 "17": "Files/telegramMenu.py",
 "18": "Files/Other.py",
 "19": "Files/TermuxS.py",
 "20": ".settings/settingsMenu.py",
}

op = str(input("Options: "))
if op in MENU_SCRIPTS:
 run_command("bash", "src/Inf.sh")
 time.sleep(0.3)
 run_python2(MENU_SCRIPTS[op])
elif op == "21":
 run_command("bash", "src/Inf.sh")
 time.sleep(0.3)
 run_command("clear")
 run_command("bash", ".settings/LICENSE.sh")
 run_command("python3", "src/Timer2.py")
 run_python2("MainMenu.py")
elif op == "22":
 run_command("bash", "src/Inf.sh")
 time.sleep(0.3)
 time.sleep(1)
 os.system("cd $HOME && git clone https://github.com/mishakorzik/AutoUpdateMyTools && cd AutoUpdateMyTools && bash AllHackingToolupdate.sh")
 #os.system("cd && cd AllHackingTools && bash src/UpdateTool.sh")
elif op == "23":
 run_command("bash", "src/Inf.sh")
 time.sleep(0.3)
 run_command("bash", "src/About.sh")
elif op == "13324715":
 print("[DEBUG] Developer mode successfully enabled!")
 time.sleep(0.8)
 os.system("cd && cd AllHackingTools && cd .settings && mv DesingLogo.py /data/data/com.termux/files/home/AllHackingTools/.temp/ && mv DesingMenu.py /data/data/com.termux/files/home/AllHackingTools/.temp/")
 print("[DEBUG] Please restart AllHackingTools!")
 os.system("cd && cd AllHackingTools && mv MainMenu.py /data/data/com.termux/files/home/AllHackingTools/.temp/temp && cd .settings && cd debug && cp MainMenu.py /data/data/com.termux/files/home/AllHackingTools/")
 print("[DEBUG] Warning! Customization has been disabled.")
elif op == "24":
 run_command("clear")
 run_command("bash", "Logo.sh")
 print("\033[1;31;40mExiting System...")
 time.sleep(0.7)
else:
 print("\033[1;31;40mInvalid input. Reloading Tools")
 time.sleep(1.6)
 run_python2("MainMenu.py")
