import requests
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pytz

# ข้อมูลจากผู้ใช้
name_user_id = input("ชื่อผู้โอนจ่าย: ")  # รับชื่อผู้โอน
name_me_id = input("ชื่อผู้รับเงิน: ")   # รับชื่อผู้รับ
phone_me_id = input("เบอร์โทรศัพท์ผู้รับ: ")  # รับเบอร์โทรผู้รับ
money_id = input("จำนวนเงิน: ")  # รับจำนวนเงินที่โอน

# เวลาในประเทศไทย
thailand_timezone = pytz.timezone('Asia/Bangkok')  # ตั้งเวลาของประเทศไทย
current_time_thailand = datetime.now(thailand_timezone)  # เวลาปัจจุบันในประเทศไทย
time = current_time_thailand.strftime("%H:%M:%S")  # เวลาในรูปแบบชั่วโมง:นาที:วินาที
day = current_time_thailand.strftime("%d")  # วัน
month = current_time_thailand.strftime("%m")  # เดือน
year = current_time_thailand.strftime("%Y")  # ปี

# โหลดภาพพื้นหลัง
image = Image.open("Bank/K-bank 4.png")  # เปิดภาพพื้นหลัง
draw = ImageDraw.Draw(image)  # สร้างวัตถุสำหรับการวาดบนภาพ

# กำหนดฟอนต์
font_size_money = 87
font_size_user = 48
font_size_me = 48
font_size_phone = 40
font_size_time = 37
font_path_money = "Font/PSL158.ttf"  # ที่อยู่ฟอนต์สำหรับจำนวนเงิน
font_path_user = "Font/PSL159.ttf"  # ที่อยู่ฟอนต์สำหรับชื่อผู้โอน
font_path_phone = "Font/PSL160.ttf"  # ที่อยู่ฟอนต์สำหรับเบอร์โทร

font_user = ImageFont.truetype(font_path_user, font_size_user)  # โหลดฟอนต์สำหรับชื่อผู้โอน
font_me = ImageFont.truetype(font_path_user, font_size_me)  # โหลดฟอนต์สำหรับชื่อผู้รับ
font_phone = ImageFont.truetype(font_path_phone, font_size_phone)  # โหลดฟอนต์สำหรับเบอร์โทร
font_time = ImageFont.truetype(font_path_user, font_size_time)  # โหลดฟอนต์สำหรับเวลา
font_order = ImageFont.truetype(font_path_user, font_size_time)  # ฟอนต์สำหรับหมายเลขคำสั่ง
font_money = ImageFont.truetype(font_path_money, font_size_money)  # โหลดฟอนต์สำหรับจำนวนเงิน

# ข้อความที่ต้องการใส่ลงในภาพ
phone = phone_me_id
text_money = money_id + ".00"  # จำนวนเงิน
text_name_user = name_user_id  # ชื่อผู้โอน
text_name_me = name_me_id  # ชื่อผู้รับ
text_name_phone = f"{phone[:3]}-xxx-{phone[6:]}"  # รูปแบบเบอร์โทรศัพท์
text_name_time = f"  {day}/{month}/{year} {time}"  # เวลาปัจจุบัน
text_name_order = "50018935012188"  # หมายเลขคำสั่ง

# ตำแหน่งข้อความ
text_position_money = (560, 270)  # ตำแหน่งข้อความจำนวนเงิน
text_position_user = (302, 485)  # ตำแหน่งชื่อผู้โอน
text_position_me = (302, 648)  # ตำแหน่งชื่อผู้รับ
text_position_phone = (302, 720)  # ตำแหน่งเบอร์โทรผู้รับ
text_position_time = (781, 885)  # ตำแหน่งเวลา
text_position_order = (827, 953)  # ตำแหน่งหมายเลขคำสั่ง

