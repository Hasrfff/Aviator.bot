
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ConversationHandler
)

TELEGRAM_TOKEN = "8100400385:AAGIwJ5JV-D21rU9aWlBM1lpLcO00vTvn4A"

WAITING_FOR_ID, GAME_SELECTION = range(2)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🎮 Welcome to Prediction Bot!\n\nPlease enter your Expectation ID:"
    )
    return WAITING_FOR_ID

def verify_id(update: Update, context: CallbackContext):
    expectation_id = update.message.text
    if expectation_id.strip():
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
        query.message.reply_text(
            "🔮 Thimbles Prediction\n\nGlass Class: C\nBalls: [Red, Blue, Green]"
        )
    elif query.data == "aviator":
        query.message.reply_text(
            "✈️ Aviator Prediction\n\nNext X: 2.85x"
        )

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("ℹ️ Type /start to begin.\nEnter your Expectation ID to continue.")

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
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

if __name__ == "__main__":
    main()
