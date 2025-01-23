import os
import time
import pyfiglet
import shutil
from colorama import init, Fore, Style

# เริ่มต้นการใช้งาน colorama
init()



# ฟังก์ชันสำหรับจัดข้อความให้อยู่ตรงกลาง
def center_text(text):
    # ดึงขนาดหน้าจอ
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns

    # แยกข้อความเป็นบรรทัดๆ
    lines = text.splitlines()

    centered_text = ""
    for line in lines:
        # คำนวณพื้นที่ว่างด้านซ้ายเพื่อให้อยู่ตรงกลาง
        centered_line = line.center(terminal_width)
        centered_text += centered_line + "\n"

    return centered_text




# สร้างข้อความ ASCII art ด้วย pyfiglet
intro = pyfiglet.figlet_format("SPAM SMS", font="calvin_s", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def sms():
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(intro)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน





# สร้างข้อความ ASCII art ด้วย pyfiglet
EMAIL = pyfiglet.figlet_format("SPAM MAIL", font="calvin_s", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def email():
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(EMAIL)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน



# สร้างข้อความ ASCII art ด้วย pyfiglet
FACEBOOK = pyfiglet.figlet_format("SPAM FACEBOOK", font="calvin_s", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def facebook():
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(FACEBOOK)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน



# สร้างข้อความ ASCII art ด้วย pyfiglet
DISCORD = pyfiglet.figlet_format("DISCORD TOOLS", font="calvin_s", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def discord():
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(DISCORD)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน




# สร้างข้อความ ASCII art ด้วย pyfiglet
IP = pyfiglet.figlet_format("DDOS & FLOAT", font="calvin_s", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def ip():
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(IP)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน





# ฟังก์ชันสำหรับแสดงโลโก้
def print_logo():
    # เคลียร์หน้าจอ
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = '''
   )   (          (        (    )   
  ())  )\  ( (  : )\  (    )\  ((.  
 (()))((_) )\)\  (_() )\  ((_) ))\  
(/ __|(_))(_((_)((_)()( )((_))((_)) 
| (_ | || | '  \/ _` | '_| || | ' \)
 \___|\_._|_|_|_|__/_|_|  \_._|_||_|
                                           
    > Gumarun Store ©
    '''
    # แสดงโลโก้ตรงกลางด้วยสีแดงและสไตล์ตัวหนา
    print(center_text(Fore.RED + Style.BRIGHT + banner))


# เรียกใช้ฟังก์ชัน
# print_intro()
# input("\nกด Enter เพื่อดำเนินการต่อ...")  # รอผู้ใช้กด Enter
# print_logo()