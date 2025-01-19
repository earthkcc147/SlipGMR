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

# กำหนดฟอนต์
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