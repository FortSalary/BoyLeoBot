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

import asyncio

import speedtest
from pyrogram import filters

from FallenMusic import SUDOERS, app


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ Chạy thử tốc độ tải xuống...**")
        test.download()
        m = m.edit("**⇆ Chạy thử nghiệm tốc độ tải lên...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ Kết quả bài kiểm tra tốc độ...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spt"]) & SUDOERS)
async def speedtest_function(_, message):
    m = await message.reply_text("**» Chạy thử tốc độ...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **Kết quả speedtest** ✯
    
<u>**❥͜͡Khách hàng :**</u>
**» __ɪsᴩ :__** {result['client']['isp']}
**» __Quốc gia :__** {result['client']['country']}
  
<u>**❥͜͡Máy chủ :**</u>
**» __Tên :__** {result['server']['name']}
**» __Quốc gia :__** {result['server']['country']}, {result['server']['cc']}
**» __Nhà tài trợ :__** {result['server']['sponsor']}
**» __Độ trễ :__** {result['server']['latency']}  
**» __ᴩɪɴɢ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
