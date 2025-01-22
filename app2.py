from PIL import Image, ImageDraw, ImageFont
import pytz
from datetime import datetime
import requests


import os
import json
from dotenv import load_dotenv


# ประกาศตัวแปร global สำหรับเก็บสถานะ
global_status = {
    "bank_name": None,
    "background_image": None,
    "logo": None,
    "logo_position": None,
    "name_user_id": None,
    "bank_user_id": None,
    "phone_user_id": None,
    "name_me_id": None,
    "bank_me_id": None,
    "phone_me_id": None,
    "money_id": None,
    "custom_time": None,
    "login_status": False,  # เพิ่มสถานะการล็อกอิน
    "logged_in_user": None  # เพิ่มชื่อผู้ใช้ที่ล็อกอินสำเร็จ
}


# ฟังก์ชันแสดงสถานะทั้งหมดที่เก็บไว้
def show_all_status():
    global global_status  # ใช้ global_status
    print("\n=== สถานะทั้งหมดที่เก็บไว้ ===")
    for key, value in global_status.items():
        print(f"{key}: {value if value else 'ยังไม่มีข้อมูล'}")


# ฟังก์ชันสำหรับล้างค่าตัวแปรสถานะ
def reset_global_status():
    for key in global_status:
        global_status[key] = None if isinstance(global_status[key], str) else False
    print("🔄 ล้างสถานะทั้งหมดเรียบร้อยแล้ว!")


# ฟังก์ชั่นสำหรับล้างสถานะที่มีอยู่ยกเว้น login_status
def clear_status():
    global_status.update({
        "bank_name": None,
        "background_image": None,
        "logo": None,
        "logo_position": None,
        "name_user_id": None,
        "bank_user_id": None,
        "phone_user_id": None,
        "name_me_id": None,
        "bank_me_id": None,
        "phone_me_id": None,
        "money_id": None,
        "custom_time": None,
        # login_status ยังคงเดิม
    })


# โหลดไฟล์ .env
load_dotenv()

# ดึงข้อมูล USERS จาก .env
USERS_JSON = os.getenv("USERS")

# แปลงข้อมูล USERS_JSON เป็น dictionary
try:
    users_data = json.loads(USERS_JSON)
except json.JSONDecodeError:
    print("ไม่สามารถแปลงข้อมูล USERS จาก .env ได้ ❌")
    exit()

# ฟังก์ชันสำหรับล็อกอิน
def login():
    global global_status  # ใช้ global_status
    print("📄 ระบบล็อกอิน 📄")
    print("===================================")

    # รับข้อมูลชื่อผู้ใช้และรหัสผ่าน
    username = input("👤 ชื่อผู้ใช้: ")
    password = input("🔒 รหัสผ่าน: ")

    # ตรวจสอบข้อมูลกับฐานข้อมูลจากไฟล์ .env
    if username in users_data:
        if users_data[username]["password"] == password:
            print("✔️ การล็อกอินสำเร็จ")
            # เก็บสถานะการล็อกอิน
            global_status["login_status"] = True
            global_status["logged_in_user"] = username
            return True
        else:
            print("❌ รหัสผ่านไม่ถูกต้อง")
    else:
        print("❌ ชื่อผู้ใช้ไม่ถูกต้อง")

    # อัปเดตสถานะการล็อกอินเป็น False
    global_status["login_status"] = False
    global_status["logged_in_user"] = None
    return False

# เรียกใช้งานฟังก์ชัน login
if not login():
    print("Login failed. Exiting program.")
    exit()  # หยุดโปรแกรมหากล็อกอินไม่สำเร็จ
else:
    print(f"เข้าสู่ระบบสำเร็จ! ผู้ใช้ที่ล็อกอิน: {global_status['logged_in_user']}")




# ตัวแปรสำหรับเปิด/ปิดโหมดดีบัก
debug_mode = False  # เปลี่ยนเป็น True/ False เพื่อปิดโหมดดีบัก

# ฟังก์ชันสำหรับการดีบักที่สามารถเปิดปิดได้
def debug_print(message):
    if debug_mode:
        print(message)


