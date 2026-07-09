import subprocess
import os


def open_notepad():
    subprocess.Popen("notepad.exe")


def open_calculator():
    subprocess.Popen("calc.exe")


def open_vscode():
    os.system("code")


def open_explorer():
    subprocess.Popen("explorer")