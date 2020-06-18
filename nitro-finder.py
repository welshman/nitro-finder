import string
import random
import requests
from discord_webhook import DiscordWebhook
import time

WEBHOOK = 'https://discordapp.com/api/webhooks/722313976238702644/Y5Irat6sMZfpQ-QUomJl7G_xBal21YRjqXlarlCpCm6QLFFvucO7J1BWdWWwOvrSwOmF'

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def build_url():
    base_url = "https://discordapp.com/api/v6/entitlements/gift-codes/"
    file_id = get_random_alphaNumeric_string(16)
    final_part = "?with_application=false&with_subscription_plan=true"
    final_url = base_url + file_id + final_part
    return final_url

while True:
 response = requests.get(build_url()).text

 if ('Nitro Monthly' or 'subscription_plan') in str(response):
   webhook = DiscordWebhook(url=WEBHOOK, content=build_url())
   response = webhook.execute()
 else:
   print("BAD - "+build_url())
 time.sleep(20)