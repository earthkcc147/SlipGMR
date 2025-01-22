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
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")


# ฟังก์ชันเพื่อส่งข้อความไปยัง Discord ด้วย Embed
def smdc(message, embed=None):
    data = {
        "content": message,  # ข้อความที่จะส่ง
        "embeds": [embed] if embed else []  # ถ้ามี Embed ก็จะใส่ในฟิลด์นี้
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
    return now.strftime("%d-%m-%Y %H:%M:%S")  # รูปแบบเวลา: DD-MM-YYYY HH:mm:ss

# ฟังก์ชันตกแต่งข้อความ
def send(username):
    current_time = get_current_time()  # รับเวลาปัจจุบัน
    message = f"🎉 ผู้ใช้ {username} เข้าสู่ระบบสำเร็จ ✅\n🕒 เวลา: {current_time}"

    # สร้าง Embed
    embed = {
        "title": f"ข้อมูลการเข้าสู่ระบบของผู้ใช้ {username}",
        "description": "รายละเอียดของการเข้าสู่ระบบ",
        "color": 0x00FF00,  # สีของ Embed (เขียว)
        "fields": [
            {"name": "📍 IP", "value": device_info['IP'], "inline": False},
            {"name": "🌏 ตำแหน่ง", "value": f"{device_info['Location']['city']}, {device_info['Location']['region']}, {device_info['Location']['country']}", "inline": False},
            {"name": "💻 ระบบปฏิบัติการ", "value": f"{device_info['Device']['os']} {device_info['Device']['os_version']}", "inline": False},
            {"name": "🔧 CPU", "value": f"{device_info['Device']['processor']} ({device_info['Device']['cpu_count']} cores)", "inline": False},
            {"name": "🔋 แบตเตอรี่", "value": device_info['Battery'], "inline": False},
            {"name": "🖥️ ความละเอียดหน้าจอ", "value": device_info['Screen Resolution'], "inline": False},
            {"name": "💾 RAM", "value": f"{device_info['Device']['memory']} (Used: {device_info['Memory']['used']} GB, Free: {device_info['Memory']['free']} GB, Usage: {device_info['Memory']['percent']}%)", "inline": False},
            {"name": "🌐 เครือข่าย", "value": device_info['Network'], "inline": False},
            {"name": "💻 GPU", "value": device_info['GPU2'], "inline": False},
            {"name": "💾 การใช้งานดิสก์", "value": device_info['Disk Usage2'], "inline": False}
        ],
        "footer": {
            "text": f"การเข้าสู่ระบบเวลา: {current_time}"
        }
    }

    # ส่งข้อความและ Embed ไปยัง Discord
    smdc(message, embed)


# ตัวอย่างการเรียกใช้ฟังก์ชัน
# send(username)