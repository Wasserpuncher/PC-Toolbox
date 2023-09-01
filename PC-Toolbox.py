import os
import shutil
import platform
import webbrowser
import subprocess
import random
import string
import hashlib
import csv
import json
import zipfile
import datetime
import requests
from bs4 import BeautifulSoup
import pyperclip
import sympy

# Funktion zum Löschen des Bildschirms je nach Plattform
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# ... (Alle anderen Funktionen bleiben unverändert)

# Funktion zum Konvertieren von Einheiten
def convert_units():
    try:
        print("Einheitenkonverter")
        print("Verfügbare Einheiten:")
        print("1. Meter zu Fuß")
        print("2. Kilogramm zu Pfund")
        choice = input("Bitte wählen Sie eine Einheit zum Konvertieren: ")

        if choice == "1":
            meters = float(input("Geben Sie die Anzahl der Meter ein: "))
            feet = meters * 3.28084
            print(f"{meters} Meter entsprechen {feet} Fuß.")
        elif choice == "2":
            kilograms = float(input("Geben Sie die Anzahl der Kilogramm ein: "))
            pounds = kilograms * 2.20462
            print(f"{kilograms} Kilogramm entsprechen {pounds} Pfund.")
        else:
            print("Ungültige Auswahl.")

    except Exception as e:
        print(f"Fehler beim Konvertieren von Einheiten: {str(e)}")

# Hauptmenü der Anwendung
def main_menu():
    while True:
        clear_screen()
        print("Willkommen im erweiterten PC-Toolbox-Programm!")
        print("1. Datei kopieren")
        print("2. Datei verschieben")
        print("3. Datei löschen")
        print("4. Dateien in Verzeichnis auflisten")
        print("5. Verzeichnis erstellen")
        print("6. Webseite öffnen")
        print("7. Befehl ausführen")
        print("8. Zufälliges Passwort generieren")
        print("9. Datei suchen")
        print("10. Systeminformationen anzeigen")
        print("11. Leere Textdatei erstellen")
        print("12. MD5-Hash einer Datei berechnen")
        print("13. CSV-Datei lesen")
        print("14. JSON-Datei schreiben")
        print("15. ZIP-Archiv extrahieren")
        print("16. ZIP-Archiv erstellen")
        print("17. Wechselkurse abrufen")
        print("18. Text in Zwischenablage kopieren")
        print("19. Einheiten konvertieren")
        print("20. Beenden")

        choice = input("Bitte wählen Sie eine Option: ")

        if choice == "1":
            source = input("Geben Sie die Quelldatei ein: ")
            destination = input("Geben Sie das Zielverzeichnis ein: ")
            copy_file(source, destination)
            input("Drücken Sie Enter, um fortzufahren...")
        elif choice == "2":
            source = input("Geben Sie die Quelldatei ein: ")
            destination = input("Geben Sie das Zielverzeichnis ein: ")
            move_file(source, destination)
            input("Drücken Sie Enter, um fortzufahren...")
        elif choice == "3":
            file_path = input("Geben Sie den Pfad zur zu löschenden Datei ein: ")
            delete_file(file_path)
            input("Drücken Sie Enter, um fortzufahren...")
        # ... (Andere Optionen bleiben unverändert)
        elif choice == "19":
            convert_units()
            input("Drücken Sie Enter, um fortzufahren...")
        elif choice == "20":
            break

if __name__ == "__main__":
    main_menu()
