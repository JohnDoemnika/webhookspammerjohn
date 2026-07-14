
from colorama import Fore, Back, Style
import time
import sys
from discord_webhook import DiscordWebhook
print (Fore.WHITE + "                            ,--" + Fore.YELLOW + ".!,")
print (Fore.WHITE + "                         __/   " + Fore.YELLOW + "-*-")
print (Fore.WHITE + "                       ,d08b.  "  + Fore.YELLOW + "'|`")
print (Fore.WHITE + "                       0088MM")
print ("                       `9MMP'")
print ("---------------------------------------------------")
print ("          python webhook obliterator " + Fore.RED + "#tuff")
print (Fore.WHITE + "---------------------------------------------------")
print (" ")

url = input("Whats the webhook url ? : ")
message = input("What message do you want to send ? : ")
times = input("How many times do you want to send your message ? : ")
between = input ("How much time do you want to put bewteen each messages ? : ")
try:
    times = int(times)
except ValueError:
    print("invalid choice !")
    sys.exit()
try:
    bewteen = float(between)
except ValueError:
    print("invalid choice !")
    sys.exit()


for i in range (times):
        webhook = DiscordWebhook(url=(url), content=(message))
        response = webhook.execute()
        time.sleep(bewteen)
