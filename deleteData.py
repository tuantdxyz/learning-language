import mariadb

def delete_data(content_en):
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

        # Xóa dữ liệu cụ thể
        cursor.execute(
            "DELETE FROM learn_en WHERE content_en = ?",
            (content_en,)
        )

        # Kiểm tra số lượng bản ghi bị xóa
        if cursor.rowcount > 0:
            print(f"Đã xóa {cursor.rowcount} bản ghi.")
        else:
            print("Không tìm thấy bản ghi nào để xóa.")

        # Lưu thay đổi
        connection.commit()

    except mariadb.Error as err:
        print(f"Lỗi kết nối: {err}")
    finally:
        if connection and connection.ping():
            cursor.close()
            connection.close()
            print("Đã đóng kết nối đến cơ sở dữ liệu.")

# Gọi hàm để xóa dữ liệu cụ thể
delete_data('Good morning, how are you today?')