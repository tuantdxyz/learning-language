#!/bin/bash

# Set encoding cho console
echo "Wellcome.."

# Kích hoạt môi trường ảo
source ./venv/bin/activate

# Cài đặt các thư viện từ requirements.txt nếu cần
pip install -r requirements.txt

# Chạy script Python
python learnLanguages.py

read -p "Press any key to exit..."