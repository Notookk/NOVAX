

import os
import asyncio
from .. import handler, Owner
from pyrogram import Client, filters
from pyrogram.types import Message
from RiZoeLX import Devs, res_grps


@Client.on_message(filters.command("tagall"))
async def tag_all(client, message):
    chat_id = message.chat.id
    
    # Get all members in the chat
    members = await client.get_chat_members(chat_id)
    
    # Construct the tag string
    tag_string = " ".join([f"@{member.user.username}" for member in members])
    
    # Send the message tagging all members
    await message.reply_text(tag_string)
