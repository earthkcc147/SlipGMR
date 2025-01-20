import subprocess
import os
from colorama import Fore, Style
from tqdm import tqdm

def autoupdate_repository():
    repo_dir = '.'  # ระบุให้ใช้โฟลเดอร์ปัจจุบัน (Tester)
    repo_url = 'https://github.com/earthkcc147/SlipGMR.git'

    # ฟังก์ชันที่ช่วยแสดง progress bar สำหรับคำสั่ง git clone
    def clone_with_progress(repo_url, repo_dir):
        process = subprocess.Popen(
            ['git', 'clone', '--depth=1', repo_url, repo_dir],  # เพิ่ม --depth=1
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        # อ่านข้อมูลจาก stdout และแสดงข้อความการดาวน์โหลด
        for line in process.stdout:
            line = line.decode('utf-8')
            if 'Receiving objects' in line:
                tqdm.write(line.strip())  # แสดงผลใน tqdm
        process.wait()

    # เช็คว่าโฟลเดอร์ repository มีอยู่แล้วหรือไม่
    if os.path.exists(repo_dir):
        print(Fore.YELLOW + "🎉 พบ repository ที่มีอยู่แล้ว กำลังดึงข้อมูลล่าสุด...")
        # ใช้คำสั่ง git fetch เพื่อดึงการเปลี่ยนแปลงทั้งหมด
        subprocess.run(['git', '-C', repo_dir, 'fetch', '--depth=1'], check=True)  # เพิ่ม --depth=1
        # รีเซ็ตไฟล์ทั้งหมดให้ตรงกับ branch main
        subprocess.run(['git', '-C', repo_dir, 'reset', '--hard', 'origin/main'], check=True)
        print(Fore.GREEN + "✔️ การอัปเดตสำเร็จ!")
    else:
        print(Fore.RED + "❌ ไม่พบ repository กำลังทำการ clone...")
        # ใช้ฟังก์ชัน clone_with_progress เพื่อแสดง progress bar
        with tqdm(total=100, desc="ดาวน์โหลด repository", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}") as pbar:
            clone_with_progress(repo_url, repo_dir)
        print(Fore.GREEN + "✔️ การ clone สำเร็จ!")

# เรียกใช้ฟังก์ชัน (หากต้องการรันโปรแกรม)
# if __name__ == '__main__':
#     autoupdate_repository()
