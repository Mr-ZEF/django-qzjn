import logging
import os
import sys
import asyncio
import json

from telegram import Bot, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import __version__ as TG_VER

from django.core.wsgi import get_wsgi_application

# sys.path.append('D:\\jupyter\\telegram_web_app\\myproject')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

# Ваши импорты из Django-приложения
# from your_app.models import ...
# from your_app.serializers import ...
# from your_app.services import ...

TOKEN = '5580744721:AAE8jfBhx5Oq6534yJxJBXYH4SSaQ4K8Gac'

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a `/start` command handler.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with a button that opens a the web app."""
    await update.message.reply_text(
        "Добро Пожаловать в Telegram WebApp",
#        reply_markup=ReplyKeyboardMarkup.from_button(
#            KeyboardButton(
#                text="Open the color picker!",
#                web_app=WebAppInfo(url="https://python-telegram-bot.org/static/webappbot"),
#            )
#        ),
    )


# Handle incoming WebAppData
async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Print the received data and remove the button."""
    # Here we use `json.loads`, since the WebApp sends the data JSON serialized string
    # (see webappbot.html)
    data = json.loads(update.effective_message.web_app_data.data)
    await update.message.reply_html(
        text=f"You selected the color with the HEX value <code>{data['hex']}</code>. The "
        f"corresponding RGB value is <code>{tuple(data['rgb'].values())}</code>.",
        reply_markup=ReplyKeyboardRemove(),
    )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))
#    await Bot.set_my_commands(commands=commands_for_Bot)
#    Bot.set_chat_menu_button(
#        type="web_app", text="Открыть Web-приложение",
#        web_app=WebAppInfo(url="://python-telegram-bot.org/static/webappbot")
#    )


    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()