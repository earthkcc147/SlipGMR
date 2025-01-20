เทนูหลัก

def main_menu(): print("📄 ระบบสร้างใบโอนจ่าย 📄") print("===================================")

# เลือกธนาคาร
print("💳 เลือกธนาคารผู้โอน:")
bank_name = select_bank()

# เลือกภาพพื้นหลังตามธนาคาร
print("🎨 เลือกภาพพื้นหลังตามธนาคาร:")
background_image = select_background(bank_name)

# เลือกโลโก้และตำแหน่งของโลโก้
print("🏷️ เลือกโลโก้และตำแหน่งของโลโก้:")
logo, logo_position = select_logo(background_image)

print("===================================")
print("📝 ข้อมูลจากผู้ใช้")
print("===================================")

# ข้อมูลจากผู้ใช้
name_user_id = input("👤 ชื่อผู้โอนจ่าย: ")
bank_user_id = input("🏦 ธ.ผู้โอน: ")
phone_user_id = input("📱 เบอร์ผู้โอน: ")

print("===================================")
print("💰 ข้อมูลผู้รับเงิน")
print("===================================")

name_me_id = input("👤 ชื่อผู้รับเงิน: ")
bank_me_id = input("🏦 ธ.ผู้รับ: ")
phone_me_id = input("📱 เบอร์โทรศัพท์ผู้รับ: ")

print("===================================")
print("💵 ข้อมูลการโอน")
print("===================================")

money_id = input("💰 จำนวนเงิน: ")

print("===================================")
print("✔️ ข้อมูลทั้งหมดถูกกรอกเรียบร้อยแล้ว ✔️")
print("📑 ระบบกำลังสร้างใบโอนจ่าย...")

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
text_name_time = f"  {day}/{month}/{year} {time}"

# ข้อความที่ต้องการใส่ลงในภาพ
debug_print("📝 ข้อความที่จะใส่ในภาพ:")
debug_print(f"👤 name_user_id: {name_user_id}")
debug_print(f"🏦 bank_user_id: {bank_user_id}")
debug_print(f"📞 phone_me_id: {phone_me_id}")
debug_print(f"📱 phone_user_id: {phone_user_id}")
debug_print(f"🧑‍💻 name_me_id: {name_me_id}")
debug_print(f"🏦 bank_me_id: {bank_me_id}")
debug_print(f"💵 money_id: {money_id}")
debug_print(f"📅 day: {day}, month: {month}, year: {year}, time: {time}")

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
    text_position_time = (55, 100)

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
            "description": f"💰 **ผู้โอน**: {name_user_id}\n🏠 **ผู้รับ**: {name_me_id}\n📞 **เบอร์โทรศัพท์ผู้รับ**: {text_name_phone}\n💵 **จำนวนเงิน**: {money_id} บาท\n🏦 **ธ.ผู้โอน**: {text_bank_user}\n📱 **เบอร์ผู้โอน**: {text_phone_user}\n🏧 **ธ.ผู้รับ**: {text_bank_me}",
            "color": 5814783,
            "fields": [
                {"name": "👤 ผู้โอนจ่าย", "value": name_user_id, "inline": True},
                {"name": "💸 ผู้รับเงิน", "value": name_me_id, "inline": True},
                {"name": "📜 เบอร์โทรศัพท์ผู้รับ", "value": text_name_phone, "inline": True},
                {"name": "💵 จำนวนเงิน", "value": f"{money_id} บาท", "inline": True},
                {"name": "⏰ เวลาการโอน", "value": f"{day}/{month}/{year} {time}", "inline": True},
                {"name": "🏦 ธ.ผู้โอน", "value": text_bank_user, "inline": True},
                {"name": "📜 เบอร์ผู้โอน", "value": text_phone_user, "inline": True},
                {"name": "🏦 ธ.ผู้รับ", "value": text_bank_me, "inline": True}
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
else:
    print(f"⚠️ เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง Discord: {response.status_code}")

เรียกใช้เมนูหลัก

if name == "main": main_menu()

ต้องการให้มีการล็อกอินก่อน

