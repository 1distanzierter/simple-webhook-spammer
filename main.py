from dhooks import Webhook
from colorama import Fore#
import requests

print(f"""
{Fore.LIGHTRED_EX}
     _                 _                     _     _                 _    
    (_)               | |                   | |   | |               | |   
 ___ _ _ __ ___  _ __ | | ___  __      _____| |__ | |__   ___   ___ | | __
/ __| | '_ ` _ \| '_ \| |/ _ \ \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ /
\__ \ | | | | | | |_) | |  __/  \ V  V /  __/ |_) | | | | (_) | (_) |   < 
|___/_|_| |_| |_| .__/|_|\___|   \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\
                | |                                                       
                |_|                                                       
                                               
                                               
 ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
/ __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
\__ \ |_) | (_| | | | | | | | | | | |  __/ |   
|___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
    | |                                        
    |_|                                        


{Fore.LIGHTWHITE_EX}#coded by artur.exe#2122

""")

WebhookURL = Webhook(input(f"{Fore.LIGHTWHITE_EX}Your Webhook URL: "))
Amount_Of_Messages = int(input(f"{Fore.LIGHTWHITE_EX}How many Messages: "))
Your_Message = input(f"{Fore.LIGHTWHITE_EX}Your Message: ")
everyone_ping = input(f"{Fore.LIGHTWHITE_EX}You want to ping @everyone? y/n ")

if everyone_ping == "y":

    i = 0

    while i < Amount_Of_Messages:
        Your_Everyone_Message = "@everyone\n" + Your_Message
        WebhookURL.send(Your_Everyone_Message)
        i += 1
    input(f"{Fore.LIGHTWHITE_EX}Press enter to exit")
    exit()

