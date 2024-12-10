import random
import time
import schedule
from plyer import notification
import sys
import codecs
import locale
locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')


# Kiểm tra và lấy tham số từ dòng lệnh
if len(sys.argv) > 1:
    interval = int(sys.argv[1])  # Tham số đầu tiên: interval
    interval = interval * 60
else:
    interval = 30 * 60  # Giá trị mặc định: 30 phút

show_terminal = False  # Giá trị mặc định
if len(sys.argv) > 2:
    show_terminal = sys.argv[2].lower() == 'true'  # Chuyển đổi thành boolean

if show_terminal:
    print("Chạy log trong terminal..")
else:
    print("Không log trong terminal..")
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    
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
    now = time.strftime('%Y-%m-%d %H:%M:%S')

    if len(all_records) < 2:
        print(f'[{now}] Đã hiển thị hết tất cả các từ. Đang reset danh sách từ..')
        with open('data.txt', 'r', encoding='utf-8') as file:
            all_records = file.readlines()

    random_records = random.sample(all_records, 2)  # Lấy ngẫu nhiên 2 bản ghi từ danh sách

    for record in random_records:
        title, message = record.strip().split(' - ')
        send_notification(title, message)
        time.sleep(5)  # Chờ 5 giây

    now = time.strftime('%Y-%m-%d %H:%M:%S')  # Cập nhật biến now
    next_notify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + interval)) 
    print(f'[{now}] Chờ đến lần hiển thị tiếp theo vào {next_notify_time}')

    # Loại bỏ các bản ghi đã được chọn khỏi danh sách all_records
    all_records = [record for record in all_records if record not in random_records]

# Lập lịch để thực hiện hàm fetch_random_records xx minute
schedule.every(interval).seconds.do(fetch_random_records)

# Chạy lần đầu tiên ngay lập tức
fetch_random_records()

while True:
    schedule.run_pending()
    time.sleep(1)