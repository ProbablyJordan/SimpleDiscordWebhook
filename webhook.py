from discord_webhook import DiscordWebhook

while True:
    url = input('Input webhook url\n')
    text = input('Insert text\n')
    webhook = DiscordWebhook(url=url, content=text)
    webhook.execute()
    print('Done!')
