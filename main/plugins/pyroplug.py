# Github.com/Vasusen-code

import asyncio, time, os

from .. import Bot, bot
from main.plugins.progress import progress_for_pyrogram
from main.plugins.helpers import screenshot

from pyrogram import Client, filters
from pyrogram.errors import ChannelBanned, ChannelInvalid, ChannelPrivate, ChatIdInvalid, ChatInvalid, FloodWait
from ethon.pyfunc import video_metadata
from ethon.telefunc import fast_upload
from telethon import events
from telethon.tl.types import DocumentAttributeVideo

def thumbnail(sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    else:
         return None
      
async def check(userbot, client, link):
    msg_id = int(link.split("/")[-1])
    if 't.me/c/' in link:
        try:
            chat = int('-100' + str(link.split("/")[-2]))
            await userbot.get_messages(chat, msg_id)
            return True, None
        except ValueError:
            return False, "**Invalid Link!**"
        except Exception:
            return False, "Have you joined the channel?"
    else:
        try:
            chat = str(link.split("/")[-2])
            await client.get_messages(chat, msg_id)
            return True, None
        except Exception:
            return False, "Maybe bot is banned from the chat, or your link is invalid!"
            
async def get_msg(userbot, client, sender, edit_id, msg_link, i, bulk=False):
    edit = ""
    chat = ""
    msg_id = int(msg_link.split("/")[-1]) + int(i)
    if 't.me/c/' in msg_link:
        chat = int('-100' + str(msg_link.split("/")[-2]))
        file = ""
        try:
            msg = await userbot.get_messages(chat, msg_id)
            if msg.media:
                if 'web_page' in msg.media:
                    edit = await client.edit_message_text(sender, edit_id, "Cloning.")
                    await client.send_message(sender, msg.text.markdown)
                    await edit.delete()
                    return None, None
            if not msg.media:
                if msg.text:
                    edit = await client.edit_message_text(sender, edit_id, "Cloning.")
                    await client.send_message(sender, msg.text.markdown)
                    await edit.delete()
                    return None, None
            edit = await client.edit_message_text(sender, edit_id, "Trying to Download.")
            file = await userbot.download_media(
                msg,
                progress=progress_for_pyrogram,
                progress_args=(
                    client,
                    "**DOWNLOADING:**\n",
                    edit,
                    time.time()
                )
            )
            await edit.edit('Preparing to Upload!')
            caption = str(file)
            if msg.caption is not None:
                caption = msg.caption
            if str(file).split(".")[-1] in ['mkv', 'mp4', 'webm', 'mpe4', 'mpeg']:
                if str(file).split(".")[-1] in ['webm', 'mkv', 'mpe4', 'mpeg']:
                    path = str(file).split(".")[0] + ".mp4"
                    os.rename(file, path) 
                    file = str(file).split(".")[0] + ".mp4"
                data = video_metadata(file)
                duration = data["duration"]
                width = data["width"]
                height = data["height"]
                thumb_path = await screenshot(file, duration, sender)
                UT = time.time()
                uploader = await fast_upload(f'{file}', f'{file}', UT, bot, edit, '**UPLOADING:**')
                attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
                await bot.send_file(
                    sender, 
                    uploader, 
                    caption=caption, 
                    thumb=thumb_path, 
                    attributes=attributes, 
                    force_document=False
                )
                os.remove(file)
            elif str(file).split(".")[-1] in ['jpg', 'jpeg', 'png', 'webp']:
                await edit.edit("Uploading photo.")
                await bot.send_file(sender, file, caption=caption)
                os.remove(file)
            else:
                thumb_path=thumbnail(sender)
                UT = time.time()
                uploader = await fast_upload(f'{file}', f'{file}', UT, bot, edit, '**UPLOADING:**')
                await bot.send_file(
                    sender, 
                    uploader, 
                    caption=caption, 
                    thumb=thumb_path, 
                    force_document=True
                )
                os.remove(file)
            await edit.delete()
            return None, None
        except (ChannelBanned, ChannelInvalid, ChannelPrivate, ChatIdInvalid, ChatInvalid):
            await client.edit_message_text(sender, edit_id, "Have you joined the channel?")
            return None, None
        except FloodWait as fw:
            print(fw)
            if bulk is True:
                return "FW", int(fw.x) + 5
            return None, await client.edit_message_text(sender, edit_id, f'Try again after {fw.x} seconds due to floodwait from telegram.')
        except Exception as e:
            print(e)
            await client.edit_message_text(sender, edit_id, f'Failed to save: `{msg_link}`')
            os.remove(file)
            return None, None
    else:
        edit = await client.edit_message_text(sender, edit_id, "Cloning.")
        chat =  msg_link.split("/")[-2]
        try:
            await client.copy_message(int(sender), chat, msg_id)
            return None, None
        except FloodWait as fw:
            print(fw)
            if bulk is True:
                return "FW", int(fw.x) + 5
            return None, await client.edit_message_text(sender, edit_id, f'Try again after {fw.x} seconds due to floodwait from telegram.')
        except Exception as e:
            print(e)
            return None, await client.edit_message_text(sender, edit_id, f'Failed to save: `{msg_link}`')
        await edit.delete()
        return None, None   
 
async def get_bulk_msg(userbot, client, sender, msg_link, i):
    x = await client.send_message(sender, "Processing!")
    await get_msg(userbot, client, sender, x.message_id, msg_link, i, bulk=True) 