# ฟังก์ชันสำหรับเลือกธนาคาร
def select_bank():
    global global_status  # ใช้ global_status

    print("เลือกธนาคารผู้โอน:")
    print("1. K-bank 🏦 (ธนาคารกสิกรไทย)")
    print("2. SCB 🏧 (ธนาคารไทยพาณิชย์)")
    print("3. Bangkok 🏙️ (ธนาคารกรุงเทพ)")
    print("4. TTB 🏛️ (ธนาคารทหารไทยธนชาต)")
    print("5. กรุงศรี 🏦 (ธนาคารกรุงศรีอยุธยา)")
    print("6. กรุงไทย 🏦 (ธนาคารกรุงไทย)")
    print("7. TrueWallet 💳 (ทรูวอลเล็ท)")  # เพิ่ม TrueWallet
    print("8. Other Bank 🎨 (ธนาคารอื่นๆ)")  # ตัวเลือกธนาคารอื่นๆ
    print("00. ออกโปรแกรม")  # เพิ่มตัวเลือกออกจากโปรแกรม
    choice = input("กรุณาเลือกหมายเลข (1-8 หรือ 00 เพื่อออกโปรแกรม): ")

    # ตรวจสอบการเลือกธนาคาร
    if choice == "1":
        bank_name = "K-bank"
    elif choice == "2":
        bank_name = "SCB"
    elif choice == "3":
        bank_name = "Bangkok"
    elif choice == "4":
        bank_name = "TTB"
    elif choice == "5":
        bank_name = "กรุงศรี"
    elif choice == "6":
        bank_name = "กรุงไทย"
    elif choice == "7":
        bank_name = "TrueWallet"
    elif choice == "8":
        bank_name = "Other Bank"
    elif choice == "00":
        reset_global_status()  # ล้างสถานะ
        print("โปรแกรมถูกปิดแล้ว.")
        exit()  # ออกจากโปรแกรม
    else:
        print("❌ ตัวเลือกไม่ถูกต้อง! เลือกใหม่.")
        return select_bank()  # ถ้าเลือกไม่ถูกต้อง ให้เลือกใหม่

    # เก็บสถานะธนาคารที่เลือก
    global_status["bank_name"] = bank_name
    print(f"📊 คุณเลือกธนาคาร: {bank_name}")
    return bank_name


# ฟังก์ชันสำหรับเลือกภาพพื้นหลังตามธนาคาร
def select_background(bank_name):
    global global_status  # ใช้ global_status เพื่อเก็บสถานะ

    print(f"เลือกภาพพื้นหลังสำหรับธนาคาร {bank_name}:")

    if bank_name == "K-bank":
        print("1. K-bank ธรรมดา 🌇")
        print("2. K-bank คริสมาสต์ 🌆")
        print("3. K-bank ใจเขียว 🌃")
        print("4. K-bank หมาคาบเงิน 🌌")
        print("5. K-bank พิเศษ 🌠")
    elif bank_name == "SCB":
        print("1. SCB ไทยพาณิชย์ 🌇")
        print("เร็วๆนี้")
    elif bank_name == "Bangkok":
        print("1. Bangkok กรุงเทพ 🌇")
        print("เร็วๆนี้")
    elif bank_name == "TTB":
        print("1. TTB 🌇")
        print("เร็วๆนี้")
    elif bank_name == "กรุงศรี":
        print("1. กรุงศรี 🌇")
        print("เร็วๆนี้")
    elif bank_name == "กรุงไทย":
        print("1. กรุงไทย 🌇")
        print("เร็วๆนี้")
    elif bank_name == "TrueWallet":
        print("1. TrueWallet 🌇")
        print("เร็วๆนี้")
    else:
        print("ไม่มีพื้นหลังสำหรับธนาคารนี้")

    print("00. ย้อนกลับ")

    choice = input("กรุณาเลือกหมายเลข (0-5): ")

    if choice == "00":
        # ล้างสถานะที่มีอยู่ยกเว้น login_status
        clear_status()
        main_menu()  # เพิ่มตัวเลือกย้อนกลับ
    elif choice == "1" and bank_name == "K-bank":
        global_status["background_image"] = "Bank/K-bank 4.png"
    elif choice == "2" and bank_name == "K-bank":
        global_status["background_image"] = "Bank/K-bank 3.png"
    elif choice == "3" and bank_name == "K-bank":
        global_status["background_image"] = "Bank/K-bank 2.png"
    elif choice == "4" and bank_name == "K-bank":
        global_status["background_image"] = "Bank/K-bank 1.png"
    elif choice == "5" and bank_name == "K-bank":
        global_status["background_image"] = "Bank/K-bank 0.png"

    elif choice == "1" and bank_name == "SCB":
        global_status["background_image"] = "Bank/SCB copy.png"

    elif choice == "1" and bank_name == "Bangkok":
        global_status["background_image"] = "Bank/Bangkok.png"

    elif choice == "1" and bank_name == "TTB":
        global_status["background_image"] = "Bank/TTB.jpg"

    elif choice == "1" and bank_name == "กรุงศรี":
        global_status["background_image"] = "Bank/กรุงศรี.png"

    elif choice == "1" and bank_name == "กรุงไทย":
        global_status["background_image"] = "Bank/กรุงไทย.png"

    elif choice == "1" and bank_name == "TrueWallet":
        global_status["background_image"] = "Bank/truemoney.png"

    else:
        print("❌ ตัวเลือกไม่ถูกต้อง! เลือกใหม่.")
        return select_background(bank_name)  # ถ้าเลือกไม่ถูกต้อง ให้เลือกใหม่

    print(f"📸 ภาพพื้นหลังที่เลือก: {global_status['background_image']}")
    return global_status["background_image"]





