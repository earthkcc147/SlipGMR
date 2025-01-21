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

def get_current_time():
    """คืนค่าระยะเวลาในประเทศไทย"""
    thailand_timezone = pytz.timezone('Asia/Bangkok')
    current_time_thailand = datetime.now(thailand_timezone)
    time = current_time_thailand.strftime("%H:%M:%S")
    day = current_time_thailand.strftime("%d")
    month = current_time_thailand.strftime("%m")
    year = current_time_thailand.strftime("%Y")
    return day, month, year, time

def load_image(image_path):
    """โหลดภาพพื้นหลัง"""
    return Image.open(image_path)

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
    
    font_path_money = "Font/PSL158.ttf"
    font_path_user = "Font/PSL159.ttf"
    font_path_phone = "Font/PSL160.ttf"
    font_path_account = "Font/PSL160.ttf"
    font_path_bank = "Font/PSL160.ttf"
    font_path_bank_me = "Font/PSL160.ttf"
    
    font_money = ImageFont.truetype(font_path_money, font_size_money)
    font_user = ImageFont.truetype(font_path_user, font_size_user)
    font_me = ImageFont.truetype(font_path_user, font_size_me)
    font_phone = ImageFont.truetype(font_path_phone, font_size_phone)
    font_time = ImageFont.truetype(font_path_user, font_size_time)
    font_account = ImageFont.truetype(font_path_account, font_size_account)
    font_bank = ImageFont.truetype(font_path_bank, font_size_bank)
    font_bank_me = ImageFont.truetype(font_path_bank_me, font_size_bank_me)
    
    return font_money, font_user, font_me, font_phone, font_time, font_account, font_bank, font_bank_me

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

def set_text_positions():
    """กำหนดตำแหน่งของข้อความในภาพ"""
    return {
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

def main():
    """ฟังก์ชันหลักในการประมวลผล"""
    # รับข้อมูลจากผู้ใช้
    name_user_id, name_me_id, phone_me_id, money_id, account_user_id, bank_user_id, bank_me_id = get_user_input()

    # รับเวลา
    day, month, year, time = get_current_time()

    # โหลดภาพพื้นหลัง
    image = load_image("Bank/K-bank 4.png")
    draw = ImageDraw.Draw(image)

    # เตรียมฟอนต์
    fonts = prepare_fonts()

    # เตรียมข้อความ
    texts = prepare_texts(name_user_id, name_me_id, phone_me_id, money_id, account_user_id, bank_user_id, bank_me_id, day, month, year, time)

    # กำหนดตำแหน่งและสีของข้อความ
    positions = set_text_positions()
    colors = set_text_colors()

    # ใส่ข้อความลงในภาพ
    add_text_to_image(draw, positions, texts, fonts, colors)

    # บันทึกภาพ
    save_image(image, "truemoney_with_text_and_banks.png")

    print("สลีปปลอมสำเร็จ! บันทึกเป็น truemoney_with_text_and_banks.png")

if __name__ == "__main__":
    main()


