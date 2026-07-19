
from colorama import Fore, Back, Style
import time
import sys
from discord_webhook import DiscordWebhook

cres = (Style.RESET_ALL)

print ("                            ,--" + Fore.YELLOW + ".!," + (cres))
print ("                         __/   " + Fore.YELLOW + "-*-" + (cres))
print ("                       ,d08b.  "  + Fore.YELLOW + "'|`" + (cres))
print ("                       0088MM")
print ("                       `9MMP'")
print ("---------------------------------------------------")
print ("          python webhook obliterator " + Fore.RED + "#tuff" + (cres))
print ("---------------------------------------------------")
print (" ")

#cool use thingy

userbanner = (Fore.RED + ("@user~/webhookspammer.py :") + Fore.WHITE)

def error():
    print(Fore.RED +"invalid choice !")


#question variables 
url = input ((userbanner) + " Whats the webhook url ? : ")
message = input ((userbanner) + " What message do you want to send ? : ")
times = input ((userbanner) + " How many times do you want to send your message ? : ")


try:
    times = int(times)
except ValueError:
    error()
    sys.exit()


between = input ((userbanner) + "How much time do you want to put between each messages ? : ")

try:
    bewteen = float(between)
except ValueError:
    error()
    sys.exit()

#spammer starting
for i in range (times):
    webhook = DiscordWebhook(url=(url), content=(message))
    response = webhook.execute()
    time.sleep(bewteen)

