# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, Message

from FallenMusic import SUDOERS, app

from .active import is_active_chat


def admin_check(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if not await is_active_chat(message.chat.id):
            return await message.reply_text("Bot không phát trực tuyến trên trò chuyện video.")

        if message.from_user.id in SUDOERS:
            return await func(_, message)

        check = await app.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "» Bạn không phải là quản trị viên, xin vui lòng ở trong giới hạn của bạn."
            )

        admin = (
            await app.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, message)
        else:
            return await message.reply_text(
                "» Bạn không có quyền quản lý video chat, vui lòng giữ nguyên giới hạn của mình."
            )

    return non_admin


def admin_check_cb(func: Callable) -> Callable:
    async def cb_non_admin(_, query: CallbackQuery):
        if not await is_active_chat(query.message.chat.id):
            return await query.answer(
                "Bot không có trong trò chuyện video.", show_alert=True
            )

        if query.from_user.id in SUDOERS:
            return await func(_, query)

        try:
            check = await app.get_chat_member(query.message.chat.id, query.from_user.id)
        except:
            return
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await query.answer(
                "» Bạn không phải là quản trị viên, hãy giữ giới hạn của mình.",
                show_alert=True,
            )

        admin = (
            await app.get_chat_member(query.message.chat.id, query.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, query)
        else:
            return await query.answer(
                "» Bạn không có quyền quản lý video chat, vui lòng giữ nguyên giới hạn của mình.",
                show_alert=True,
            )

    return cb_non_admin
