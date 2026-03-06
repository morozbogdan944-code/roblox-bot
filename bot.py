import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatMember
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.error import TelegramError

TOKEN = "8774370442:AAFX_9GqAUjpJe4mnnLhdN08U8OJwmCQNm0"
CHANNEL_USERNAME = "@LuaRobloxScripts"
CHANNEL_LINK = "https://t.me/LuaRobloxScripts"

logging.basicConfig(level=logging.INFO)

GAMES = {
    "arsenal": {
        "name": "🔫 Arsenal",
        "hubs": {
            "FelipeHub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/FELIPEHUB1/Felipehub-scripts/refs/heads/main/Arsenal"))()',
            "QuotasHub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Insertl/QuotasHub/main/BETAv1.3"))()',
            "Z3US": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/blackowl1231/Z3US/refs/heads/main/main.lua"))()',
        }
    },
    "blox_fruits": {
        "name": "🍎 Blox Fruits",
        "hubs": {
            "Heart Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Jadelly/bloxfruit/refs/heads/main/HeartHub", true))()',
            "Zyn Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/jaiasof/Zyn-Hub/refs/heads/main/Zyn%20Loader", true))()',
            "High Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Jadelly/bloxfruit/refs/heads/main/HighLoader", true))()',
            "Leaf Hub": 'repeat task.wait() until game:IsLoaded() and game.Players.LocalPlayer\nloadstring(game:HttpGet("https://github.com/LeafHubAcademy/LeafHub/raw/refs/heads/main/Leaf.lua"))()',
            "Hoho Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/acsu123/HOHO_H/main/Loading_UI"))()',
            "Blue X Hub": '_G.AutoTranslate = true\n_G.SaveConfig = true\nloadstring(game:HttpGet("https://raw.githubusercontent.com/Dev-BlueX/BlueX-Hub/refs/heads/main/Main.lua"))()',
        }
    },
    "murder_mystery": {
        "name": "🔪 Murder Mystery 2",
        "hubs": {
            "Vertex": "loadstring(game:HttpGet('https://raw.smokingscripts.org/vertex.lua'))()",
            "SnapSanixHUB": "loadstring(game:HttpGet('https://raw.githubusercontent.com/Roman34296589/SnapSanixHUB/refs/heads/main/SnapSanixHUB.lua'))()",
        }
    },
    "adopt_me": {
        "name": "🐣 Adopt Me",
        "hubs": {
            "Elysia": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/eIysia-dev/release/refs/heads/main/open-src.lua"))()',
        }
    },
    "pet_sim": {
        "name": "🐾 Pet Simulator X",
        "hubs": {
            "ExtremeHub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ExtremeAntonis/extremehub/main/loader.lua"))()',
        }
    },
    "brookhaven": {
        "name": "🏠 Brookhaven RP",
        "hubs": {
            "SP Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/as6cd0/SP_Hub/refs/heads/main/Brookhaven"))()',
            "Soluna Script": 'loadstring(game:HttpGet("https://pastebin.com/raw/LCmR8qkj"))()',
            "Hexagon Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/nxvap/Hexagon/refs/heads/main/brookhaven"))()',
        }
    },
    "tower_of_hell": {
        "name": "🗼 Tower of Hell",
        "hubs": {
            "TheBigHubs": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/yyeptech/thebighubs/refs/heads/main/toh.lua"))()',
        }
    },
    "da_hood": {
        "name": "🏙️ Da Hood",
        "hubs": {
            "Vortex": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ImagineProUser/vortexdahood/main/vortex", true))()',
        }
    },
    "bee_swarm": {
        "name": "🐝 Bee Swarm Simulator",
        "hubs": {
            "Kron Hub": "loadstring(game:HttpGet('https://raw.githubusercontent.com/DevKron/Kron_Hub/refs/heads/main/version_1.0'))('')",
        }
    },
    "escape_tsunami": {
        "name": "🌊 Escape Tsunami For Brainrots",
        "hubs": {
            "Rat Hub X": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Ratkinator/RatX/refs/heads/main/Loader.lua",true))()',
            "Mamaboy Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/nhandzqua1733-blip/mamaboyhubdZ/refs/heads/main/WindUI.lua.txt"))()',
        }
    },
    "nights_forest": {
        "name": "🌲 99 Nights in the Forest",
        "hubs": {
            "Avestix Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/idkjustarandomdudeherenothingtosee/avestix/refs/heads/main/src/main.tsx"))()',
            "Voidware": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/VapeVoidware/VW-Add/main/nightsintheforest.lua", true))()',
            "Raygull Utility": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/raygull3d/99-Nights-in-the-Forest-Script/refs/heads/main/99%20Days%20Scirpt%20By%20Raygull.lua"))()',
            "KaylaHub": 'loadstring(game:HttpGet("https://api.junkie-development.de/api/v1/luascripts/public/ad7c016956c3291b5a7d67e6c9465eabe7569c2569cf3682be766df972d6b7d6/download"))()',
            "Foxname Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/caomod2077/Script/refs/heads/main/FoxnameHub.lua"))()',
            "Rx1m": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Rx1m/CpsHub/refs/heads/main/Hub", true))()',
        }
    },
    "rivals": {
        "name": "⚔️ Rivals",
        "hubs": {
            "Keyless Aimbot": 'loadstring(game:HttpGet("https://scriptblox.com/raw/RIVALS-Rival-Keyless-Aimbot-29053"))()',
            "Vylera Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/vylerascripts/vylera-scripts/main/vylerarivals.lua"))()',
        }
    },
    "violence_district": {
        "name": "💥 Violence District",
        "hubs": {
            "TexRBLX Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/TexRBLX/Roblox-stuff/refs/heads/main/violence-district/script.lua"))()',
        }
    },
    "steal_brainrot": {
        "name": "🧠 Steal a Brainrot",
        "hubs": {
            "Chilli Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/tienkhanh1/spicy/main/Chilli.lua"))()',
            "Arbix Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Youifpg/Steal-a-Brainrot-op/refs/heads/main/Arbixhub-obfuscated.lua"))()',
        }
    },
    "survive_lava": {
        "name": "🔥 Survive LAVA for Brainrots",
        "hubs": {
            "Tora Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/AX-Archive/ArceusXArchive/refs/heads/main/Tora%20Isme"))()',
            "Arther Hub": 'loadstring(game:HttpGet("https://api.luarmor.net/files/v3/loaders/2529a5f9dfddd5523ca4e22f21cceffa.lua"))()',
            "Rika Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ianoci/RIKA-HUB/refs/heads/main/Source"))()',
        }
    },
    "tsb": {
        "name": "💪 The Strongest Battlegrounds",
        "hubs": {
            "Speed Hub X": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/AhmadV99/Speed-Hub-X/main/Speed%20Hub%20X.lua", true))()',
            "Phantasm": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ATrainz/Phantasm/refs/heads/main/Games/TSB.lua"))()',
            "LuaRBX": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/l44378120-cmyk/CVGFC/main/TSB", true))()',
        }
    },
    "knockout": {
        "name": "🥊 Knockout",
        "hubs": {
            "JNHH Gaming": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/JNHHGaming/Knockout/refs/heads/main/Knockout",true))()',
        }
    },
    "dress_impress": {
        "name": "👗 Dress To Impress",
        "hubs": {
            "DTI GUI V2": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/hellohellohell012321/DTI-GUI-V2/main/dti_gui_v2.lua",true))()',
        }
    },
    "evade": {
        "name": "🏃 Evade",
        "hubs": {
            "Gumanba Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/gumanba/Scripts/main/EvadeEvent"))()',
            "Dara Hub": 'loadstring(game:HttpGet("https://darahub.vercel.app/H8WJF2993DJ38RII8SI39X9811I8FI2KDFF9B9EKOWID8CKWW88DIC9X9/Mainloader.lua"))()',
            "Babyhamsta": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Babyhamsta/RBLX_Scripts/main/Evade/main.lua"))()',
        }
    },
    "jujutsu_shen": {
        "name": "⚡ Jujutsu Shenanigans",
        "hubs": {
            "TBO Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/cool5013/TBO/main/TBOscript"))()',
        }
    },
    "blade_ball": {
        "name": "⚽ Blade Ball",
        "hubs": {
            "Pastebin Redz": 'loadstring(game:HttpGet("https://pastebin.com/raw/XJ8bRWyg"))()',
            "Trevous Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ImNotRox1/Trevous-Hub/refs/heads/main/blade-ball.lua"))()',
            "BeanzHub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/pid4k/scripts/main/BeanzHub.lua", true))()',
        }
    },
    "fish_it": {
        "name": "🎣 Fish It",
        "hubs": {
            "Chloe X Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/MajestySkie/Chloe-X/main/Main/ChloeX"))()',
            "Meng Hub": 'loadstring(game:HttpGet("https://menghub.dannnnbiasalah.workers.dev/"))()',
            "Lynx Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/4LynxX/Lynx/refs/heads/main/LynxxMain.lua"))()',
        }
    },
    "jujutsu_inf": {
        "name": "✨ Jujutsu Infinite",
        "hubs": {
            "Qwenzy Hub": "loadstring(game:HttpGet('https://raw.githubusercontent.com/mrqwenzy/QWENZY_HUB/refs/heads/main/JujutsuInfinite'))()",
            "Limitless Hub": 'loadstring(game:HttpGet("https://pastebin.com/raw/nANQXrtM"))()',
            "nuIIism Limitless": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/nuIIism/limitless/main/main.lua"))()',
        }
    },
    "dead_rails": {
        "name": "🚂 Dead Rails",
        "hubs": {
            "Ring Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/erewe23/deadrailsring.github.io/refs/heads/main/ringta.lua"))()',
        }
    },
    "bedwars": {
        "name": "🛏️ BedWars",
        "hubs": {
            "VoidWare": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/VapeVoidware/vapevoidware/main/NewMainScript.lua", true))()',
        }
    },
    "flee_facility": {
        "name": "🏃 Flee the Facility",
        "hubs": {
            "Celeron Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ghostofcelleron/Celeron/refs/heads/main/Flee%20The%20Facility%20(OS)",true))()',
        }
    },
    "creatures_sonaria": {
        "name": "🦎 Creatures of Sonaria",
        "hubs": {
            "Lunar Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Mangnex/Lunar-Hub/refs/heads/main/FreeLoader.lua"))()',
        }
    },
    "volleyball": {
        "name": "🏐 Volleyball Legends",
        "hubs": {
            "TheDarkoneMarcillisePex": "loadstring(game:HttpGet('https://raw.githubusercontent.com/TheDarkoneMarcillisePex/Other-Scripts/refs/heads/main/Volleyball%20Legends%20GUI'))()",
            "Loki's Voley": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/M1zard/LokisVoley/refs/heads/main/VolleyBallLegendsScript.lua"))()',
        }
    },
    "run_brainrots": {
        "name": "💨 Run For Brainrots",
        "hubs": {
            "Gumanba Hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/gumanba/Scripts/main/RunForBrainrots"))()',
        }
    },
    "forsaken": {
        "name": "👻 Forsaken",
        "hubs": {
            "CursedHub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/zxcursedsocute/Forsaken-Script/refs/heads/main/lua"))()',
        }
    },
    "legend_speed": {
        "name": "🏎️ Legend Speed",
        "hubs": {
            "OpScript": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/YukiTM/Roblox/main/Legends",true))()',
        }
    },
}


