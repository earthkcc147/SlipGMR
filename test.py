from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pytz

def get_user_input():
    """รับข้อมูลจากผู้ใช้"""
    name_user_id = input("ชื่อผู้โอนจ่าย: ")
    name_me_id = input("ชื่อผู้รับเงิน: ")
    phone_me_id = input("หมายเลขบัญชีผู้รับ: ")
    money_id = input("จำนวนเงิน: ")
    account_user_id = input("หมายเลขบัญชีผู้โอน: ")
    bank_user_id = input("ชื่อธนาคารผู้โอน: ")
    bank_me_id = input("ชื่อธนาคารผู้รับ: ")

    return name_user_id, name_me_id, phone_me_id, money_id, account_user_id, bank_user_id, bank_me_id


def get_user_defined_time():
    """ถามผู้ใช้ว่าต้องการกำหนดวันที่หรือไม่ และรับอินพุต"""
    thailand_timezone = pytz.timezone('Asia/Bangkok')
    current_time_thailand = datetime.now(thailand_timezone)

    # แปลงเดือนเป็นชื่อภาษาไทยแบบย่อ
    thai_months = {
        "01": "ม.ค.", "02": "ก.พ.", "03": "มี.ค.", "04": "เม.ย.",
        "05": "พ.ค.", "06": "มิ.ย.", "07": "ก.ค.", "08": "ส.ค.",
        "09": "ก.ย.", "10": "ต.ค.", "11": "พ.ย.", "12": "ธ.ค."
    }

    # ถามว่าต้องการกำหนดวันที่เองหรือไม่
    use_custom_time = input("ต้องการดัดแปลงวันที่และเวลาหรือไม่? (y/n หรือ Enter = ไม่ดัดแปลง): ").lower()

    if use_custom_time == "y":
        print("กรุณากรอกวันที่และเวลา:")

        # ให้ผู้ใช้เลือกเดือนจากตัวเลข
        input_date = input("วันที่ (รูปแบบ DD): ")
        input_month = input("เดือน (เลือกจากตัวเลข 01-12): ")
        input_year = input("ปี (พ.ศ.): ")
        input_time = input("เวลา (รูปแบบ HH:MM): ")

        # ตรวจสอบว่าเดือนที่กรอกอยู่ในช่วงที่ถูกต้อง
        if input_month not in thai_months:
            print("เดือนที่กรอกไม่ถูกต้อง! ใช้เดือนปัจจุบันแทน")
            input_month = current_time_thailand.strftime("%m")

        # ใช้ค่าที่ผู้ใช้ป้อน
        day = int(input_date) if input_date else int(current_time_thailand.strftime("%d"))
        month = thai_months[input_month] if input_month else thai_months[current_time_thailand.strftime("%m")]
        year = str(int(input_year))[-2:] if input_year else str(int(current_time_thailand.strftime("%Y")) + 543)[-2:]
        time = input_time if input_time else current_time_thailand.strftime("%H:%M") + " น."
    else:
        # ใช้วันที่และเวลาปัจจุบัน
        day = int(current_time_thailand.strftime("%d"))
        month = thai_months[current_time_thailand.strftime("%m")]
        year = str(int(current_time_thailand.strftime("%Y")) + 543)[-2:]
        time = current_time_thailand.strftime("%H:%M") + " น."

    # รวมวันที่และเวลาเป็นข้อความเดียว (โดยไม่มีเครื่องหมาย /)
    defined_time = f"{day} {month} {year} {time}"

    # ส่งคืน defined_time
    return defined_time



def load_image(image_path):
    """โหลดภาพพื้นหลัง"""
    return Image.open(image_path)

def load_logo(logo_path):
    """โหลดโลโก้"""
    return Image.open(logo_path)

