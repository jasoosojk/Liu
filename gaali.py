from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# List of galis
galis = [
    "Teri ma ka bhosda sale maderchod ki aulad 🤬!",
    "Abe Randi ke bacche tara maa chod dunga zyada mat kar!",
    "Tara maa ka bhosda mai se hu madarchod!",
    "bhosdike Randi ke pille kyu Gaand mai ungli kar raha hai tu aapni mummy ko bhej na idar!",
    "tari maa ki chut mai bakari ka lund!",
    "Bahen ke lawde aapni aukat Mai rahe varna tari maa Randi ki bacchi",
    "char chavana ghode pe tu mare Lawde pe!",
    "kutte ke aulad madarchod randi ke aulad",
    "Abey Gandi",
    "Bakwaas band kar Bkl!"
]

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Namaste! Mujhse baat karo aur galiyan suno. 😜")

# Help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Mujhe kuch bhi bhejo, aur main tumhe ek 'special' reply dunga!")

# Gali responder
def gali_responder(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    random_gali = random.choice(galis)
    update.message.reply_text(f"{random_gali}")

def main():
    # Replace 'YOUR_BOT_TOKEN' with your Telegram bot token
    TOKEN = "8199466321:AAExiElx5M5nrSxBlZp7HEnMb4H3IFbY3U0"
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Register message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, gali_responder))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__'
    main()
