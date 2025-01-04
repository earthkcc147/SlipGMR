# function/script.py
import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pytz

def create_fake_receipt(name_user_id, name_me_id, phone_me_id, money_id):
    # เวลาในประเทศไทย
    thailand_timezone = pytz.timezone('Asia/Bangkok')
    current_time_thailand = datetime.now(thailand_timezone)
    time = current_time_thailand.strftime("%H:%M:%S")
    day = current_time_thailand.strftime("%d")
    month = current_time_thailand.strftime("%m")
    year = current_time_thailand.strftime("%Y")

    # โหลดภาพพื้นหลัง
    print("🖼️ กำลังโหลดภาพพื้นหลัง... ⏳")
    image = Image.open(os.path.join(os.path.dirname(__file__), "truemoney.png"))  # โหลดภาพจากโฟลเดอร์เดียวกัน
    draw = ImageDraw.Draw(image)

    # กำหนดขนาดและฟอนต์
    font_size_money = 87
    font_size_user = 48
    font_size_me = 48
    font_size_phone = 40
    font_size_time = 37

    font_path_money = os.path.join(os.path.dirname(__file__), "Lato-Heavy.ttf")  # ระบุฟอนต์จากโฟลเดอร์เดียวกัน
    font_path_user = os.path.join(os.path.dirname(__file__), "Kanit-ExtraLight.ttf")
    font_path_phone = os.path.join(os.path.dirname(__file__), "Prompt-Light.ttf")

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

    # ตรวจสอบว่าโฟลเดอร์ "textnew" มีอยู่หรือไม่ ถ้าไม่มีให้สร้าง
    folder_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "textnew")
    if not os.path.exists(folder_path):
        print("📂 โฟลเดอร์ textnew ไม่พบ, กำลังสร้าง...")
        os.makedirs(folder_path)

    # สร้างชื่อไฟล์โดยใช้ชื่อผู้โอน, ชื่อผู้รับ, จำนวนเงิน, เบอร์โทรผู้รับ
    file_name = f"{name_user_id}_{name_me_id}_{money_id}_{phone_me_id}.png"
    
    # บันทึกภาพที่มีข้อความในโฟลเดอร์ "textnew"
    print("💾 กำลังบันทึกไฟล์... 📸")
    image.save(os.path.join(folder_path, file_name))
    print(f"✅ สลีปปลอมสำเร็จ! บันทึกเป็น textnew/{file_name}")