def prepare_fonts():
    """เตรียมฟอนต์ต่างๆ"""
    font_size_money = 87
    font_size_user = 48
    font_size_me = 48
    font_size_phone = 40
    font_size_time = 37
    font_size_account = 40
    font_size_bank = 40
    font_size_bank_me = 40
    font_size_order = 40  # เพิ่มฟอนต์สำหรับข้อความ 'order'

    font_path_money = "Font/PSL158.ttf"
    font_path_user = "Font/PSL159.ttf"
    font_path_phone = "Font/PSL160.ttf"
    font_path_account = "Font/PSL160.ttf"
    font_path_bank = "Font/PSL160.ttf"
    font_path_bank_me = "Font/PSL160.ttf"
    font_path_order = "Font/PSL160.ttf"  # เพิ่มเส้นทางฟอนต์สำหรับข้อความ 'order'

    font_money = ImageFont.truetype(font_path_money, font_size_money)
    font_user = ImageFont.truetype(font_path_user, font_size_user)
    font_me = ImageFont.truetype(font_path_user, font_size_me)
    font_phone = ImageFont.truetype(font_path_phone, font_size_phone)
    font_time = ImageFont.truetype(font_path_user, font_size_time)
    font_account = ImageFont.truetype(font_path_account, font_size_account)
    font_bank = ImageFont.truetype(font_path_bank, font_size_bank)
    font_bank_me = ImageFont.truetype(font_path_bank_me, font_size_bank_me)
    font_order = ImageFont.truetype(font_path_order, font_size_order)  # สร้างฟอนต์สำหรับข้อความ 'order'

    return font_money, font_user, font_me, font_phone, font_time, font_account, font_bank, font_bank_me, font_order

def prepare_texts(name_user_id, name_me_id, phone_me_id, money_id, account_user_id, bank_user_id, bank_me_id, day, month, year, time):
    """เตรียมข้อความที่จะใส่ลงในภาพ"""
    text_money = money_id + ".00"
    text_name_user = name_user_id
    text_name_me = name_me_id
    text_name_phone = f"{phone_me_id[:3]}-xxx-{phone_me_id[6:]}"
    text_name_time = f"  {day}/{month}/{year} {time}"
    text_name_order = "50018935012188"
    text_account_user = f"บัญชีผู้โอน: {account_user_id}"
    text_bank_user = f"ธนาคารผู้โอน: {bank_user_id}"
    text_bank_me = f"ธนาคารผู้รับ: {bank_me_id}"

    return text_money, text_name_user, text_name_me, text_name_phone, text_name_time, text_name_order, text_account_user, text_bank_user, text_bank_me

def set_text_positions_for_background(background_file):
    """กำหนดตำแหน่งของข้อความในภาพพื้นหลังแต่ละแบบ"""
    positions = {}

    if background_file == "Bank/K-bank 4.png":
        positions = {
            'money': (560, 270),
            'user': (302, 485),
            'me': (302, 648),
            'phone': (302, 720),
            'time': (781, 885),
            'order': (827, 953),
            'account': (302, 805),
            'bank': (302, 860),
            'bank_me': (302, 933)
        }
    elif background_file == "Bank/SCB 1.png":
        positions = {
            'money': (480, 250),
            'user': (250, 460),
            'me': (250, 620),
            'phone': (250, 690),
            'time': (700, 850),
            'order': (750, 910),
            'account': (250, 770),
            'bank': (250, 820),
            'bank_me': (250, 880)
        }
    elif background_file == "Bank/Siam 1.png":
        positions = {
            'money': (500, 260),
            'user': (280, 470),
            'me': (280, 630),
            'phone': (280, 700),
            'time': (760, 870),
            'order': (800, 930),
            'account': (280, 780),
            'bank': (280, 830),
            'bank_me': (280, 890)
        }
    # เพิ่มกรณีที่ผู้ใช้เลือกภาพพื้นหลังอื่นๆ ตามที่ต้องการ

    return positions

def set_text_colors():
    """กำหนดสีของข้อความ"""
    return {
        'money': (44, 44, 44),
        'user': (-20, -20, -20),
        'me': (-20, -20, -20),
        'phone': (80, 80, 80),
        'time': (60, 60, 60),
        'order': (60, 60, 60),
        'account': (80, 80, 80),
        'bank': (80, 80, 80),
        'bank_me': (80, 80, 80)
    }

def add_text_to_image(draw, positions, texts, fonts, colors):
    """ใส่ข้อความลงในภาพ"""
    draw.text(positions['money'], texts[0], font=fonts[0], fill=colors['money'])
    draw.text(positions['user'], texts[1], font=fonts[1], fill=colors['user'])
    draw.text(positions['me'], texts[2], font=fonts[2], fill=colors['me'])
    draw.text(positions['phone'], texts[3], font=fonts[3], fill=colors['phone'])
    draw.text(positions['time'], texts[4], font=fonts[4], fill=colors['time'])
    draw.text(positions['order'], texts[5], font=fonts[1], fill=colors['order'])
    draw.text(positions['account'], texts[6], font=fonts[6], fill=colors['account'])
    draw.text(positions['bank'], texts[7], font=fonts[7], fill=colors['bank'])
    draw.text(positions['bank_me'], texts[8], font=fonts[8], fill=colors['bank_me'])