# ฟังก์ชั่นสำหรับเลือกโลโก้
def select_logo(background_image):
    print("เลือกธนาคารผู้รับ:")
    print("1. K-bank 🏦 (ธนาคารกสิกรไทย)")
    print("2. SCB 🏦 (ธนาคารไทยพาณิชย์)")
    print("3. Bangkok 🏦 (ธนาคารกรุงเทพ)")
    print("4. ออมสิน 🏦 (ธนาคารออมสิน)")
    print("5. กรุงศรี 🏦 (ธนาคารกรุงศรีอยุธยา)")
    print("6. กรุงไทย 🏦 (ธนาคารกรุงไทย)")
    print("7. UOB 🏦 (ธนาคารยูโอบี)")
    print("8. Citi 🏦 (ธนาคารซิตี้แบงก์)")
    print("9. TTB 🏦 (ธนาคารทหารไทยธนชาต)")
    print("10. Another Logo 🎨 (โลโก้ธนาคารอื่นๆ)")  # เพิ่มโลโก้ตัวเลือกอื่นๆ ได้
    print("00. เริ่มใหม่ 🔄")  # เพิ่มตัวเลือกสำหรับเลือกพื้นหลังใหม่
    choice = input("กรุณาเลือกหมายเลข (1-10 หรือ 00 เพื่อเลือกพื้นหลังใหม่): ")

    if choice == "00":
        # ล้างสถานะที่มีอยู่ยกเว้น login_status
        clear_status()
        print("🔄 ระบบเริ่มใหม่! กรุณาเลือกอีกครั้ง.")
        main_menu()  # เรียกเมนูหลักใหม่
        return  # หยุดการทำงานในฟังก์ชันนี้

    if choice == "1":
        logo_image = "Bank/K-bank.png"
    elif choice == "2":
        logo_image = "Bank/imgbin_thailand-siam-commercial-bank-refinancing-kasikornbank-png.png"
    elif choice == "3":
        logo_image = "Bank/Asset-2@4x (0_3).png"
    elif choice == "4":
        logo_image = "Bank/truemoneywallet-Promptpay-aw-logobank-20220325-1a-400x183 (1_2).png"
    elif choice == "5":
        logo_image = "Bank/truemoneywallet-Promptpay-aw-logobank-20220325-1a-400x183 (0_2).png"
    elif choice == "6":
        logo_image = "Bank/krung-thai-bank-money.png"
    elif choice == "7":
        logo_image = "Bank/Logo-bank (1_4).png"
    elif choice == "8":
        logo_image = "Bank/Logo-bank (1_2).png"
    elif choice == "9":
        logo_image = "Bank/IMG_197712.png"
    elif choice == "10":
        logo_image = "Bank/AnotherLogo.png"  # ตัวอย่างโลโก้อื่นๆ
    else:
        print("❌ ตัวเลือกไม่ถูกต้อง! เลือกใหม่.")
        return select_logo(background_image)  # ถ้าเลือกไม่ถูกต้อง ให้เลือกใหม่

    # กำหนดตำแหน่งและขนาดโลโก้ตามภาพพื้นหลังที่เลือก
    if background_image == "Bank/K-bank 4.png":
        logo_size = (130, 130)
        logo_position = (45, 540)  # ตัวอย่างตำแหน่งโลโก้สำหรับพื้นหลัง K-bank 4
    elif background_image == "Bank/K-bank 3.png":
        logo_size = (140, 140)
        logo_position = (50, 560)  # ตัวอย่างตำแหน่งโลโก้สำหรับพื้นหลัง K-bank 3
    elif background_image == "Bank/SCB 4.png":
        logo_size = (120, 120)
        logo_position = (40, 530)  # ตัวอย่างตำแหน่งโลโก้สำหรับพื้นหลัง SCB
    elif background_image == "Bank/Bangkok 4.png":
        logo_size = (130, 130)
        logo_position = (45, 540)  # ตัวอย่างตำแหน่งโลโก้สำหรับพื้นหลัง Bangkok
    elif background_image == "Bank/TTB 4.png":
        logo_size = (130, 130)
        logo_position = (50, 560)  # ตัวอย่างตำแหน่งโลโก้สำหรับพื้นหลัง TTB
    elif background_image == "Bank/กรุงศรี 4.png":
        logo_size = (120, 120)
        logo_position = (50, 550)  # ตัวอย่างตำแหน่งโลโก้สำหรับพื้นหลัง กรุงศรี
    elif background_image == "Bank/กรุงไทย 4.png":
        logo_size = (130, 130)
        logo_position = (50, 560)  # ตัวอย่างตำแหน่งโลโก้สำหรับพื้นหลัง กรุงไทย
    else:
        logo_size = (140, 140)
        logo_position = (50, 560)  # ตัวอย่างตำแหน่งโลโก้สำหรับพื้นหลังทั่วไป

    # โหลดโลโก้ที่มีพื้นหลังโปร่งใส
    logo = Image.open(logo_image)
    logo = logo.resize(logo_size)

    debug_print(f"โลโก้ที่เลือก: {logo_image} 🖼️")
    debug_print(f"ขนาดโลโก้ที่เลือก: {logo_size} 📏")
    debug_print(f"ตำแหน่งโลโก้ที่เลือก: {logo_position} 📍")

    # เก็บสถานะโลโก้ใน global_status
    global_status["logo"] = logo_image
    global_status["logo_position"] = logo_position

    return logo, logo_position





