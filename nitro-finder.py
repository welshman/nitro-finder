import string
import random
import requests
from discord_webhook import DiscordWebhook
import time

WEBHOOK = '[DISCORD WEBHOOK URL HERE]'

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

while True:
 base_url = "https://discordapp.com/api/v6/entitlements/gift-codes/"
 file_id = get_random_alphaNumeric_string(16)
 final_part = "?with_application=false&with_subscription_plan=true"
 final_url = base_url + file_id + final_part
 response = requests.get(final_url).text

 if ('Nitro Monthly' or 'subscription_plan') in str(response):
   webhook = DiscordWebhook(url=WEBHOOK, content="https://discord.gift/"+file_id)
   response = webhook.execute()
 else:
   print("BAD - https://discord.gift/"+file_id)
 time.sleep(20)
