import telebot
import os
from loguru import logger
from src.utils.io import write_json
from src.data import DATA_DIR
from src.utils.constance import keyboards


class Bot:
    """
    Template for Telegram bot"""
    def __init__(self):
        # create bot object
        self.bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
        self.send_welcome = self.bot.message_handler(
            commands=['start', 'help']
        )(self.send_welcome)
        self.echo_all = self.bot.message_handler(
            func=lambda m: True
        )(self.echo_all)

    def run(self):
        # like infinite while loop
        logger.info('Bot is running')
        self.bot.infinity_polling()

    def send_welcome(self, message):
        """
        Replay to command messages
        """
        self.bot.reply_to(message, "Howdy, how are you doing?")

    # def echo_all(self, message):
    #     """
    #     Replay to a text message
    #     """
    #     write_json(DATA_DIR / 'Message.json', message.json)
    #     self.bot.reply_to(message, message.text)

    def echo_all(self, message):
        """
        Send message to a text message and show markup keyboard
        """
        write_json(DATA_DIR / 'Message.json', message.json)
        self.bot.send_message(
            message.chat.id, message.text,
            reply_markup=keyboards.main)


if __name__ == '__main__':
    logger.info('Bot Started')
    bot = Bot()
    bot.run()
    logger.info('Done!')
