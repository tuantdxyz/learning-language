@echo off

REM Set encoding cho console
chcp 65001 > nul

echo Wellcome..

REM Kích hoạt môi trường ảo
call .\venv\Scripts\activate

REM Cài đặt các thư viện từ requirements.txt nếu cần
::pip install -r requirements.txt
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

REM Chạy script Python
py .\learnLanguages.py

pause