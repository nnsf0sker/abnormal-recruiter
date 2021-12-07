import logging

from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from interviewer import Interviewer

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


interviewer = Interviewer()


def on_start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    reply_messages = interviewer.start_interview(user_id)

    for message in reply_messages:
        update.message.reply_text(message)


def on_message(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    answer = update.message.text

    reply_messages = interviewer.process_answer(user_id, answer)

    for message in reply_messages:
        update.message.reply_text(message)


def on_finish(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    reply_messages = interviewer.finish_interview(user_id)

    for message in reply_messages:
        update.message.reply_text(message)


def main():
    updater = Updater("<secret_hash>", use_context=True)

    dp = updater.dispatcher

    start_handler = CommandHandler("start", on_start)
    message_handler = MessageHandler(Filters.all, on_message)
    finish_handler = CommandHandler("finish", on_finish)

    dp.add_handler(start_handler)
    dp.add_handler(message_handler)
    dp.add_handler(finish_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
