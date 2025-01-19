from PIL import Image, ImageDraw, ImageFont
import pytz
from datetime import datetime
import requests

# ฟังก์ชั่นสำหรับเลือกภาพพื้นหลัง
def select_background():
    print("เลือกภาพพื้นหลัง:")
    print("1. K-bank 4")
    print("2. K-bank 5")
    print("3. K-bank 6")

    choice = input("กรุณาเลือกหมายเลข (1-3): ")

    if choice == "1":
        return "Bank/K-bank 4.png"
    elif choice == "2":
        return "Bank/K-bank 5.png"
    elif choice == "3":
        return "Bank/K-bank 6.png"
    else:
        print("ตัวเลือกไม่ถูกต้อง! เลือกใหม่.")
        return select_background()  # ถ้าเลือกไม่ถูกต้อง ให้เลือกใหม่

# ฟังก์ชั่นสำหรับเลือกโลโก้
def select_logo():
    print("เลือกโลโก้:")
    print("1. K-bank")
    print("2. Another Logo")  # เพิ่มโลโก้ตัวเลือกอื่นๆ ได้
    choice = input("กรุณาเลือกหมายเลข (1-2): ")

    if choice == "1":
        return "Bank/K-bank.png"
    elif choice == "2":
        return "Bank/AnotherLogo.png"  # ตัวอย่างโลโก้อื่นๆ
    else:
        print("ตัวเลือกไม่ถูกต้อง! เลือกใหม่.")
        return select_logo()  # ถ้าเลือกไม่ถูกต้อง ให้เลือกใหม่