async def is_subscribed(bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        return member.status in [ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.OWNER]
    except TelegramError:
        return False


async def not_subscribed_message(query):
    text = (
        "❌ <b>Доступ закрыт!</b>\n\n"
        "Чтобы получить скрипты — подпишись на канал:\n"
        f"👉 <a href='{CHANNEL_LINK}'>t.me/LuaRobloxScripts</a>\n\n"
        "После подписки нажми кнопку ниже 👇"
    )
    keyboard = [
        [InlineKeyboardButton("📢 Подписаться", url=CHANNEL_LINK)],
        [InlineKeyboardButton("✅ Я подписался!", callback_data="check_sub")],
    ]
    await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    subscribed = await is_subscribed(update.get_bot(), update.effective_user.id)

    if not subscribed:
        text = (
            f"👋 Привет, <b>{user}</b>!\n\n"
            "🎮 Это лучший бот по скриптам для Roblox!\n\n"
            "⛔ Чтобы получить доступ к скриптам — подпишись на канал:\n"
            f"👉 <a href='{CHANNEL_LINK}'>t.me/LuaRobloxScripts</a>"
        )
        keyboard = [
            [InlineKeyboardButton("📢 Подписаться", url=CHANNEL_LINK)],
            [InlineKeyboardButton("✅ Я подписался!", callback_data="check_sub")],
        ]
    else:
        text = (
            f"👋 Привет, <b>{user}</b>!\n\n"
            "🎮 Добро пожаловать в лучший бот по скриптам для Roblox!\n\n"
            "⬇️ Выбери игру и получи скрипт:"
        )
        keyboard = [[InlineKeyboardButton("🎮 Выбрать игру", callback_data="choose_game")]]

    await update.message.reply_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id

    if data == "check_sub":
        subscribed = await is_subscribed(update.get_bot(), user_id)
        if subscribed:
            text = (
                "✅ <b>Подписка подтверждена!</b>\n\n"
                "🎮 Теперь выбирай игру и получай скрипты!"
            )
            keyboard = [[InlineKeyboardButton("🎮 Выбрать игру", callback_data="choose_game")]]
            await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            text = (
                "❌ <b>Ты ещё не подписался!</b>\n\n"
                "Подпишись на канал и нажми кнопку снова:\n"
                f"👉 <a href='{CHANNEL_LINK}'>t.me/LuaRobloxScripts</a>"
            )
            keyboard = [
                [InlineKeyboardButton("📢 Подписаться", url=CHANNEL_LINK)],
                [InlineKeyboardButton("✅ Я подписался!", callback_data="check_sub")],
            ]
            await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    # Проверка подписки для всех остальных действий
    subscribed = await is_subscribed(update.get_bot(), user_id)
    if not subscribed:
        await not_subscribed_message(query)
        return

    if data == "choose_game":
        text = "🎮 <b>Выбери игру:</b>"
        keyboard = []
        row = []
        for key, val in GAMES.items():
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
        if game_key in GAMES:
            game = GAMES[game_key]
            text = f"{game['name']} — <b>выбери хаб:</b>"
            keyboard = []
            for hub_name in game["hubs"]:
                keyboard.append([InlineKeyboardButton(f"⚡ {hub_name}", callback_data=f"hub_{game_key}|{hub_name}")])
            keyboard.append([InlineKeyboardButton("🔙 Назад к играм", callback_data="choose_game")])
            await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("hub_"):
        parts = data.replace("hub_", "").split("|", 1)
        if len(parts) == 2:
            game_key, hub_name = parts
            if game_key in GAMES and hub_name in GAMES[game_key]["hubs"]:
                script = GAMES[game_key]["hubs"][hub_name]
                game_name = GAMES[game_key]["name"]
                text = (
                    f"{game_name} — <b>{hub_name}</b>\n\n"
                    f"👇 Нажми на скрипт чтобы скопировать:\n\n"
                    f"<code>{script}</code>"
                )
                keyboard = [
                    [InlineKeyboardButton("🔙 Другой хаб", callback_data=f"game_{game_key}")],
                    [InlineKeyboardButton("🎮 Другая игра", callback_data="choose_game")],
                    [InlineKeyboardButton("🏠 Главное меню", callback_data="back_start")],
                ]
                await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "back_start":
        user = query.from_user.first_name
        text = (
            f"👋 Привет, <b>{user}</b>!\n\n"
            "🎮 Добро пожаловать в лучший бот по скриптам для Roblox!\n\n"
            "⬇️ Выбери игру и получи скрипт:"
        )
        keyboard = [[InlineKeyboardButton("🎮 Выбрать игру", callback_data="choose_game")]]
        await query.edit_message_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Бот запущен!")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
