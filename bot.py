import requests
import custom_schedule
import time
import telepot




def send(bot):
    chat_id = -1001367674629
    bot.sendMessage(chat_id, "Started in FI-83! Time: " + (str(int(time.strftime("%H"))+3)+time.strftime(":%M")) + '\n Week: ' + str(int(time.strftime("%W")) % 2))
    # bot.sendPhoto(chat_id, photo=open('1.jpg', 'rb'))

def main():
    bot = telepot.Bot("1112357683:AAHsOL-X4oOku65teNY074LZuHbHdIFfGSs")
    lessons = custom_schedule.create_schedule()
    send(bot)
    while True:
        time.sleep(1)
        for lesson in lessons:
            if lesson.day == time.strftime("%w") and lesson.time == (str(int(time.strftime("%H"))+3)+time.strftime(":%M")):
                if lesson.week == 3 or lesson.week == int(time.strftime("%W")) % 2:
                    chat_id = -1001187367399
                    message_id = bot.sendMessage(chat_id, lesson.name + '\n' + lesson.zoom).message_id
                    bot.pinChatMessage(chat_id = chat_id, message_id = message_id)
                    # if lesson.name == 'Мат.прога | Хмельницкий':
                        # bot.sendPhoto(chat_id, photo=open('1.jpg', 'rb'))
                    # if message_id != None:
                    time.sleep(70)
                        



if __name__ == '__main__':
	main()