<<<<<<< HEAD
#Specia Thanks To @spechide sar
#
#(c) Shrimadhav U K
#
# This file is part of UniBorg
#
# UniBorg is free software; you cannot redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# UniBorg is not distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import asyncio
from datetime import datetime
=======
# (c) Shrimadhav U K - UniBorg
# Thanks to Prakasaka for porting.

>>>>>>> d534b8c4c9d341136a53d884099f428df7de8d1f
import io
import os
import requests
from userbot.events import register
<<<<<<< HEAD
from userbot import CMD_HELP, REM_BG_API_KEY, TEMP_DOWNLOAD_DIRECTORY
from userbot.modules.upload_download import progress
=======
from telethon.tl.types import MessageMediaPhoto
from userbot import CMD_HELP, REM_BG_API_KEY, TEMP_DOWNLOAD_DIRECTORY
>>>>>>> d534b8c4c9d341136a53d884099f428df7de8d1f


@register(outgoing=True, pattern="^.rbg(?: |$)(.*)")
async def kbg(remob):
    """ For .rbg command, Remove Image Background. """
    if not remob.text[0].isalpha() and remob.text[0] not in ("/", "#", "@", "!"):
<<<<<<< HEAD
        if remob.fwd_from:
            return
        if REM_BG_API_KEY is None:
            await remob.edit("You need API token from remove.bg to use this plugin.")
            return False
        input_str = remob.pattern_match.group(1)
        start = datetime.now()
=======
        if REM_BG_API_KEY is None:
            await remob.edit("`Error: Remove.BG API key missing! Add it to environment vars or config.env.`")
            return
        input_str = remob.pattern_match.group(1)
>>>>>>> d534b8c4c9d341136a53d884099f428df7de8d1f
        message_id = remob.message.id
        if remob.reply_to_msg_id:
            message_id = remob.reply_to_msg_id
            reply_message = await remob.get_reply_message()
<<<<<<< HEAD
            # check if media message
            await remob.edit("Downloading this media ...")
            try:
                downloaded_file_name = await remob.client.download_media(
                    reply_message,
                    TEMP_DOWNLOAD_DIRECTORY
                )
            except Exception as e:
                await remob.edit(str(e))
                return
            else:
                await remob.edit("sending to ReMove.BG")
                output_file_name = ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
        elif input_str:
            await remob.edit("sending to ReMove.BG")
            output_file_name = ReTrieveURL(input_str)
        else:
            await remob.edit(HELP_STR)
=======
            await remob.edit("`Processing..`")
            try:
                if isinstance(reply_message.media, MessageMediaPhoto) or "image" in reply_message.media.document.mime_type.split('/'):
                    downloaded_file_name = await remob.client.download_media(
                        reply_message,
                        TEMP_DOWNLOAD_DIRECTORY
                    )
                    await remob.edit("`Removing background from this image..`")
                    output_file_name = ReTrieveFile(downloaded_file_name)
                    os.remove(downloaded_file_name)
                else:
                    await remob.edit("`How do I remove the background from this ?`")
            except Exception as e:
                await remob.edit(str(e))
                return
        elif input_str:
            await remob.edit(f"`Removing background from online image hosted at`\n{input_str}")
            output_file_name = ReTrieveURL(input_str)
        else:
            await remob.edit("`I need something to remove the background from.`")
>>>>>>> d534b8c4c9d341136a53d884099f428df7de8d1f
            return
        contentType = output_file_name.headers.get("content-type")
        if "image" in contentType:
            with io.BytesIO(output_file_name.content) as remove_bg_image:
<<<<<<< HEAD
                remove_bg_image.name = "BG_ReMove.png"
                await remob.client.send_file(
                    remob.chat_id,
                    remove_bg_image,
                    force_document=True,
                    supports_streaming=False,
                    allow_cache=False,
                    reply_to=message_id
                )
            end = datetime.now()
            duration = (end - start).seconds
            await remob.edit("Background Removed in {} seconds using ReMove.BG API".format(duration))
        else:
            await remob.edit("ReMove.BG API returned Errors. Please Use Valid Api Key\n`{}".format(output_file_name.content.decode("UTF-8")))
=======
                remove_bg_image.name = "removed_bg.png"
                await remob.client.send_file(
                    remob.chat_id,
                    remove_bg_image,
                    caption="Background removed using remove.bg",
                    force_document=True,
                    reply_to=message_id
                )
                await remob.delete()
        else:
            await remob.edit("**Error (Invalid API key, I guess ?)**\n`{}`".format(output_file_name.content.decode("UTF-8")))
>>>>>>> d534b8c4c9d341136a53d884099f428df7de8d1f


# this method will call the API, and return in the appropriate format
# with the name provided.
def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True
    )
    return r


def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    data = {
      "image_url": input_url
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        data=data,
        allow_redirects=True,
        stream=True
    )
    return r


CMD_HELP.update({
<<<<<<< HEAD
    "remove_bg": ".rbg <ImageLink> or Reply Any Image\
\nUsage: Remove Image Background."
=======
    "remove_bg": ".rbg <Link to Image> or reply to any image\
\nUsage: Removes the background of images, using remove.bg API"
>>>>>>> d534b8c4c9d341136a53d884099f428df7de8d1f
})
