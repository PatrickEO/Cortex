import pytchat
import os
import json
import platform

def load():
    with open("./config.json","r") as config_file:
        config_data = json.load(config_file)
        system_language = config_data["SystemLanguage"]
        language_path = config_data["LanguagePath"]
        temp_path = config_data["TempPath"]
        audio_path = config_data["AudioPath"]
        confirm = config_data["Confirm"]
        deny = config_data["Deny"]
        back = config_data["Back"]
        supported_languages = config_data["SupportedLanguages"]
        regions = config_data["Regions"]
        if open(str(language_path+system_language+".json")):
            with open(str(language_path+system_language+".json"),"r") as language:
                system_text = json.load(language)
    config_file.close()
    def clear():
        if platform.system().lower().__contains__("windowns"):
            print("windowns")
            clear = os.system("cls")
        elif platform.system().lower().__contains__("linux"):
            print("linux")
            clear = os.system("clear")
    
    ID = input('ID: ')
    try:
        chat = pytchat.create(video_id=ID)
        while chat.is_alive():
            for c in chat.get().sync_items():
                print(f"{c.datetime} [{c.author.name}]- {c.message}")
                if c.message.__contains__("/"):
                    print("command")
        else:
            print("chat morto.")
    except:
        print("ERROR")
load()