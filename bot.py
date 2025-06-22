import os
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# ✅ Replace this token with your real BotFather token
TELEGRAM_TOKEN = "8100400385:AAGIwJ5JV-D21rU9aWlBM1lpLcO00vTvn4A"
API_BASE_URL = "https://your-api-server.com"

WAITING_FOR_ID, GAME_SELECTION = range(2)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎮 Welcome to Prediction Bot!\n\nPlease enter your Expectation ID:")
    return WAITING_FOR_ID

def verify_id(update: Update, context: CallbackContext):
    expectation_id = update.message.text
    response = requests.post(f"{API_BASE_URL}/verify_id", json={"id": expectation_id})

    if response.status_code == 200:
        keyboard = [
            [InlineKeyboardButton("🎲 Thimbles", callback_data="timbles")],
            [InlineKeyboardButton("✈️ Aviator", callback_data="aviator")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("✅ ID Verified!\n\nChoose a game:", reply_markup=reply_markup)
        return GAME_SELECTION
    else:
        update.message.reply_text("❌ Invalid ID! Please enter a valid Expectation ID:")
        return WAITING_FOR_ID

def game_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "timbles":
        response = requests.get(f"{API_BASE_URL}/game/timbles/latest")
        if response.status_code == 200:
            data = response.json()
            query.message.reply_text(
                f"🔮 Timbles Prediction\n\nGlass Class: {data['glass_class']}\nBalls: {data['balls']}"
            )
    elif query.data == "aviator":
        response = requests.get(f"{API_BASE_URL}/game/aviator/next")
        if response.status_code == 200:
            data = response.json()
            query.message.reply_text(
                f"✈️ Next Aviator X: {data['x_bet']}x"
            )

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("ℹ️ Type /start to begin.\nEnter your Expectation ID to continue.")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            WAITING_FOR_ID: [MessageHandler(Filters.text & ~Filters.command, verify_id)],
            GAME_SELECTION: [CallbackQueryHandler(game_selection)]
        },
        fallbacks=[CommandHandler("help", help_command)]
    )
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if name == "main":
    main()