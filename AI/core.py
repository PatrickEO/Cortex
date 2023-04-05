from gtts import gTTS
from playsound import playsound
import json
import os
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
    def menu(d_error:str):
        clear()
        print("0 - "+str(system_text["Menu"].get("0")))
        print("1 - "+str(system_text["Menu"].get("1")))
        print("2 - "+str(system_text["Menu"].get("2")))
        print("3 - "+str(system_text["Menu"].get("3")))
        print("4 - "+str(system_text["Menu"].get("4")))
        print("5 - "+str(system_text["Menu"].get("5")))
        print(back+" = "+str(system_text["Menu"].get("A")))
        print(d_error)

        option = input(str(system_text["Menu"].get("B")))
        if option == "0":
            exit
        elif option == "1":
            _create_audio()
        elif option == "2":
            _speak()
        elif option == "3":
                clear()
                print(str(system_text["Help"].get("A")))
                print("af : "+str(system_text["Help"].get("0")))
                print("ar : "+str(system_text["Help"].get("1")))
                print("az : "+str(system_text["Help"].get("2")))
                print("be : "+str(system_text["Help"].get("3")))
                print("bg : "+str(system_text["Help"].get("4")))
                print("bn : "+str(system_text["Help"].get("5")))
                print("ca : "+str(system_text["Help"].get("6")))
                print("cs : "+str(system_text["Help"].get("7")))
                print("cy : "+str(system_text["Help"].get("8")))
                print("da : "+str(system_text["Help"].get("9")))
                print("de : "+str(system_text["Help"].get("10")))
                print("el : "+str(system_text["Help"].get("11")))
                print("en : "+str(system_text["Help"].get("12")))
                print("eo : "+str(system_text["Help"].get("13")))
                print("es : "+str(system_text["Help"].get("14")))
                print("et : "+str(system_text["Help"].get("15")))
                print("eu : "+str(system_text["Help"].get("16")))
                print("fa : "+str(system_text["Help"].get("17")))
                print("fi : "+str(system_text["Help"].get("18")))
                print("fr : "+str(system_text["Help"].get("19")))
                print("ga : "+str(system_text["Help"].get("20")))
                print("gl : "+str(system_text["Help"].get("21")))
                print("gu : "+str(system_text["Help"].get("22")))
                print("hi : "+str(system_text["Help"].get("23")))
                print("hr : "+str(system_text["Help"].get("24")))
                print("ht : "+str(system_text["Help"].get("25")))
                print("hu : "+str(system_text["Help"].get("26")))
                print("id : "+str(system_text["Help"].get("27")))
                print("is : "+str(system_text["Help"].get("28")))
                print("it : "+str(system_text["Help"].get("29")))
                print("iw : "+str(system_text["Help"].get("30")))
                print("ja : "+str(system_text["Help"].get("31")))
                print("ka : "+str(system_text["Help"].get("32")))
                print("kn : "+str(system_text["Help"].get("33")))
                print("ko : "+str(system_text["Help"].get("34")))
                print("la : "+str(system_text["Help"].get("35")))
                print("lt : "+str(system_text["Help"].get("36")))
                print("lv : "+str(system_text["Help"].get("37")))
                print("mk : "+str(system_text["Help"].get("38")))
                print("ms : "+str(system_text["Help"].get("39")))
                print("mt : "+str(system_text["Help"].get("40")))
                print("nl : "+str(system_text["Help"].get("41")))
                print("no : "+str(system_text["Help"].get("42")))
                print("pl : "+str(system_text["Help"].get("43")))
                print("pt : "+str(system_text["Help"].get("44")))
                print("ro : "+str(system_text["Help"].get("45")))
                print("ru : "+str(system_text["Help"].get("46")))
                print("sk : "+str(system_text["Help"].get("47")))
                print("sl : "+str(system_text["Help"].get("48")))
                print("sq : "+str(system_text["Help"].get("49")))
                print("sr : "+str(system_text["Help"].get("50")))
                print("sv : "+str(system_text["Help"].get("51")))
                print("sw : "+str(system_text["Help"].get("52")))
                print("ta : "+str(system_text["Help"].get("53")))
                print("te : "+str(system_text["Help"].get("54")))
                print("th : "+str(system_text["Help"].get("55")))
                print("tl : "+str(system_text["Help"].get("56")))
                print("tr : "+str(system_text["Help"].get("57")))
                print("uk : "+str(system_text["Help"].get("58")))
                print("ur : "+str(system_text["Help"].get("59")))
                print("vi : "+str(system_text["Help"].get("60")))
                print("yi : "+str(system_text["Help"].get("61")))
                print("zh-CN : "+str(system_text["Help"].get("62")))
                print("zh-TW : "+str(system_text["Help"].get("63")))
                p = input(".....")
                menu("")
        elif option == "4":
            settings()
        elif option == "5":
            load()
        else:
            errormsg = str("!ERROR! - "+str(system_text["Menu"].get("error0")))
            menu(errormsg)


    def _create_audio():
        clear()
        text = str(input(str(system_text["CreateAudio"].get("0"))))
        if text.__contains__(back):
            menu("")
        else:
            text_lang = str(input(str(system_text["CreateAudio"].get("1"))))
            print(text_lang)
            if text_lang.__contains__(back):
                menu("")
            elif supported_languages.__contains__(text_lang):
                if regions.get(text_lang):
                    text_region = str(input(str(system_text["CreateAudio"].get("2"))))
                    if text_region.__contains__(back):
                        menu("")
                    elif regions.get(text_lang).get(text_region):
                        slow_mode = str(input(str(system_text["CreateAudio"].get("3"))))
                        if slow_mode.__contains__(back):
                            menu("")
                        else:
                            _slow = bool
                            if confirm.__contains__(slow_mode):
                                _slow = True
                            elif deny.__contains__(slow_mode):
                                _slow = False
                            else:
                                errormsg = str("!ERROR! - ("+slow_mode+") "+str(system_text["CreateAudio"].get("error2")))
                                menu(errormsg)
                            if _slow == False or True:
                                region = regions.get(text_lang).get(text_region)
                                myobj = gTTS(text=text, lang=text_lang, slow=_slow, tld=region)
                                filename = str(input(str(system_text["CreateAudio"].get("4"))))
                                if filename.__contains__(back):
                                    menu("")
                                else:
                                    filetype = str(input(str(system_text["CreateAudio"].get("5"))))
                                    if filetype.__contains__(back):
                                        menu("")
                                    else:
                                        file = filename + filetype
                                        myobj.save(audio_path+file)
                                        with open("save.json","r") as f:
                                            data = json.load(f)
                                            data["audio_list"].append(audio_path+file)
                                            with open("save.json", "w") as f:
                                                json.dump(data, f)
                                                f.close()
                                                menu("")
                    else:
                        errormsg = str("!ERROR! - "+str(system_text["CreateAudio"].get("error1")))
                        menu(errormsg)
                else:
                    slow_mode = str(input(str(system_text["CreateAudio"].get("3"))))
                    if slow_mode.__contains__(back):
                        menu("")
                    else:
                        _slow = bool
                        if confirm.__contains__(slow_mode):
                            _slow = True
                        elif deny.__contains__(slow_mode):
                            _slow = False
                        else:
                            errormsg = str("!ERROR! - ("+slow_mode+") "+str(system_text["CreateAudio"].get("error2")))
                            menu(errormsg)
                        if _slow == False or True:
                            myobj = gTTS(text=text, lang=text_lang, slow=_slow)
                            filename = str(input(str(system_text["CreateAudio"].get("4"))))
                            if filename.__contains__(back):
                                menu("")
                            else:
                                filetype = str(input(str(system_text["CreateAudio"].get("5"))))
                                if filetype.__contains__(back):
                                    menu("")
                                else:
                                    file = filename + filetype
                                    myobj.save(audio_path+file)
                                    with open("save.json","r") as f:
                                        data = json.load(f)
                                        data["audio_list"].append(audio_path+file)
                                        with open("save.json", "w") as f:
                                            json.dump(data, f)
                                            f.close()
                                            menu("")
            else:
                errormsg = str("!ERROR! - "+str(system_text["CreateAudio"].get("error0")))
                menu(errormsg)

    def _speak():
        with open("save.json","r") as f:
            sdata = json.load(f)
            size = len(sdata["audio_list"])
            while size:
                    if size <= 0:
                        menu("")
                        break
                    elif size > 0:
                        playsound(sdata["audio_list"].__getitem__(0))
                        os.remove(sdata["audio_list"].__getitem__(0))
                        sdata["audio_list"].remove(sdata["audio_list"].__getitem__(0))
                        with open("save.json","w") as f:
                            json.dump(sdata,f)
            else:
                menu("")
        menu("")

    def settings():
        clear()
        print("0 - "+str(system_text["Settings"].get("0")))
        print("1 - "+str(system_text["Settings"].get("1")))
        print("2 - "+str(system_text["Settings"].get("2")))
        settings_choice = str(input(str(system_text["Settings"].get("A"))))
        if settings_choice.__contains__(back):
            menu('')
        elif settings_choice == "0" or "1" or "2":
            if settings_choice == "0":
                menu('')
            elif settings_choice == "1":
                clear()
                settings_language = str(input(str(system_text["Settings"].get("1a0"))))
                if supported_languages.__contains__(settings_language):
                    if regions.get(settings_language):
                        settings_region = str(input(str(system_text["Settings"].get("1a1"))))
                        if settings_region.__contains__(back):
                            menu("")
                        elif regions.get(settings_language).get(settings_region):
                            with open("config.json","r") as f:
                                        cfg_data = json.load(f)
                                        cfg_data["SystemLanguage"] = str(settings_language+"-"+settings_region)
                                        with open("config.json", "w") as f:
                                            json.dump(cfg_data, f)
                                            f.close()
                                            menu("")
                        else:
                            errormsg = str("!ERROR! - "+str(system_text["Settings"].get("error2")))
                            menu(errormsg)
                    else:
                        with open("config.json","r") as f:
                                        cfg_data = json.load(f)
                                        cfg_data["SystemLanguage"] = str(settings_language)
                                        with open("config.json", "w") as f:
                                            json.dump(cfg_data, f)
                                            f.close()
                                            menu("")
                else:
                    errormsg = str("!ERROR! - "+str(system_text["Settings"].get("error1")))
                    menu(errormsg)
            elif settings_choice == "2":
                clear()
                print("0 - "+str(system_text["Settings"].get("0")))
                print("1 - "+str(system_text["Settings"].get("2a0")))
                print("2 - "+str(system_text["Settings"].get("2a1")))
                print("3 - "+str(system_text["Settings"].get("2a2")))
                settings_path_choice = str(input(str(system_text["Settings"].get("A"))))
                if settings_path_choice == "0" or "1" or "2" or "3":
                    clear()
                    if settings_path_choice == "1":
                        settings_path_language = str(input(str(system_text["Settings"].get("A"))))
                        with open("config.json","r") as f:
                                        lp_cfg_data = json.load(f)
                                        lp_cfg_data["LanguagePath"] = str(settings_path_language)
                                        with open("config.json", "w") as f:
                                            json.dump(lp_cfg_data, f)
                                            f.close()
                                            menu("")
                    elif settings_path_choice == "2":
                        settings_path_temp = str(input(str(system_text["Settings"].get("A"))))
                        with open("config.json","r") as f:
                                        tmp_cfg_data = json.load(f)
                                        tmp_cfg_data["TempPath"] = str(settings_path_temp)
                                        with open("config.json", "w") as f:
                                            json.dump(tmp_cfg_data, f)
                                            f.close()
                                            menu("")
                    elif settings_path_choice == "3":
                        settings_path_audio = str(input(str(system_text["Settings"].get("A"))))
                        with open("config.json","r") as f:
                                        audio_cfg_data = json.load(f)
                                        audio_cfg_data["AudioPath"] = str(settings_path_audio)
                                        with open("config.json", "w") as f:
                                            json.dump(audio_cfg_data, f)
                                            f.close()
                                            menu("")
                else:
                    errormsg = str("!ERROR! - "+str(system_text["Settings"].get("error0")))
                    menu(errormsg)
        else:
            errormsg = str("!ERROR! - "+str(system_text["Settings"].get("error0")))
            menu(errormsg)
    menu("")
load()