# เมนูหลัก
def main_menu():
    print("ระบบสร้างใบโอนจ่าย")
    
    # เลือกภาพพื้นหลัง
    background_image = select_background()
    
    # เลือกโลโก้
    logo_image = select_logo()

    # ข้อมูลจากผู้ใช้
    name_user_id = input("ชื่อผู้โอนจ่าย: ")
    bank_user_id = input("ธ.ผู้โอน: ")
    phone_user_id = input("เบอร์ผู้โอน: ")

    name_me_id = input("ชื่อผู้รับเงิน: ")
    bank_me_id = input("ธ.ผู้รับ: ")
    phone_me_id = input("เบอร์โทรศัพท์ผู้รับ: ")

    money_id = input("จำนวนเงิน: ")

    # เวลาในประเทศไทย
    thailand_timezone = pytz.timezone('Asia/Bangkok')
    current_time_thailand = datetime.now(thailand_timezone)
    time = current_time_thailand.strftime("%H:%M:%S")
    day = current_time_thailand.strftime("%d")
    month = current_time_thailand.strftime("%m")
    year = current_time_thailand.strftime("%Y")

    # โหลดภาพพื้นหลังตามที่เลือก
    image = Image.open(background_image)
    draw = ImageDraw.Draw(image)

    # กำหนดฟอนต์
    font_size_user = 48
    font_size_bank_user = 48
    font_size_phone_user = 40
    font_size_me = 48
    font_size_bank_me = 48
    font_size_phone = 40
    font_size_order = 36
    font_size_money = 87
    font_size_time = 37

    font_path_user = "Font/PSL159.ttf"
    font_path_bank_user = "Font/PSL159.ttf"
    font_path_phone_user = "Font/PSL160.ttf"
    font_path_name_me = "Font/PSL159.ttf"
    font_path_bank_me = "Font/PSL159.ttf"
    font_path_phone = "Font/PSL160.ttf"
    font_path_order = "Font/PSL159.ttf"
    font_path_money = "Font/PSL158.ttf"

    font_user = ImageFont.truetype(font_path_user, font_size_user)
    font_bank_user = ImageFont.truetype(font_path_bank_user, font_size_bank_user)
    font_phone_user = ImageFont.truetype(font_path_phone_user, font_size_phone_user)
    font_me = ImageFont.truetype(font_path_name_me, font_size_me)
    font_bank_me = ImageFont.truetype(font_path_bank_me, font_size_bank_me)
    font_phone = ImageFont.truetype(font_path_phone, font_size_phone)
    font_order = ImageFont.truetype(font_path_order, font_size_order)
    font_money = ImageFont.truetype(font_path_money, font_size_money)
    font_time = ImageFont.truetype(font_path_user, font_size_time)

    # ข้อความที่ต้องการใส่ลงในภาพ
    text_name_user = name_user_id
    text_bank_user = bank_user_id
    text_name_phone = f"{phone_me_id[:3]}-xxx-{phone_me_id[6:]}"
    text_phone_user = phone_user_id
    text_name_me = name_me_id
    text_bank_me = bank_me_id
    phone = phone_me_id
    text_name_order = "50018935012188"
    text_money = money_id + ".00"
    text_name_time = f"  {day}/{month}/{year} {time}"

    # ตำแหน่งข้อความ
    text_position_user = (250, 220) # ชื่อผู้โอน
    text_position_bank_user = (250, 280)  # ธ.ผู้โอน
    text_position_phone_user = (250, 340)  # เบอร์ผู้โอน
    text_position_me = (250, 540) # ชื่อผู้รับ
    text_position_bank_me = (250, 600)  # ธ.ผู้รับ
    text_position_phone = (250, 660) # เบอร์ผู้รับ
    text_position_order = (445, 820) # เลขออเดอร์
    text_position_money = (370, 900) # จำนวนเงิน
    text_position_time = (55, 100) # เวลา

    # สีของข้อความ
    text_color_user = (-20, -20, -20)
    text_color_bank_user = (60, 60, 60)
    text_color_phone_user = (60, 60, 60)
    text_color_me = (-20, -20, -20)
    text_color_bank_me = (60, 60, 60)
    text_color_phone = (80, 80, 80)
    text_color_order = (60, 60, 60)
    text_color_money = (44, 44, 44)
    text_color_time = (60, 60, 60)

    # ใส่ข้อความลงในภาพ
    draw.text(text_position_user, text_name_user, font=font_user, fill=text_color_user)
    draw.text(text_position_bank_user, text_bank_user, font=font_bank_user, fill=text_color_bank_user)
    draw.text(text_position_phone_user, text_phone_user, font=font_phone_user, fill=text_color_phone_user)
    draw.text(text_position_me, text_name_me, font=font_me, fill=text_color_me)
    draw.text(text_position_bank_me, text_bank_me, font=font_bank_me, fill=text_color_bank_me)
    draw.text(text_position_phone, text_name_phone, font=font_phone, fill=text_color_phone)
    draw.text(text_position_order, text_name_order, font=font_order, fill=text_color_order)
    draw.text(text_position_money, text_money, font=font_money, fill=text_color_money)
    draw.text(text_position_time, text_name_time, font=font_time, fill=text_color_time)

    # โหลดโลโก้ที่มีพื้นหลังโปร่งใส
    logo = Image.open(logo_image)
    logo = logo.resize((130, 130))

    # ตำแหน่งโลโก้
    logo_position = (50, image.height - logo.height - 500)

    # แทรกโลโก้ที่มีพื้นหลังโปร่งใสลงในภาพ
    image.paste(logo, logo_position, logo)

    # บันทึกภาพที่มีข้อความและโลโก้
    image.save("truemoney_with_text_and_logo.png")

    # ส่งข้อมูลไปยัง Discord webhook
    discord_webhook_url = 'https://discord.com/api/webhooks/1319637403572371516/IY66xXXh10co7Ur2-9i3RrM-iVh60s9xS6CBjfO7iY1_AqHm5c9KkUrbXkga9A75I-Hz'

    embed_data = {
        "content": "ข้อมูลการโอนจ่าย",
        "embeds": [
            {
                "title": "รายละเอียดการโอนเงิน",
                "description": f"ผู้โอน: {name_user_id}\nผู้รับ: {name_me_id}\nเบอร์โทรศัพท์ผู้รับ: {text_name_phone}\nจำนวนเงิน: {money_id} บาท\nธ.ผู้โอน: {text_bank_user}\nเบอร์ผู้โอน: {text_phone_user}\nธ.ผู้รับ: {text_bank_me}",
                "color": 5814783,
                "fields": [
                    {"name": "ผู้โอนจ่าย", "value": name_user_id, "inline": True},
                    {"name": "ผู้รับเงิน", "value": name_me_id, "inline": True},
                    {"name": "เบอร์โทรศัพท์ผู้รับ", "value": text_name_phone, "inline": True},
                    {"name": "จำนวนเงิน", "value": f"{money_id} บาท", "inline": True},
                    {"name": "เวลาการโอน", "value": f"{day}/{month}/{year} {time}", "inline": True},
                    {"name": "ธ.ผู้โอน", "value": text_bank_user, "inline": True},
                    {"name": "เบอร์ผู้โอน", "value": text_phone_user, "inline": True},
                    {"name": "ธ.ผู้รับ", "value": text_bank_me, "inline": True}
                ]
            }
        ]
    }

    # ส่งคำขอไปยัง Discord webhook
    response = requests.post(discord_webhook_url, json=embed_data)  # ใช้ json แทน data

    # ส่งภาพหลังจาก Embed
    with open("truemoney_with_text_and_logo.png", "rb") as f:
        image_file = f.read()

    response = requests.post(
        discord_webhook_url,
        files={'file': ('truemoney_with_text_and_logo.png', image_file)}
    )

    if response.status_code == 200:
        print("ส่งข้อมูลไปยัง Discord สำเร็จ")
    else:
        print(f"เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง Discord: {response.status_code}")

# เรียกใช้เมนูหลัก
if __name__ == "__main__":
    main_menu()