# สีของข้อความ
text_color_money = (44, 44, 44)  # สีข้อความจำนวนเงิน
text_color_user = (-20, -20, -20)  # สีข้อความชื่อผู้โอน
text_color_me = (-20, -20, -20)  # สีข้อความชื่อผู้รับ
text_color_phone = (80, 80, 80)  # สีข้อความเบอร์โทร
text_color_time = (60, 60, 60)  # สีข้อความเวลา
text_color_order = (60, 60, 60)  # สีข้อความหมายเลขคำสั่ง

# ใส่ข้อความลงในภาพ
draw.text(text_position_money, text_money, font=font_money, fill=text_color_money)  # ใส่จำนวนเงิน
draw.text(text_position_user, text_name_user, font=font_user, fill=text_color_user)  # ใส่ชื่อผู้โอน
draw.text(text_position_me, text_name_me, font=font_me, fill=text_color_me)  # ใส่ชื่อผู้รับ
draw.text(text_position_phone, text_name_phone, font=font_phone, fill=text_color_phone)  # ใส่เบอร์โทร
draw.text(text_position_time, text_name_time, font=font_time, fill=text_color_time)  # ใส่เวลา
draw.text(text_position_order, text_name_order, font=font_order, fill=text_color_order)  # ใส่หมายเลขคำสั่ง

# บันทึกภาพที่มีข้อความ
image.save("truemoney_with_textnew.png")  # บันทึกภาพ

# ส่งข้อมูลไปยัง Discord webhook
discord_webhook_url = 'https://discord.com/api/webhooks/1319637403572371516/IY66xXXh10co7Ur2-9i3RrM-iVh60s9xS6CBjfO7iY1_AqHm5c9KkUrbXkga9A75I-Hz'

# สร้างคำขอ JSON สำหรับ Discord Embed พร้อมกับ add.fields
embed_data = {
    "content": "ข้อมูลการโอนจ่าย",  # ข้อความใน Discord
    "embeds": [
        {
            "title": "รายละเอียดการโอนเงิน",  # หัวข้อของ Embed
            "description": f"ผู้โอน: {name_user_id}\nผู้รับ: {name_me_id}\nเบอร์โทรศัพท์ผู้รับ: {text_name_phone}\nจำนวนเงิน: {money_id} บาท",
            "color": 5814783,  # สีของ Embed
            "fields": [
                {
                    "name": "ผู้โอนจ่าย",  # ชื่อฟิลด์
                    "value": name_user_id,  # ข้อมูลที่จะแสดง
                    "inline": True
                },
                {
                    "name": "ผู้รับเงิน",  # ชื่อฟิลด์
                    "value": name_me_id,  # ข้อมูลที่จะแสดง
                    "inline": True
                },
                {
                    "name": "เบอร์โทรศัพท์ผู้รับ",  # ชื่อฟิลด์
                    "value": text_name_phone,  # ข้อมูลที่จะแสดง
                    "inline": True
                },
                {
                    "name": "จำนวนเงิน",  # ชื่อฟิลด์
                    "value": f"{money_id} บาท",  # ข้อมูลที่จะแสดง
                    "inline": True
                },
                {
                    "name": "เวลาการโอน",  # ชื่อฟิลด์
                    "value": f"{day}/{month}/{year} {time}",  # ข้อมูลที่จะแสดง
                    "inline": True
                }
            ]
        }
    ]
}

# ส่งคำขอไปยัง Discord webhook
response = requests.post(
    discord_webhook_url,
    json=embed_data  # ใช้ json แทน data
)

# ส่งภาพหลังจาก Embed
with open("truemoney_with_textnew.png", "rb") as f:
    image_file = f.read()

    response = requests.post(
        discord_webhook_url,
        files={'file': ('truemoney_with_textnew.png', image_file)}  # ส่งไฟล์ภาพ
    )

if response.status_code == 200:
    print("ส่งข้อมูลไปยัง Discord สำเร็จ")  # แสดงข้อความเมื่อส่งข้อมูลสำเร็จ
else:
    print(f"เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง Discord: {response.status_code}")  # แสดงข้อความเมื่อมีข้อผิดพลาด