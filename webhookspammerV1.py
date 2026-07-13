import time
from discord_webhook import DiscordWebhook
url = input("Whats the webhook url ? : ")
message = input("What message do you want to send ? : ")
times = int(input("How many times do you want to send your message ? : "))
print ("Starting")

for i in range (times):
    webhook = DiscordWebhook(url=(url), content=(message))
    response = webhook.execute()
    time.sleep(0.5)