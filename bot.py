import requests
import schedule
import custom_schedule
import time

class TelegramBot():

    def __init__(self, url):
        self.url = url
        self.chat_id = -1001367674629

    def get_updates(self):
        response = requests.get(self.url + 'getUpdates')
        return response.json()

    def last_update(self):
        results = self.get_updates()['result']
        last_updates = len(results) - 1
        return results[last_updates]

    def get_last_chat_id(self):
        return self.last_update()['message']['chat']['id']

    def send_message(self, chat_id, text):
        params = {'chat_id' : chat_id, 'text' : text}
        response = requests.post(self.url + 'sendMessage', data=params)
        return response

def send(bot):
    chat_id = -1001367674629
    bot.send_message(chat_id, "anime")

def main():
    bot = TelegramBot("https://api.telegram.org/bot1112357683:AAHsOL-X4oOku65teNY074LZuHbHdIFfGSs/")
    lessons = custom_schedule.create_schedule()
    while True:
        time.sleep(1)
        for lesson in lessons:
            if lesson.day == time.strftime("%w") and lesson.time == time.strftime("%H:%M"):
                if lesson.week == 3 or lesson.week == int(time.strftime("%W")) % 2:
                    chat_id = -1001367674629
                    resp = bot.send_message(chat_id, lesson.name + '\n' + lesson.zoom)
                    if resp.status_code == 200:
                        time.sleep(70)



if __name__ == '__main__':
	main()