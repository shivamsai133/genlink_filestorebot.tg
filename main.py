# main.py

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import os
import requests

# Your bot's token from BotFather
TOKEN = "YOUR_BOT_TOKEN"  # Replace this with your Telegram bot token

# Start command: Sent when the user starts the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to Genlink Filestore Bot! Send me any file, and I will generate a download link for it."
    )

# File handling function: When a user sends a file
def handle_file(update: Update, context: CallbackContext):
    # Get file from Telegram
    file = update.message.document
    file_name = file.file_name
    file_id = file.file_id

    # Download the file
    new_file = context.bot.get_file(file_id)
    new_file.download(file_name)

    # Here, we assume you're using a simple HTTP server to serve files.
    # You can upload the file to a cloud service later (AWS S3, Google Drive, etc).
    download_link = f"Your file '{file_name}' is available for download at: https://example.com/{file_name}"

    # Send the download link back to the user
    update.message.reply_text(download_link)

# Main function: Start the bot
def main():
    # Set up the Updater and Dispatcher
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    # Add handlers for /start command and file messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.Document.ALL, handle_file))

    # Start polling for messages
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

