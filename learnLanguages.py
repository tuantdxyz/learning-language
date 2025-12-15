import random
import time
import schedule
from plyer import notification
import sys
import codecs
import locale
import pyttsx3

locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')

# --- Cấu hình tham số từ dòng lệnh ---
if len(sys.argv) > 1:
    interval = int(sys.argv[1]) * 60
else:
    interval = 30 * 60  # mặc định 30 phút

show_terminal = False
if len(sys.argv) > 2:
    show_terminal = sys.argv[2].lower() == 'true'

if show_terminal:
    print("Chạy log trong terminal..")
else:
    print("Không log trong terminal..")
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# --- Đọc dữ liệu từ file ---
with open('data.txt', 'r', encoding='utf-8') as file:
    all_records = file.readlines()

# --- Hàm đọc giọng nói ---
def speak_text(text, rate_factor=0.8, voice_index=0): # rate speaking = 0.8
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[voice_index].id)  # chọn giọng nam phổ biến
    rate = engine.getProperty('rate')
    engine.setProperty('rate', int(rate * rate_factor))
    engine.say(text)
    engine.runAndWait()

# --- Hàm gửi thông báo ---
def send_notification(title, message):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{now}] Hiển thị thông báo: {title} - {message}')
    notification.notify(
        title=title,
        message=message,
        app_name='Random Notification App',
        app_icon="icon.ico"
    )
    # Đọc giọng nói luôn sau khi thông báo
    speak_text(message, rate_factor=0.8, voice_index=0)   # rate 0.8

# --- Hàm lấy ngẫu nhiên bản ghi ---
def fetch_random_records():
    global all_records
    now = time.strftime('%Y-%m-%d %H:%M:%S')

    if len(all_records) < 2:
        print(f'[{now}] Đã hiển thị hết tất cả các từ. Reset danh sách..')
        with open('data.txt', 'r', encoding='utf-8') as file:
            all_records = file.readlines()

    random_records = random.sample(all_records, 2)

    for record in random_records:
        record = record.strip()
        if ' - ' in record:
            try:
                title, message = record.split(' - ', 1)
                send_notification(title.strip(), message.strip())
                time.sleep(8)   # waiting 8s
            except Exception as e:
                print(f'Lỗi xử lý dòng: {record} - {e}')
        else:
            print(f'Bỏ qua dòng không hợp lệ: {record}')

    next_notify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + interval))
    print(f'[{now}] Chờ đến lần hiển thị tiếp theo vào {next_notify_time}')

    # Loại bỏ bản ghi đã chọn
    all_records = [record for record in all_records if record not in random_records]

# --- Lập lịch ---
schedule.every(interval).seconds.do(fetch_random_records)

# Chạy lần đầu
fetch_random_records()

while True:
    schedule.run_pending()
    time.sleep(1)
