#!/usr/bin/python3
#Copyright 2021 AllHackingTools
#Written by : Misha Korzhik
#Github     : http://github.com/mishakorzik

import os
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOME = Path.home()


def run_in(cwd, *cmd):
    subprocess.run([str(part) for part in cmd], cwd=str(cwd), check=False, shell=False)


def run(*cmd):
    run_in(ROOT, *cmd)


def run_menu(command):
    run("bash", "src/Inf.sh")
    run("python2", command)


os.system("clear")
run("bash", "Logo.sh")
run("bash", "src/MenuOps.sh")

op = str(input("Options: "))
if op == "1":
    run_menu("Files/IpMenu.py")
elif op == "2":
    run_menu("Files/RouterMenu.py")
elif op == "3":
    run_menu("Files/MailMenu.py")
elif op == "4":
    run_menu("Files/WebMenu.py")
elif op == "5":
    run_menu("Files/CamHackMenu.py")
elif op == "6":
    run_menu("Files/AndroidMenu.py")
elif op == "7":
    run_menu("Files/SQLinjectionMenu.py")
elif op == "8":
    run_menu("Files/SocialMenu.py")
elif op == "9":
    run_menu("Files/SpamMenu.py")
elif op == "10":
    run_menu("Files/AnalistickMenu.py")
elif op == "11":
    run_menu("Files/DarkSearchMenu.py")
elif op == "12":
    run_menu("Files/PhishingMenu.py")
elif op == "13":
    run_menu("Files/PassworldMenu.py")
elif op == "14":
    run_menu("Files/WordlistGeneratorMenu.py")
elif op == "15":
    run_menu("Files/XSSAttackMenu.py")
elif op == "16":
    run_menu("Files/discordMenu.py")
elif op == "17":
    run_menu("Files/telegramMenu.py")
elif op == "18":
    run_menu("Files/Other.py")
elif op == "19":
    run_menu("Files/TermuxS.py")
elif op == "20":
    run_menu(".settings/settingsMenu.py")
elif op == "21":
    run("bash", "src/Inf.sh")
    run("bash", ".settings/LICENSE.sh")
    run("python3", "src/Timer2.py")
    run("python2", "MainMenu.py")
elif op == "22":
    run("bash", "src/Inf.sh")
    run_in(HOME, "git", "clone", "https://github.com/mishakorzik/AutoUpdateMyTools")
    run_in(HOME / "AutoUpdateMyTools", "bash", "AllHackingToolupdate.sh")
elif op == "23":
    run("bash", "src/Inf.sh")
    run("bash", "src/About.sh")
elif op == "13324715":
    print("[DEBUG] Developer mode successfully enabled!")
    time.sleep(0.8)
    run_in(ROOT / ".settings", "mv", "DesingLogo.py", str(ROOT / ".temp" / "DesingLogo.py"))
    run_in(ROOT / ".settings", "mv", "DesingMenu.py", str(ROOT / ".temp" / "DesingMenu.py"))
    print("[DEBUG] Please restart AllHackingTools!")
    run_in(ROOT, "mv", "MainMenu.py", str(ROOT / ".temp" / "temp"))
    run_in(ROOT / ".settings" / "debug", "cp", "MainMenu.py", str(ROOT))
    print("[DEBUG] Warning! Customization has been disabled.")
elif op == "24":
    os.system("clear")
    run("bash", "Logo.sh")
    print("\033[1;31;40mExiting System...")
    time.sleep(0.7)
else:
    print("\033[1;31;40mInvalid input. Reloading Tools")
    time.sleep(1.6)
    run_in(HOME, "python2", "MainMenu.py")
