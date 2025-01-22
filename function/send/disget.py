import requests
from datetime import datetime
from dotenv import load_dotenv
import os
from function.get import get_full_info  # นำเข้า get_device_info จาก get.py

# เรียกข้อมูลจาก get_full_info
device_info = get_full_info()

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึงค่า Webhook URL จาก .env
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# ฟังก์ชันเพื่อส่งข้อความไปยัง Discord
def smdc(message):
    data = {
        "content": message  # ข้อความที่จะส่ง
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:  # 204 แปลว่าส่งสำเร็จ
            print("ส่งข้อความไปที่ Discord สำเร็จ ✅")
        else:
            print(f"เกิดข้อผิดพลาด: {response.status_code} ❌")
            print(response.text)
    except requests.RequestException as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e} ❌")

# ฟังก์ชันเพื่อรับเวลาปัจจุบันในรูปแบบที่ต้องการ
def get_current_time():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")  # รูปแบบเวลา: YYYY-MM-DD HH:mm:ss

# ฟังก์ชันตกแต่งข้อความ
def send(username):
    current_time = get_current_time()  # รับเวลาปัจจุบัน
    message = (
        f"🎉 ผู้ใช้ {username} เข้าสู่ระบบสำเร็จ ✅\n"
        f"🕒 เวลา: {current_time}\n"
        f"🖥️ อุปกรณ์ที่เข้าสู่ระบบ:\n"
        f"📍 IP: {device_info['IP']}\n"
        f"🌏 ตำแหน่ง: {device_info['Location']['city']}, {device_info['Location']['region']}, {device_info['Location']['country']}\n"
        f"💻 ระบบปฏิบัติการ: {device_info['Device']['os']} {device_info['Device']['os_version']}\n"
        f"🔧 CPU: {device_info['Device']['processor']} ({device_info['Device']['cpu_count']} cores)\n"
        f"🔋 แบตเตอรี่: {device_info['Battery']}\n"
        f"🖥️ ความละเอียดหน้าจอ: {device_info['Screen Resolution']}\n"
        f"💾 RAM: {device_info['Device']['memory']} (Used: {device_info['Memory']['used']} GB, Free: {device_info['Memory']['free']} GB, Usage: {device_info['Memory']['percent']}%)\n"
        f"🌐 เครือข่าย: {device_info['Network']}\n"
        f"🖥️ ความละเอียดหน้าจอ: {device_info['Screen Resolution2']}\n"
        f"💻 GPU: {device_info['GPU2']}\n"  # ข้อมูล GPU
        f"💾 การใช้งานดิสก์: {device_info['Disk Usage2']}\n"  # ข้อมูลดิสก์
    )

    # ส่งข้อความไปยัง Discord
    smdc(message)

# ตัวอย่างการเรียกใช้ฟังก์ชัน
# send(username)