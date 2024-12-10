import random
import time
import schedule
from plyer import notification
import sys
import codecs
import locale
locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')


# Đọc dữ liệu từ file data.txt
with open('data.txt', 'r', encoding='utf-8') as file:
    all_records = file.readlines()

def send_notification(title, message):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{now}] Hiển thị thông báo: {title} - {message}')
    notification.notify(
        title=title,
        message=message,
        app_name='Random Notification App',
        app_icon="icon.ico"
    )
    

def fetch_random_records():
    global all_records

    if len(all_records) < 2:
        print(f'[{now}] Đã hiển thị hết tất cả các từ vựng. Reset danh sách từ vựng.')
        with open('data.txt', 'r', encoding='utf-8') as file:
            all_records = file.readlines()

    random_records = random.sample(all_records, 2)  # Lấy ngẫu nhiên 2 bản ghi từ danh sách

    for record in random_records:
        title, message = record.strip().split(' - ')
        send_notification(title, message)
        time.sleep(5)  # Chờ 5 giây

    now = time.strftime('%Y-%m-%d %H:%M:%S')
    next_notify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 300)) # thêm 5 phút
    print(f'[{now}] Chờ đến lần hiển thị tiếp theo vào {next_notify_time}')

    # Loại bỏ các bản ghi đã được chọn khỏi danh sách all_records
    all_records = [record for record in all_records if record not in random_records]

# Lập lịch để thực hiện hàm fetch_random_records xx minute
schedule.every(30).minutes.do(fetch_random_records)

# Chạy lần đầu tiên ngay lập tức
fetch_random_records()

while True:
    schedule.run_pending()
    time.sleep(1)