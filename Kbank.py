import requests
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pytz

# รับข้อมูลจากผู้ใช้
name_user_id = input("ชื่อผู้โอนจ่าย: ")
name_me_id = input("ชื่อผู้รับเงิน: ")
phone_me_id = input("เบอร์โทรศัพท์ผู้รับ: ")
money_id = input("จำนวนเงิน: ")

# เวลาในประเทศไทย
thailand_timezone = pytz.timezone('Asia/Bangkok')
current_time_thailand = datetime.now(thailand_timezone)
time = current_time_thailand.strftime("%H:%M:%S")
day = current_time_thailand.strftime("%d")
month = current_time_thailand.strftime("%m")
year = current_time_thailand.strftime("%Y")

# โหลดภาพพื้นหลัง
image = Image.open("Bank/K-bank 4.png")
draw = ImageDraw.Draw(image)

# กำหนดขนาดและฟอนต์
font_size_money = 87
font_size_user = 48
font_size_me = 48
font_size_phone = 40
font_size_time = 37

font_path_money = "Font/PSL158.ttf"
font_path_user = "Font/PSL159.ttf"
font_path_phone = "Font/PSL160.ttf"

font_money = ImageFont.truetype(font_path_money, font_size_money)
font_user = ImageFont.truetype(font_path_user, font_size_user)
font_me = ImageFont.truetype(font_path_user, font_size_me)
font_phone = ImageFont.truetype(font_path_phone, font_size_phone)
font_time = ImageFont.truetype(font_path_user, font_size_time)
font_order = ImageFont.truetype(font_path_user, font_size_time)

# เตรียมข้อความที่จะใส่ลงไปในภาพ
phone = phone_me_id
text_money = money_id + ".00"
text_name_user = name_user_id
text_name_me = name_me_id
text_name_phone = f"{phone[:3]}-xxx-{phone[6:]}"
text_name_time = f"  {day}/{month}/{year} {time}"
text_name_order = "50018935012188"

# กำหนดตำแหน่งของข้อความในภาพ
text_position_money = (560, 270)
text_position_user = (302, 485)
text_position_me = (302, 648)
text_position_phone = (302, 720)
text_position_time = (781, 885)
text_position_order = (827, 953)

# กำหนดสีของข้อความ
text_color_money = (44, 44, 44)
text_color_user = (-20, -20, -20)
text_color_me = (-20, -20, -20)
text_color_phone = (80, 80, 80)
text_color_time = (60, 60, 60)
text_color_order = (60, 60, 60)

# ใส่ข้อความลงในภาพ
draw.text(text_position_money, text_money, font=font_money, fill=text_color_money)
draw.text(text_position_user, text_name_user, font=font_user, fill=text_color_user)
draw.text(text_position_me, text_name_me, font=font_me, fill=text_color_me)
draw.text(text_position_phone, text_name_phone, font=font_phone, fill=text_color_phone)
draw.text(text_position_time, text_name_time, font=font_time, fill=text_color_time)
draw.text(text_position_order, text_name_order, font=font_order, fill=text_color_order)

# บันทึกภาพที่มีข้อความ
image.save("truemoney_with_textnew.png")

print("สลีปปลอมสำเร็จ! บันทึกเป็น truemoney_with_textnew.png")

# ส่งภาพไปยัง Discord webhook
discord_webhook_url = 'https://discord.com/api/webhooks/1319637403572371516/IY66xXXh10co7Ur2-9i3RrM-iVh60s9xS6CBjfO7iY1_AqHm5c9KkUrbXkga9A75I-Hz'  # ใส่ URL ของ Discord webhook ที่คุณต้องการใช้

# เปิดไฟล์ภาพ
with open("truemoney_with_textnew.png", "rb") as f:
    image_file = f.read()

# สร้างคำขอ JSON สำหรับ Discord Embed
embed_data = {
    "content": "ข้อมูลการโอนจ่าย",  # ข้อความที่ต้องการแสดงใน Discord
    "embeds": [
        {
            "title": "รายละเอียดการโอนเงิน",
            "description": f"ผู้โอน: {name_user_id}\nผู้รับ: {name_me_id}\nเบอร์โทรศัพท์ผู้รับ: {text_name_phone}\nจำนวนเงิน: {money_id} บาท",
            "color": 5814783
        }
    ]
}

# ส่งคำขอไปยัง Discord webhook
response = requests.post(discord_webhook_url, data=embed_data, files={'file': ('truemoney_with_textnew.png', image_file)})

if response.status_code == 204:
    print("ส่งข้อมูลไปยัง Discord สำเร็จ")
else:
    print(f"เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง Discord: {response.status_code}")