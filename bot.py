import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ============================
# ВСТАВЬ СВОЙ ТОКЕН СЮДА 👇
TOKEN = "8774370442:AAFX_9GqAUjpJe4mnnLhdN08U8OJwmCQNm0"
# ============================

logging.basicConfig(level=logging.INFO)

# ========== СКРИПТЫ ==========
SCRIPTS = {
    "blox_fruits": {
        "name": "🍎 Blox Fruits",
        "script": """-- 🍎 Blox Fruits Script
-- Автор: @LuaRobloxScripts

loadstring(game:HttpGet("https://raw.githubusercontent.com/examplescript/bloxfruits/main/script.lua"))()"""
    },
    "arsenal": {
        "name": "🔫 Arsenal",
        "script": """-- 🔫 Arsenal Script
-- Автор: @LuaRobloxScripts

loadstring(game:HttpGet("https://raw.githubusercontent.com/examplescript/arsenal/main/script.lua"))()"""
    },
    "brookhaven": {
        "name": "🏠 Brookhaven",
        "script": """-- 🏠 Brookhaven Script
-- Автор: @LuaRobloxScripts

loadstring(game:HttpGet("https://raw.githubusercontent.com/examplescript/brookhaven/main/script.lua"))()"""
    },
    "pet_simulator": {
        "name": "🐾 Pet Simulator X",
        "script": """-- 🐾 Pet Simulator X Script
-- Автор: @LuaRobloxScripts

loadstring(game:HttpGet("https://raw.githubusercontent.com/examplescript/petsim/main/script.lua"))()"""
    },
    "da_hood": {
        "name": "🏙️ Da Hood",
        "script": """-- 🏙️ Da Hood Script
-- Автор: @LuaRobloxScripts

loadstring(game:HttpGet("https://raw.githubusercontent.com/examplescript/dahood/main/script.lua"))()"""
    },
    "murder_mystery": {
        "name": "🔪 Murder Mystery 2",
        "script": """-- 🔪 Murder Mystery 2 Script
-- Автор: @LuaRobloxScripts

loadstring(game:HttpGet("https://raw.githubusercontent.com/examplescript/mm2/main/script.lua"))()"""
    },
}

# ========== /start ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    text = (
        f"👋 Привет, *{user}*\\! Ты попал в лучшего бота в Telegram по скриптам для Roblox 🎮\n\n"
        f"📢 Подпишись на канал создателя:\n"
        f"👉 [t\\.me/LuaRobloxScripts](https://t.me/LuaRobloxScripts)\n\n"
        f"⬇️ Используй команды ниже или нажми кнопку чтобы выбрать скрипт\\!"
    )
    keyboard = [[InlineKeyboardButton("🎮 Выбрать скрипт", callback_data="choose_game")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode="MarkdownV2", reply_markup=reply_markup)

# ========== /scripts ==========
async def scripts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_game_menu(update.message.reply_text)

# ========== Показать меню игр ==========
async def show_game_menu(reply_func):
    text = "🎮 *На что хочешь скрипты?*\nВыбери игру:"
    keyboard = []
    row = []
    for key, val in SCRIPTS.items():
        row.append(InlineKeyboardButton(val["name"], callback_data=f"game_{key}"))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await reply_func(text, parse_mode="Markdown", reply_markup=reply_markup)

# ========== Обработка кнопок ==========
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "choose_game":
        text = "🎮 *На что хочешь скрипты?*\nВыбери игру:"
        keyboard = []
        row = []
        for key, val in SCRIPTS.items():
            row.append(InlineKeyboardButton(val["name"], callback_data=f"game_{key}"))
            if len(row) == 2:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)
        keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back_start")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=reply_markup)

    elif data.startswith("game_"):
        game_key = data.replace("game_", "")
        if game_key in SCRIPTS:
            game = SCRIPTS[game_key]
            script_text = game["script"]
            text = (
                f"{game['name']} — скрипт готов\\!\n\n"
                f"👇 *Нажми на скрипт чтобы скопировать:*\n\n"
                f"`{script_text}`\n\n"
                f"📢 Больше скриптов: [t\\.me/LuaRobloxScripts](https://t.me/LuaRobloxScripts)"
            )
            keyboard = [
                [InlineKeyboardButton("🎮 Другой скрипт", callback_data="choose_game")],
                [InlineKeyboardButton("🏠 Главное меню", callback_data="back_start")],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(text, parse_mode="MarkdownV2", reply_markup=reply_markup)

    elif data == "back_start":
        user = query.from_user.first_name
        text = (
            f"👋 Привет, *{user}*\\! Ты попал в лучшего бота в Telegram по скриптам для Roblox 🎮\n\n"
            f"📢 Подпишись на канал создателя:\n"
            f"👉 [t\\.me/LuaRobloxScripts](https://t.me/LuaRobloxScripts)\n\n"
            f"⬇️ Нажми кнопку чтобы выбрать скрипт\\!"
        )
        keyboard = [[InlineKeyboardButton("🎮 Выбрать скрипт", callback_data="choose_game")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, parse_mode="MarkdownV2", reply_markup=reply_markup)

# ========== Запуск ==========
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scripts", scripts_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
