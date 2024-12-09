import mariadb
import schedule
import time
import random
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Task Automation",
        app_icon="icon.ico"
    )

def fetch_random_records():
    connection = None  # Khởi tạo biến connection
    try:
        connection = mariadb.connect(
            host='10.63.163.172',
            user='tuantd',
            password='admin123',
            database='test_db2',
            port=3306
        )
        print("Kết nối đến cơ sở dữ liệu thành công.")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM learn_en")
        records = cursor.fetchall()

        print(f"Tổng số bản ghi trong bảng: {len(records)}")

        if len(records) < 2:
            print("Không đủ bản ghi để lấy.")
            cursor.close()
            return

        random_records = random.sample(records, 2)  # lấy ngẫu nhiên 2 bản ghi

        for record in random_records:
            title = f"En: {record[1]}"
            message = f"Vi: {record[2]}"
            send_notification(title, message)
            time.sleep(5)   # chờ 5s

    except mariadb.Error as err:
        print(f"Lỗi kết nối: {err}")
    finally:
        if connection and connection.ping():  # Kiểm tra nếu connection đã được khởi tạo
            cursor.close()
            connection.close()
            print("Đã đóng kết nối đến cơ sở dữ liệu.")

# Lập lịch chạy hàm mỗi xx phút
schedule.every(5).minutes.do(fetch_random_records)

# Chạy lần đầu tiên ngay lập tức
fetch_random_records()

while True:
    schedule.run_pending()
    time.sleep(1)