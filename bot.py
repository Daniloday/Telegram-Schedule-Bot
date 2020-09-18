import requests
import custom_schedule
import time

class TelegramBot():

    def __init__(self, url):
        self.url = url
        self.chat_id = -1001367674629
        # chat_id = -1001187367399

    def get_updates(self):
        response = requests.get(self.url + 'getUpdates')
        return response.json()

    def last_update(self):
        results = self.get_updates()['result']
        last_updates = len(results) - 1
        return results[last_updates]

    def get_last_chat_id(self):
        return self.last_update()['message']['chat']['id']

    def send_message(self, text):
        params = {'chat_id' : self.chat_id, 'text' : text}
        response = requests.post(self.url + 'sendMessage', data=params)
        return response

    def pin_message(self,message_id):
        params = {'chat_id' : self.chat_id, 'message_id' : message_id, "disable_notification" : False}
        response = requests.post(self.url + 'pinChatMessage', data=params)
        return response


def send(bot):
    resp = bot.send_message("Hello world!")
    bot.pin_message(int(resp.json()["result"]["message_id"]))

def main():
    bot = TelegramBot("https://api.telegram.org/bot1112357683:AAHsOL-X4oOku65teNY074LZuHbHdIFfGSs/")
    lessons = custom_schedule.create_schedule()
    send(bot)
    while True:
        time.sleep(1)
        for lesson in lessons:
            if lesson.day == time.strftime("%w") and lesson.time == (str(int(time.strftime("%H"))+3)+time.strftime(":%M")):
                if lesson.week == 3 or lesson.week == int(time.strftime("%W")) % 2:
                    resp = bot.send_message(lesson.name + '\n' + lesson.zoom)
                    bot.pin_message(int(resp.json()["result"]["message_id"]))
                    if resp.status_code == 200:
                        time.sleep(70)



if __name__ == '__main__':
	main()