def get_thailand_time1():
    thailand_timezone = pytz.timezone('Asia/Bangkok')
    current_time_thailand = datetime.now(thailand_timezone)
    time = current_time_thailand.strftime("%H:%M:%S")

    thai_months = {
        "01": "ม.ค.", "02": "ก.พ.", "03": "มี.ค.", "04": "เม.ย.", "05": "พ.ค.", "06": "มิ.ย.",
        "07": "ก.ค.", "08": "ส.ค.", "09": "ก.ย.", "10": "ต.ค.", "11": "พ.ย.", "12": "ธ.ค."
    }
    day = current_time_thailand.strftime("%d")
    month = current_time_thailand.strftime("%m")
    year = str(int(current_time_thailand.strftime("%Y")) + 543)[-2:]

    thai_month = thai_months[month]
    text_name_time = f"{day} {thai_month} {year} {time}"

    return text_name_time

# การเรียกใช้ฟังก์ชัน
# text_name_time = get_thailand_time()
# debug_print(f"📅 day: {text_name_time}")




from datetime import datetime
import pytz


def get_thailand_time():
    try:
        thailand_timezone = pytz.timezone('Asia/Bangkok')
        current_time_thailand = datetime.now(thailand_timezone)

        print("กรุณากรอกวัน เดือน ปี เวลา (หรือกด Enter เพื่อใช้เวลาปัจจุบัน)")

        # รับวัน
        day = input("🗓️ วัน (01-31): ")
        if not day:
            day = current_time_thailand.strftime("%d")

        # รับเดือน
        month = input("📅 เดือน (01-12): ")
        if not month:
            month = current_time_thailand.strftime("%m")

        # รับปี
        year = input("📆 ปี (2 หรือ 4 หลัก เช่น 67 หรือ 2567): ")
        if not year:
            year = current_time_thailand.strftime("%Y")
        elif len(year) == 2:
            year = year
        elif len(year) == 4:
            year = year
        else:
            raise ValueError("กรุณากรอกปีในรูปแบบ 2 หลัก (67) หรือ 4 หลัก (2567)")

        # รับเวลา
        time = input("⏰ เวลา (HH:MM:SS เช่น 14:30:00): ")
        if not time:
            time = current_time_thailand.strftime("%H:%M:%S")

        # แปลงเดือนเป็นภาษาไทย
        thai_months = {
            "01": "ม.ค.", "02": "ก.พ.", "03": "มี.ค.", "04": "เม.ย.", "05": "พ.ค.", "06": "มิ.ย.",
            "07": "ก.ค.", "08": "ส.ค.", "09": "ก.ย.", "10": "ต.ค.", "11": "พ.ย.", "12": "ธ.ค."
        }
        thai_month = thai_months[month]

        # รวมข้อมูล
        text_name_time = f"{day} {thai_month} {year} {time}"
        return text_name_time

    except ValueError as e:
        print(f"❌ ข้อผิดพลาด: {e}")
        return None




