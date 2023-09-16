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

from FallenMusic import BOT_NAME

PM_START_TEXT = """
💥Xin chào {0}, 🥀
๏ Tôi là** {1} !

➻ Bot nghe siêu cấp vip pro.
"""

START_TEXT = f"""
**Xin chào** {0}, 🥀
  {1} Bây giờ có thể phát các bài hát trong {2}.

──────────────────
➻ <a href="https://shope.ee/5pfwQ1rhsO">\nĐọc thêm...</a>.
"""

HELP_TEXT = f"""
<u>❄ **CÁC LỆNH CÓ SẴN CHO NGƯỜI DÙNG TRONG {BOT_NAME} :**</u>

๏ /play : Bắt đầu truyền bài hát được yêu cầu trên trò chuyện video.
๏ /pause : Tạm dừng.
๏ /resume : Tiếp tục dòng đã tạm dừng.
๏ /skip : Bỏ qua bài hiện tại và truyền bài hát tiếp theo.
๏ /end : Xóa hàng và kết thúc dòng hát hiện tại.

๏ /ping : Hiện Ping và thống kê hệ thống của bot.
๏ /sudolist : Hiển thị danh sách người sử dụng bot Sudo.

๏ /song : Tải bài hát.

๏ /search : Tìm video trên Youtube.
"""

HELP_SUDO = f"""
<u>✨ **Lệnh của trợ lý {BOT_NAME} :**</u>

๏ /activevc : Danh sách giọng nói hoạt động hiện tại.
๏ /eval or /sh : Chạy mã được cung cấp trên máy chủ của bot.
๏ /speedtest : Tốc độ máy chủ của bot .
๏ /sysstats : Hệ thống máy chủ của bot.

๏ /setname : Thay đổi tên tài khoản trợ lý.
๏ /setbio : Thay đổi Bio.
๏ /setpfp [trả lời ảnh] : Thay đổi PFP của trợ lý.
๏ /delpfp : Xóa PFP hiện tại của trợ lý.
"""

HELP_DEV = f"""
<u>✨ **Lệnh của Ad {BOT_NAME} :**</u>

๏ /config : Nhận tất cả các biến cấu hình của bot.
๏ /broadcast : Gửi tin đến nhóm hỗ trợ.
๏ /rmdownloads : Xóa các tệp tin cache trên máy chủ của bot.
๏ /leaveall : Tài khoản trợ lý thoát tất cả cuộc trò truyện.

๏ /addsudo [username] : Thêm người dùng vào danh sách người dùng sudo.
๏ /rmsudo [username] : Xóa người dùng sudo.
"""
