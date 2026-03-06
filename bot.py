import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8774370442:AAFX_9GqAUjpJe4mnnLhdN08U8OJwmCQNm0"

logging.basicConfig(level=logging.INFO)

SCRIPTS = {
    "blox_fruits": {
        "name": "🍎 Blox Fruits",
        "script": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ВСТАВЬ_СКРИПТ/bloxfruits.lua"))()'
    },
    "arsenal": {
        "name": "🔫 Arsenal",
        "script": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ВСТАВЬ_СКРИПТ/arsenal.lua"))()'
    },
    "brookhaven": {
        "name": "🏠 Brookhaven",
        "script": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ВСТАВЬ_СКРИПТ/brookhaven.lua"))()'
    },
    "pet_simulator": {
        "name": "🐾 Pet Simulator X",
        "script": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ВСТАВЬ_СКРИПТ/petsim.lua"))()'
    },
    "da_hood": {
        "name": "🏙️ Da Hood",
        "script": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ВСТАВЬ_СКРИПТ/dahood.lua"))()'
    },
    "murder_mystery": {
        "name": "🔪 Murder Mystery 2",
        "script": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ВСТАВЬ_СКРИПТ/mm2.lua"))()'
    },
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    text = (
        f"👋 Привет, <b>{user}</b>! Ты попал в лучшего бота в Telegram по скриптам для Roblox 🎮\n\n"
        f"📢 Подпишись на канал создателя:\n"
        f"👉 <a href='https://t.me/LuaRobloxScripts'>t.me/LuaRobloxScripts</a>\n\n"
        f"⬇️ Нажми кнопку чтобы выбрать скрипт!"
    )
    keyboard = [[InlineKeyboardButton("🎮 Выбрать скрипт", callback_data="choose_game")]]
    await update.message.reply_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "choose_game":
        text = "🎮 <b>На что хочешь скрипты?</b>\nВыбери игру:"
        keyboard = []
        row = []
        for key, val in SCRIPTS.items():
            row.append(InlineKeyboardButton(val["name"], callback_data=f"game_{key}"))
            if len(row) == 2:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)
        keyboard.append([InlineKeyboardButton("🏠 Главное меню", callback_data="back_start")])
        await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("game_"):
        game_key = data.replace("game_", "")
        if game_key in SCRIPTS:
            game = SCRIPTS[game_key]
            text = (
                f"{game['name']} — скрипт готов!\n\n"
                f"👇 <b>Нажми на скрипт чтобы скопировать:</b>\n\n"
                f"<code>{game['script']}</code>\n\n"
                f"📢 Больше скриптов: <a href='https://t.me/LuaRobloxScripts'>t.me/LuaRobloxScripts</a>"
            )
            keyboard = [
                [InlineKeyboardButton("🎮 Другой скрипт", callback_data="choose_game")],
                [InlineKeyboardButton("🏠 Главное меню", callback_data="back_start")],
            ]
            await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "back_start":
        user = query.from_user.first_name
        text = (
            f"👋 Привет, <b>{user}</b>! Ты попал в лучшего бота в Telegram по скриптам для Roblox 🎮\n\n"
            f"📢 Подпишись на канал создателя:\n"
            f"👉 <a href='https://t.me/LuaRobloxScripts'>t.me/LuaRobloxScripts</a>\n\n"
            f"⬇️ Нажми кнопку чтобы выбрать скрипт!"
        )
        keyboard = [[InlineKeyboardButton("🎮 Выбрать скрипт", callback_data="choose_game")]]
        await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Бот запущен!")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