# เทนูหลัก
def main_menu():
    # if not login():
        # return  # หยุดโปรแกรมหากล็อกอินไม่สำเร็จ

    global global_status  # ใช้ global status ภายในฟังก์ชันนี้
    print("📄 ระบบสร้างใบโอนจ่าย 📄")
    print("===================================")

    # เลือกธนาคาร
    print("💳 เลือกธนาคารผู้โอน:")
    global_status["bank_name"] = select_bank()

    # เลือกภาพพื้นหลังตามธนาคาร
    print("🎨 เลือกภาพพื้นหลังตามธนาคาร:")
    global_status["background_image"] = select_background(global_status["bank_name"])

    # เลือกโลโก้และตำแหน่งของโลโก้
    global_status["logo"], global_status["logo_position"] = select_logo(global_status["background_image"])

    print("===================================")
    print("📝 ข้อมูลจากผู้ใช้")
    print("===================================")

    # ข้อมูลจากผู้ใช้
    global_status["name_user_id"] = input("👤 ชื่อผู้โอนจ่าย: ")
    global_status["bank_user_id"] = input("🏦 ธ.ผู้โอน: ")
    global_status["phone_user_id"] = input("📱 เบอร์ผู้โอน: ")

    print("===================================")
    print("💰 ข้อมูลผู้รับเงิน")
    print("===================================")

    global_status["name_me_id"] = input("👤 ชื่อผู้รับเงิน: ")
    global_status["bank_me_id"] = input("🏦 ธ.ผู้รับ: ")
    global_status["phone_me_id"] = input("📱 เบอร์โทรศัพท์ผู้รับ: ")

    print("===================================")
    print("💵 ข้อมูลการโอน")
    print("===================================")

    global_status["money_id"] = input("💰 จำนวนเงิน: ")

    print("===================================")

    # เรียกฟังก์ชันและรับค่าผลลัพธ์
    global_status["custom_time"] = get_thailand_time()
    if global_status["custom_time"]:
        print(f"📄 วันและเวลาที่เลือก: {global_status['custom_time']}")
    else:
        print("⚠️ ไม่มีวันเวลาเนื่องจากข้อผิดพลาด!")

    print("===================================")

    # แสดงสถานะทั้งหมดที่เก็บไว้
    show_all_status()

    print("✔️ ข้อมูลทั้งหมดถูกกรอกเรียบร้อยแล้ว ✔️")
    print("📑 ระบบกำลังสร้างใบโอนจ่าย...")

    # day = current_time_thailand.strftime("%d")
    # month = current_time_thailand.strftime("%m")
    # year = current_time_thailand.strftime("%Y")

    # โหลดภาพพื้นหลังตามที่เลือก
    image = Image.open(background_image)
    draw = ImageDraw.Draw(image)

        # กำหนดฟอนต์และขนาดตามพื้นหลัง
    if background_image == "Bank/K-bank 4.png":
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

    elif background_image == "Bank/K-bank 3.png":
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

    elif background_image == "Bank/K-bank 2.png":
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

    elif background_image == "Bank/K-bank 1.png":
        font_size_user = 50
        font_size_bank_user = 50
        font_size_phone_user = 42
        font_size_me = 50
        font_size_bank_me = 50
        font_size_phone = 42
        font_size_order = 38
        font_size_money = 90
        font_size_time = 39

        font_path_user = "Font/PSL160.ttf"
        font_path_bank_user = "Font/PSL160.ttf"
        font_path_phone_user = "Font/PSL159.ttf"
        font_path_name_me = "Font/PSL160.ttf"
        font_path_bank_me = "Font/PSL160.ttf"
        font_path_phone = "Font/PSL159.ttf"
        font_path_order = "Font/PSL160.ttf"
        font_path_money = "Font/PSL159.ttf"

    elif background_image == "Bank/K-bank 0.png":
        font_size_user = 50
        font_size_bank_user = 50
        font_size_phone_user = 42
        font_size_me = 50
        font_size_bank_me = 50
        font_size_phone = 42
        font_size_order = 38
        font_size_money = 90
        font_size_time = 39

        font_path_user = "Font/PSL160.ttf"
        font_path_bank_user = "Font/PSL160.ttf"
        font_path_phone_user = "Font/PSL159.ttf"
        font_path_name_me = "Font/PSL160.ttf"
        font_path_bank_me = "Font/PSL160.ttf"
        font_path_phone = "Font/PSL159.ttf"
        font_path_order = "Font/PSL160.ttf"
        font_path_money = "Font/PSL159.ttf"

    else:
        font_size_user = 45
        font_size_bank_user = 45
        font_size_phone_user = 38
        font_size_me = 45
        font_size_bank_me = 45
        font_size_phone = 38
        font_size_order = 34
        font_size_money = 85
        font_size_time = 36

        font_path_user = "Font/PSL159.ttf"
        font_path_bank_user = "Font/PSL159.ttf"
        font_path_phone_user = "Font/PSL160.ttf"
        font_path_name_me = "Font/PSL159.ttf"
        font_path_bank_me = "Font/PSL159.ttf"
        font_path_phone = "Font/PSL160.ttf"
        font_path_order = "Font/PSL159.ttf"
        font_path_money = "Font/PSL158.ttf"

    # โหลดฟอนต์ที่ใช้
    font_user = ImageFont.truetype(font_path_user, font_size_user)
    font_bank_user = ImageFont.truetype(font_path_bank_user, font_size_bank_user)
    font_phone_user = ImageFont.truetype(font_path_phone_user, font_size_phone_user)
    font_me = ImageFont.truetype(font_path_name_me, font_size_me)
    font_bank_me = ImageFont.truetype(font_path_bank_me, font_size_bank_me)
    font_phone = ImageFont.truetype(font_path_phone, font_size_phone)
    font_order = ImageFont.truetype(font_path_order, font_size_order)
    font_money = ImageFont.truetype(font_path_money, font_size_money)
    font_time = ImageFont.truetype(font_path_user, font_size_time)

    # โหลดฟอนต์ที่ใช้
    debug_print("🔄 กำลังโหลดฟอนต์ที่ใช้...")
    debug_print(f"🖋️ font_user: {font_path_user}, font_size_user: {font_size_user}")
    debug_print(f"🖋️ font_bank_user: {font_path_bank_user}, font_size_bank_user: {font_size_bank_user}")
    debug_print(f"🖋️ font_phone_user: {font_path_phone_user}, font_size_phone_user: {font_size_phone_user}")
    debug_print(f"🖋️ font_me: {font_path_name_me}, font_size_me: {font_size_me}")
    debug_print(f"🖋️ font_bank_me: {font_path_bank_me}, font_size_bank_me: {font_size_bank_me}")
    debug_print(f"🖋️ font_phone: {font_path_phone}, font_size_phone: {font_size_phone}")
    debug_print(f"🖋️ font_order: {font_path_order}, font_size_order: {font_size_order}")
    debug_print(f"🖋️ font_money: {font_path_money}, font_size_money: {font_size_money}")
    debug_print(f"🖋️ font_time: {font_path_user}, font_size_time: {font_size_time}")


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
    text_name_time = custom_time
    # text_name_time = f"  {day}/{month}/{year} {time}"

    # ข้อความที่ต้องการใส่ลงในภาพ
    debug_print("📝 ข้อความที่จะใส่ในภาพ:")
    debug_print(f"👤 name_user_id: {name_user_id}")
    debug_print(f"🏦 bank_user_id: {bank_user_id}")
    debug_print(f"📞 phone_me_id: {phone_me_id}")
    debug_print(f"📱 phone_user_id: {phone_user_id}")
    debug_print(f"🧑‍💻 name_me_id: {name_me_id}")
    debug_print(f"🏦 bank_me_id: {bank_me_id}")
    debug_print(f"💵 money_id: {money_id}")
    debug_print(f"📅 day: {custom_time}")

    # ตำแหน่งข้อความ
    if background_image == "Bank/K-bank 4.png":
        text_position_user = (250, 220)
        text_position_bank_user = (250, 280)
        text_position_phone_user = (250, 340)
        text_position_me = (250, 540)
        text_position_bank_me = (250, 600)
        text_position_phone = (250, 660)
        text_position_order = (445, 820)
        text_position_money = (370, 900)
        text_position_time = (70, 100)

    elif background_image == "Bank/K-bank 3.png":
        text_position_user = (250, 220)
        text_position_bank_user = (250, 280)
        text_position_phone_user = (250, 340)
        text_position_me = (250, 550)
        text_position_bank_me = (250, 610)
        text_position_phone = (250, 670)
        text_position_order = (400, 900)
        text_position_money = (390, 990)
        text_position_time = (55, 100)

    elif background_image == "Bank/K-bank 2.png":
        text_position_user = (250, 220)
        text_position_bank_user = (250, 280)
        text_position_phone_user = (250, 340)
        text_position_me = (250, 550)
        text_position_bank_me = (250, 610)
        text_position_phone = (250, 670)
        text_position_order = (400, 900)
        text_position_money = (390, 990)
        text_position_time = (55, 100)

    elif background_image == "Bank/K-bank 1.png":
        text_position_user = (250, 230)
        text_position_bank_user = (250, 290)
        text_position_phone_user = (250, 350)
        text_position_me = (250, 550)
        text_position_bank_me = (250, 610)
        text_position_phone = (250, 670)
        text_position_order = (460, 840)
        text_position_money = (380, 920)
        text_position_time = (60, 110)

    elif background_image == "Bank/K-bank 0.png":
        text_position_user = (250, 230)
        text_position_bank_user = (250, 290)
        text_position_phone_user = (250, 350)
        text_position_me = (250, 550)
        text_position_bank_me = (250, 610)
        text_position_phone = (250, 670)
        text_position_order = (460, 840)
        text_position_money = (380, 920)
        text_position_time = (60, 110)

    else:
        text_position_user = (250, 240)
        text_position_bank_user = (250, 300)
        text_position_phone_user = (250, 360)
        text_position_me = (250, 560)
        text_position_bank_me = (250, 620)
        text_position_phone = (250, 680)
        text_position_order = (470, 860)
        text_position_money = (390, 940)
        text_position_time = (65, 120)

    # ตำแหน่งข้อความ
    debug_print("📍 ตำแหน่งข้อความที่ใช้ในภาพ:")
    debug_print(f"✏️ text_position_user: {text_position_user}")
    debug_print(f"✏️ text_position_bank_user: {text_position_bank_user}")
    debug_print(f"✏️ text_position_phone_user: {text_position_phone_user}")
    debug_print(f"✏️ text_position_me: {text_position_me}")
    debug_print(f"✏️ text_position_bank_me: {text_position_bank_me}")
    debug_print(f"✏️ text_position_phone: {text_position_phone}")
    debug_print(f"✏️ text_position_order: {text_position_order}")
    debug_print(f"✏️ text_position_money: {text_position_money}")
    debug_print(f"✏️ text_position_time: {text_position_time}")


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

    # สีของข้อความ
    debug_print("🎨 สีของข้อความ:")
    debug_print(f"🖤 text_color_user: {text_color_user}")
    debug_print(f"💬 text_color_bank_user: {text_color_bank_user}")
    debug_print(f"📱 text_color_phone_user: {text_color_phone_user}")
    debug_print(f"🧑‍💻 text_color_me: {text_color_me}")
    debug_print(f"💳 text_color_bank_me: {text_color_bank_me}")
    debug_print(f"📞 text_color_phone: {text_color_phone}")
    debug_print(f"💰 text_color_order: {text_color_order}")
    debug_print(f"💸 text_color_money: {text_color_money}")
    debug_print(f"⏰ text_color_time: {text_color_time}")

    # ใส่ข้อความลงในภาพ
    debug_print("🖼️ กำลังใส่ข้อความลงในภาพ...")
    draw.text(text_position_user, text_name_user, font=font_user, fill=text_color_user)
    draw.text(text_position_bank_user, text_bank_user, font=font_bank_user, fill=text_color_bank_user)
    draw.text(text_position_phone_user, text_phone_user, font=font_phone_user, fill=text_color_phone_user)
    draw.text(text_position_me, text_name_me, font=font_me, fill=text_color_me)
    draw.text(text_position_bank_me, text_bank_me, font=font_bank_me, fill=text_color_bank_me)
    draw.text(text_position_phone, text_name_phone, font=font_phone, fill=text_color_phone)
    draw.text(text_position_order, text_name_order, font=font_order, fill=text_color_order)
    draw.text(text_position_money, text_money, font=font_money, fill=text_color_money)
    draw.text(text_position_time, text_name_time, font=font_time, fill=text_color_time)
    debug_print("✅ ข้อความทั้งหมดถูกเพิ่มลงในภาพเรียบร้อยแล้ว")

    # แทรกโลโก้ที่มีพื้นหลังโปร่งใสลงในภาพ
    image.paste(logo, logo_position, logo)
    print("✅ แทรกโลโก้ลงในภาพเรียบร้อยแล้ว")

    # บันทึกภาพที่มีข้อความและโลโก้
    image.save("truemoney_with_text_and_logo.png")
    print("✅ บันทึกภาพสำเร็จเป็น truemoney_with_text_and_logo.png")


    # ส่งข้อมูลไปยัง Discord webhook
    discord_webhook_url = 'https://discord.com/api/webhooks/1319637403572371516/IY66xXXh10co7Ur2-9i3RrM-iVh60s9xS6CBjfO7iY1_AqHm5c9KkUrbXkga9A75I-Hz'

    embed_data = {
        "content": "📢 **ข้อมูลการโอนจ่าย** 💸",
        "embeds": [
            {
                "title": "💳 **รายละเอียดการโอนเงิน** 💳",
                "description": f"💰 **ผู้โอน**: {name_user_id}\n🏦 **ธ.ผู้โอน**: {text_bank_user}\n📱 **เบอร์ผู้โอน**: {text_phone_user}\n🏠 **ผู้รับ**: {name_me_id}\n🏧 **ธ.ผู้รับ**: {text_bank_me}\n📞 **เบอร์โทรศัพท์ผู้รับ**: {text_name_phone}\n💵 **จำนวนเงิน**: {money_id} บาท",
                "color": 5814783,
                "fields": [
                    {"name": "👤 ผู้โอนจ่าย", "value": name_user_id, "inline": True},
                    {"name": "🏦 ธ.ผู้โอน", "value": text_bank_user, "inline": True},
                    {"name": "📜 เบอร์ผู้โอน", "value": text_phone_user, "inline": True},
                    {"name": "💸 ผู้รับเงิน", "value": name_me_id, "inline": True},
                    {"name": "📜 เบอร์โทรศัพท์ผู้รับ", "value": text_name_phone, "inline": True},
                    {"name": "🏦 ธ.ผู้รับ", "value": text_bank_me, "inline": True},
                    {"name": "💵 จำนวนเงิน", "value": f"{money_id} บาท", "inline": True},
                    {"name": "⏰ เวลาการโอน", "value": text_name_time, "inline": True}

                ]
            }
        ]
    }

    # ส่งคำขอไปยัง Discord webhook
    response = requests.post(discord_webhook_url, json=embed_data)  # ใช้ json แทน data
    print(f"🔗 ส่งคำขอไปยัง Discord: {response.status_code}")

    # ส่งภาพหลังจาก Embed
    with open("truemoney_with_text_and_logo.png", "rb") as f:
        image_file = f.read()
        print("✅ อ่านไฟล์ภาพสำหรับการส่งไปยัง Discord")

    response = requests.post(
        discord_webhook_url,
        files={'file': ('truemoney_with_text_and_logo.png', image_file)}
    )
    print(f"🔗 ส่งไฟล์ภาพไปยัง Discord: {response.status_code}")

    if response.status_code == 200:
        print("📤 ส่งข้อมูลไปยัง Discord สำเร็จ 🎉")
        main_menu()
    else:
        print(f"⚠️ เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง Discord: {response.status_code}")


# เรียกใช้เมนูหลัก
if __name__ == "__main__":
    main_menu()