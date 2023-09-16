from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("» Thay đổi ảnh hồ sơ của trợ lý...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» {ASS_MENTION} Thay đổi ảnh hồ sơ trợ lý thành công."
            )
        except:
            return await fuk.edit_text("» Thay đổi ảnh hồ sơ của trợ lý thất bại!")
    else:
        await message.reply_text(
            "» Trả lời ảnh để thay đổi ảnh hồ sơ của trợ lý."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "» Đã xóa thành công ảnh hồ sơ của trợ lý."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("» Thất bại khi xóa ảnh hồ sơ của trợ lý!")


@app.on_message(filters.command(["assbio", "setbio"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ASS_MENTION} Thay đổi Bio thành công."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"» {ASS_MENTION} Thay đổi Bio thành công.")
    else:
        return await message.reply_text(
            "» Trả lời tin nhắn hoặc đưa ra một văn bản để thay đổi Tiểu sử của trợ lý."
        )


@app.on_message(filters.command(["assname", "setname"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ASS_MENTION} Đã đổi tên thành công."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ASS_MENTION} Đã đổi tên thành công.")
    else:
        return await message.reply_text(
            "» Trả lời tin nhắn hoặc đưa ra một văn bản để thay đổi tên của trợ lý."
        )
