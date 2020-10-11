import requests
import custom_schedule
import time
import telepot

class TelegramBot():

    def __init__(self, url):
        self.url = url
        # self.chat_id = -1001187367399
        # chat_id = -1001367674629

    def get_updates(self):
        response = requests.get(self.url + 'getUpdates')
        return response.json()

    def last_update(self):
        results = self.get_updates()['result']
        last_updates = len(results) - 1
        return results[last_updates]

    def get_last_chat_id(self):
        return self.last_update()['message']['chat']['id']

    def send_message(self, text, chat_id):
        params = {'chat_id' : chat_id, 'text' : text}
        response = requests.post(self.url + 'sendMessage', data=params)
        return response

    def pin_message(self, message_id, chat_id):
        params = {'chat_id' : chat_id, 'message_id' : message_id, "disable_notification" : False}
        response = requests.post(self.url + 'pinChatMessage', data=params)
        return response

    # def send_photo(self, path, chat_id):
    #     image = Image.open(path)
    #     image.get
    #     photo = open(path, 'rb')
    #     photo.
    #     params = {'chat_id' : chat_id, 'photo' : photo}
    #     response = requests.post(self.url + 'sendMessage', data=params)
    #     return response



def send(bot):
    chat_id = -1001367674629
    bot.sendMessage(chat_id, "Started in FI-83! Time: " + (str(int(time.strftime("%H"))+3)+time.strftime(":%M")) + '\n Week: ' + str(int(time.strftime("%W")) % 2))

def main():
    bot = telepot.Bot("https://api.telegram.org/bot1112357683:AAHsOL-X4oOku65teNY074LZuHbHdIFfGSs/")
    lessons = custom_schedule.create_schedule()
    send(bot)
    while True:
        time.sleep(1)
        for lesson in lessons:
            if lesson.day == time.strftime("%w") and lesson.time == (str(int(time.strftime("%H"))+3)+time.strftime(":%M")):
                if lesson.week == 3 or lesson.week == int(time.strftime("%W")) % 2:
                    chat_id = -1001187367399
                    resp = bot.sendMessage(chat_id, lesson.name + '\n' + lesson.zoom)
                    bot.pin_message(int(resp.json()["result"]["message_id"]), chat_id)
                    if resp.status_code == 200:
                        time.sleep(70)



if __name__ == '__main__':
	main()