def save_image(image, output_path):
    """บันทึกภาพที่มีข้อความ"""
    image.save(output_path)

def choose_bank():
    """ให้ผู้ใช้เลือกธนาคารที่ต้องการ"""
    banks = {
        1: {"name": "K-Bank", "backgrounds": {
            1: {"name": "K-Bank 1", "file": "Bank/K-bank 1.png"},
            2: {"name": "K-Bank 2", "file": "Bank/K-bank 2.png"},
            3: {"name": "K-Bank 3", "file": "Bank/K-bank 3.png"},
            4: {"name": "K-Bank 4", "file": "Bank/K-bank 4.png"}
        }},
        2: {"name": "SCB", "backgrounds": {
            1: {"name": "SCB 1", "file": "Bank/SCB 1.png"},
            2: {"name": "SCB 2", "file": "Bank/SCB 2.png"},
        }},
        3: {"name": "Siam Commercial", "backgrounds": {
            1: {"name": "Siam 1", "file": "Bank/Siam 1.png"},
            2: {"name": "Siam 2", "file": "Bank/Siam 2.png"},
        }},
    }

    print("เลือกธนาคาร (กรุณาเลือกหมายเลข):")
    for key, value in banks.items():
        print(f"{key}: {value['name']}")

    while True:
        try:
            bank_choice = int(input("เลือกหมายเลขธนาคารที่ต้องการ: "))
            if bank_choice in banks:
                print(f"คุณเลือกธนาคาร: {banks[bank_choice]['name']}")
                print("เลือกภาพพื้นหลัง (กรุณาเลือกหมายเลข):")
                for key, value in banks[bank_choice]["backgrounds"].items():
                    print(f"{key}: {value['name']}")

                while True:
                    try:
                        background_choice = int(input("เลือกหมายเลขภาพพื้นหลังที่ต้องการ: "))
                        if background_choice in banks[bank_choice]["backgrounds"]:
                            return banks[bank_choice]["backgrounds"][background_choice]["file"]
                        else:
                            print("กรุณาเลือกหมายเลขที่ถูกต้อง!")
                    except ValueError:
                        print("กรุณากรอกหมายเลขที่ถูกต้อง!")
            else:
                print("กรุณาเลือกหมายเลขที่ถูกต้อง!")
        except ValueError:
            print("กรุณากรอกหมายเลขที่ถูกต้อง!")

def choose_logo():
    """ให้ผู้ใช้เลือกโลโก้ที่ต้องการ"""
    logos = {
        1: {"name": "Logo 1", "file": "Bank/K-bank.png"},
        2: {"name": "Logo 2", "file": "Logos/logo2.png"},
        3: {"name": "Logo 3", "file": "Logos/logo3.png"},
    }

    print("เลือกโลโก้ (กรุณาเลือกหมายเลข):")
    for key, value in logos.items():
        print(f"{key}: {value['name']}")

    while True:
        try:
            choice = int(input("เลือกหมายเลขโลโก้ที่ต้องการ: "))
            if choice in logos:
                return logos[choice]["file"]
            else:
                print("กรุณาเลือกหมายเลขที่ถูกต้อง!")
        except ValueError:
            print("กรุณากรอกหมายเลขที่ถูกต้อง!")

def get_logo_size_and_position(background_image_path):
    """กำหนดขนาดและตำแหน่งของโลโก้ตามภาพพื้นหลัง"""
    if background_image_path == "Bank/K-bank 1.png":
        logo_size = (80, 80)  # ขนาดโลโก้สำหรับ K-Bank 1
        logo_position = (30, 30)  # ตำแหน่งโลโก้สำหรับ K-Bank 1
    elif background_image_path == "Bank/SCB 1.png":
        logo_size = (120, 120)  # ขนาดโลโก้สำหรับ SCB 1
        logo_position = (50, 50)  # ตำแหน่งโลโก้สำหรับ SCB 1
    elif background_image_path == "Bank/Siam 1.png":
        logo_size = (100, 100)  # ขนาดโลโก้สำหรับ Siam 1
        logo_position = (40, 40)  # ตำแหน่งโลโก้สำหรับ Siam 1
    else:
        logo_size = (100, 100)  # ขนาดโลโก้ทั่วไป
        logo_position = (20, 20)  # ตำแหน่งโลโก้ทั่วไป

    return logo_size, logo_position


import requests

