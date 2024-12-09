import mariadb

def insert_data_from_file(file_path):
    connection = None
    try:
        # Kết nối đến cơ sở dữ liệu
        connection = mariadb.connect(
            host='xx',
            user='xx',
            password='xx',
            database='xx',
            port=3306
        )
        cursor = connection.cursor()

        # Mở file và đọc nội dung
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):  # Lặp qua từng cặp câu
                content_en = lines[i].strip()  # Dòng tiếng Anh
                content_vi = lines[i+1].strip()  # Dòng tiếng Việt
                # Chèn dữ liệu vào bảng
                cursor.execute(
                    "INSERT INTO learn_en (content_en, content_vi) VALUES (?, ?)",
                    (content_en, content_vi)
                )

        # Lưu thay đổi
        connection.commit()
        print("Dữ liệu đã được chèn thành công.")

    except mariadb.Error as err:
        print(f"Lỗi kết nối: {err}")
    finally:
        if connection and connection.ping():
            cursor.close()
            connection.close()
            print("Đã đóng kết nối đến cơ sở dữ liệu.")

# Gọi hàm để chèn dữ liệu từ file
insert_data_from_file('data.txt')