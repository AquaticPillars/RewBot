#!/usr/bin/env python3
import logging

from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Dispatcher,
    Updater,
)


def start(update: Update, context: CallbackContext) -> None:
    if update.message is None:
        return
    update.message.reply_text("This is a bot", quote=True)


def main(token: str) -> None:
    updater = Updater(token, use_context=True)
    dispatcher: Dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    import argparse

    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Runs TG bot")
    parser.add_argument(
        "token",
        action="store",
        type=str,
        help="Telegram Token for the bot",
    )
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    main(args.token)
