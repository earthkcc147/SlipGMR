import os
import time
import pyfiglet
import shutil
from colorama import init, Fore, Style


# เริ่มต้นการใช้งาน colorama
init(autoreset=True)

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')


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



import os
from wcwidth import wcswidth  # ใช้ wcwidth สำหรับการคำนวณความกว้างของข้อความ

def remove_color_formatting(message):
    # ใช้ regular expression เพื่อลบรหัสสีออกจากข้อความ
    return re.sub(r'\033\[[0-9;]*m', '', message)

def print_centered(message):
    # ลบรหัสสีออกจากข้อความก่อนคำนวณความกว้าง
    plain_message = remove_color_formatting(message)
    # หาความกว้างของจอ
    terminal_width = os.get_terminal_size().columns
    # คำนวณความกว้างของข้อความที่แท้จริง
    message_width = wcswidth(message)
    # คำนวณการจัดตำแหน่งให้ตรงกลาง
    padding_left = (terminal_width - message_width) // 2
    print(' ' * padding_left + message)


# สร้างข้อความ ASCII art ด้วย pyfiglet
intro = pyfiglet.figlet_format("Welcome\nTo\nGumarun Store", font="cybermedium", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def print_intro():
    clear_console()
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(intro)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line + Style.RESET_ALL)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน

    # input(Fore.GREEN + "\nกด Enter เพื่อดำเนินการต่อ..." + Style.RESET_ALL)

    print_centered("welcome to Gumarun Store")
    # เรียกใช้งาน print_centered สำหรับข้อความที่ต้องการ
    print_centered(Fore.GREEN + "กด Enter เพื่อดำเนินการต่อ..." + Style.RESET_ALL)

    # รอให้ผู้ใช้กด Enter
    input()  # หรือใส่ข้อความให้ตรงกลางนี้ไปหลังจากรอ input ก็ได้
    clear_console()



# สร้างข้อความ ASCII art ด้วย pyfiglet
login = pyfiglet.figlet_format("LOGIN", font="standard", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def print_login():
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(login)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน





# สร้างข้อความ ASCII art ด้วย pyfiglet
HOME = pyfiglet.figlet_format("Welcome\nยินดีต้อนรับ\n", font="calvin_s", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def home():
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(HOME)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line + Style.RESET_ALL)  # ทำให้ข้อความเป็นสีเหลือง
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