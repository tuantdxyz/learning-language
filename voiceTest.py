import pyttsx3

engine = pyttsx3.init()

# Lấy danh sách giọng đọc
voices = engine.getProperty('voices')

# In ra để biết có những giọng nào
for i, v in enumerate(voices):
    print(i, v.name)

# Ví dụ: chọn giọng nam phổ biến "Microsoft David Desktop"
engine.setProperty('voice', voices[0].id)  # thường là giọng nam

# Điều chỉnh tốc độ (giảm xuống 90% so với mặc định)
rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate * 0.5))

text = "The journey from Hanoi to Da Nang was really tiring but exciting."
engine.say(text)
engine.runAndWait()