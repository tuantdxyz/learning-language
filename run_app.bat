@echo off

REM Set encoding cho console
chcp 65001 > nul

echo Wellcome to learn..

REM Kích hoạt môi trường ảo
call .\venv\Scripts\activate

REM Cài đặt các thư viện từ requirements.txt nếu cần
::pip install -r requirements.txt
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -q -r requirements.txt

REM Cấu hình
set /p interval="Mặc định 30 phút nếu không nhập. Nhập khoảng thời gian (phút): "
set /p show_terminal="Mặc định không hiển thị log. Hiện terminal? (true/false): "

REM Chạy script Python
py .\learnLanguages.py %interval% %show_terminal%

pause