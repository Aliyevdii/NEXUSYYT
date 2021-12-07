# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **xoş gəlmisiniz [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) yeni Telegram-ın video zəngləri vasitəsilə qruplarda musiqi və video oynatmağa imkan verir!**

💡 **üzərinə klikləməklə Botun bütün əmrlərini və onların necə işlədiyini öyrənin » 🇦🇿 Əmrlər düyməsi!**

🔖 **Bu botdan necə istifadə edəcəyinizi bilmək üçün, lütfən, » ❓ Əsas Bələdçi düyməsini klikləyin!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni Qrupunuza əlavə edin ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Əsas Bələdçi", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("🇦🇿 Əmrlər", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ Sahib", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Rəsmi Qrup", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Rəsmi Kanal", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🇦🇿🇦🇿🇦🇿🇦🇿🇦🇿", url=""
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Bu botdan istifadə üçün əsas bələdçi:**

1.) **Əvvəlcə məni öz qrupuna əlavə et.**
2.) **Sonra, məni administrator kimi təşviq edin və Anonim Admin istisna olmaqla, bütün icazələri verin.**
3.) **Məni təbliğ etdikdən sonra admin məlumatlarını yeniləmək üçün qrupa /reload yazın.**
3.) **Qrupunuza @{ASSISTANT_NAME} əlavə edin və ya onu dəvət etmək üçün /userbotjoin yazın.**
4.) **Video/musiqi oxutmağa başlamazdan əvvəl video çatı yandırın.**
5.) **Bəzən /reload əmrindən istifadə etməklə botun yenidən yüklənməsi bəzi problemi həll etməyə kömək edə bilər.**
📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **Bu botla bağlı əlavə suallarınız varsa, burada dəstək söhbətimdə deyə bilərsiniz: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **izahatı oxumaq və mövcud əmrlərin siyahısına baxmaq üçün aşağıdakı düyməni basın !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 sudo cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 geri", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» /mplay (song name/link) - video söhbətdə musiqi çalın
» /stream (query/link) - yt canlı/radio canlı musiqini yayımlayın
» /vplay (video name/link) - video söhbətdə video oynayın
» /vstream - youtube live/m3u8-dən canlı video oynayın
» /playlist - sizə pleylist göstərin
» /video (query) - youtube-dan videonu endir
» /song (query) - youtube-dan mahnı yükləmək
» /lyric (query) - mahnının sözlərini sil
» /search (query) - youtube video linkini axtarın

» /ping - bot ping statusunu göstərin
» /uptime - botun işləmə müddətini göstərin
» /alive - botun canlı məlumatını göstərin (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 burada admin əmrləri var:

» /pause - axını dayandırın
» /resume - axını davam etdirin
» /skip - növbəti axına keçin
» /stop - axını dayandırın
» /vmute - axını sustuurn
» /vunmute - səsli söhbətdə istifadəçi robotunun səsini açın
» /volume `1-200` - səsli söhbət musiqisində userbotun səssizliyini tənzimləyin (userbot admin olmalıdır)
» /reload - botu yenidən yükləyin və admin məlumatlarını təzələyin
» /userbotjoin - istifadəçi robotunu qrupa qoşulmağa dəvət edin
» /userbotleave - userbot-a qrupdan çıxmağı əmr edin

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 yalnız bu düyməyə toxuna bilən səsli söhbətləri idarə etmək icazəsi olan admin !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ ****Ayarlar {query.message.chat.title}\n\n⏸ : axını dayandırın\n▶️ : axını davam etdirin\n🔇 : istifadəçi robotunu susdur\n🔊 : userbotun səsini açın\n⏹ : axını dayandırın",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("settings⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ hazırda heç nə yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
