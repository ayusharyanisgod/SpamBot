async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from RiZoeLXSpam import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from RiZoeLXSpam import CMD_HNDLR as hl

@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Rizoel) == 2:
            message = str(Rizoel[1])
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(rizoel) == 2:
            message = str(rizoel[1])
            counter = int(rizoel[0])
            for _ in range(counter):
                 async with e.client.action(e.chat_id, "typing"):
                     if e.reply_to_msg_id:
                          await smex.reply(message)
                     else:
                          await e.client.send_message(e.chat_id, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Rizoelsexy = Rizoel[1:]
        if len(Rizoelsexy) == 2:
            message = str(Rizoelsexy[1])
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hl))
async def unlimitedspam(event):
  if e.sender_id in SUDO_USERS:
    try:
      op = event.text[7:]
      x = None
      while x == None:
        await event.client.send_message(event.chat, op)
        await asyncio.sleep(0.3)
    except Exception as e:
      await event.reply("Oops!! Something went wrong.\n\n" + str(e))
