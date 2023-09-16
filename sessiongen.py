import asyncio

from pyrogram import Client, __version__ as ver


API_ID = input("\nEnter Your API ID :\n > ")
API_HASH = input("\nEnter Your API HASH :\n > ")

print("\n\nNhập số điện thoại liên kết với tài khoản Telegram của bạn khi được hỏi.\n\n")

fallen = Client("BoyLeo", api_id=API_ID, api_hash=API_HASH, in_memory=True)


async def main():
    await fallen.start()
    sess = await fallen.export_session_string()
    txt = f"Đây là Phiên chuỗi Pyrogram {ver} của bạn\n\n<code>{sess}</code>\n\nĐừng chia sẻ nó với bất kỳ ai."
    ok = await fallen.send_message("me", txt)
    print(f"Đây là Phiên chuỗi Pyrogram {ver} của bạn.\n{sess}\nNhấp đúp để sao chép.") 


asyncio.run(main())