def send_to_discord(image_path, name_user_id, name_me_id, phone_me_id, money_id, account_user_id, bank_user_id, bank_me_id, day, month, year, time_part):
    """ฟังก์ชันในการส่งข้อมูลไปยัง Discord Webhook พร้อมรูปภาพ"""
    webhook_url = "https://discord.com/api/webhooks/1319637403572371516/IY66xXXh10co7Ur2-9i3RrM-iVh60s9xS6CBjfO7iY1_AqHm5c9KkUrbXkga9A75I-Hz"

    # รวม day, month, year และ time_part เป็น defined_time
    defined_time = f"{day} {month} {year} {time_part}"

    # เตรียมข้อมูล Embed ที่จะส่งไปยัง Discord
    embed = {
        "title": "ข้อมูลการโอนเงิน",
        "description": f"จาก: {name_user_id}\nถึง: {name_me_id}\nหมายเลขบัญชีผู้รับ: {phone_me_id}\nจำนวนเงิน: {money_id}\nหมายเลขบัญชีผู้โอน: {account_user_id}\nธนาคารผู้โอน: {bank_user_id}\nธนาคารผู้รับ: {bank_me_id}\nวันที่และเวลา: {defined_time}",
        "color": 65280  # สีเขียว
    }

    # เตรียมข้อมูลที่แนบ (ภาพ)
    files = {
        "file": open(image_path, "rb")
    }

    data = {
        "embeds": [embed]
    }

    # ส่ง POST request ไปยัง Discord Webhook
    response = requests.post(webhook_url, json=data, files=files)

    # ตรวจสอบว่าโพสต์สำเร็จหรือไม่
    if response.status_code == 204:
        print("ข้อมูลถูกส่งไปยัง Discord เรียบร้อยแล้ว!")
    else:
        print(f"เกิดข้อผิดพลาดในการส่งข้อมูล: {response.status_code} - {response.text}")

def main():
    """ฟังก์ชันหลักในการประมวลผล"""
    # ให้ผู้ใช้เลือกธนาคารและภาพพื้นหลัง
    background_image_path = choose_bank()

    # ให้ผู้ใช้เลือกโลโก้
    logo_path = choose_logo()

    # รับข้อมูลจากผู้ใช้
    name_user_id, name_me_id, phone_me_id, money_id, account_user_id, bank_user_id, bank_me_id = get_user_input()

    # รับวันและเวลา (ผู้ใช้กำหนด หรือใช้ค่าเริ่มต้น)
    defined_time = get_user_defined_time()  # คืนค่าเป็นข้อความเดียวที่รวมวัน เดือน ปี และเวลา

    # แยก defined_time ออกเป็นวัน เดือน ปี และเวลา
    date_part, time_part = defined_time.rsplit(" ", 1)  # แยกเวลาออกจากวันที่

    # แยกวันที่ออกเป็นวันที่, เดือน และปี
    date_parts = date_part.split(" ")
    day = date_parts[0]
    month = date_parts[1]
    year = date_parts[2]

    # โหลดภาพพื้นหลังที่เลือก
    image = load_image(background_image_path)
    draw = ImageDraw.Draw(image)

    # โหลดโลโก้ที่เลือก
    logo = load_logo(logo_path)

    # กำหนดขนาดและตำแหน่งของโลโก้ตามภาพพื้นหลัง
    logo_size, logo_position = get_logo_size_and_position(background_image_path)

    # ปรับขนาดโลโก้ให้เหมาะสม
    logo = logo.resize(logo_size)

    # วางโลโก้ลงในภาพ
    image.paste(logo, logo_position, logo)  # ใช้ alpha channel ในกรณีที่โลโก้มีความโปร่งใส

    # เตรียมฟอนต์
    fonts = prepare_fonts()

    # เตรียมข้อความ
    texts = prepare_texts(name_user_id, name_me_id, phone_me_id, money_id, account_user_id, bank_user_id, bank_me_id, day, month, year, time_part)

    # กำหนดตำแหน่งข้อความตามภาพพื้นหลัง
    positions = set_text_positions_for_background(background_image_path)

    # กำหนดสีของข้อความ
    colors = set_text_colors()

    # ใส่ข้อความลงในภาพ
    add_text_to_image(draw, positions, texts, fonts, colors)

    # บันทึกภาพที่มีข้อความ
    image_path = "output_image.png"
    save_image(image, image_path)

    print("สลีปปลอมสำเร็จ! บันทึกเป็น output_image.png")

    # ส่งข้อมูลไปยัง Discord
    send_to_discord(image_path, name_user_id, name_me_id, phone_me_id, money_id, account_user_id, bank_user_id, bank_me_id, day, month, year, time_part)


if __name__ == "__main__":
    main()